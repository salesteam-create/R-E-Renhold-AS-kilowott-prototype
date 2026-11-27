"""Writes sitemap.xml (with Norwegian/English alternates) and robots.txt.

Run from the prototype folder:  python3 blog-src/build_sitemap.py
Only indexable pages are listed: the guide page (noindex) and the old tips-og-rad redirects are left out.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import articles_no, articles_en  # noqa: E402
from pages_content import PAGES, ORDER_SERVICES, ORDER_AREAS  # noqa: E402

BASE = 'https://www.rentogeffektivt.no'
DATE = '2026-11-27'

pairs = [('', None)]                                   # homepage: Norwegian only
pairs.append(('jobb-hos-oss.html', None))
pairs.append(('blogg/', 'blog/'))
for no, en in zip(articles_no.ARTICLES, articles_en.ARTICLES):
    pairs.append((f'blogg/{no["slug"]}.html', f'blog/{en["slug"]}.html'))
for k in ORDER_SERVICES + ORDER_AREAS:
    pairs.append((PAGES[k]['no']['path'], PAGES[k]['en']['path']))

for no, en in pairs:
    for p in (no, en):
        if p is None: continue
        f = os.path.join(ROOT, p if p and not p.endswith('/') else (p + 'index.html'))
        assert os.path.exists(f), f

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for no, en in pairs:
    for loc in (no, en):
        if loc is None: continue
        out.append('  <url>')
        out.append(f'    <loc>{BASE}/{loc}</loc>')
        out.append(f'    <lastmod>{DATE}</lastmod>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="nb" href="{BASE}/{no}"/>')
        if en is not None:
            out.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE}/{en}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/{no}"/>')
        out.append('  </url>')
out.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

robots = f"""User-agent: *
Allow: /
Disallow: /blog-src/

Sitemap: {BASE}/sitemap.xml
"""
open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(robots)
print('urls', sum(1 for no, en in pairs for x in (no, en) if x is not None))
