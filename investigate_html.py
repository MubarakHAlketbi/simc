#!/usr/bin/env python3
"""Investigate the HTML structure of a talent calc page"""
from dotenv import load_dotenv
import os, re
load_dotenv('/home/mubarak/.hermes/.env')
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])

url = "https://www.wowhead.com/talent-calc/rogue/outlaw/fatebound"
result = app.scrape(url, formats=['html'])
html = result.html if hasattr(result, 'html') else result.get('html', '')

# Look for structural markers
print("=== Key Structural Markers ===")
markers = [
    'data-class-spec',
    'data-hero',
    'data-tree',
    'data-spec',
    'talent-tree',
    'hero-tree',
    'class-tree',
    'spec-tree',
    'fatebound',
    'trickster',
    'outlaw',
    'rogue',
    'aria-label',
    'spell=',
]
for m in markers:
    count = html.count(m)
    if count > 0:
        idx = html.find(m)
        print(f"'{m}': {count} occurrences, first at {idx}")
        print(f"  Context: ...{html[max(0,idx-50):idx+100]}...")
        print()

# Save first 5000 chars and chars around data-class-spec
print("\n=== Around data-class-spec ===")
idx = html.find('data-class-spec')
if idx >= 0:
    print(html[max(0,idx-200):idx+500])

# Look at the full range of spell links
print("\n=== All spell href contexts (first 20) ===")
spell_re = re.compile(r'spell=(\d+)/([a-z0-9\-]+)')
all_spells = spell_re.findall(html)
for s in all_spells[:20]:
    idx = html.find(f'spell={s[0]}/{s[1]}')
    print(f"spell={s[0]}/{s[1]} at pos {idx}")
    # show 200 chars around it
    print(f"  {html[max(0,idx-100):idx+200]}")
    print()
