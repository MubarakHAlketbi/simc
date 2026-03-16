#!/usr/bin/env python3
"""Fix hero talent separation in all info_base.md files."""

import os
import re
import time
from pathlib import Path

FIRECRAWL_API_KEY = os.environ.get('FIRECRAWL_API_KEY', '')
if not FIRECRAWL_API_KEY:
    env_file = Path.home() / '.hermes' / '.env'
    with open(env_file) as f:
        for line in f:
            if line.startswith('FIRECRAWL_API_KEY='):
                FIRECRAWL_API_KEY = line.split('=', 1)[1].strip()
                break

from firecrawl import Firecrawl
app = Firecrawl(api_key=FIRECRAWL_API_KEY)

node_re = re.compile(
    r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
    r'[^>]*?aria-label=["\']([^"\']+)["\']',
    re.DOTALL
)

def get_talents_from_url(url):
    try:
        result = app.scrape(url=url, formats=['html'])
        html = result.html if hasattr(result, 'html') else ''
        seen = set()
        talents = []
        for m in node_re.finditer(html):
            spell_id, slug, name = m.group(1), m.group(2), m.group(3)
            key = (spell_id, name)
            if key not in seen:
                seen.add(key)
                talents.append({'spell_id': spell_id, 'slug': slug, 'name': name})
        return talents
    except Exception as e:
        print(f"  ERROR: {e}", flush=True)
        return []

def format_talent_list(talents):
    if not talents:
        return "No talent data available."
    lines = [f"- {t['spell_id']} | {t['name']} | {t['slug']}" for t in talents]
    return '\n'.join(lines)

ALL_SPECS = [
    {
        'class': 'death-knight', 'spec': 'blood',
        'hero_urls': [
            ('Deathbringer', 'https://www.wowhead.com/talent-calc/death-knight/blood/deathbringer'),
            ("San'layn", 'https://www.wowhead.com/talent-calc/death-knight/blood/sanlayn'),
        ],
    },
    {
        'class': 'death-knight', 'spec': 'frost',
        'hero_urls': [
            ('Deathbringer', 'https://www.wowhead.com/talent-calc/death-knight/frost/deathbringer'),
            ('Rider of the Apocalypse', 'https://www.wowhead.com/talent-calc/death-knight/frost/rider-of-the-apocalypse'),
        ],
    },
    {
        'class': 'death-knight', 'spec': 'unholy',
        'hero_urls': [
            ('Rider of the Apocalypse', 'https://www.wowhead.com/talent-calc/death-knight/unholy/rider-of-the-apocalypse'),
            ("San'layn", 'https://www.wowhead.com/talent-calc/death-knight/unholy/sanlayn'),
        ],
    },
    {
        'class': 'demon-hunter', 'spec': 'devourer',
        'hero_urls': [
            ('Annihilator', 'https://www.wowhead.com/talent-calc/demon-hunter/devourer/annihilator'),
            ('Void Scarred', 'https://www.wowhead.com/talent-calc/demon-hunter/devourer/void-scarred'),
        ],
    },
    {
        'class': 'demon-hunter', 'spec': 'havoc',
        'hero_urls': [
            ('Aldrachi Reaver', 'https://www.wowhead.com/talent-calc/demon-hunter/havoc/aldrachi-reaver'),
            ('Fel Scarred', 'https://www.wowhead.com/talent-calc/demon-hunter/havoc/fel-scarred'),
        ],
    },
    {
        'class': 'demon-hunter', 'spec': 'vengeance',
        'hero_urls': [
            ('Aldrachi Reaver', 'https://www.wowhead.com/talent-calc/demon-hunter/vengeance/aldrachi-reaver'),
            ('Annihilator', 'https://www.wowhead.com/talent-calc/demon-hunter/vengeance/annihilator'),
        ],
    },
    {
        'class': 'druid', 'spec': 'balance',
        'hero_urls': [
            ("Elune's Chosen", 'https://www.wowhead.com/talent-calc/druid/balance/elunes-chosen'),
            ('Keeper of the Grove', 'https://www.wowhead.com/talent-calc/druid/balance/keeper-of-the-grove'),
        ],
    },
    {
        'class': 'druid', 'spec': 'feral',
        'hero_urls': [
            ('Druid of the Claw', 'https://www.wowhead.com/talent-calc/druid/feral/druid-of-the-claw'),
            ('Wildstalker', 'https://www.wowhead.com/talent-calc/druid/feral/wildstalker'),
        ],
    },
    {
        'class': 'druid', 'spec': 'guardian',
        'hero_urls': [
            ('Druid of the Claw', 'https://www.wowhead.com/talent-calc/druid/guardian/druid-of-the-claw'),
            ("Elune's Chosen", 'https://www.wowhead.com/talent-calc/druid/guardian/elunes-chosen'),
        ],
    },
    {
        'class': 'evoker', 'spec': 'augmentation',
        'hero_urls': [
            ('Chronowarden', 'https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden'),
            ('Scalecommander', 'https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander'),
        ],
    },
    {
        'class': 'evoker', 'spec': 'devastation',
        'hero_urls': [
            ('Flameshaper', 'https://www.wowhead.com/talent-calc/evoker/devastation/flameshaper'),
            ('Scalecommander', 'https://www.wowhead.com/talent-calc/evoker/devastation/scalecommander'),
        ],
    },
]

