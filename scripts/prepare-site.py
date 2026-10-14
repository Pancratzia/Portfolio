#!/usr/bin/env python3
"""Prepare static pages, analytics and sitemap before each publication."""
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timezone
from urllib.parse import urlsplit
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from lxml import etree
from create_404 import create_pages
from create_contact import remove_forms

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = 'https://www.pancratzia.com'
OLD_ORIGIN = 'https://pancratzia-portfolio.bloomycocoa32.chatgpt.site'
STATE = ROOT / '.openai/sitemap-state.json'
GTM = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MJ25B2CM');</script>
<!-- End Google Tag Manager -->"""
GA4 = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8PBFVMNNQS"></script>
<script>window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-8PBFVMNNQS');</script>"""
NOSCRIPT = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MJ25B2CM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.noindex = False
        self.canonical = None
        self.alternates = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot'):
            if 'noindex' in a.get('content', '').lower():
                self.noindex = True
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'link' and a.get('rel') == 'alternate' and a.get('hreflang'):
            self.alternates.append((a['hreflang'], a.get('href', '')))


def prepare():
    remove_forms()
    create_pages()
    previous = json.loads(STATE.read_text()) if STATE.exists() else {}
    today = datetime.now(timezone.utc).date().isoformat()
    records = {}
    entries = []
    locale_routes = {}
    for page in sorted(DIST.rglob('*.html')):
        if page == DIST / 'sitemap.html':
            continue  # Generated sitemap presentation, never an indexable site page.
        text = page.read_text()
        text = text.replace(OLD_ORIGIN, ORIGIN)
        # Remove our exact blocks before reinserting: repeated builds stay idempotent.
        for snippet in (GTM, GA4, NOSCRIPT):
            text = text.replace(snippet, '')
        if 'GTM-MJ25B2CM' in text or 'G-8PBFVMNNQS' in text:
            raise ValueError(f'Unexpected duplicate analytics markup: {page}')
        # Keep charset first, then place both loaders at the top of head.
        head = re.search(r'<head>\s*(<meta\s+charset=[^>]+>)?', text, re.I)
        if not head:
            raise ValueError(f'Missing head: {page}')
        text = text.replace('<script src="/locale.js"></script>', '')
        head = re.search(r'<head>\s*(<meta\s+charset=[^>]+>)?', text, re.I)
        text = text[:head.end()] + '<script src="/locale.js"></script>' + GTM + GA4 + text[head.end():]
        text, count = re.subn(r'(<body\b[^>]*>)', lambda m: m[1] + NOSCRIPT, text, count=1, flags=re.I)
        if count != 1:
            raise ValueError(f'Missing body: {page}')
        relative = page.relative_to(DIST).as_posix()
        route = '/' + (relative[:-10] if relative.endswith('index.html') else relative)
        base_route = route[3:] if route.startswith('/es/') else route
        english_file = DIST / (base_route.lstrip('/') + 'index.html' if base_route.endswith('/') else base_route.lstrip('/'))
        spanish_file = DIST / 'es' / english_file.relative_to(DIST)
        if english_file.exists() and spanish_file.exists():
            pair = {'en': base_route, 'es': '/es' + base_route}
            locale_routes[route] = pair
            if route.endswith('.html'):
                locale_routes[route[:-5]] = pair
            elif route.endswith('/') and route != '/':
                locale_routes[route.rstrip('/')] = pair
                locale_routes[route + 'index.html'] = pair
        canonical = ORIGIN + route
        # New pages receive a canonical URL even if their template omitted it.
        if not re.search(r'<link\b[^>]*rel=["\']canonical["\']', text, re.I):
            text = text.replace('</head>', f'<link rel="canonical" href="{canonical}"></head>')
        page.write_text(text)
        meta = Metadata()
        meta.feed(text)
        digest = hashlib.sha256(text.encode()).hexdigest()
        old = previous.get(relative, {})
        lastmod = old.get('lastmod', today) if old.get('sha256') == digest else today
        records[relative] = {'sha256': digest, 'lastmod': lastmod}
        if meta.noindex or meta.canonical != canonical:
            continue
        entries.append((canonical, lastmod, meta.alternates))
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    xhtml = 'http://www.w3.org/1999/xhtml'
    ET.register_namespace('', ns)
    ET.register_namespace('xhtml', xhtml)
    sitemap = ET.Element(f'{{{ns}}}urlset')
    included = {url for url, _, _ in entries}
    for url, lastmod, alternates in entries:
        item = ET.SubElement(sitemap, f'{{{ns}}}url')
        ET.SubElement(item, f'{{{ns}}}loc').text = url
        ET.SubElement(item, f'{{{ns}}}lastmod').text = lastmod
        for language, href in alternates:
            if href in included:
                ET.SubElement(item, f'{{{xhtml}}}link', {'rel':'alternate', 'hreflang':language, 'href':href})
    ET.indent(sitemap, space='  ')
    xml_body = ET.tostring(sitemap, encoding='utf-8')
    stylesheet = b'<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>'
    (DIST / 'sitemap.xml').write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + stylesheet + b'\n' + xml_body + b'\n')
    # A matching HTML view stays readable in browsers without native XSLT.
    transform = etree.XSLT(etree.parse(str(DIST / 'sitemap.xsl')))
    rendered = str(transform(etree.fromstring(xml_body)))
    rendered = rendered.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + GTM + GA4)
    rendered = rendered.replace('<body>', '<body>' + NOSCRIPT, 1)
    (DIST / 'sitemap.html').write_text(rendered)
    robots = DIST / 'robots.txt'
    rules = robots.read_text() if robots.exists() else 'User-agent: *\nAllow: /\n'
    rules = re.sub(r'^Sitemap:.*\n?', '', rules, flags=re.M | re.I)
    robots.write_text(rules.rstrip() + f'\nSitemap: {ORIGIN}/sitemap.xml\n')
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(records, indent=2, sort_keys=True) + '\n')
    locale_script = """(function(){
  'use strict';
  const pages = __PAGES__;
  let language;
  try { language = localStorage.getItem('pancratzia-language'); } catch (_) {}
  if (language !== 'es' && language !== 'en') {
    language = /^es(?:-|$)/i.test(navigator.language || '') ? 'es' : 'en';
  }
  const pair = pages[location.pathname];
  const currentLanguage = /^\\/es(?:\\/|$)/.test(location.pathname) ? 'es' : 'en';
  if (pair && language !== currentLanguage) {
    location.replace(pair[language] + location.search + location.hash);
  }
  document.addEventListener('click', function(event){
    const link = event.target.closest && event.target.closest('a.language');
    if (!link) return;
    const choice = link.getAttribute('lang');
    if (choice === 'en' || choice === 'es') {
      try { localStorage.setItem('pancratzia-language', choice); } catch (_) {}
    }
  }, true);
})();
""".replace('__PAGES__', json.dumps(locale_routes, sort_keys=True))
    (DIST / 'locale.js').write_text(locale_script)
    print(f'Prepared {len(records)} pages with GTM + GA4; sitemap contains {len(entries)} indexable URLs.')


if __name__ == '__main__':
    prepare()
