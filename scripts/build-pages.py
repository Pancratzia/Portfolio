"""Prepare GitHub Pages output for a project URL or the custom domain."""
from pathlib import Path
import argparse
import json
import re
import runpy
import shutil

ROOT = Path(__file__).resolve().parents[1]


def build(base_path=''):
    base_path = '/' + base_path.strip('/') if base_path.strip('/') else ''
    runpy.run_path(str(ROOT/'scripts/prepare-site.py'), run_name='__main__')
    output = ROOT/'_site'
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(ROOT/'dist', output)
    (output/'.nojekyll').write_text('')
    if base_path:
        for file in output.rglob('*'):
            if not file.is_file() or file.suffix not in ('.html', '.css', '.xsl', '.xml'):
                continue
            text = file.read_text()
            text = re.sub(r'((?:href|src|action)=["\'])/(?!/)', lambda m:m[1]+base_path+'/', text)
            text = re.sub(r'(url\(["\']?)/(?!/)', lambda m:m[1]+base_path+'/', text)
            if file.suffix == '.html':
                text = text.replace('<script src="'+base_path+'/locale.js"></script>', '<script>window.PANCRATZIA_BASE_PATH='+json.dumps(base_path)+';</script><script src="'+base_path+'/locale.js"></script>')
            file.write_text(text)
        locale = output/'locale.js'
        text = locale.read_text()
        match = re.search(r'const pages = (\{.*?\});', text)
        routes = json.loads(match[1])
        routes = {base_path+key:{lang:base_path+value for lang,value in pair.items()} for key,pair in routes.items()}
        text = text[:match.start(1)] + json.dumps(routes, sort_keys=True) + text[match.end(1):]
        text = text.replace('.test(location.pathname)', '.test(location.pathname.slice('+str(len(base_path))+') || "/")')
        locale.write_text(text)
        app = output/'app.js'
        text = app.read_text().replace("contactLink.href=(es?'/es':'')+'/contact/?service='", "contactLink.href="+json.dumps(base_path)+"+(es?'/es':'')+'/contact/?service='")
        app.write_text(text)
    print('GitHub Pages output:', output, 'base path:', base_path or '/')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-path', default='')
    build(parser.parse_args().base_path)
