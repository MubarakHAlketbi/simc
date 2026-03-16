#!/usr/bin/env python3
"""Process WoW spec data from Wowhead: guides + talent trees -> info_base.md files"""

import os
import re
import json
import time
from pathlib import Path

# Load Firecrawl API key
FIRECRAWL_API_KEY = os.environ.get('FIRECRAWL_API_KEY', '')
if not FIRECRAWL_API_KEY:
    # Try loading from .env
    env_file = Path.home() / '.hermes' / '.env'
    with open(env_file) as f:
        for line in f:
            if line.startswith('FIRECRAWL_API_KEY='):
                FIRECRAWL_API_KEY = line.split('=', 1)[1].strip()
                break

from firecrawl import Firecrawl
app = Firecrawl(api_key=FIRECRAWL_API_KEY)

def scrape_page(url, fmt='markdown'):
    """Scrape a URL using Firecrawl."""
    try:
        result = app.scrape(url=url, formats=[fmt])
        if fmt == 'html':
            return result.html if hasattr(result, 'html') else ''
        else:
            return result.markdown if hasattr(result, 'markdown') else ''
    except Exception as e:
        print(f"  ERROR scraping {url}: {e}")
        return ''

def parse_talents_from_html(html, class_spec_key):
    """Extract talent nodes from Firecrawl HTML.
    Returns dict with 'class_spec_talents' and 'hero_talents'.
    """
    node_re = re.compile(
        r'href=["\']https://www\.wowhead\.com/(?:beta/)?spell=(\d+)/([a-z0-9\-]+)[^"\']*["\']'
        r'[^>]*?aria-label=["\']([^"\']+)["\']',
        re.DOTALL
    )
    
    # Find the data-class-spec section
    spec_section = ''
    spec_match = re.search(
        rf'data-class-spec=["\']({re.escape(class_spec_key)})["\'][^>]*>(.*?)(?=data-class-spec=|$)',
        html, re.DOTALL
    )
    
    # Alternative: find the container div with data-class-spec
    spec_container_re = re.compile(
        rf'data-class-spec=["\']{re.escape(class_spec_key)}["\']',
        re.DOTALL
    )
    spec_pos = spec_container_re.search(html)
    
    class_spec_talents = []
    hero_talents = []
    
    if spec_pos:
        # Get the surrounding section - look for the opening tag
        start = html.rfind('<', 0, spec_pos.start())
        # Find end of this section by looking for closing tag depth
        section_start = start
        # Just grab a large chunk
        section_end = min(len(html), section_start + 200000)
        spec_section = html[section_start:section_end]
        
        # Find talent nodes in this section
        seen = set()
        for m in node_re.finditer(spec_section):
            spell_id, slug, name = m.group(1), m.group(2), m.group(3)
            key = (spell_id, name)
            if key not in seen:
                seen.add(key)
                class_spec_talents.append({'spell_id': spell_id, 'slug': slug, 'name': name})
    
    # For hero talents: find section outside the class-spec container
    # Look for hero talent sections marked differently
    # The hero tree is typically in a separate container before/after the class-spec section
    
    # Find all spell links in the FULL html for hero talents
    # Hero talents appear outside the data-class-spec container
    # We'll get all talents and subtract the class/spec ones
    all_talents = []
    seen_all = set()
    for m in node_re.finditer(html):
        spell_id, slug, name = m.group(1), m.group(2), m.group(3)
        key = (spell_id, name)
        if key not in seen_all:
            seen_all.add(key)
            all_talents.append({'spell_id': spell_id, 'slug': slug, 'name': name})
    
    # Hero talents = all talents minus class/spec talents
    cs_keys = {(t['spell_id'], t['name']) for t in class_spec_talents}
    hero_talents = [t for t in all_talents if (t['spell_id'], t['name']) not in cs_keys]
    
    return {
        'class_spec_talents': class_spec_talents,
        'hero_talents': hero_talents,
        'all_talents': all_talents
    }

def format_talent_list(talents):
    """Format talent list for markdown."""
    if not talents:
        return "No talent data available."
    lines = []
    for t in talents:
        lines.append(f"- {t['spell_id']} | {t['name']} | {t['slug']}")
    return '\n'.join(lines)

