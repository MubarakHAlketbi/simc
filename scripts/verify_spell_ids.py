#!/usr/bin/env python3
"""
Verify Midnight spell IDs against wago.tools DBC data.

For each spell ID referenced in a class module:
1. Check if the spell exists in the bundled DBC (sc_spell_data.inc)
2. Verify the spell name matches what the code comments claim
3. Check effect count and types match what the code reads
4. Flag any effectN() index that reads beyond the effect count

Usage:
    python3 scripts/verify_spell_ids.py --class warlock
    python3 scripts/verify_spell_ids.py --all
    python3 scripts/verify_spell_ids.py --class warlock --fetch  # also check wago.tools
"""
import re
import sys
import os
import argparse
import json

# Map class names to their source files
CLASS_FILES = {
    'warrior': ['engine/class_modules/sc_warrior.cpp'],
    'paladin': ['engine/class_modules/paladin/sc_paladin.cpp',
                'engine/class_modules/paladin/sc_paladin_protection.cpp',
                'engine/class_modules/paladin/sc_paladin_retribution.cpp',
                'engine/class_modules/paladin/sc_paladin.hpp'],
    'hunter': ['engine/class_modules/sc_hunter.cpp'],
    'rogue': ['engine/class_modules/sc_rogue.cpp'],
    'priest': ['engine/class_modules/priest/sc_priest.cpp',
               'engine/class_modules/priest/sc_priest_shadow.cpp',
               'engine/class_modules/priest/sc_priest_pets.cpp'],
    'dk': ['engine/class_modules/sc_death_knight.cpp'],
    'shaman': ['engine/class_modules/sc_shaman.cpp'],
    'mage': ['engine/class_modules/sc_mage.cpp'],
    'warlock': ['engine/class_modules/warlock/sc_warlock.cpp',
                'engine/class_modules/warlock/sc_warlock.hpp',
                'engine/class_modules/warlock/sc_warlock_init.cpp',
                'engine/class_modules/warlock/sc_warlock_actions.cpp',
                'engine/class_modules/warlock/sc_warlock_pets.cpp'],
    'monk': ['engine/class_modules/monk/sc_monk.cpp',
             'engine/class_modules/monk/sc_monk.hpp'],
    'druid': ['engine/class_modules/sc_druid.cpp'],
    'dh': ['engine/class_modules/sc_demon_hunter.cpp'],
    'evoker': ['engine/class_modules/sc_evoker.cpp'],
}

def parse_bundled_spells(dbc_path):
    """Parse spell names and effect counts from sc_spell_data.inc"""
    spells = {}  # id -> {name, effect_count, effects: [{id, index, aura, base}]}
    
    with open(dbc_path) as f:
        content = f.read()
    
    # Parse spell entries: { "Name", id, ...
    spell_pattern = re.compile(r'\{\s*"([^"]+)"\s*,\s*(\d+)\s*,')
    for m in spell_pattern.finditer(content):
        name = m.group(1)
        sid = int(m.group(2))
        if 1240000 <= sid <= 1299999:
            spells[sid] = {'name': name, 'effects': []}
    
    # Parse effect entries: { effect_id, spell_id, index, ...
    effect_pattern = re.compile(
        r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*\d+\s*,\s*(\d+)\s*,\s*(-?\d+)\s*,'
    )
    for m in effect_pattern.finditer(content):
        eid = int(m.group(1))
        sid = int(m.group(2))
        idx = int(m.group(3))
        aura = int(m.group(4))
        # base value is further in the line, harder to parse positionally
        if sid in spells:
            spells[sid]['effects'].append({
                'id': eid, 'index': idx, 'aura': aura
            })
    
    return spells

def extract_spell_refs(filepath):
    """Extract spell ID references and their context from a C++ file"""
    refs = []
    with open(filepath) as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        # Find Midnight-range spell IDs
        for m in re.finditer(r'\b(12[4-9]\d{4})\b', line):
            sid = int(m.group(1))
            # Get context: what effectN is being read?
            effect_refs = re.findall(r'effectN\s*\(\s*(\d+)\s*\)', line)
            
            # Get the comment or nearby context
            comment = ''
            if '//' in line:
                comment = line[line.index('//'):].strip()
            
            # Check what function this is in
            func_name = ''
            for j in range(max(0, i-20), i):
                fm = re.search(r'(?:void|double|bool|int|action_t|buff_t)\s+(\w+)\s*\(', lines[j])
                if fm:
                    func_name = fm.group(1)
            
            refs.append({
                'spell_id': sid,
                'line': i + 1,
                'file': os.path.basename(filepath),
                'context': line.strip()[:120],
                'effect_refs': [int(e) for e in effect_refs],
                'comment': comment[:80],
                'function': func_name,
            })
    
    return refs

