#!/usr/bin/env python3
"""Build the v3 Pancratzia site (EN + ES) into dist/.

Usage: python scripts/v3/build.py   then   python scripts/prepare-site.py
Long-form pages (service details, articles, legal) are read from the existing
dist/ before it is regenerated, so their copy is preserved in both languages.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from core import DIST, STATE
import legacy
import pages_home
import pages_main

HERE = Path(__file__).resolve().parent
LEGACY_COMMIT = '06b4182'
KEEP = {'locale.js', 'sitemap.xsl', 'robots.txt', 'sitemap.xml', 'site.css', 'site.js'}

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#7136d0"/><path fill="#fff" d="M7 5h12l6 6v6l-6 6h-5v4H7V5Zm7 6v6h3l2-2v-2l-2-2h-3Z"/><path fill="#ddd0ef" d="M26 20l1 3 3 1-3 1-1 3-1-3-3-1 3-1Z"/></svg>\n'
MARK = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="#251b33"/><path fill="#f5f2ec" d="M11 9h17l9 9v8l-9 9h-8v6h-9V9Zm9 8v10h5l3-3v-4l-3-3h-5Z"/><path fill="#b994f5" d="M38 30l1.6 4.4L44 36l-4.4 1.6L38 42l-1.6-4.4L32 36l4.4-1.6Z"/></svg>\n'


def main():
    # Long-form copy comes from the last pre-v3 build, kept in git history.
    import subprocess, tempfile, tarfile, io
    tmp = Path(tempfile.mkdtemp())
    data = subprocess.run(['git', 'archive', LEGACY_COMMIT, 'dist'], cwd=DIST.parent, capture_output=True, check=True).stdout
    tarfile.open(fileobj=io.BytesIO(data)).extractall(tmp, filter='data')
    old = legacy.load(tmp / 'dist')
    for f in list(DIST.rglob('*')):
        if f.is_file() and 'assets' not in f.parts and f.name not in KEEP and f.suffix in ('.html', '.css', '.js'):
            f.unlink()
    (DIST / 'site.css').write_text((HERE / 'base.css').read_text() + '\n' + (HERE / 'extra.css').read_text())
    (DIST / 'site.js').write_text((HERE / 'site.js').read_text())
    (DIST / 'assets/favicon.svg').write_text(FAVICON)
    (DIST / 'assets/pancratzia-mark.svg').write_text(MARK)
    for es in (False, True):
        STATE['es'] = es
        pages_home.home()
        pages_main.work(); pages_main.cases(); pages_main.services_hub(); pages_main.pricing(); pages_main.process()
        pages_main.about(); pages_main.faq(); pages_main.contact(); pages_main.blog_index()
    legacy.render(old)
    n = len(list(DIST.rglob('index.html')))
    print(f'v3 build: {n} index pages')


if __name__ == '__main__':
    main()