def scrape_guide_page(url):
    """Scrape a guide page, returning markdown content."""
    print(f"  Fetching guide: {url}")
    content = scrape_page(url, 'markdown')
    if not content:
        print(f"  WARN: Empty content for {url}")
    return content

SPECS = [
    {
        'class': 'death-knight',
        'spec': 'blood',
        'role': 'Tank',
        'class_display': 'Death Knight',
        'spec_display': 'Blood',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/death-knight/blood/overview-pve-tank',
            'https://www.wowhead.com/guide/classes/death-knight/blood/basics',
            'https://www.wowhead.com/guide/classes/death-knight/blood/abilities-talents-pve-tank',
            'https://www.wowhead.com/guide/classes/death-knight/blood/stat-priority-pve-tank',
            'https://www.wowhead.com/guide/classes/death-knight/blood/rotation-cooldowns-pve-tank',
            'https://www.wowhead.com/guide/classes/death-knight/blood/enchants-gems-pve-tank',
        ],
        'hero_urls': [
            ('deathbringer', 'https://www.wowhead.com/talent-calc/death-knight/blood/deathbringer'),
            ('sanlayn', 'https://www.wowhead.com/talent-calc/death-knight/blood/sanlayn'),
        ],
        'class_spec_key': 'death-knight-blood',
    },
    {
        'class': 'death-knight',
        'spec': 'frost',
        'role': 'DPS',
        'class_display': 'Death Knight',
        'spec_display': 'Frost',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/death-knight/frost/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/frost/basics',
            'https://www.wowhead.com/guide/classes/death-knight/frost/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/frost/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/frost/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/frost/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('deathbringer', 'https://www.wowhead.com/talent-calc/death-knight/frost/deathbringer'),
            ('rider-of-the-apocalypse', 'https://www.wowhead.com/talent-calc/death-knight/frost/rider-of-the-apocalypse'),
        ],
        'class_spec_key': 'death-knight-frost',
    },
    {
        'class': 'death-knight',
        'spec': 'unholy',
        'role': 'DPS',
        'class_display': 'Death Knight',
        'spec_display': 'Unholy',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/death-knight/unholy/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/unholy/basics',
            'https://www.wowhead.com/guide/classes/death-knight/unholy/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/unholy/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/unholy/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/death-knight/unholy/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('rider-of-the-apocalypse', 'https://www.wowhead.com/talent-calc/death-knight/unholy/rider-of-the-apocalypse'),
            ('sanlayn', 'https://www.wowhead.com/talent-calc/death-knight/unholy/sanlayn'),
        ],
        'class_spec_key': 'death-knight-unholy',
    },
    {
        'class': 'demon-hunter',
        'spec': 'devourer',
        'role': 'DPS',
        'class_display': 'Demon Hunter',
        'spec_display': 'Devourer',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/basics',
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/devourer/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('annihilator', 'https://www.wowhead.com/talent-calc/demon-hunter/devourer/annihilator'),
            ('void-scarred', 'https://www.wowhead.com/talent-calc/demon-hunter/devourer/void-scarred'),
        ],
        'class_spec_key': 'demon-hunter-devourer',
    },
    {
        'class': 'demon-hunter',
        'spec': 'havoc',
        'role': 'DPS',
        'class_display': 'Demon Hunter',
        'spec_display': 'Havoc',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/basics',
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/demon-hunter/havoc/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('aldrachi-reaver', 'https://www.wowhead.com/talent-calc/demon-hunter/havoc/aldrachi-reaver'),
            ('fel-scarred', 'https://www.wowhead.com/talent-calc/demon-hunter/havoc/fel-scarred'),
        ],
        'class_spec_key': 'demon-hunter-havoc',
    },
    {
        'class': 'demon-hunter',
        'spec': 'vengeance',
        'role': 'Tank',
        'class_display': 'Demon Hunter',
        'spec_display': 'Vengeance',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/overview-pve-tank',
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/basics',
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/abilities-talents-pve-tank',
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/stat-priority-pve-tank',
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/rotation-cooldowns-pve-tank',
            'https://www.wowhead.com/guide/classes/demon-hunter/vengeance/enchants-gems-pve-tank',
        ],
        'hero_urls': [
            ('aldrachi-reaver', 'https://www.wowhead.com/talent-calc/demon-hunter/vengeance/aldrachi-reaver'),
            ('annihilator', 'https://www.wowhead.com/talent-calc/demon-hunter/vengeance/annihilator'),
        ],
        'class_spec_key': 'demon-hunter-vengeance',
    },
    {
        'class': 'druid',
        'spec': 'balance',
        'role': 'DPS',
        'class_display': 'Druid',
        'spec_display': 'Balance',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/druid/balance/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/balance/basics',
            'https://www.wowhead.com/guide/classes/druid/balance/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/balance/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/balance/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/balance/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('elunes-chosen', 'https://www.wowhead.com/talent-calc/druid/balance/elunes-chosen'),
            ('keeper-of-the-grove', 'https://www.wowhead.com/talent-calc/druid/balance/keeper-of-the-grove'),
        ],
        'class_spec_key': 'druid-balance',
    },
    {
        'class': 'druid',
        'spec': 'feral',
        'role': 'DPS',
        'class_display': 'Druid',
        'spec_display': 'Feral',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/druid/feral/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/feral/basics',
            'https://www.wowhead.com/guide/classes/druid/feral/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/feral/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/feral/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/druid/feral/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('druid-of-the-claw', 'https://www.wowhead.com/talent-calc/druid/feral/druid-of-the-claw'),
            ('wildstalker', 'https://www.wowhead.com/talent-calc/druid/feral/wildstalker'),
        ],
        'class_spec_key': 'druid-feral',
    },
    {
        'class': 'druid',
        'spec': 'guardian',
        'role': 'Tank',
        'class_display': 'Druid',
        'spec_display': 'Guardian',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/druid/guardian/overview-pve-tank',
            'https://www.wowhead.com/guide/classes/druid/guardian/basics',
            'https://www.wowhead.com/guide/classes/druid/guardian/abilities-talents-pve-tank',
            'https://www.wowhead.com/guide/classes/druid/guardian/stat-priority-pve-tank',
            'https://www.wowhead.com/guide/classes/druid/guardian/rotation-cooldowns-pve-tank',
            'https://www.wowhead.com/guide/classes/druid/guardian/enchants-gems-pve-tank',
        ],
        'hero_urls': [
            ('druid-of-the-claw', 'https://www.wowhead.com/talent-calc/druid/guardian/druid-of-the-claw'),
            ('elunes-chosen', 'https://www.wowhead.com/talent-calc/druid/guardian/elunes-chosen'),
        ],
        'class_spec_key': 'druid-guardian',
    },
    {
        'class': 'evoker',
        'spec': 'augmentation',
        'role': 'Support DPS',
        'class_display': 'Evoker',
        'spec_display': 'Augmentation',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/evoker/augmentation/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/augmentation/basics',
            'https://www.wowhead.com/guide/classes/evoker/augmentation/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/augmentation/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/augmentation/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/augmentation/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('chronowarden', 'https://www.wowhead.com/talent-calc/evoker/augmentation/chronowarden'),
            ('scalecommander', 'https://www.wowhead.com/talent-calc/evoker/augmentation/scalecommander'),
        ],
        'class_spec_key': 'evoker-augmentation',
    },
    {
        'class': 'evoker',
        'spec': 'devastation',
        'role': 'DPS',
        'class_display': 'Evoker',
        'spec_display': 'Devastation',
        'guide_urls': [
            'https://www.wowhead.com/guide/classes/evoker/devastation/overview-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/devastation/basics',
            'https://www.wowhead.com/guide/classes/evoker/devastation/abilities-talents-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/devastation/stat-priority-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/devastation/rotation-cooldowns-pve-dps',
            'https://www.wowhead.com/guide/classes/evoker/devastation/enchants-gems-pve-dps',
        ],
        'hero_urls': [
            ('flameshaper', 'https://www.wowhead.com/talent-calc/evoker/devastation/flameshaper'),
            ('scalecommander', 'https://www.wowhead.com/talent-calc/evoker/devastation/scalecommander'),
        ],
        'class_spec_key': 'evoker-devastation',
    },
]

