"""Shared chrome and helpers for the v3 Pancratzia site (EN + ES)."""
from pathlib import Path
import html as _html

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / 'dist'
ORIGIN = 'https://www.pancratzia.com'
STATE = {'es': False}


def t(en, es):
    return es if STATE['es'] else en


def u(path):
    """Localized internal URL."""
    if STATE['es'] and path.startswith('/') and not path.startswith('/assets') and not path.startswith('/es'):
        return '/es' + path
    return path


def esc(s):
    return _html.escape(s, quote=True)


LOGO = '<svg width="34" height="34" viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" fill="#251b33"></rect><path fill="#f5f2ec" d="M11 9h17l9 9v8l-9 9h-8v6h-9V9Zm9 8v10h5l3-3v-4l-3-3h-5Z"></path><path class="spark" fill="#b994f5" d="M38 30l1.6 4.4L44 36l-4.4 1.6L38 42l-1.6-4.4L32 36l4.4-1.6Z"></path></svg>'
LOGO_DARK = '<svg width="32" height="32" viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" fill="#7136d0"></rect><path fill="#fff" d="M11 9h17l9 9v8l-9 9h-8v6h-9V9Zm9 8v10h5l3-3v-4l-3-3h-5Z"></path><path fill="#ddd0ef" d="M38 30l1.6 4.4L44 36l-4.4 1.6L38 42l-1.6-4.4L32 36l4.4-1.6Z"></path></svg>'
STAR = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true"><path class="spark" fill="{c}" d="M12 0l3 9 9 3-9 3-3 9-3-9-9-3 9-3Z"></path></svg>'
CHECK = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 8.5l3 3 7-7"></path></svg>'
ARR = '<span class="arr" aria-hidden="true">→</span>'


def star(size=24, color='#7136d0'):
    return STAR.format(s=size, c=color)


def nav(active, path):
    items = [('/work/', t('Work', 'Proyectos')), ('/services/', t('Services', 'Servicios')), ('/pricing/', t('Pricing', 'Precios')), ('/about/', t('About', 'Sobre mí')), ('/blog/', t('Journal', 'Blog'))]
    on = ' class="on" aria-current="page"'
    links = ''.join('<a href="' + u(h) + '"' + (on if active == h else '') + '>' + l + '</a>' for h, l in items)
    other = path if STATE['es'] else '/es' + path
    other_lang = 'en' if STATE['es'] else 'es'
    switch = f'<a class="language" lang="{other_lang}" hreflang="{other_lang}" href="{other}" style="font-size: 14px; text-decoration: none">{t("EN / <span class=sm>ES</span>", "<span class=sm>EN</span> / ES")}</a>'
    return f'''<a class="skip" href="#main">{t('Skip to content', 'Saltar al contenido')}</a>
<header class="nav"><div class="wrap nav-in">
<a class="logo" href="{u('/')}" aria-label="{t('Pancratzia home', 'Inicio de Pancratzia')}">{LOGO}<span>pancratzia<span class="pu">.</span></span></a>
<nav class="navlinks" id="menu" aria-label="{t('Main', 'Principal')}">{links}<a class="mobile-only" href="{u('/contact/')}">{t('Contact', 'Contacto')}</a></nav>
<div class="row" style="gap: 16px">{switch}<a class="btn btn-p hide-m" href="{u('/contact/')}" style="min-height: 44px; padding: 0 20px; font-size: 15px">{t('Start a project', 'Empezar un proyecto')}</a><button class="menu-btn" type="button" aria-controls="menu" aria-expanded="false" aria-label="{t('Open menu', 'Abrir menú')}"><span></span><span></span></button></div>
</div></header>'''


