"""Shared 'Services' dropdown for the header of generated pages.

desktop(lang, prefix, label, current_key=None) returns the dropdown for the main nav.
mobile(lang, prefix, current_key=None) returns indented sub-links for the mobile menu.
prefix is the path from the page to the site root, e.g. '../'.
"""
from pages_content import PAGES, ORDER_SERVICES

DESC = {
    'no': {
        'office': 'Daglig eller regelmessig renhold av kontorer, butikker og fellesarealer.',
        'special': 'Grundig rengjøring når det faste renholdet ikke strekker til.',
        'floor': 'Oppskuring og ny bone som gir vinyl- og linoleumsgulv nytt liv.',
    },
    'en': {
        'office': 'Daily or regular cleaning of offices, shops and shared areas.',
        'special': 'Thorough cleaning when regular cleaning is not enough.',
        'floor': 'Stripping and a new coat of polish that bring vinyl and linoleum floors back to life.',
    },
}
ICONS = [
    '<path d="M5 12l5 5L20 7"/>',
    '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
]
CHEV = '<svg class="dd-c" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def _kind(i):
    return ['office', 'special', 'floor'][i]


def desktop(lang, prefix, label, current_key=None):
    items = []
    for i, k in enumerate(ORDER_SERVICES):
        p = PAGES[k][lang]
        cur = ' aria-current="page"' if k == current_key else ''
        ic = f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[i]}</svg>'
        items.append(f'<a href="{prefix}{p["path"]}"{cur}><span class="ddi">{ic}</span>'
                     f'<span><b>{p["crumb"]}</b><small>{DESC[lang][_kind(i)]}</small></span></a>')
    active = ' aria-current="true"' if current_key in ORDER_SERVICES else ''
    return (f'<div class="dd"><a class="dd-t" href="{prefix}index.html#tjenester"{active}>{label}{CHEV}</a>'
            f'<div class="dd-p">{"".join(items)}</div></div>')


def mobile(lang, prefix, current_key=None):
    out = []
    for k in ORDER_SERVICES:
        p = PAGES[k][lang]
        cur = ' aria-current="page"' if k == current_key else ''
        out.append(f'<a class="msub" href="{prefix}{p["path"]}"{cur}>{p["crumb"]}</a>')
    return ''.join(out)
