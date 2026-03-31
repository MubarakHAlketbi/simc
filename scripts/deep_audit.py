#!/usr/bin/env python3
"""
Deep class module audit: trace spell variable assignments to effectN reads.

Strategy:
1. Parse all spell variable assignments: X = find_spell(ID), find_talent_spell(tree, ID), 
   sets->set(SPEC, TIER, BN), find_specialization_spell(ID), etc.
2. For each effectN(N) read, trace back through the variable chain to the spell ID
3. Check effectN(N) against DBC effect count
4. Flag from_seconds(base_value()) on values >= 1000

Usage:
    python3 scripts/deep_audit.py --class warrior
    python3 scripts/deep_audit.py --all
    python3 scripts/deep_audit.py --all --verbose
"""
import re
import sys
import os
import argparse
from collections import defaultdict

CLASS_FILES = {
    'warrior': ['engine/class_modules/sc_warrior.cpp'],
    'paladin': ['engine/class_modules/paladin/sc_paladin.cpp',
                'engine/class_modules/paladin/sc_paladin.hpp',
                'engine/class_modules/paladin/sc_paladin_protection.cpp',
                'engine/class_modules/paladin/sc_paladin_retribution.cpp',
                'engine/class_modules/paladin/sc_paladin_holy.cpp'],
    'hunter': ['engine/class_modules/sc_hunter.cpp'],
    'rogue': ['engine/class_modules/sc_rogue.cpp'],
    'priest': ['engine/class_modules/priest/sc_priest.cpp',
               'engine/class_modules/priest/sc_priest.hpp',
               'engine/class_modules/priest/sc_priest_shadow.cpp',
               'engine/class_modules/priest/sc_priest_discipline.cpp',
               'engine/class_modules/priest/sc_priest_holy.cpp',
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

def load_dbc_effects(dbc_path):
    """Load spell ID -> max effect index from DBC."""
    spells = {}  # spell_id -> {name, effects: {N: base_value}}
    
    with open(dbc_path) as f:
        for line in f:
            line = line.strip()
            # Spell header: { "Name", id, ...  }, /* eid1, eid2 */
            m = re.match(r'\{\s*"([^"]+)"\s*,\s*(\d+)\s*,', line)
            if m:
                name = m.group(1)
                sid = int(m.group(2))
                comment = re.search(r'/\*\s*([\d,\s]+)\s*\*/', line)
                ecount = 0
                if comment:
                    ecount = len([x.strip() for x in comment.group(1).split(',') if x.strip()])
                spells[sid] = {'name': name, 'effect_count': ecount, 'effects': {}}
            
            # Effect: { eid, spell_id, idx, type, subtype, ..., base_value(pos15), ...
            em = re.match(r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,', line)
            if em:
                eid = int(em.group(1))
                sid = int(em.group(2))
                idx = int(em.group(3))
                if sid in spells:
                    fields = line.split(',')
                    bv = 0.0
                    if len(fields) >= 16:
                        try:
                            bv = float(fields[15].strip())
                        except ValueError:
                            pass
                    spells[sid]['effects'][idx + 1] = bv  # 1-indexed
    
    return spells

def build_spell_map(filepath):
    """Parse a C++ file and build: variable_name -> spell_id mapping.
    
    Handles patterns:
    - X = find_spell(ID)
    - X = find_spell(ID, SPEC)
    - X = find_talent_spell(tree, ID)
    - X = find_talent_spell(tree, "Name")   -- can't resolve
    - X = find_specialization_spell(ID)
    - X = sets->set(SPEC, TIER, BN)  -- resolve from set bonus DBC
    - X = conditional_spell_lookup(cond, ID)
    """
    spell_map = {}  # partial var name -> spell_id
    
    if not os.path.exists(filepath):
        return spell_map
    
    with open(filepath) as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('//'):
            continue
        
        # Pattern: anything = ... find_spell(ID) ...
        # We want to capture the left side variable and the spell ID
        for m in re.finditer(r'(\w[\w.>:-]*\w)\s*=\s*[^;]*?find_spell\s*\(\s*(\d+)', line):
            var = m.group(1)
            sid = int(m.group(2))
            # Normalize: take last 2 parts of dotted name
            parts = re.split(r'[.>:-]+', var)
            key = parts[-1] if parts else var
            spell_map[key] = sid
            if len(parts) >= 2:
                spell_map['.'.join(parts[-2:])] = sid
        
        # conditional_spell_lookup
        for m in re.finditer(r'(\w[\w.>:-]*\w)\s*=\s*[^;]*?conditional_spell_lookup\s*\([^,]+,\s*(\d+)', line):
            var = m.group(1)
            sid = int(m.group(2))
            parts = re.split(r'[.>:-]+', var)
            key = parts[-1] if parts else var
            spell_map[key] = sid
        
        # find_talent_spell with ID (not name)
        for m in re.finditer(r'(\w[\w.>:-]*\w)\s*=\s*[^;]*?find_talent_spell\s*\([^,]+,\s*(\d+)', line):
            var = m.group(1)
            sid = int(m.group(2))
            parts = re.split(r'[.>:-]+', var)
            key = parts[-1] if parts else var
            spell_map[key] = sid
        
        # find_specialization_spell with ID
        for m in re.finditer(r'(\w[\w.>:-]*\w)\s*=\s*[^;]*?find_specialization_spell\s*\(\s*(\d+)', line):
            var = m.group(1)
            sid = int(m.group(2))
            parts = re.split(r'[.>:-]+', var)
            key = parts[-1] if parts else var
            spell_map[key] = sid
    
    return spell_map

def resolve_effectn_spell(line, lineno, lines, spell_map):
    """Try to determine the spell ID for an effectN call on a given line.
    Returns (spell_id, resolution_method) or (None, None).
    """
    # 1. Direct: find_spell(ID)->effectN(N)
    m = re.search(r'find_spell\s*\(\s*(\d+)[^)]*\)\s*->\s*effectN', line)
    if m:
        return int(m.group(1)), 'direct'
    
    # 2. Variable->effectN: X->effectN(N) or X.effectN(N)
    # Find the variable name before ->effectN or .effectN
    m = re.search(r'(\w[\w.>:-]*\w)\s*->\s*effectN\s*\(\s*(\d+)', line)
    if not m:
        m = re.search(r'(\w[\w.>:-]*\w)\s*\)\s*->\s*effectN\s*\(\s*(\d+)', line)
    if m:
        var = m.group(1)
        # Try various name resolutions
        parts = re.split(r'[.>:-]+', var)
        # Try exact, then last part, then last 2 parts
        for attempt in [var, parts[-1], '.'.join(parts[-2:]) if len(parts) >= 2 else None]:
            if attempt and attempt in spell_map:
                return spell_map[attempt], f'var:{attempt}'
    
    # 3. Chained: X->data().effectN(N)
    m = re.search(r'(\w[\w.>:-]*\w)\s*->\s*data\s*\(\s*\)\s*\.\s*effectN\s*\(\s*(\d+)', line)
    if m:
        var = m.group(1)
        parts = re.split(r'[.>:-]+', var)
        for attempt in [parts[-1], '.'.join(parts[-2:]) if len(parts) >= 2 else None]:
            if attempt and attempt in spell_map:
                return spell_map[attempt], f'data:{attempt}'
    
    # 4. set_bonuses/sets->set: inline resolution not easy, mark as tier_set
    if 'sets->set(' in line or 'set_bonuses.' in line or 'tier_set.' in line:
        return None, 'tier_set'
    
    return None, None

def audit_file(filepath, spells, verbose=False):
    """Audit a single C++ file for effectN issues."""
    issues = []
    stats = {'total': 0, 'resolved': 0, 'unresolved': 0, 'oob': 0, 'tier_set': 0}
    
    if not os.path.exists(filepath):
        return issues, stats
    
    # Build spell map for this file
    spell_map = build_spell_map(filepath)
    
    with open(filepath) as f:
        lines = f.readlines()
    
    fname = os.path.basename(filepath)
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('//'):
            continue
        
        for m in re.finditer(r'effectN\s*\(\s*(\d+)\s*\)', line):
            effect_n = int(m.group(1))
            stats['total'] += 1
            
            # What accessor?
            after = line[m.end():]
            acc_m = re.match(r'\s*\.\s*(\w+)', after)
            accessor = acc_m.group(1) if acc_m else ''
            
            sid, method = resolve_effectn_spell(line, i, lines, spell_map)
            
            if method == 'tier_set':
                stats['tier_set'] += 1
                stats['resolved'] += 1
                continue
            
            if sid is None:
                stats['unresolved'] += 1
                continue
            
            stats['resolved'] += 1
            
            if sid not in spells:
                continue
            
            spell = spells[sid]
            max_n = max(spell['effects'].keys()) if spell['effects'] else spell['effect_count']
            
            if max_n > 0 and effect_n > max_n:
                stats['oob'] += 1
                issues.append({
                    'type': 'EFFECT_OOB',
                    'file': fname,
                    'line': i + 1,
                    'spell_id': sid,
                    'spell_name': spell['name'],
                    'effect_n': effect_n,
                    'max_effects': max_n,
                    'context': stripped[:150],
                    'method': method,
                })
            
            # Check from_seconds + base_value pattern
            bv = spell['effects'].get(effect_n, 0)
            if isinstance(bv, (int, float)):
                if 'from_seconds' in line and ('base_value' in line or accessor == 'base_value'):
                    if abs(bv) >= 1000:
                        issues.append({
                            'type': 'FROM_SECONDS_MS',
                            'file': fname,
                            'line': i + 1,
                            'spell_id': sid,
                            'spell_name': spell['name'],
                            'effect_n': effect_n,
                            'base_value': bv,
                            'context': stripped[:150],
                        })
                
                # percent() on huge values
                if accessor == 'percent' and abs(bv) > 200:
                    issues.append({
                        'type': 'PERCENT_LARGE',
                        'file': fname,
                        'line': i + 1,
                        'spell_id': sid,
                        'spell_name': spell['name'],
                        'effect_n': effect_n,
                        'base_value': bv,
                        'context': stripped[:150],
                    })
    
    return issues, stats

def audit_class(class_name, spells, verbose=False):
    """Audit all files for a class."""
    files = CLASS_FILES.get(class_name, [])
    if not files:
        print(f"Unknown class: {class_name}")
        return None
    
    print(f"\n{'='*80}")
    print(f"DEEP AUDIT: {class_name.upper()}")
    print(f"{'='*80}")
    
    all_issues = []
    total = defaultdict(int)
    
    for filepath in files:
        issues, stats = audit_file(filepath, spells, verbose)
        all_issues.extend(issues)
        for k, v in stats.items():
            total[k] += v
    
    print(f"  effectN reads:  {total['total']}")
    print(f"  Resolved:       {total['resolved']} ({total['resolved']*100//max(total['total'],1)}%)")
    print(f"    via variable: {total['resolved'] - total['tier_set']}")
    print(f"    via tier_set: {total['tier_set']}")
    print(f"  Unresolved:     {total['unresolved']}")
    print(f"  Effect OOB:     {total['oob']}")
    
    oob = [i for i in all_issues if i['type'] == 'EFFECT_OOB']
    fsms = [i for i in all_issues if i['type'] == 'FROM_SECONDS_MS']
    pctl = [i for i in all_issues if i['type'] == 'PERCENT_LARGE']
    
    if oob:
        print(f"\n  *** EFFECT OOB ({len(oob)}) ***")
        for i in oob:
            print(f"    {i['file']}:{i['line']} {i['spell_name']} ({i['spell_id']})")
            print(f"      effectN({i['effect_n']}) but max={i['max_effects']} [via {i['method']}]")
            print(f"      {i['context']}")
    
    if fsms:
        print(f"\n  *** FROM_SECONDS ON MS VALUE ({len(fsms)}) ***")
        for i in fsms:
            print(f"    {i['file']}:{i['line']} {i['spell_name']} ({i['spell_id']})")
            print(f"      effectN({i['effect_n']}) base_value={i['base_value']}")
            print(f"      from_seconds({i['base_value']}) = {i['base_value']}s -- should be {i['base_value']/1000}s?")
            print(f"      {i['context']}")
    
    if pctl:
        print(f"\n  *** PERCENT ON LARGE VALUE ({len(pctl)}) ***")
        for i in pctl:
            print(f"    {i['file']}:{i['line']} {i['spell_name']} ({i['spell_id']})")
            print(f"      effectN({i['effect_n']}) base_value={i['base_value']} -> percent()={i['base_value']/100}")
            print(f"      {i['context']}")
    
    if not all_issues:
        print(f"\n  No issues found!")
    
    return {'total': dict(total), 'issues': all_issues}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--class', dest='cls')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    
    dbc_path = 'engine/dbc/generated/sc_spell_data.inc'
    print("Loading DBC...")
    spells = load_dbc_effects(dbc_path)
    print(f"  {len(spells)} spells loaded")
    
    classes = list(CLASS_FILES.keys()) if args.all else [args.cls]
    
    grand = defaultdict(int)
    all_issues = []
    
    for cls in classes:
        if cls:
            r = audit_class(cls, spells, args.verbose)
            if r:
                for k, v in r['total'].items():
                    grand[k] += v
                all_issues.extend(r['issues'])
    
    if args.all:
        print(f"\n{'='*80}")
        print(f"GRAND TOTAL: {grand['total']} effectN reads, {grand['resolved']} resolved ({grand['resolved']*100//max(grand['total'],1)}%), {grand['oob']} OOB")
        print(f"{'='*80}")
        if all_issues:
            for i in all_issues:
                print(f"  [{i['type']}] {i['file']}:{i['line']} {i.get('spell_name','?')} ({i.get('spell_id','?')})")

if __name__ == '__main__':
    main()
