"""Build localized error pages from the current site's navigation and footer (v3 design)."""
from pathlib import Path
import re

DIST = Path(__file__).resolve().parents[1] / 'dist'


def create_pages():
    for es in (False, True):
        prefix = '/es' if es else ''
        source = (DIST / ('es/index.html' if es else 'index.html')).read_text()
        head = re.search(r'<head>(.*?)</head>', source, re.S)[1]
        head = re.sub(r'<title>.*?</title>', '<title>' + ('Página no encontrada | Pancratzia' if es else 'Page not found | Pancratzia') + '</title>', head)
        head = re.sub(r'<link rel="(canonical|alternate)"[^>]*>', '', head)
        head = re.sub(r'<meta (name="description"|property="og:[^"]+"|name="twitter:card")[^>]*>', '', head)
        head += '<meta name="robots" content="noindex,follow">'
        top = re.search(r'<a class="skip".*?</header>', source, re.S)[0]
        top = re.sub(r'(<a class="language"[^>]*href=")[^"]*', lambda m: m[1] + ('/404.html' if es else '/es/404.html'), top)
        footer = re.search(r'<footer class="foot">.*?</footer>', source, re.S)[0]
        eyebrow = '404 / Un pequeño desvío' if es else '404 / A small detour'
        h1 = 'Esta página se fue <span class="pu">de paseo.</span>' if es else 'This page <span class="pu">wandered off.</span>'
        copy = 'Puede que el enlace haya cambiado o que la página ya no exista.' if es else 'The link may have changed, or the page may no longer exist.'
        home, work = ('Volver al inicio', 'Ver proyectos') if es else ('Back to home', 'Explore projects')
        lang = 'es' if es else 'en'
        html = f'''<!doctype html><html lang="{lang}"><head>{head}</head><body><div class="pz">{top}<main id="main"><section class="sec not-found"><div class="wrap pad"><p class="eyebrow">{eyebrow}</p><h1 class="h1">{h1}</h1><p class="lead" style="margin-top: 24px">{copy}</p><div class="row" style="margin-top: 32px"><a class="btn btn-p" href="{prefix}/">{home} <span class="arr" aria-hidden="true">→</span></a><a class="btn btn-g" href="{prefix}/work/">{work}</a><a class="btn btn-g" href="mailto:me@pancratzia.com">me@pancratzia.com</a></div></div></section></main>{footer}</div></body></html>'''
        (DIST / ('es/404.html' if es else '404.html')).write_text(html)


if __name__ == '__main__':
    create_pages()
