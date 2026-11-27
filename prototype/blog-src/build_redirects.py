"""Turns the old tips-og-rad/ pages into redirects to their new blogg/ addresses."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.rentogeffektivt.no'
PAGES = ['index', 'fordeler-med-profesjonelt-renhold', 'tips-til-rent-kontor', 'sjekkliste-flyttevask',
         'boning-og-vedlikehold-av-gulv', 'hovedrengjoring-bedrift-og-hjem']
os.makedirs(os.path.join(ROOT, 'tips-og-rad'), exist_ok=True)
for name in PAGES:
    target = f'../blogg/{name}.html'
    canon = f'{BASE}/blogg/' + ('' if name == 'index' else name + '.html')
    page = f'''<!doctype html>
<html lang="nb"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Siden har flyttet</title><meta name="robots" content="noindex">
<link rel="canonical" href="{canon}"><meta http-equiv="refresh" content="0; url={target}">
</head><body style="font-family:system-ui,sans-serif;padding:24px">
<p>Siden har flyttet til <a href="{target}">bloggen</a>.</p>
</body></html>
'''
    with open(os.path.join(ROOT, 'tips-og-rad', name + '.html'), 'w', encoding='utf-8') as f:
        f.write(page)
print('ok', len(PAGES))
