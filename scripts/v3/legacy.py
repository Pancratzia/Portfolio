"""Carry long-form content (service details, articles, legal) from the previous
build into the v3 design. Run load() BEFORE the new pages overwrite dist/."""
import re
from bs4 import BeautifulSoup
from core import DIST, STATE, t, u, write_page, ARR

DROP = ['pre', 'svg', 'script', 'style', 'nav', '.svc-art', '.closing', '.conversion-row', '.svc-actions', '.s-mono',
        '.article-share', '.share', '.closing-star', '.svc-breadcrumb', 'button']


def _clean(node):
    for sel in DROP:
        for el in node.select(sel):
            el.decompose()
    for el in node.find_all(True):
        for attr in ('class', 'style', 'data-reveal', 'width', 'height', 'fetchpriority'):
            el.attrs.pop(attr, None)
    for em in node.find_all('em'):
        em.name = 'span'
        em['class'] = 'pu'
    return node


def _inner(el):
    return ''.join(str(c) for c in el.contents).strip()


def load(src=DIST):
    pages = {}
    for f in sorted(src.rglob('index.html')):
        rel = '/' + f.relative_to(src).parent.as_posix() + '/'
        rel = rel.replace('//', '/')
        es = rel.startswith('/es/')
        base = rel[3:] if es else rel
        kind = None
        if base.startswith('/services/') and base != '/services/':
            kind = 'service'
        elif base.startswith('/blog/') and base != '/blog/':
            kind = 'post'
        elif base in ('/privacy/', '/terms/', '/storage/', '/thanks/'):
            kind = 'legal'
        if not kind:
            continue
        soup = BeautifulSoup(f.read_text(), 'html.parser')
        main = soup.find('main')
        title = soup.title.get_text(strip=True) if soup.title else ''
        desc = soup.find('meta', attrs={'name': 'description'})
        desc = desc['content'] if desc else ''
        noindex = bool(soup.find('meta', attrs={'name': 'robots', 'content': re.compile('noindex')}))
        h1 = main.find('h1')
        eyebrow = ''
        for cand in main.select('.eyebrow, .s-eyebrow, .article-meta'):
            if h1 and cand.sourceline and h1.sourceline and cand.sourceline <= h1.sourceline:
                eyebrow = cand.get_text(' ', strip=True)
            break
        lead = main.select_one('.svc-lead, .article-deck, .page-heading > p, .svc-hero p:not(.s-eyebrow)')
        lead_html = lead.get_text(' ', strip=True) if lead else ''
        cover = main.select_one('.article-cover img')
        cover_src = cover['src'] if cover else None
        h1_html = re.sub(r'<br\s*/?>', ' ', str(_clean(BeautifulSoup(str(h1), 'html.parser')).h1)) if h1 else ''
        h1_html = re.sub(r'^<h1>|</h1>$', '', h1_html)
        # remove heading pieces from body
        for sel in ['.page-heading', '.svc-hero', '.article-header', '.article-cover', '.svc-breadcrumb', '.article-toc']:
            for el in main.select(sel):
                el.decompose()
        toc = None
        if kind == 'post':
            body = main.select_one('article') or main
            # drop "Share this guide" and the closing promo
            for h in body.find_all(['h2', 'h3']):
                if re.search(r'share|compart', h.get_text(), re.I):
                    parent = h.parent if h.parent and h.parent.name in ('section', 'div', 'aside') and h.parent is not body else None
                    (parent or h).decompose()
            toc = [(s.get('id'), s.find('h2').get_text(strip=True)) for s in body.find_all('section', id=True) if s.find('h2')]
            blocks = _inner(_clean(body))
        else:
            _clean(main)
            blocks = []
            secs = [x for x in main.find_all('section') if not x.find_parent('section')]
            if not secs:
                secs = main.find_all(['article', 'div'], recursive=False)
            for sec in secs:
                head = sec.find(['h2'])
                label = head.get_text(' ', strip=True) if head else ''
                if head:
                    head.decompose()
                if not label:
                    p = sec.find('p')
                    if p and len(p.get_text()) < 40 and p.get_text().isupper():
                        label = p.get_text(strip=True).capitalize()
                        p.decompose()
                content = _inner(sec)
                if re.search(r'your next website|tu próximo sitio|shall we build|construimos|let.s build|creamos', label, re.I):
                    continue
                if content or label:
                    blocks.append((label, content))
        pages[(base, es)] = dict(kind=kind, title=title, desc=desc, noindex=noindex, eyebrow=eyebrow, h1=h1_html, lead=lead_html,
                                 cover=cover_src, toc=toc, blocks=blocks)
    return pages