def process_spec_talents(spec_info):
    cls = spec_info['class']
    spec = spec_info['spec']
    print(f"\nProcessing hero talents: {cls}/{spec}", flush=True)
    
    # Get talents from both hero pages
    talents_by_hero = {}
    for hero_name, hero_url in spec_info['hero_urls']:
        print(f"  Fetching: {hero_url}", flush=True)
        talents = get_talents_from_url(hero_url)
        talents_by_hero[hero_name] = talents
        print(f"  Got {len(talents)} total talents", flush=True)
        time.sleep(1)
    
    hero_names = [h for h, _ in spec_info['hero_urls']]
    if len(hero_names) < 2:
        return
    
    # Compute shared (class+spec) and unique (hero) talents
    t1 = talents_by_hero[hero_names[0]]
    t2 = talents_by_hero[hero_names[1]]
    
    k1 = {(t['spell_id'], t['name']) for t in t1}
    k2 = {(t['spell_id'], t['name']) for t in t2}
    
    shared_keys = k1 & k2
    
    class_spec_talents = [t for t in t1 if (t['spell_id'], t['name']) in shared_keys]
    hero1_talents = [t for t in t1 if (t['spell_id'], t['name']) not in shared_keys]
    hero2_talents = [t for t in t2 if (t['spell_id'], t['name']) not in shared_keys]
    
    print(f"  Class/spec: {len(class_spec_talents)}, {hero_names[0]}: {len(hero1_talents)}, {hero_names[1]}: {len(hero2_talents)}", flush=True)
    
    # Update the info_base.md
    info_path = Path(f'wowhead/{cls}/{spec}/info_base.md')
    if not info_path.exists():
        print(f"  WARN: {info_path} not found!", flush=True)
        return
    
    content = info_path.read_text()
    
    # Replace the talent tree section
    new_talent_section = f"""## Talent Tree — Class & Spec Tree Talents
{format_talent_list(class_spec_talents)}

## Hero Talent Trees
### {hero_names[0]}
{format_talent_list(hero1_talents)}

### {hero_names[1]}
{format_talent_list(hero2_talents)}

"""
    
    # Find and replace the talent section in the file
    # The section runs from "## Talent Tree" to "## Rotation"
    talent_section_re = re.compile(
        r'## Talent Tree.*?(?=## Rotation / Priority)',
        re.DOTALL
    )
    
    new_content = talent_section_re.sub(new_talent_section, content)
    
    if new_content == content:
        print(f"  WARN: Pattern not found in {info_path}", flush=True)
    else:
        info_path.write_text(new_content)
        print(f"  Updated: {info_path}", flush=True)


for spec_info in ALL_SPECS:
    try:
        process_spec_talents(spec_info)
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        import traceback
        traceback.print_exc()

print("\nAll specs updated!", flush=True)
