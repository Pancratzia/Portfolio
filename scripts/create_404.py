"""Build localized error pages from the current site's navigation and footer."""
from pathlib import Path
import re

DIST = Path(__file__).resolve().parents[1] / 'dist'


def create_pages():
    for language in ('en', 'es'):
        es = language == 'es'
        prefix = '/es' if es else ''
        source = (DIST / ('es/index.html' if es else 'index.html')).read_text()
        header = re.search(r'<header>.*?</header>', source, re.S)[0]
        other = '/404.html' if es else '/es/404.html'
        header = re.sub(r'(<a class="language" href=")[^"]*', lambda m: m[1] + other, header)
        footer = re.search(r'<footer>.*?</footer>', source, re.S)[0]
        styles = ''.join(re.findall(r'<link rel="stylesheet"[^>]*>', source))
        title = 'Página no encontrada | Pancratzia' if es else 'Page not found | Pancratzia'
        description = 'Esta página no está disponible. Vuelve al inicio o descubre los proyectos de Laura Ortega.' if es else 'This page is unavailable. Return home or explore Laura Ortega’s projects.'
        eyebrow = 'UN PEQUEÑO DESVÍO' if es else 'A SMALL DETOUR'
        heading = 'Esta página se fue<br>de <em>paseo.</em>' if es else 'This page<br><em>wandered off.</em>'
        copy = 'Puede que el enlace haya cambiado o que la página ya no exista. Pero todavía podemos encontrar algo bonito por aquí.' if es else 'The link may have changed, or the page may no longer exist. There’s still plenty of good work to discover here.'
        home = 'Volver al inicio' if es else 'Back to home'
        projects = 'Ver proyectos' if es else 'Explore projects'
        contact = '¿Necesitas ayuda? Hablemos ↗' if es else 'Need a hand? Let’s talk ↗'
        art = '''<div class="lost-cards" aria-hidden="true"><span class="lost-orbit"></span><span class="lost-card lost-four-a">4</span><span class="lost-card lost-zero">0<svg viewBox="0 0 100 100"><path d="M50 5Q55 45 95 50Q55 55 50 95Q45 55 5 50Q45 45 50 5Z" fill="currentColor"/></svg></span><span class="lost-card lost-four-b">4</span><svg class="lost-spark spark-a" viewBox="0 0 100 100"><path d="M50 0Q55 45 100 50Q55 55 50 100Q45 55 0 50Q45 45 50 0Z" fill="currentColor"/></svg><svg class="lost-spark spark-b" viewBox="0 0 100 100"><path d="M50 0Q55 45 100 50Q55 55 50 100Q45 55 0 50Q45 45 50 0Z" fill="currentColor"/></svg></div>'''
        html = f'''<!doctype html><html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><meta name="robots" content="noindex,follow"><meta name="theme-color" content="#7136d0"><link rel="canonical" href="https://www.pancratzia.com{prefix}/404.html"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">{styles}<link rel="stylesheet" href="/404.css"><script src="/app.js" defer></script></head><body><div class="scroll-progress" aria-hidden="true"></div><div class="cursor-glow" aria-hidden="true"></div><a class="skip" href="#main">{'Saltar al contenido' if es else 'Skip to content'}</a>{header}<main id="main"><section class="not-found"><div class="not-found-copy"><span class="eyebrow">404 / {eyebrow}</span><h1>{heading}</h1><p>{copy}</p><div class="conversion-row"><a class="button" href="{prefix}/">{home} <span>↗</span></a><a class="button secondary" href="{prefix}/work/">{projects} <span>↗</span></a></div><a class="text-link lost-contact" href="{prefix}/contact/">{contact}</a></div>{art}</section></main>{footer}</body></html>'''
        (DIST / ('es/404.html' if es else '404.html')).write_text(html)


if __name__ == '__main__':
    create_pages()