def render(pages):
    for (base, es), p in pages.items():
        STATE['es'] = es
        hero = f'''<section class="sec dots" style="position: relative; overflow: hidden"><svg class="hero-deco spin hide-m" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0l3 9 9 3-9 3-3 9-3-9-9-3 9-3Z"></path></svg><div class="wrap pad g2" style="gap: 56px; align-items: end; padding-bottom: 72px; position: relative">
<div><p class="crumb">{_crumb(base)}</p>{f'<p class="eyebrow up d1">{p["eyebrow"]}</p>' if p['eyebrow'] else ''}<h1 class="h1 up d2" style="font-size: 68px">{p['h1']}</h1></div>
<div class="up d3" style="display: flex; flex-direction: column; gap: 24px">{f'<p class="lead">{p["lead"]}</p>' if p['lead'] else ''}{_actions(p['kind'], base)}</div>
</div></section>'''
        if p['kind'] == 'post':
            cover = f'<section class="sec"><div class="wrap" style="padding-top: 48px; padding-bottom: 48px"><div class="shot" style="aspect-ratio: 16 / 9"><img src="{p["cover"]}" alt="" width="1672" height="941"></div></div></section>' if p['cover'] else ''
            toc = ''.join(f'<li><a href="#{a}" style="text-decoration: none">{h}</a></li>' for a, h in (p['toc'] or []))
            aside = f'''<aside class="hide-m" style="position: sticky; top: 110px; align-self: start; display: flex; flex-direction: column; gap: 14px"><p class="eyebrow" style="margin: 0">{t('In this article', 'En este artículo')}</p><ol class="list" style="font-size: 15px">{toc}</ol><a class="btn btn-p" href="mailto:me@pancratzia.com" style="margin-top: 16px; justify-content: center">{t('Discuss my website', 'Hablemos de mi sitio')} {ARR}</a></aside>'''
            body = hero + cover + f'<section class="sec"><div class="wrap pad g2" style="gap: 64px; grid-template-columns: 280px minmax(0, 1fr); padding-top: 72px">{aside}<article class="prose">{p["blocks"]}</article></div></section>'
        else:
            blocks = ''.join(f'<div class="svc-block reveal"><h2>{l}</h2><div>{c}</div></div>' if l else f'<div class="svc-block reveal"><span></span><div>{c}</div></div>' for l, c in p['blocks'])
            body = hero + f'<section class="sec"><div class="wrap" style="padding-top: 24px; padding-bottom: 72px">{blocks}</div></section>'
        body = body.replace('ChatGPT Sites', 'GitHub Pages')
        active = '/services/' if p['kind'] == 'service' else ('/blog/' if p['kind'] == 'post' else None)
        write_page(base, p['title'], p['desc'], body, active=active, noindex=p['noindex'], image=p['cover'] or '/assets/laura-portrait.webp', with_cta=p['kind'] != 'legal')


def _crumb(base):
    parts = [x for x in base.strip('/').split('/')]
    names = {'services': t('Services', 'Servicios'), 'blog': t('Journal', 'Blog')}
    if parts[0] in names and len(parts) > 1:
        out = f'<a href="{u("/" + parts[0] + "/")}">{names[parts[0]]}</a>'
        if len(parts) > 2:
            out += f' / <a href="{u("/" + parts[0] + "/" + parts[1] + "/")}">{parts[1].replace("-", " ").capitalize()}</a>'
        return out
    return f'<a href="{u("/")}">{t("Home", "Inicio")}</a>'


def _actions(kind, base):
    if kind == 'service':
        return f'<div class="row"><a class="btn btn-p" href="mailto:me@pancratzia.com">{t("Discuss this project", "Hablemos de este proyecto")} {ARR}</a><a class="btn btn-g" href="{u("/pricing/")}">{t("See starting prices", "Ver precios de partida")}</a></div>'
    return ''
