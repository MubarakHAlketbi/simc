#!/usr/bin/env python3
"""Scrape all talent calc pages and save as JSON"""
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
    """Scrape a talent calculator page and return class/spec talents + hero talents"""
    print(f"  Scraping: {url}")
    result = app.scrape(url, formats=['html'])
    html = result.html if hasattr(result, 'html') else result.get('html', '')
    print(f"  HTML length: {len(html)}")
    
    if not html:
        return [], []
    
    # Find the class-spec section
    spec_marker = f'data-class-spec="{class_spec}"'
    spec_idx = html.find(spec_marker)
    
    if spec_idx >= 0:
        # Get a chunk starting before the spec marker and extending well into the tree
        spec_section_start = max(0, spec_idx - 5000)
        # Find end - look for another major section marker or take 200k chars
        spec_section = html[spec_section_start:spec_idx + 200000]
    else:
        print(f"  WARNING: '{spec_marker}' not found, using full HTML")
        spec_section = html
    
    class_spec_talents = parse_section(spec_section)
    print(f"  Class/Spec talents found: {len(class_spec_talents)}")
    
    # For hero talents, try to find sections AFTER the class-spec tree
    # The hero tree is usually after the main tree
    if spec_idx >= 0:
        # Look in the HTML after the spec section for hero talents
        hero_search_start = spec_idx + 50000  # skip past the main tree
        hero_section = html[hero_search_start:]
    else:
        hero_section = html[len(html)//2:]
    
    hero_talents = parse_section(hero_section)
    
    # Remove duplicates that appear in class_spec (hero talents should be unique)
    class_spec_ids = {t['spell_id'] for t in class_spec_talents}
    hero_talents = [t for t in hero_talents if t['spell_id'] not in class_spec_ids]
    print(f"  Hero talents found: {len(hero_talents)}")
    
    return class_spec_talents, hero_talents

# All talent calc URLs to scrape
specs = [
    # (url, class_spec, hero_name, output_key)
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
        cs_talents, h_talents = scrape_talent_calc(url, class_spec, hero_name)
        results[key] = {
            'class_spec_talents': cs_talents,
            'hero_talents': h_talents,
            'hero_name': hero_name,
            'class_spec': class_spec
        }
        print(f"  Done: {len(cs_talents)} class/spec, {len(h_talents)} hero talents")
    except Exception as e:
        print(f"  ERROR: {e}")
        results[key] = {'error': str(e), 'class_spec_talents': [], 'hero_talents': [], 'hero_name': hero_name, 'class_spec': class_spec}
    
    time.sleep(1)  # Rate limiting

# Save results
with open('/home/mubarak/simc/talent_data.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nDone! Saved to talent_data.json")
print(f"Keys: {list(results.keys())}")