GUIDE_NAMES = ['overview', 'basics', 'abilities-talents', 'stat-priority', 'rotation-cooldowns', 'enchants-gems']


def process_spec(spec_info):
    cls = spec_info['class']
    spec = spec_info['spec']
    print(f"\n{'='*60}")
    print(f"Processing: {spec_info['class_display']} {spec_info['spec_display']}")
    print(f"{'='*60}")
    
    # Step 1: Fetch guide pages
    guide_contents = {}
    for i, url in enumerate(spec_info['guide_urls']):
        name = GUIDE_NAMES[i]
        print(f"  Guide [{i+1}/6]: {name}")
        content = scrape_guide_page(url)
        guide_contents[name] = content
        time.sleep(0.5)  # rate limit
    
    # Step 2: Fetch talent calc pages via Firecrawl HTML
    hero_talent_data = {}
    class_spec_talents = None
    
    for hero_name, hero_url in spec_info['hero_urls']:
        print(f"  Hero Talents [{hero_name}]: {hero_url}")
        html = scrape_page(hero_url, 'html')
        if not html:
            print(f"  WARN: Empty HTML for {hero_url}")
            hero_talent_data[hero_name] = []
            continue
        
        talents = parse_talents_from_html(html, spec_info['class_spec_key'])
        
        # First hero URL gives us the class/spec talents
        if class_spec_talents is None:
            class_spec_talents = talents['class_spec_talents']
        
        hero_talent_data[hero_name] = talents['hero_talents']
        print(f"  Found {len(talents['class_spec_talents'])} class/spec talents, {len(talents['hero_talents'])} hero talents")
        time.sleep(1)
    
    if class_spec_talents is None:
        class_spec_talents = []
    
    # Step 3: Write info_base.md
    output_path = Path(f'wowhead/{cls}/{spec}/info_base.md')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    all_sources = spec_info['guide_urls'] + [url for _, url in spec_info['hero_urls']]
    
    # Build the markdown content
    content = f"""# {spec_info['class_display']} {spec_info['spec_display']} — Midnight (12.0.1) Information Base
Generated: 2026-03-17
Sources:
{chr(10).join('- ' + url for url in all_sources)}

"""
    
    # Extract sections from guide content
    overview_text = guide_contents.get('overview', 'No data available.')
    basics_text = guide_contents.get('basics', 'No data available.')
    abilities_text = guide_contents.get('abilities-talents', 'No data available.')
    stat_text = guide_contents.get('stat-priority', 'No data available.')
    rotation_text = guide_contents.get('rotation-cooldowns', 'No data available.')
    enchants_text = guide_contents.get('enchants-gems', 'No data available.')
    
    content += f"""## Overview
{overview_text}

## Stat Priority
{stat_text}

## Core Abilities
{abilities_text}

## Talent Tree — Class & Spec Tree Talents
{format_talent_list(class_spec_talents)}

## Hero Talent Trees
"""
    
    for hero_name, hero_url in spec_info['hero_urls']:
        display_name = hero_name.replace('-', ' ').title()
        content += f"""### {display_name}
{format_talent_list(hero_talent_data.get(hero_name, []))}

"""
    
    content += f"""## Rotation / Priority
{rotation_text}

## Tier Set Bonuses (MID1)
Information about MID1 tier set bonuses not available in current guide pages. Check Wowhead's gear/tier set pages for the latest information.

## Enchants, Gems, Consumables
{enchants_text}

## SimC Implementation Notes
See abilities-talents guide section above for detailed mechanical interactions.
Key notes extracted from guide content:
{basics_text}
"""
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"  Written: {output_path} ({len(content)} chars)")
    return True


# Process all specs
results = []
for spec_info in SPECS:
    try:
        success = process_spec(spec_info)
        results.append((spec_info['class'], spec_info['spec'], success))
    except Exception as e:
        print(f"ERROR processing {spec_info['class']}/{spec_info['spec']}: {e}")
        import traceback
        traceback.print_exc()
        results.append((spec_info['class'], spec_info['spec'], False))

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
for cls, spec, success in results:
    status = "OK" if success else "FAILED"
    print(f"  {cls}/{spec}: {status}")
