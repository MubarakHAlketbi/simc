#!/usr/bin/env python3
"""Fetch remaining guide pages using Firecrawl"""
from dotenv import load_dotenv
import os, json, time
load_dotenv('/home/mubarak/.hermes/.env')
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ['FIRECRAWL_API_KEY'])

def fetch_page(url):
    """Fetch a page and return markdown content"""
    try:
        result = app.scrape(url, formats=['markdown'])
        md = result.markdown if hasattr(result, 'markdown') else result.get('markdown', '')
        return md
    except Exception as e:
        return f"ERROR: {e}"

# Pages that failed with web_extract (403 key limit exceeded)
pages_to_fetch = {
    # Rogue enchants
    'rogue_outlaw_enchants': 'https://www.wowhead.com/guide/classes/rogue/outlaw/enchants-gems-pve-dps',
    'rogue_subtlety_enchants': 'https://www.wowhead.com/guide/classes/rogue/subtlety/enchants-gems-pve-dps',
    
    # Shaman enchants  
    'shaman_elemental_enchants': 'https://www.wowhead.com/guide/classes/shaman/elemental/enchants-gems-pve-dps',
    'shaman_enhancement_enchants': 'https://www.wowhead.com/guide/classes/shaman/enhancement/enchants-gems-pve-dps',
    
    # Warlock - all pages needed
    'warlock_affliction_enchants': 'https://www.wowhead.com/guide/classes/warlock/affliction/enchants-gems-pve-dps',
    'warlock_demonology_overview': 'https://www.wowhead.com/guide/classes/warlock/demonology/overview-pve-dps',
    'warlock_demonology_basics': 'https://www.wowhead.com/guide/classes/warlock/demonology/basics',
    'warlock_demonology_abilities': 'https://www.wowhead.com/guide/classes/warlock/demonology/abilities-talents-pve-dps',
    'warlock_demonology_stats': 'https://www.wowhead.com/guide/classes/warlock/demonology/stat-priority-pve-dps',
    'warlock_demonology_rotation': 'https://www.wowhead.com/guide/classes/warlock/demonology/rotation-cooldowns-pve-dps',
    'warlock_demonology_enchants': 'https://www.wowhead.com/guide/classes/warlock/demonology/enchants-gems-pve-dps',
    'warlock_destruction_overview': 'https://www.wowhead.com/guide/classes/warlock/destruction/overview-pve-dps',
    'warlock_destruction_basics': 'https://www.wowhead.com/guide/classes/warlock/destruction/basics',
    'warlock_destruction_abilities': 'https://www.wowhead.com/guide/classes/warlock/destruction/abilities-talents-pve-dps',
    'warlock_destruction_stats': 'https://www.wowhead.com/guide/classes/warlock/destruction/stat-priority-pve-dps',
    'warlock_destruction_rotation': 'https://www.wowhead.com/guide/classes/warlock/destruction/rotation-cooldowns-pve-dps',
    'warlock_destruction_enchants': 'https://www.wowhead.com/guide/classes/warlock/destruction/enchants-gems-pve-dps',
    
    # Warrior - all pages needed
    'warrior_arms_overview': 'https://www.wowhead.com/guide/classes/warrior/arms/overview-pve-dps',
    'warrior_arms_basics': 'https://www.wowhead.com/guide/classes/warrior/arms/basics',
    'warrior_arms_abilities': 'https://www.wowhead.com/guide/classes/warrior/arms/abilities-talents-pve-dps',
    'warrior_arms_stats': 'https://www.wowhead.com/guide/classes/warrior/arms/stat-priority-pve-dps',
    'warrior_arms_rotation': 'https://www.wowhead.com/guide/classes/warrior/arms/rotation-cooldowns-pve-dps',
    'warrior_arms_enchants': 'https://www.wowhead.com/guide/classes/warrior/arms/enchants-gems-pve-dps',
    'warrior_fury_overview': 'https://www.wowhead.com/guide/classes/warrior/fury/overview-pve-dps',
    'warrior_fury_basics': 'https://www.wowhead.com/guide/classes/warrior/fury/basics',
    'warrior_fury_abilities': 'https://www.wowhead.com/guide/classes/warrior/fury/abilities-talents-pve-dps',
    'warrior_fury_stats': 'https://www.wowhead.com/guide/classes/warrior/fury/stat-priority-pve-dps',
    'warrior_fury_rotation': 'https://www.wowhead.com/guide/classes/warrior/fury/rotation-cooldowns-pve-dps',
    'warrior_fury_enchants': 'https://www.wowhead.com/guide/classes/warrior/fury/enchants-gems-pve-dps',
    'warrior_protection_overview': 'https://www.wowhead.com/guide/classes/warrior/protection/overview-pve-tank',
    'warrior_protection_basics': 'https://www.wowhead.com/guide/classes/warrior/protection/basics',
    'warrior_protection_abilities': 'https://www.wowhead.com/guide/classes/warrior/protection/abilities-talents-pve-tank',
    'warrior_protection_stats': 'https://www.wowhead.com/guide/classes/warrior/protection/stat-priority-pve-tank',
    'warrior_protection_rotation': 'https://www.wowhead.com/guide/classes/warrior/protection/rotation-cooldowns-pve-tank',
    'warrior_protection_enchants': 'https://www.wowhead.com/guide/classes/warrior/protection/enchants-gems-pve-tank',
    
    # Shaman elemental stats (failed earlier)
    'shaman_elemental_stats': 'https://www.wowhead.com/guide/classes/shaman/elemental/stat-priority-pve-dps',
}

results = {}
for key, url in pages_to_fetch.items():
    print(f"Fetching {key}...")
    content = fetch_page(url)
    results[key] = {'url': url, 'content': content}
    if content.startswith('ERROR'):
        print(f"  ERROR: {content[:100]}")
    else:
        print(f"  OK: {len(content)} chars")
    time.sleep(0.5)

with open('/home/mubarak/simc/guide_data.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f"Saved {len(results)} pages to guide_data.json")
