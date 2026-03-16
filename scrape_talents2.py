#!/usr/bin/env python3
"""Scrape all talent calc pages with correct tree separation"""
from dotenv import load_dotenv
import os, re, json, time
load_dotenv('/home/mubarak/.hermes/.env')
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])

node_re = re.compile(
    r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
    r'[^>]*?aria-label=["\']([^"\']+)["\']',
    re.DOTALL
)

def parse_section(html_section):
    matches = node_re.findall(html_section)
    seen = set()
    talents = []
    for spell_id, slug, name in matches:
        key = (spell_id, name)
        if key not in seen:
            seen.add(key)
            talents.append({'spell_id': spell_id, 'slug': slug, 'name': name})
    return talents

def scrape_talent_calc(url, class_spec, hero_name):
    """Scrape a talent calculator page and return class, spec, hero talents"""
    print(f"  Scraping: {url}")
    result = app.scrape(url, formats=['html'])
    html = result.html if hasattr(result, 'html') else result.get('html', '')
    print(f"  HTML length: {len(html)}")
    
    if not html:
        return [], [], []
    
    # Find tree type boundaries
    class_tree_start = html.find('data-tree-type="class"')
    spec_tree_start = html.find('data-tree-type="spec"')
    hero_tree_start = html.find('data-tree-type="hero"')
    
    print(f"  Tree positions: class={class_tree_start}, spec={spec_tree_start}, hero={hero_tree_start}")
    
    if class_tree_start >= 0 and spec_tree_start >= 0:
        class_section = html[class_tree_start:spec_tree_start]
        spec_section = html[spec_tree_start:hero_tree_start if hero_tree_start >= 0 else len(html)]
        hero_section = html[hero_tree_start:] if hero_tree_start >= 0 else ""
    else:
        print(f"  WARNING: Could not find tree sections, using fallback")
        class_section = html
        spec_section = ""
        hero_section = ""
    
    class_talents = parse_section(class_section)
    spec_talents = parse_section(spec_section)
    hero_talents = parse_section(hero_section)
    
    # Get hero tree name from HTML
    hero_title = "Unknown"
    if hero_tree_start >= 0:
        title_match = re.search(r'dragonflight-talent-trees-tree-title-name[^>]*>([^<]+)<', html[hero_tree_start:hero_tree_start+500])
        if title_match:
            hero_title = title_match.group(1).strip()
    
    print(f"  Class: {len(class_talents)}, Spec: {len(spec_talents)}, Hero: {len(hero_talents)} ({hero_title})")
    
    return class_talents, spec_talents, hero_talents, hero_title

# All talent calc URLs to scrape
specs = [
    ("https://www.wowhead.com/talent-calc/rogue/outlaw/fatebound", "rogue-outlaw", "fatebound", "rogue_outlaw_fatebound"),
    ("https://www.wowhead.com/talent-calc/rogue/outlaw/trickster", "rogue-outlaw", "trickster", "rogue_outlaw_trickster"),
    ("https://www.wowhead.com/talent-calc/rogue/subtlety/deathstalker", "rogue-subtlety", "deathstalker", "rogue_subtlety_deathstalker"),
    ("https://www.wowhead.com/talent-calc/rogue/subtlety/trickster", "rogue-subtlety", "trickster", "rogue_subtlety_trickster"),
    ("https://www.wowhead.com/talent-calc/shaman/elemental/farseer", "shaman-elemental", "farseer", "shaman_elemental_farseer"),
    ("https://www.wowhead.com/talent-calc/shaman/elemental/stormbringer", "shaman-elemental", "stormbringer", "shaman_elemental_stormbringer"),
    ("https://www.wowhead.com/talent-calc/shaman/enhancement/stormbringer", "shaman-enhancement", "stormbringer", "shaman_enhancement_stormbringer"),
    ("https://www.wowhead.com/talent-calc/shaman/enhancement/totemic", "shaman-enhancement", "totemic", "shaman_enhancement_totemic"),
    ("https://www.wowhead.com/talent-calc/warlock/affliction/hellcaller", "warlock-affliction", "hellcaller", "warlock_affliction_hellcaller"),
    ("https://www.wowhead.com/talent-calc/warlock/affliction/soul-harvester", "warlock-affliction", "soul-harvester", "warlock_affliction_soul_harvester"),
    ("https://www.wowhead.com/talent-calc/warlock/demonology/diabolist", "warlock-demonology", "diabolist", "warlock_demonology_diabolist"),
    ("https://www.wowhead.com/talent-calc/warlock/demonology/soul-harvester", "warlock-demonology", "soul-harvester", "warlock_demonology_soul_harvester"),
    ("https://www.wowhead.com/talent-calc/warlock/destruction/diabolist", "warlock-destruction", "diabolist", "warlock_destruction_diabolist"),
    ("https://www.wowhead.com/talent-calc/warlock/destruction/hellcaller", "warlock-destruction", "hellcaller", "warlock_destruction_hellcaller"),
    ("https://www.wowhead.com/talent-calc/warrior/arms/colossus", "warrior-arms", "colossus", "warrior_arms_colossus"),
    ("https://www.wowhead.com/talent-calc/warrior/arms/slayer", "warrior-arms", "slayer", "warrior_arms_slayer"),
    ("https://www.wowhead.com/talent-calc/warrior/fury/mountain-thane", "warrior-fury", "mountain-thane", "warrior_fury_mountain_thane"),
    ("https://www.wowhead.com/talent-calc/warrior/fury/slayer", "warrior-fury", "slayer", "warrior_fury_slayer"),
    ("https://www.wowhead.com/talent-calc/warrior/protection/colossus", "warrior-protection", "colossus", "warrior_protection_colossus"),
    ("https://www.wowhead.com/talent-calc/warrior/protection/mountain-thane", "warrior-protection", "mountain-thane", "warrior_protection_mountain_thane"),
]

results = {}
for url, class_spec, hero_name, key in specs:
    print(f"\nProcessing {key}...")
    try:
        c_talents, s_talents, h_talents, hero_title = scrape_talent_calc(url, class_spec, hero_name)
        results[key] = {
            'class_talents': c_talents,
            'spec_talents': s_talents,
            'hero_talents': h_talents,
            'hero_name': hero_name,
            'hero_title': hero_title,
            'class_spec': class_spec
        }
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        results[key] = {
            'error': str(e),
            'class_talents': [], 'spec_talents': [], 'hero_talents': [],
            'hero_name': hero_name, 'hero_title': hero_name, 'class_spec': class_spec
        }
    
    time.sleep(0.5)

# Save results
with open('/home/mubarak/simc/talent_data2.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nDone! Saved to talent_data2.json")

# Summary
for key, data in results.items():
    ct = len(data.get('class_talents', []))
    st = len(data.get('spec_talents', []))
    ht = len(data.get('hero_talents', []))
    hero_title = data.get('hero_title', '?')
    print(f"  {key}: class={ct}, spec={st}, hero={ht} ({hero_title})")