def cta():
    return f'''<section class="cta"><div class="wrap pad g2" style="gap: 48px; align-items: end">
<div><p class="eyebrow" style="color: #ddd0ef">{t('Open to project inquiries', 'Abierta a nuevos proyectos')}</p><h2 class="h2">{t('Your next website starts with a hello.', 'Tu próximo sitio web empieza con un hola.')}</h2></div>
<div class="row" style="justify-content: flex-end"><a class="btn btn-w" href="{u('/contact/')}">{t("Let's build something", 'Construyamos algo')} {ARR}</a><a class="btn btn-w" href="mailto:me@pancratzia.com">me@pancratzia.com</a></div>
</div></section>'''


def footer():
    col = 'style="margin: 0 0 6px; font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: #b994f5"'
    return f'''<footer class="foot"><div class="wrap" style="padding-top: 64px; padding-bottom: 40px">
<div class="g4" style="gap: 40px">
<div style="display: flex; flex-direction: column; gap: 16px"><a class="logo" href="{u('/')}" style="color: #f5f2ec">{LOGO_DARK}pancratzia.</a><p style="margin: 0; font-size: 14px; line-height: 1.6">{t('Thoughtfully designed. Carefully built.', 'Diseño con intención. Desarrollo con cuidado.')}</p></div>
<div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px"><p {col}>{t('Explore', 'Explorar')}</p><a href="{u('/work/')}">{t('Work', 'Proyectos')}</a><a href="{u('/services/')}">{t('Services', 'Servicios')}</a><a href="{u('/process/')}">{t('Process', 'Proceso')}</a><a href="{u('/pricing/')}">{t('Pricing', 'Precios')}</a></div>
<div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px"><p {col}>{t('Studio', 'Estudio')}</p><a href="{u('/about/')}">{t('About', 'Sobre mí')}</a><a href="{u('/blog/')}">{t('Journal', 'Blog')}</a><a href="{u('/faq/')}">FAQ</a><a href="{u('/contact/')}">{t('Contact', 'Contacto')}</a></div>
<div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px"><p {col}>{t('Connect', 'Contacto directo')}</p><a href="mailto:me@pancratzia.com">me@pancratzia.com</a><a href="https://webflow.com/@pancratzia">Webflow ↗</a><a href="https://www.upwork.com/freelancers/~016a6410dfa02febf5">Upwork ↗</a><a href="https://www.linkedin.com/in/leortegaperez/">LinkedIn ↗</a></div>
</div>
<div class="row" style="justify-content: space-between; margin-top: 56px; padding-top: 24px; border-top: 1px solid #4a3f55; font-size: 13px"><span>© 2026 Laura Ortega · Pancratzia · {t('Remote, worldwide', 'Remoto, en todo el mundo')} · EN / ES</span><span class="row" style="gap: 20px"><a href="{u('/privacy/')}">{t('Privacy', 'Privacidad')}</a><a href="{u('/terms/')}">{t('Terms', 'Términos')}</a><a href="{u('/storage/')}">{t('Browser storage', 'Almacenamiento')}</a></span></div>
</div></footer>'''


def write_page(path, title, desc, body, active=None, image='/assets/laura-portrait.webp', noindex=False, with_cta=True):
    """path: English route like '/work/'. Writes the current language version."""
    es = STATE['es']
    route = ('/es' + path) if es else path
    lang = 'es' if es else 'en'
    alt_en, alt_es = ORIGIN + path, ORIGIN + '/es' + path
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ''
    doc = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">{robots}
<meta name="theme-color" content="#7136d0">
<link rel="canonical" href="{ORIGIN + route}">
<link rel="alternate" hreflang="en" href="{alt_en}"><link rel="alternate" hreflang="es" href="{alt_es}"><link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{ORIGIN + route}"><meta property="og:image" content="{ORIGIN + image}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&amp;family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css">
<script src="/site.js" defer></script>
</head><body>
<div class="pz">
{nav(active, path)}
<main id="main">
{body}
{cta() if with_cta else ''}
</main>
{footer()}
</div>
</body></html>
'''
    out = DIST / route.lstrip('/') / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    return out
