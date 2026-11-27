"""Builds the service and area pages (Norwegian and English).

Run from the prototype folder:  python3 blog-src/build_pages.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from build_blog import esc, ld, BASE, HOME, DIRECTIONS, BUSINESS, ICON_ARROW, ICON_MENU, LANGS  # noqa: E402
from pages_content import PAGES, AREA_LINKS, ORDER_SERVICES, ORDER_AREAS  # noqa: E402
import svcnav  # noqa: E402

OTHER = {'no': 'en', 'en': 'no'}
BLOG = {'no': '../blogg/index.html', 'en': '../blog/index.html'}
CITIES = ["Haugesund", "Karmøy", "Tysvær", "Bokn", "Sveio"]
EXTRA = {
    'no': dict(services_h='Våre tjenester', areas_h='Områder', more_services='Alle tjenestene våre', area_services='Tjenester i området', here='Du er her', short='Kort fortalt', home_services='Tjenester'),
    'en': dict(services_h='Our services', areas_h='Areas', more_services='All our services', area_services='Services in this area', here='You are here', short='In short', home_services='Services'),
}


def head(lang, key, title, desc, image, schemas):
    C = LANGS[lang]
    p = PAGES[key]
    url = f"{BASE}/{p[lang]['path']}"
    alt_url = f"{BASE}/{p[OTHER[lang]]['path']}"
    no_url = f"{BASE}/{p['no']['path']}"
    return f'''<!doctype html>
<html lang="{C['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{C['html']}" href="{url}">
<link rel="alternate" hreflang="{LANGS[OTHER[lang]]['html']}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{no_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{image}">
<meta property="og:locale" content="{C['locale']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../assets/blog.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
'''


def header(lang, key):
    L = LANGS[lang]['L']
    p = PAGES[key]
    here = os.path.basename(p[lang]['path'])
    there = '../' + p[OTHER[lang]]['path']
    no_href = here if lang == 'no' else there
    en_href = here if lang == 'en' else there
    switch = (f'<div class="lang" role="group" aria-label="{L["lang"]}">'
              f'<a href="{no_href}" hreflang="nb" aria-current="{str(lang == "no").lower()}">NO</a>'
              f'<a href="{en_href}" hreflang="en" aria-current="{str(lang == "en").lower()}">EN</a></div>')
    rest = (f'<a href="{HOME}#om-oss">{L["about"]}</a>'
            f'<a href="{BLOG[lang]}">{L["blog"]}</a><a href="{HOME}#kontakt">{L["contact"]}</a>')
    links = svcnav.desktop(lang, '../', L['services'], key) + rest
    mlinks = f'<a href="{HOME}#tjenester">{L["services"]}</a>' + svcnav.mobile(lang, '../', key) + rest
    return f'''<header class="site-h pad">
  <div class="wrap nav">
    <a class="logo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176"></a>
    <nav class="links" aria-label="{L['mainnav']}">{links}</nav>
    {switch}
    <a class="btn btn-quote" href="{HOME}#kontakt">{L['quote']}</a>
    <details class="mnav"><summary aria-label="{L['menu']}">{ICON_MENU}</summary>
      <nav aria-label="{L['mobnav']}">{mlinks}<a class="btn btn-quote" href="{HOME}#kontakt">{L['quote_free']}</a></nav>
    </details>
  </div>
</header>
'''


def footer(lang):
    L = LANGS[lang]['L']
    svc = ''.join(f'<a href="../{PAGES[k][lang]["path"]}">{esc(PAGES[k][lang]["crumb"])}</a>' for k in ORDER_SERVICES)
    areas = ''.join(f'<a href="../{PAGES[k][lang]["path"]}">{esc(PAGES[k][lang]["h1"])}</a>' for k in ORDER_AREAS)
    return f'''<footer class="site-f pad">
  <div class="wrap">
    <div class="fgrid">
      <div class="fcol"><a class="flogo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176" loading="lazy"></a></div>
      <div class="fcol">{svc}</div>
      <div class="fcol">{areas}<a href="{BLOG[lang]}">{L['blog']}</a></div>
      <div class="fcol"><a href="mailto:post@rentogeffektivt.no">post@rentogeffektivt.no</a><a href="{DIRECTIONS}" target="_blank" rel="noopener">Stølsmyr 16, 5542 Karmsund</a><span>{L['hours']}</span></div>
    </div>
    <div class="legal"><span>© 2026 R &amp; E Renhold AS · Org.nr. 916 712 731</span><span>{L['proto']}</span></div>
  </div>
</footer>
<script>{{try{{localStorage.setItem('re-lang','{lang}')}}catch(e){{}}}}var sc=document.querySelector('.svc-switch [aria-current]');if(sc){{var sw=sc.parentNode;sw.scrollLeft+=sc.getBoundingClientRect().left-sw.getBoundingClientRect().left-(sc.previousElementSibling?44:16)}}document.addEventListener('click',function(e){{var a=e.target.closest('a[href^="#"]');if(!a)return;var id=a.getAttribute('href').slice(1),el=id&&document.getElementById(id);if(!el)return;e.preventDefault();el.scrollIntoView({{behavior:'smooth',block:'start'}});try{{history.replaceState(null,'','#'+id)}}catch(_){{}}}});</script>
</body>
</html>
'''


def link_card(lang, key, current=False):
    t = PAGES[key][lang]
    href = '../' + t['path']
    here = f'<span class="here">{EXTRA[lang]["here"]}</span>' if current else ''
    cur = ' aria-current="page"' if current else ''
    return f'''<article class="card{' current' if current else ''}">
  <a href="{href}" tabindex="-1" aria-hidden="true" class="cimg"><img src="../img/{PAGES[key]['img']}" alt="{esc(t['alt'])}" width="1200" height="750" loading="lazy">{here}</a>
  <div class="cb"><h3><a href="{href}"{cur}>{esc(t['h1'])}</a></h3><p>{esc(t['intro'][:110].rsplit(' ', 1)[0])} …</p>
  <a class="more" href="{href}" aria-label="{LANGS[lang]['L']['more']}: {esc(t['h1'])}">{LANGS[lang]['L']['more']} {ICON_ARROW}</a></div>
</article>'''


def build(lang, key):
    C = LANGS[lang]
    L = C['L']
    X = EXTRA[lang]
    P = PAGES[key]
    t = P[lang]
    url = f"{BASE}/{t['path']}"
    biz = dict(BUSINESS, **{"@context": "https://schema.org"})
    schemas = [biz,
               {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": C['in'],
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t['faq']]},
               {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                   {"@type": "ListItem", "position": 1, "name": L['home'], "item": BASE + "/"},
                   {"@type": "ListItem", "position": 2, "name": X['services_h'] if P['kind'] == 'service' else X['areas_h'], "item": BASE + "/#tjenester"},
                   {"@type": "ListItem", "position": 3, "name": t['crumb'], "item": url}]}]
    if P['kind'] == 'service':
        schemas.insert(0, {"@context": "https://schema.org", "@type": "Service", "name": t['h1'], "serviceType": t['crumb'],
                           "description": t['desc'], "url": url, "inLanguage": C['in'], "provider": {"@id": BASE + "/#business"},
                           "areaServed": [{"@type": "City", "name": c} for c in CITIES]})
        others = [k for k in ORDER_SERVICES if k != key]
        rel_h = X['more_services']
    else:
        biz["areaServed"] = {"@type": "City", "name": P['city']}
        others = ORDER_SERVICES
        rel_h = X['area_services']
    body = t['body'].strip().replace('{haugesund}', AREA_LINKS[lang]['haugesund']).replace('{karmoy}', AREA_LINKS[lang]['karmoy'])
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in t['faq'])
    cta_h, cta_p = t['cta']
    crumb_mid = X['services_h'] if P['kind'] == 'service' else X['areas_h']
    rel = ''.join(link_card(lang, k, current=(k == key)) for k in ORDER_SERVICES)
    switch = ''
    related = f'''<section class="related pad" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h">{rel_h}</h2><div class="rgrid r3">{rel}</div></div></section>'''
    if P['kind'] == 'service':
        items = []
        for k in ORDER_SERVICES:
            o = PAGES[k][lang]; cur = k == key
            items.append(f'''<a href="../{o['path']}"{' aria-current="page"' if cur else ''}><img src="../img/{PAGES[k]['img']}" alt="" width="56" height="56" loading="eager"><span><b>{esc(o['crumb'])}</b><small>{X['here'] if cur else LANGS[lang]['L']['more']}</small></span></a>''')
        switch = f'<nav class="svc-switch" aria-label="{X["services_h"]}">{"".join(items)}</nav>'
        related = ''
    html_out = head(lang, key, t['seo_title'], t['desc'], P['img'], schemas) + header(lang, key) + f'''<main>
  <div class="pad">
    <div class="ahead">
      <nav class="crumbs" aria-label="{L['crumbs']}"><a href="{HOME}">{L['home']}</a><span aria-hidden="true">/</span><a href="{HOME}#tjenester">{crumb_mid}</a><span aria-hidden="true">/</span><span>{esc(t['crumb'])}</span></nav>
      {switch}
      <h1>{esc(t['h1'])}</h1>
      <p class="lead-in">{esc(t['intro'])}</p>
      <a class="btn btn-quote" href="{HOME}#kontakt">{L['quote_free']} {ICON_ARROW}</a>
    </div>
    <div class="ahero"><img src="../img/{P['img']}" alt="{esc(t['alt'])}" width="1200" height="750" fetchpriority="high"></div>
    <article class="article">
      {body}
      <aside class="cta"><div><h2>{esc(cta_h)}</h2><p>{esc(cta_p)}</p></div><a class="btn btn-quote" href="{HOME}#kontakt">{L['quote_free']} {ICON_ARROW}</a></aside>
      <section aria-labelledby="faq-h"><h2 id="faq-h">{L['faq']}</h2><div class="faq">{faq}</div></section>
    </article>
  </div>
  {related}
</main>
''' + footer(lang)
    out = os.path.join(ROOT, t['path'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f"{t['path']}  title {len(t['seo_title'])}  desc {len(t['desc'])}")


if __name__ == '__main__':
    for key in ORDER_SERVICES + ORDER_AREAS:
        for lang in ('no', 'en'):
            build(lang, key)
