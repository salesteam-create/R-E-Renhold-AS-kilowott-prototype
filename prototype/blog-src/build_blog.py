"""Builds the bilingual blog for the Rent og effektivt prototype.

Run from the prototype folder:  python3 blog-src/build_blog.py
Writes  blogg/  (Norwegian) and  blog/  (English), one index page plus one page per article.
Article content lives in articles_no.py and articles_en.py (same order = same article).
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import articles_no, articles_en  # noqa: E402

BASE = 'https://www.rentogeffektivt.no'
DATE = '2026-11-27'
HOME = '../index.html'
DIRECTIONS = 'https://www.google.com/maps/dir/?api=1&amp;destination=R%20%26%20E%20Renhold%20AS%2C%20St%C3%B8lsmyr%2016%2C%205542%20Karmsund'

LANGS = {
    'no': {'dir': 'blogg', 'html': 'nb', 'locale': 'nb_NO', 'in': 'nb-NO', 'items': articles_no.ARTICLES,
           'L': dict(home='Forside', blog='Blogg', services='Tjenester', about='Om oss', contact='Kontakt',
                     quote='Få pristilbud', quote_free='Be om pristilbud', menu='Meny', mainnav='Hovedmeny', mobnav='Mobilmeny',
                     crumbs='Brødsmuler', toc='Innhold', faq='Ofte stilte spørsmål', related='Les også', more='Les mer',
                     read='min lesetid', published='Publisert', date='27. november 2026', hours='Man til fre 08:00 til 16:00',
                     proto='Prototype laget av Kilowott', lang='Språk',
                     idx_title='Blogg: tips og råd om renhold | R&E Renhold Haugesund',
                     idx_desc='Praktiske råd om kontorrenhold, flyttevask, gulvpleie og hovedrengjøring fra et lokalt renholdsfirma på Haugalandet.',
                     idx_h1='Blogg: tips og råd om renhold',
                     idx_lead='Praktiske råd fra hverdagen som renholdsfirma på Haugalandet. For bedrifter som vil ha det rent, og alle som vil gjøre jobben enklere.')},
    'en': {'dir': 'blog', 'html': 'en', 'locale': 'en_GB', 'in': 'en', 'items': articles_en.ARTICLES,
           'L': dict(home='Home', blog='Blog', services='Services', about='About', contact='Contact',
                     quote='Get a quote', quote_free='Request a quote', menu='Menu', mainnav='Main menu', mobnav='Mobile menu',
                     crumbs='Breadcrumb', toc='Contents', faq='Frequently asked questions', related='Read more', more='Read more',
                     read='min read', published='Published', date='27 November 2026', hours='Mon to Fri 08:00 to 16:00',
                     proto='Prototype by Kilowott', lang='Language',
                     idx_title='Blog: cleaning tips and advice | R&E Renhold Haugesund',
                     idx_desc='Practical advice on office cleaning, move-out cleaning, floor care and deep cleaning from a local cleaning company in Haugalandet.',
                     idx_h1='Blog: cleaning tips and advice',
                     idx_lead='Practical advice from our everyday work as a cleaning company in Haugalandet. For businesses that want clean premises, and anyone who wants to make the job easier.')},
}
OTHER = {'no': 'en', 'en': 'no'}
assert len(articles_no.ARTICLES) == len(articles_en.ARTICLES)
NO_INDEX = {a['slug']: i for i, a in enumerate(articles_no.ARTICLES)}

BUSINESS = {
    "@type": "LocalBusiness", "@id": BASE + "/#business", "name": "R & E Renhold AS", "alternateName": "Rent og effektivt",
    "url": BASE + "/", "logo": BASE + "/img/logo-dark.png", "image": BASE + "/img/hero.webp",
    "telephone": "+47 454 02 012", "email": "post@rentogeffektivt.no",
    "address": {"@type": "PostalAddress", "streetAddress": "Stølsmyr 16", "postalCode": "5542",
                "addressLocality": "Karmsund", "addressRegion": "Rogaland", "addressCountry": "NO"},
    "geo": {"@type": "GeoCoordinates", "latitude": 59.3882553, "longitude": 5.3267368},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "16:00"}],
    "areaServed": [{"@type": "City", "name": n} for n in ["Haugesund", "Karmøy", "Tysvær", "Bokn", "Sveio"]],
}
ICON_ARROW = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_MENU = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'


def esc(s):
    return html.escape(s, quote=True)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace('</', '<\\/') + '</script>'


def read_minutes(a):
    text = a["intro"] + " " + a["body"] + " " + " ".join(q + " " + x for q, x in a["faq"])
    return max(2, round(len(re.sub(r'<[^>]+>', ' ', text).split()) / 200))


def page_file(lang, i=None):
    return 'index.html' if i is None else LANGS[lang]['items'][i]['slug'] + '.html'


def abs_url(lang, i=None):
    f = page_file(lang, i)
    return f"{BASE}/{LANGS[lang]['dir']}/" + ('' if f == 'index.html' else f)


def head(lang, i, title, desc, image, og_type, schemas):
    C = LANGS[lang]
    alt = OTHER[lang]
    return f'''<!doctype html>
<html lang="{C['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{abs_url(lang, i)}">
<link rel="alternate" hreflang="{C['html']}" href="{abs_url(lang, i)}">
<link rel="alternate" hreflang="{LANGS[alt]['html']}" href="{abs_url(alt, i)}">
<link rel="alternate" hreflang="x-default" href="{abs_url('no', i)}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{abs_url(lang, i)}">
<meta property="og:image" content="{BASE}/{image}">
<meta property="og:locale" content="{C['locale']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="../assets/blog.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
'''


def header(lang, i):
    L = LANGS[lang]['L']
    alt = OTHER[lang]
    other_href = f"../{LANGS[alt]['dir']}/{page_file(alt, i)}"
    no_href = other_href if lang == 'en' else page_file(lang, i)
    en_href = other_href if lang == 'no' else page_file(lang, i)
    switch = (f'<div class="lang" role="group" aria-label="{L["lang"]}">'
              f'<a href="{no_href}" hreflang="nb" data-lang="no" aria-current="{str(lang == "no").lower()}">NO</a>'
              f'<a href="{en_href}" hreflang="en" data-lang="en" aria-current="{str(lang == "en").lower()}">EN</a></div>')
    cur = ' aria-current="page"' if i is None else ''
    links = (f'<a href="{HOME}#tjenester">{L["services"]}</a><a href="{HOME}#om-oss">{L["about"]}</a>'
             f'<a href="index.html"{cur}>{L["blog"]}</a><a href="{HOME}#kontakt">{L["contact"]}</a>')
    return f'''<header class="site-h pad">
  <div class="wrap nav">
    <a class="logo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176"></a>
    <nav class="links" aria-label="{L['mainnav']}">{links}</nav>
    {switch}
    <a class="btn btn-quote" href="{HOME}#kontakt">{L['quote']}</a>
    <details class="mnav"><summary aria-label="{L['menu']}">{ICON_MENU}</summary>
      <nav aria-label="{L['mobnav']}">{links}<a class="btn btn-quote" href="{HOME}#kontakt">{L['quote_free']}</a></nav>
    </details>
  </div>
</header>
'''


def footer(lang):
    L = LANGS[lang]['L']
    return f'''<footer class="site-f pad">
  <div class="wrap">
    <div class="fgrid">
      <div class="fcol"><a class="flogo" href="{HOME}"><img src="../img/logo-dark.png" alt="R&amp;E Renhold, Rent &amp; Effektivt" width="624" height="176" loading="lazy"></a></div>
      <div class="fcol"><a href="{HOME}#tjenester">{L['services']}</a><a href="index.html">{L['blog']}</a><a href="{HOME}#kontakt">{L['quote']}</a></div>
      <div class="fcol"><a href="mailto:post@rentogeffektivt.no">post@rentogeffektivt.no</a><a href="{DIRECTIONS}" target="_blank" rel="noopener">Stølsmyr 16, 5542 Karmsund</a></div>
      <div class="fcol"><span>{L['hours']}</span><span>Org.nr. 916 712 731</span></div>
    </div>
    <div class="legal"><span>© 2026 R &amp; E Renhold AS</span><span>{L['proto']}</span></div>
  </div>
</footer>
<script>{{try{{localStorage.setItem('re-lang','{lang}')}}catch(e){{}}}}document.addEventListener('click',function(e){{var a=e.target.closest('a[href^="#"]');if(!a)return;var id=a.getAttribute('href').slice(1),el=id&&document.getElementById(id);if(!el)return;e.preventDefault();el.scrollIntoView({{behavior:'smooth',block:'start'}});try{{history.replaceState(null,'','#'+id)}}catch(_){{}}}});</script>
</body>
</html>
'''


def card(lang, i, level='h2', feat=False, lazy=True):
    a = LANGS[lang]['items'][i]
    L = LANGS[lang]['L']
    url = page_file(lang, i)
    return f'''<article class="card{' feat' if feat else ''}">
  <a href="{url}" tabindex="-1" aria-hidden="true"><img src="../img/blog/{a["img"]}" alt="{esc(a["alt"])}" width="1200" height="750"{' loading="lazy"' if lazy else ''}></a>
  <div class="cb">
    <div class="meta"><span class="tag">{esc(a["tag"])}</span><span>{read_minutes(a)} {L['read']}</span></div>
    <{level}><a href="{url}">{esc(a["h1"])}</a></{level}>
    <p>{esc(a["excerpt"])}</p>
    <a class="more" href="{url}" aria-label="{L['more']}: {esc(a["h1"])}">{L['more']} {ICON_ARROW}</a>
  </div>
</article>'''


def crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": name, "item": u} for n, (name, u) in enumerate(items)]}


def article_page(lang, i):
    C = LANGS[lang]
    L = C['L']
    a = C['items'][i]
    img = f'img/blog/{a["img"]}'
    schemas = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "mainEntityOfPage": abs_url(lang, i),
         "headline": a["h1"], "description": a["desc"], "image": f'{BASE}/{img}', "inLanguage": C['in'],
         "datePublished": DATE, "dateModified": DATE,
         "author": {"@type": "Organization", "name": "R & E Renhold AS", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "R & E Renhold AS", "logo": {"@type": "ImageObject", "url": BASE + "/img/logo-dark.png"}},
         "about": {"@id": BASE + "/#business"}},
        dict(BUSINESS, **{"@context": "https://schema.org"}),
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": C['in'],
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": x}} for q, x in a["faq"]]},
        crumb_ld([(L['home'], BASE + "/"), (L['blog'], abs_url(lang)), (a["h1"], abs_url(lang, i))]),
    ]
    toc = ''.join(f'<li><a href="#{t_id}">{esc(t)}</a></li>' for t_id, t in a["toc"])
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(x)}</p></details>' for q, x in a["faq"])
    related_idx = [NO_INDEX[s] for s in articles_no.ARTICLES[i]["related"]]
    rel = ''.join(card(lang, r, level='h3') for r in related_idx)
    cta_h, cta_p = a["cta"]
    return head(lang, i, a["seo_title"], a["desc"], img, 'article', schemas) + header(lang, i) + f'''<main>
  <div class="pad">
    <div class="ahead">
      <nav class="crumbs" aria-label="{L['crumbs']}"><a href="{HOME}">{L['home']}</a><span aria-hidden="true">/</span><a href="index.html">{L['blog']}</a><span aria-hidden="true">/</span><span>{esc(a["tag"])}</span></nav>
      <h1>{esc(a["h1"])}</h1>
      <div class="meta"><span class="tag">{esc(a["tag"])}</span><span>{L['published']} <time datetime="{DATE}">{L['date']}</time></span><span>{read_minutes(a)} {L['read']}</span></div>
    </div>
    <div class="ahero"><img src="../img/blog/{a["img"]}" alt="{esc(a["alt"])}" width="1200" height="750" fetchpriority="high"></div>
    <article class="article">
      <p class="intro">{esc(a["intro"])}</p>
      <nav class="toc" aria-label="{L['toc']}"><b>{L['toc']}</b><ol>{toc}</ol></nav>
      {a["body"].strip()}
      <aside class="cta"><div><h2>{esc(cta_h)}</h2><p>{esc(cta_p)}</p></div><a class="btn btn-quote" href="{HOME}#kontakt">{L['quote_free']} {ICON_ARROW}</a></aside>
      <section aria-labelledby="faq-h"><h2 id="faq-h">{L['faq']}</h2><div class="faq">{faq}</div></section>
    </article>
  </div>
  <section class="related pad" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h">{L['related']}</h2><div class="rgrid">{rel}</div></div></section>
</main>
''' + footer(lang)


def index_page(lang):
    C = LANGS[lang]
    L = C['L']
    items = C['items']
    schemas = [
        {"@context": "https://schema.org", "@type": "Blog", "name": L['idx_h1'], "url": abs_url(lang), "inLanguage": C['in'],
         "publisher": {"@id": BASE + "/#business"},
         "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": abs_url(lang, n), "datePublished": DATE} for n, a in enumerate(items)]},
        dict(BUSINESS, **{"@context": "https://schema.org"}),
        crumb_ld([(L['home'], BASE + "/"), (L['blog'], abs_url(lang))]),
    ]
    cards = card(lang, 0, feat=True, lazy=False) + ''.join(card(lang, n) for n in range(1, len(items)))
    return head(lang, None, L['idx_title'], L['idx_desc'], 'img/blog/' + items[0]["img"], 'website', schemas) + header(lang, None) + f'''<main>
  <section class="bhead pad">
    <div class="wrap">
      <nav class="crumbs" aria-label="{L['crumbs']}"><a href="{HOME}">{L['home']}</a><span aria-hidden="true">/</span><span>{L['blog']}</span></nav>
      <h1>{L['idx_h1']}</h1>
      <p class="lead">{L['idx_lead']}</p>
    </div>
  </section>
  <div class="pad"><div class="wrap bgrid">{cards}</div></div>
</main>
''' + footer(lang)


def main():
    for lang, C in LANGS.items():
        out = os.path.join(ROOT, C['dir'])
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(index_page(lang))
        for i, a in enumerate(C['items']):
            with open(os.path.join(out, a['slug'] + '.html'), 'w', encoding='utf-8') as f:
                f.write(article_page(lang, i))
            print(f"{C['dir']}/{a['slug']}.html  {read_minutes(a)} min  title {len(a['seo_title'])}  desc {len(a['desc'])}")


if __name__ == '__main__':
    main()
