#!/usr/bin/env python3
from dotenv import load_dotenv
import os, re
load_dotenv('/home/mubarak/.hermes/.env')
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])

url = "https://www.wowhead.com/talent-calc/rogue/outlaw/fatebound"
result = app.scrape(url, formats=['html'])
html = result.html if hasattr(result, 'html') else result.get('html', '')

# Find all tree-type occurrences
tree_re = re.compile(r'data-tree-type="([^"]+)"')
tree_types = tree_re.findall(html)
print(f"All data-tree-type values: {tree_types}")

# Find positions and names of each tree section
print("\n=== Tree sections ===")
for m in tree_re.finditer(html):
    pos = m.start()
    tree_type = m.group(1)
    # Get the tree title near this
    context = html[pos:pos+300]
    # Look for tree title
    title_m = re.search(r'dragonflight-talent-trees-tree-title-name[^>]*>([^<]+)<', context)
    title = title_m.group(1) if title_m else "?"
    print(f"  data-tree-type='{tree_type}' at pos {pos}: '{title}'")

# Find where each tree section starts and ends
print("\n=== Looking for tree boundaries ===")
class_tree_start = html.find('data-tree-type="class"')
spec_tree_start = html.find('data-tree-type="spec"')
hero_tree_start = html.find('data-tree-type="hero"')
print(f"Class tree at: {class_tree_start}")
print(f"Spec tree at: {spec_tree_start}")
print(f"Hero tree at: {hero_tree_start}")

# Count spells in each section
node_re = re.compile(
    r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
    r'[^>]*?aria-label=["\']([^"\']+)["\']',
    re.DOTALL
)

if class_tree_start >= 0 and spec_tree_start >= 0:
    class_section = html[class_tree_start:spec_tree_start]
    spec_section = html[spec_tree_start:hero_tree_start if hero_tree_start >= 0 else len(html)]
    hero_section = html[hero_tree_start:] if hero_tree_start >= 0 else ""
    
    class_talents = node_re.findall(class_section)
    spec_talents = node_re.findall(spec_section)
    hero_talents = node_re.findall(hero_section)
    
    print(f"\nClass tree talents: {len(class_talents)}")
    for t in class_talents[:5]:
        print(f"  {t[0]} | {t[2]}")
    
    print(f"\nSpec tree talents: {len(spec_talents)}")
    for t in spec_talents[:5]:
        print(f"  {t[0]} | {t[2]}")
    
    print(f"\nHero tree talents: {len(hero_talents)}")
    for t in hero_talents[:5]:
        print(f"  {t[0]} | {t[2]}")