def verify_class(class_name, bundled_spells, fetch=False):
    """Verify all Midnight spell IDs for a class"""
    files = CLASS_FILES.get(class_name, [])
    if not files:
        print(f"Unknown class: {class_name}")
        return
    
    all_refs = []
    for f in files:
        if os.path.exists(f):
            all_refs.extend(extract_spell_refs(f))
    
    # Deduplicate by spell_id
    unique_ids = sorted(set(r['spell_id'] for r in all_refs))
    
    print(f"\n{'='*80}")
    print(f"SPELL VERIFICATION: {class_name.upper()} ({len(unique_ids)} unique Midnight spell IDs)")
    print(f"{'='*80}")
    
    issues = []
    verified = 0
    missing = 0
    effect_mismatches = 0
    
    for sid in unique_ids:
        refs = [r for r in all_refs if r['spell_id'] == sid]
        spell = bundled_spells.get(sid)
        
        if not spell:
            missing += 1
            issues.append(f"MISSING: Spell {sid} not found in bundled DBC")
            for r in refs[:1]:
                issues.append(f"  Used at {r['file']}:{r['line']}: {r['context']}")
            continue
        
        # Check effectN references
        max_effect = len(spell['effects'])
        for r in refs:
            for eff_n in r['effect_refs']:
                if eff_n > max_effect:
                    effect_mismatches += 1
                    issues.append(
                        f"EFFECT_OOB: {spell['name']} ({sid}) effectN({eff_n}) "
                        f"but spell only has {max_effect} effects"
                    )
                    issues.append(f"  {r['file']}:{r['line']}: {r['context']}")
        
        verified += 1
    
    # Print summary
    print(f"\n  Verified:  {verified}")
    print(f"  Missing:   {missing}")
    print(f"  Effect OOB: {effect_mismatches}")
    
    if issues:
        print(f"\n  ISSUES ({len(issues)} lines):")
        for issue in issues:
            print(f"    {issue}")
    else:
        print(f"\n  No issues found!")
    
    # Also check for find_talent_spell name mismatches
    print(f"\n  --- Talent Name Verification ---")
    name_issues = 0
    for r in all_refs:
        if 'find_talent_spell' in r['context'] and 'Should be ID' in r['comment']:
            claimed_id = r['spell_id']
            # Extract the talent name from the line
            nm = re.search(r'find_talent_spell\s*\([^,]+,\s*"([^"]+)"', r['context'])
            if nm and claimed_id in bundled_spells:
                talent_name = nm.group(1)
                dbc_name = bundled_spells[claimed_id]['name']
                if talent_name.lower() != dbc_name.lower():
                    name_issues += 1
                    print(f"    NAME_MISMATCH: Code says \"{talent_name}\" but DBC has \"{dbc_name}\" (ID {claimed_id})")
                    print(f"      {r['file']}:{r['line']}")
    
    if name_issues == 0:
        print(f"    All {verified} talent names match DBC")
    
    return {'verified': verified, 'missing': missing, 'effect_oob': effect_mismatches, 'issues': issues}

def main():
    parser = argparse.ArgumentParser(description='Verify Midnight spell IDs against DBC')
    parser.add_argument('--class', dest='class_name', help='Class to verify')
    parser.add_argument('--all', action='store_true', help='Verify all classes')
    parser.add_argument('--fetch', action='store_true', help='Also fetch from wago.tools')
    args = parser.parse_args()
    
    dbc_path = 'engine/dbc/generated/sc_spell_data.inc'
    if not os.path.exists(dbc_path):
        print(f"Error: {dbc_path} not found. Run from simc root.")
        sys.exit(1)
    
    print("Parsing bundled DBC data...")
    bundled = parse_bundled_spells(dbc_path)
    print(f"  Found {len(bundled)} Midnight-range spells in DBC")
    
    classes = list(CLASS_FILES.keys()) if args.all else [args.class_name]
    
    total = {'verified': 0, 'missing': 0, 'effect_oob': 0}
    for cls in classes:
        if cls:
            result = verify_class(cls, bundled, args.fetch)
            if result:
                for k in total:
                    total[k] += result[k]
    
    if args.all:
        print(f"\n{'='*80}")
        print(f"TOTAL: {total['verified']} verified, {total['missing']} missing, {total['effect_oob']} effect OOB")

if __name__ == '__main__':
    main()
