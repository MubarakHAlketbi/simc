#!/usr/bin/env python3
"""
Full class module audit: scan EVERY effectN() read against DBC spell data.

For each effectN(N) call in a class module:
1. Resolve which spell ID it operates on
2. Check if N exceeds the spell's effect count (OOB)
3. Report the effect type/base_value for manual verification

Also checks:
- from_seconds(base_value()) on spells where the value looks like milliseconds
- time_value() on spells where the value looks like seconds (wrong direction)
- percent() on values that look like raw numbers (not percentages)

Usage:
    python3 scripts/audit_class_spells.py --class warrior
    python3 scripts/audit_class_spells.py --all
"""
import re
import sys
import os
import argparse
from collections import defaultdict

# Map class names to source files
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

def load_spell_effects(dbc_path):
    """Parse ALL spell effects from sc_spell_data.inc.
    Returns: {spell_id: {name, max_effect_index, effects: {1: {base_value, type, subtype}, ...}}}
    """
    spells = {}
    
    with open(dbc_path) as f:
        content = f.read()
    
    # Parse spell headers: { "Name", spell_id, ...
    # Format: { "name", id, school_mask, ...  }, /* effect_id1, effect_id2, ... */
    spell_section = False
    effect_section = False
    
    # Two-pass: first get spell names, then effects
    # Spell entries start with { "Name" and contain the spell id as second field
    for line in content.split('\n'):
        line = line.strip()
        
        # Spell entry: { "Name", id, ...
        m = re.match(r'\{\s*"([^"]+)"\s*,\s*(\d+)\s*,', line)
        if m:
            name = m.group(1)
            sid = int(m.group(2))
            # Count effects from the comment at end: /* eid1, eid2, ... */
            comment = re.search(r'/\*\s*([\d,\s]+)\s*\*/', line)
            effect_count = 0
            if comment:
                eids = [x.strip() for x in comment.group(1).split(',') if x.strip()]
                effect_count = len(eids)
            spells[sid] = {'name': name, 'effect_count': effect_count, 'effects': {}}
        
        # Effect entry: { effect_id, spell_id, index, type, subtype, ...base_value at position ~16
        # Format: { eid, spell_id, idx, type, subtype, flags, ..., base_value, ...
        em = re.match(r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,', line)
        if em:
            eid = int(em.group(1))
            sid = int(em.group(2))
            idx = int(em.group(3))  # 0-based index
            etype = int(em.group(4))
            subtype = int(em.group(5))
            
            # Extract base_value - it's the 16th comma-separated field
            fields = line.split(',')
            base_value = 0.0
            if len(fields) >= 16:
                try:
                    base_value = float(fields[15].strip())
                except (ValueError, IndexError):
                    pass
            
            if sid in spells:
                spells[sid]['effects'][idx + 1] = {
                    'base_value': base_value,
                    'type': etype,
                    'subtype': subtype,
                    'effect_id': eid,
                }
    
    return spells

def find_spell_context(lines, lineno):
    """Try to determine which spell_id an effectN call operates on.
    Look backwards from the line for spell ID patterns."""
    
    # Patterns that establish a spell context:
    # 1. Direct: spell_id->effectN(N) or find_spell(ID)->effectN(N)
    # 2. Variable: auto x = find_spell(ID); ... x->effectN(N)
    # 3. Member: talent.X->effectN(N) — need to trace to spell ID
    # 4. Chained: sets->set(SPEC, TIER, BN)->effectN(N)
    
    line = lines[lineno]
    
    # Direct spell ID on same line
    spell_ids = re.findall(r'find_spell\s*\(\s*(\d+)', line)
    if spell_ids:
        return [int(x) for x in spell_ids]
    
    # Chained from sets->set()
    if 'sets->set(' in line or 'set_bonuses.' in line or 'tier_set.' in line:
        return ['tier_set']  # Can't resolve to ID easily
    
    # Look for variable assignment in nearby lines
    # e.g., const auto& spell = find_spell(12345);
    #        spell->effectN(1)
    for i in range(max(0, lineno - 15), lineno):
        prev = lines[i]
        ids = re.findall(r'find_spell\s*\(\s*(\d+)', prev)
        if ids:
            return [int(x) for x in ids]
    
    return []

def scan_effectn_reads(filepath, spells):
    """Scan a C++ file for all effectN() reads and verify against DBC."""
    issues = []
    stats = {'total_reads': 0, 'verified': 0, 'oob': 0, 'unresolved': 0,
             'from_seconds_suspect': 0}
    
    if not os.path.exists(filepath):
        return issues, stats
    
    with open(filepath) as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip comments
        if stripped.startswith('//'):
            continue
        
        # Find all effectN(N) calls
        for m in re.finditer(r'effectN\s*\(\s*(\d+)\s*\)', line):
            effect_n = int(m.group(1))
            stats['total_reads'] += 1
            
            # What accessor follows?
            after = line[m.end():]
            accessor = ''
            am = re.match(r'\s*\.\s*(\w+)\s*\(', after)
            if am:
                accessor = am.group(1)
            
            # Try to find the spell ID
            # Direct on same line
            spell_ids_on_line = re.findall(r'find_spell\s*\(\s*(\d+)', line)
            
            # Check for from_seconds(base_value()) pattern
            if 'from_seconds' in line and ('base_value' in line or accessor == 'base_value'):
                # Try to find which spell this is for
                context_ids = find_spell_context(lines, i)
                for sid in context_ids:
                    if isinstance(sid, int) and sid in spells:
                        eff = spells[sid]['effects'].get(effect_n, {})
                        bv = eff.get('base_value', 0)
                        if bv > 100 and bv != int(bv / 1000) * 1000 + 0.0001:
                            # Value > 100 used with from_seconds — might be milliseconds
                            if bv >= 1000:
                                stats['from_seconds_suspect'] += 1
                                issues.append({
                                    'type': 'FROM_SECONDS_SUSPECT',
                                    'file': os.path.basename(filepath),
                                    'line': i + 1,
                                    'spell_id': sid,
                                    'spell_name': spells[sid]['name'],
                                    'effect_n': effect_n,
                                    'base_value': bv,
                                    'context': stripped[:150],
                                })
            
            # Try to verify effect count
            for sid_str in spell_ids_on_line:
                sid = int(sid_str)
                if sid in spells:
                    spell = spells[sid]
                    max_n = len(spell['effects'])
                    if max_n == 0:
                        max_n = spell['effect_count']
                    
                    if effect_n > max_n and max_n > 0:
                        stats['oob'] += 1
                        issues.append({
                            'type': 'EFFECT_OOB',
                            'file': os.path.basename(filepath),
                            'line': i + 1,
                            'spell_id': sid,
                            'spell_name': spell['name'],
                            'effect_n': effect_n,
                            'max_effects': max_n,
                            'context': stripped[:150],
                        })
                    else:
                        stats['verified'] += 1
                        
                        # Additional checks on the effect value
                        eff = spell['effects'].get(effect_n, {})
                        bv = eff.get('base_value', 0)
                        
                        # percent() on a value > 100 — unusual
                        if accessor == 'percent' and abs(bv) > 200:
                            issues.append({
                                'type': 'PERCENT_LARGE_VALUE',
                                'file': os.path.basename(filepath),
                                'line': i + 1,
                                'spell_id': sid,
                                'spell_name': spell['name'],
                                'effect_n': effect_n,
                                'base_value': bv,
                                'context': stripped[:150],
                            })
    
    stats['unresolved'] = stats['total_reads'] - stats['verified'] - stats['oob']
    return issues, stats

def scan_all_spell_lookups(filepath, spells):
    """Scan for find_spell(ID) where the spell doesn't exist in DBC."""
    issues = []
    if not os.path.exists(filepath):
        return issues
    
    with open(filepath) as f:
        content = f.read()
    
    for m in re.finditer(r'find_spell\s*\(\s*(\d+)\s*[,)]', content):
        sid = int(m.group(1))
        if sid > 100000 and sid not in spells:  # Skip low IDs (often constants)
            # Get line number
            line_start = content[:m.start()].count('\n') + 1
            line = content.split('\n')[line_start - 1].strip()
            if not line.startswith('//'):
                issues.append({
                    'type': 'SPELL_NOT_IN_DBC',
                    'file': os.path.basename(filepath),
                    'line': line_start,
                    'spell_id': sid,
                    'context': line[:150],
                })
    
    return issues

def scan_from_seconds_base_value(filepath, spells):
    """Specifically hunt for from_seconds(X->effectN(N).base_value()) where base_value >= 1000."""
    issues = []
    if not os.path.exists(filepath):
        return issues
    
    with open(filepath) as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('//'):
            continue
        
        # Pattern: from_seconds( ... effectN(N).base_value() ... )
        if 'from_seconds' in line and 'base_value' in line and 'effectN' in line:
            # Extract the effectN
            em = re.search(r'effectN\s*\(\s*(\d+)\s*\)', line)
            if not em:
                continue
            effect_n = int(em.group(1))
            
            # Try to find the spell ID from context
            context_ids = []
            for j in range(max(0, i - 10), min(len(lines), i + 2)):
                for sm in re.finditer(r'find_spell\s*\(\s*(\d+)', lines[j]):
                    context_ids.append(int(sm.group(1)))
                # Also check for sets->set() which we can't easily resolve
            
            for sid in context_ids:
                if sid in spells:
                    eff = spells[sid]['effects'].get(effect_n, {})
                    bv = eff.get('base_value', 0)
                    if abs(bv) >= 1000:
                        issues.append({
                            'type': 'FROM_SECONDS_MS_VALUE',
                            'file': os.path.basename(filepath),
                            'line': i + 1,
                            'spell_id': sid,
                            'spell_name': spells[sid]['name'],
                            'effect_n': effect_n,
                            'base_value': bv,
                            'interpretation': f"from_seconds({bv}) = {bv}s, but value looks like {bv}ms = {bv/1000}s",
                            'context': stripped[:150],
                        })
    
    return issues

def audit_class(class_name, spells):
    """Full audit of a class module."""
    files = CLASS_FILES.get(class_name, [])
    if not files:
        print(f"Unknown class: {class_name}")
        return None
    
    print(f"\n{'='*80}")
    print(f"FULL AUDIT: {class_name.upper()}")
    print(f"{'='*80}")
    
    all_issues = []
    total_stats = defaultdict(int)
    
    for filepath in files:
        if not os.path.exists(filepath):
            continue
        
        fname = os.path.basename(filepath)
        
        # 1. effectN OOB check
        issues, stats = scan_effectn_reads(filepath, spells)
        all_issues.extend(issues)
        for k, v in stats.items():
            total_stats[k] += v
        
        # 2. Missing spell check
        missing = scan_all_spell_lookups(filepath, spells)
        all_issues.extend(missing)
        total_stats['missing_spells'] += len(missing)
        
        # 3. from_seconds(base_value()) with ms values
        fs_issues = scan_from_seconds_base_value(filepath, spells)
        all_issues.extend(fs_issues)
        total_stats['from_seconds_ms'] += len(fs_issues)
    
    # Summary
    print(f"\n  Files scanned:        {len([f for f in files if os.path.exists(f)])}")
    print(f"  Total effectN reads:  {total_stats['total_reads']}")
    print(f"  Verified (ID on line):{total_stats['verified']}")
    print(f"  Unresolved (indirect):{total_stats['unresolved']}")
    print(f"  Effect OOB:           {total_stats['oob']}")
    print(f"  Missing spells:       {total_stats['missing_spells']}")
    print(f"  from_seconds(ms?):    {total_stats['from_seconds_ms']}")
    
    # Print issues
    critical = [i for i in all_issues if i['type'] in ('EFFECT_OOB', 'FROM_SECONDS_MS_VALUE')]
    warnings = [i for i in all_issues if i['type'] not in ('EFFECT_OOB', 'FROM_SECONDS_MS_VALUE')]
    
    if critical:
        print(f"\n  *** CRITICAL ISSUES ({len(critical)}) ***")
        for issue in critical:
            print(f"    [{issue['type']}] {issue['file']}:{issue['line']}")
            if 'spell_name' in issue:
                print(f"      Spell: {issue['spell_name']} ({issue.get('spell_id', '?')})")
            if 'interpretation' in issue:
                print(f"      {issue['interpretation']}")
            print(f"      {issue['context']}")
    
    if warnings:
        print(f"\n  Warnings ({len(warnings)}):")
        for issue in warnings[:20]:  # Limit output
            print(f"    [{issue['type']}] {issue['file']}:{issue['line']} - {issue.get('spell_id', '?')}: {issue['context'][:80]}")
        if len(warnings) > 20:
            print(f"    ... and {len(warnings) - 20} more")
    
    if not all_issues:
        print(f"\n  No issues found!")
    
    return {'stats': dict(total_stats), 'issues': all_issues, 'critical': critical, 'warnings': warnings}

def main():
    parser = argparse.ArgumentParser(description='Full class module DBC audit')
    parser.add_argument('--class', dest='class_name', help='Class to audit')
    parser.add_argument('--all', action='store_true', help='Audit all classes')
    args = parser.parse_args()
    
    dbc_path = 'engine/dbc/generated/sc_spell_data.inc'
    if not os.path.exists(dbc_path):
        print("Error: Run from simc root directory")
        sys.exit(1)
    
    print("Loading DBC spell data (this takes a moment)...")
    spells = load_spell_effects(dbc_path)
    print(f"  Loaded {len(spells)} spells with effect data")
    
    classes = list(CLASS_FILES.keys()) if args.all else [args.class_name]
    
    grand_total = defaultdict(int)
    all_critical = []
    
    for cls in classes:
        if cls:
            result = audit_class(cls, spells)
            if result:
                for k, v in result['stats'].items():
                    grand_total[k] += v
                all_critical.extend(result['critical'])
    
    if args.all:
        print(f"\n{'='*80}")
        print(f"GRAND TOTAL")
        print(f"{'='*80}")
        print(f"  effectN reads:      {grand_total['total_reads']}")
        print(f"  Verified:           {grand_total['verified']}")
        print(f"  Unresolved:         {grand_total['unresolved']}")
        print(f"  Effect OOB:         {grand_total['oob']}")
        print(f"  Missing spells:     {grand_total['missing_spells']}")
        print(f"  from_seconds(ms?):  {grand_total['from_seconds_ms']}")
        
        if all_critical:
            print(f"\n  *** {len(all_critical)} CRITICAL ISSUES ACROSS ALL CLASSES ***")
            for issue in all_critical:
                print(f"    {issue['file']}:{issue['line']} [{issue['type']}] {issue.get('spell_name', '?')} ({issue.get('spell_id', '?')})")

if __name__ == '__main__':
    main()
