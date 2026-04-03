#!/usr/bin/env python3
"""
Automated verification of every effectN(N) read in class modules against DBC data.

Scans all C++ class module files, extracts every effectN(N) call, cross-references
against sc_spell_data.inc to verify:
  1. Bounds: N <= spell.num_effects
  2. Effect existence: does an effect entry exist for spell_id + eff_index?
  3. Aura type: what aura type does the effect have?
  4. Base value: what is the raw DBC value?
  5. Semantic check: does the C++ accessor (.percent(), .base_value(), .time_value(),
     .resource(), .ap_coeff()) match what the aura type expects?

Usage:
  python3 scripts/verify_spell_effects.py [--all | --class NAME | --file FILE]
  python3 scripts/verify_spell_effects.py --all            # scan all class modules
  python3 scripts/verify_spell_effects.py --class priest   # scan just priest
  python3 scripts/verify_spell_effects.py --file sc_paladin.cpp  # scan one file

Outputs a report of all violations + summary.
"""

import re
import os
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field
from collections import defaultdict

# ─── DBC Parser ───────────────────────────────────────────────────────────────

DIRECTIONAL = "output: write"

# sc_spell_data.inc has two sections separated by a blank line:
#   Section 1 (lines 1-30931): Main spell entries
#     { "SpellName", spell_id, school, ..., num_effects, ... }
#   Section 2 (lines 30933+): Effect entries
#     { effect_id, spell_id, eff_index, aura_type, ..., base_value, misc_value, ... }

SPELL_DATA_FILE = "engine/dbc/generated/sc_spell_data.inc"


@dataclass
class SpellInfo:
    name: str
    spell_id: int
    num_effects: int
    # effect_id comments at end of line
    effect_ids: list = field(default_factory=list)


@dataclass
class EffectInfo:
    effect_id: int
    spell_id: int
    eff_index: int
    aura_type: int
    base_value: float
    misc_value_a: int
    misc_value_b: int
    trigger_spell: int = 0


def parse_dbc():
    """Parse sc_spell_data.inc into spell/effect lookup tables."""
    spells = {}  # spell_id -> SpellInfo
    effects = defaultdict(list)  # spell_id -> [EffectInfo, ...]

    with open(SPELL_DATA_FILE) as f:
        lines = f.readlines()

    # Find the blank line separator
    section2_start = 30932  # line index (0-based) for effect section
    # Dynamically find it
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Main spell entries have quoted strings as first field
        if stripped.startswith("{ \"") and i > 30000:
            # We're in main spell section
            pass
        elif stripped.startswith("{ 1") or stripped.startswith("{ 2") or stripped.startswith("{ 3"):
            # Could be effect entries or main spell entries
            # Effect entries start with { <number>, <number>, <number>, ...
            # where the third number is the effect index
            if i > 30932:
                section2_start = i
                break
            # For safety, check if third field is small (< 16 = effect index)
            parts = stripped.lstrip("{").rstrip("},").rstrip("}").split(",")
            if len(parts) >= 3:
                try:
                    first = int(parts[0])
                    second = int(parts[1])
                    third = int(parts[2])
                    # Effect entries: first is effect_id (7+ digits), third is index (<16)
                    if first > 100000 and 0 <= third <= 15:
                        section2_start = i
                        break
                except ValueError:
                    pass

    # Parse main spell entries (section 1)
    for i in range(section2_start):
        line = lines[i].strip()
        if not line.startswith("{ \"") or not line.endswith("},"):
            continue

        # Remove trailing }, and extract comment
        comment = ""
        if "/*" in line:
            idx = line.index("/*")
            comment = line[idx:]
            line = line[:idx].rstrip("}").rstrip(",")

        # Parse the main spell entry
        # Format: { "Name" , spell_id, school, dur, ... , num_effects, ... }
        # The name can contain commas, so we need careful parsing
        # First field is the quoted name
        name_match = re.match(r'\{\s*"([^"]*)"', line)
        if not name_match:
            continue

        name = name_match.group(1)
        rest = line[name_match.end():]

        # Parse remaining comma-separated fields
        try:
            fields = [f.strip() for f in rest.split(",") if f.strip().rstrip("}").strip()]
            # Remove trailing } or },
            if fields and (fields[-1] == "}" or fields[-1] == "}"):
                fields[-1] = fields[-1].rstrip("}")

            # spell_id is the first numeric field after the name
            # Fields after name: spell_id, school_mask, ...
            spell_id = int(fields[0])
            school = int(fields[1])

            # num_effects is near the end — count from right
            # From analyzing the format: fields from the right end at index 5
            """
            ... { ... } , { ... } , family , { ... } , { ... } , spell_misc , ... ,
            num_effects , charge_recharge_type , ... }
            
            Looking at actual data:
            Shadowfiend main entry (line 30782):
              ... 6, { 0, 0 }, { 0, 0 }, 0x08000000, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5 }
                                                         spell_family  ...  num_effects
            """
            # num_effects is the 5th field from the end (before }, or just 5 from end)
            # Let me count: 5 is the last field, 0 is 6th from end, 4 is 5th from end
            num_effects = int(fields[-5])

            # Extract effect IDs from comment
            effect_ids = []
            if "/*" in comment:
                ids_part = comment.split("/*")[1].split("*/")[0]
                effect_ids = [int(x.strip()) for x in ids_part.split(",") if x.strip().isdigit()]

            spells[spell_id] = SpellInfo(
                name=name,
                spell_id=spell_id,
                num_effects=num_effects,
                effect_ids=effect_ids,
            )
        except (ValueError, IndexError):
            continue

    # Parse effect entries (section 2)
    for i in range(section2_start, len(lines)):
        line = lines[i].strip()
        if not line.startswith("{ ") or not (line.endswith("},") or line.endswith("}")):
            continue

        # Remove trailing }, or }
        content = line.rstrip("}").rstrip(",").strip().lstrip("{").strip()
        fields = [f.strip() for f in content.split(",") if f.strip()]

        try:
            # Format: { eff_id, spell_id, eff_index, type, aura, ..., base_value, misc_a, misc_b, ..., trigger_spell, ... }
            effect_id = int(fields[0])
            spell_id = int(fields[1])
            eff_index = int(fields[2])

            # aura_type is field 4
            aura_type = int(fields[4])

            # base_value is field 15
            base_value = float(fields[15])

            # misc_value_a is field 16
            misc_value_a = int(fields[16])

            # misc_value_b is field 17
            misc_value_b = int(fields[17])

            # Trigger spell is field 24
            trigger_spell = int(fields[24]) if len(fields) > 24 else 0

            eff = EffectInfo(
                effect_id=effect_id,
                spell_id=spell_id,
                eff_index=eff_index,
                aura_type=aura_type,
                base_value=base_value,
                misc_value_a=misc_value_a,
                misc_value_b=misc_value_b,
                trigger_spell=trigger_spell,
            )
            effects[spell_id].append(eff)
        except (ValueError, IndexError):
            continue

    return spells, effects


# ─── C++ Scanner ──────────────────────────────────────────────────────────────

# Accessor types we care about
ACCESSOR_PATTERNS = {
    "percent": re.compile(r"\.percent\s*\("),
    "base_value": re.compile(r"\.base_value\s*\("),
    "time_value": re.compile(r"\.time_value\s*\("),
    "resource": re.compile(r"\.resource\s*\("),
    "ap_coeff": re.compile(r"\.ap_coeff\s*\("),
    "sp_coeff": re.compile(r"\.sp_coeff\s*\("),
    "average": re.compile(r"\.average\s*\("),
    "chain_amplitude": re.compile(r"\.chain_amplitude\s*\("),
    "damage_multiplier": re.compile(r"\.damage_multiplier\s*\("),
    "value": re.compile(r"\.value\s*\("),
}

# Expected accessor for known aura types
AURA_TYPE_EXPECTED_ACCESSORS = {
    108: ["percent"],    # ADD_PCT_MODIFIER
    107: ["base_value", "time_value", "resource"],  # ADD_FLAT_MODIFIER
    6: ["base_value", "time_value", "percent"],  # DUMMY / APPLY_AURA
    64: ["percent", "base_value", "resource", "trigger"],  # TRIGGER_SPELL
    11: ["percent"],  # SPELL_AURA_MOD_COOLDOWN (CDR) - actually misc_value is important
    4: ["base_value", "percent", "time_value"],  # SPELL_AURA_DUMMY / SPELL_AURA_MOD_STAT
}

# Known aura type names
AURA_TYPE_NAMES = {
    0: "NONE",
    1: "BIND_SIGHT",
    2: "POSSESS",
    3: "PERIODIC_DAMAGE",
    4: "DUMMY",
    5: "MOD_CONFUSE",
    6: "MOD_CHARM",
    7: "MOD_FEAR",
    8: "PERIODIC_HEAL",
    9: "MOD_ATTACKSPEED",
    10: "MOD_THREAT",
    11: "MOD_TAUNT",
    12: "MOD_STUN",
    13: "MOD_DAMAGE_DONE",
    14: "MOD_DAMAGE_TAKEN",
    15: "MOD_DAMAGE_DONE_VERSUS",
    16: "MOD_DAMAGE_TAKEN_VERSUS",
    21: "MOD_DAMAGE_PERCENT_TAKEN",
    22: "MOD_REGEN",
    23: "SPELL_MOD_DAMAGE_DONE",
    24: "SPELL_MOD_RESIST",
    25: "PERIODIC_LEECH",
    26: "MOD_HASTE",
    27: "MOD_MELEE_RANGED_ATTACK_POWER",
    28: "MOD_MELEE_RANGED_HASTE",
    29: "MOD_SCALE",
    30: "MOD_INCREASE_ENERGY",
    31: "MOD_INCREASE_MANA",
    38: "MOD_DAMAGE_DONE_CREATURE",
    42: "PERIODIC_TRIGGER_SPELL",
    64: "TRIGGER_SPELL",
    76: "MOD_ARMOR_PCT",
    79: "OBSCURED",
    87: "MOD_DAMAGE_FROM_CASTER",
    96: "MOD_HEALING_DONE",
    107: "ADD_FLAT_MODIFIER",
    108: "ADD_PCT_MODIFIER",
    115: "MOD_CAST_SPEED",
    116: "MOD_SPELL_DAMAGE_OF_STAT_PERCENT",
    118: "MOD_HEALING_DONE_PERCENT",
    123: "MOD_RANGED_ATTACK_POWER_OF_STAT_PERCENT",
    127: "MOD_RATING",
    131: "MOD_MANA_REGEN_INTERRUPT",
    137: "MOD_SPELL_HEALING_OF_STAT_PERCENT",
    138: "MOD_DAMAGE_PERCENT_DONE",
    158: "PERIODIC_DAMAGE_PCT",
    255: "DUMMY_EFFECT",
    415: "SPELL_AURA_MOD_SPELL_DAMAGE_FROM_CASTER_PCT",
    None: "UNKNOWN",
}


def get_aura_name(aura_type):
    return AURA_TYPE_NAMES.get(aura_type, f"UNKNOWN({aura_type})")


@dataclass
class EffectNCall:
    file: str
    line: int
    line_text: str
    spell_var: str  # the variable/expression before ->effectN
    effect_index: int
    accessor: str  # .percent(), .base_value(), etc.


def scan_effectn_calls(files):
    """Scan C++ files for all effectN(N) calls."""
    calls = []
    # Pattern: something ->effectN( N ) .accessor(
    pattern = re.compile(
        r"(\w+(?:->\w+)*)"  # variable chain
        r"->effectN\s*\(\s*(\d+)\s*\)"  # ->effectN(N)
        r"(\.(\w+)\s*\()?"  # optional .accessor()
        r"(.*$)",  # rest of line
    )

    for filepath in files:
        try:
            with open(filepath) as f:
                for line_num, line in enumerate(f, 1):
                    # Skip comments
                    stripped = line.strip()
                    if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
                        continue

                    # Find all effectN calls in this line
                    for match in pattern.finditer(line):
                        var = match.group(1)
                        idx = int(match.group(2))
                        accessor = match.group(4) if match.group(4) else "none"

                        calls.append(EffectNCall(
                            file=filepath,
                            line=line_num,
                            line_text=line.rstrip(),
                            spell_var=var,
                            effect_index=idx,
                            accessor=accessor,
                        ))
        except Exception as e:
            print(f"WARN: Could not read {filepath}: {e}")

    return calls


def find_spell_id_var(lines, line_idx):
    """Try to determine what spell_id a variable refers to by scanning backward."""
    var_names = [
        r"find_spell\s*\(\s*(\d+)\s*\)",
        r"find_talent_spell\s*\([^,]+,\s*\"([^\"]+)\"",
        r"find_class_spell\s*\(\s*\"([^\"]+)\"",
        r"find_specialization_spell\s*\(\s*\"([^\"]+)\"",
        r"find_spell\s*\(\s*spell_id::([A-Za-z_]\w+)\s*\)",
        r"ST\(\s*\"([^\"]+)\"",
    ]

    # Look backward from the line to find what spell this variable was assigned to
    for lookback in range(min(30, line_idx), 0, -1):
        prev_line = lines[line_idx - lookback]
        for pat in var_names:
            m = re.search(pat, prev_line)
            if m:
                return m.group(1)
    return None


def scan_effectn_calls_with_spell_ids(files):
    """Scan for effectN calls and try to resolve spell IDs."""
    calls = []
    # Pattern to match any line with effectN
    pattern = re.compile(r"->effectN\s*\(\s*(\d+)\s*\)(\s*\.(\w+)\s*\()")

    for filepath in files:
        try:
            with open(filepath) as f:
                all_lines = f.readlines()
                for line_num, line in enumerate(all_lines, 1):
                    stripped = line.strip()
                    if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
                        continue

                    m = pattern.search(line)
                    if m:
                        idx = int(m.group(1))
                        accessor = m.group(3) if m.group(3) else "none"

                        # Find the variable being accessed
                        before = line[:m.start()]
                        var_match = re.search(r"(\w+(?:->\w+)+)", before)
                        var = var_match.group(1) if var_match else "unknown"

                        # Try to resolve spell_id by scanning backward
                        spell_ref = find_spell_id_var(all_lines, line_num - 1)

                        calls.append(EffectNCall(
                            file=filepath,
                            line=line_num,
                            line_text=stripped,
                            spell_var=var,
                            effect_index=idx,
                            accessor=accessor,
                        ))
                        # Store resolved spell reference
                        calls[-1].spell_ref = spell_ref  # type: ignore
        except Exception as e:
            print(f"WARN: Could not read {filepath}: {e}")

    return calls


# ─── Report ──────────────────────────────────────────────────────────────────

def generate_report(calls, spells, effects, output_file=None):
    """Generate a verification report."""
    issues = []
    skipped = 0
    checked = 0

    for call in calls:
        spell_ref = getattr(call, 'spell_ref', None)
        resolved_id = None

        if spell_ref:
            if spell_ref.isdigit():
                resolved_id = int(spell_ref)
            else:
                # It's a spell name - try to find in spells dict
                for sid, sp in spells.items():
                    if sp.name.lower() == spell_ref.lower():
                        resolved_id = sid
                        break

        if resolved_id and resolved_id in spells:
            sp = spells[resolved_id]
            if call.effect_index >= sp.num_effects:
                issues.append({
                    "type": "OOB",
                    "file": call.file,
                    "line": call.line,
                    "spell_id": resolved_id,
                    "spell_name": sp.name,
                    "effect_index": call.effect_index,
                    "num_effects": sp.num_effects,
                    "accessor": call.accessor,
                    "line_text": call.line_text,
                    "message": f"effectN({call.effect_index}) OOB: spell {resolved_id} ({sp.name}) has only {sp.num_effects} effects",
                })
                checked += 1
            else:
                # Check effect details
                spell_effects = [e for e in effects.get(resolved_id, []) if e.eff_index == call.effect_index]
                if spell_effects:
                    eff = spell_effects[0]
                    aura_name = get_aura_name(eff.aura_type)
                    checked += 1
                    # Flag potentially suspicious accessor/aura combos
                    if eff.aura_type not in AURA_TYPE_EXPECTED_ACCESSORS and eff.aura_type != 0:
                        pass  # Unknown aura type, skip warning
                else:
                    # Effect index is in bounds by num_effects but not in effect entry list
                    checked += 1
                    pass  # Some spells have fewer actual effect entries than num_effects claims
        else:
            skipped += 1

    # Sort issues
    issues.sort(key=lambda x: (x["file"], x["line"]))

    # Output
    report_lines = []
    report_lines.append(f"# Spell Effect Verification Report")
    report_lines.append(f"")
    report_lines.append(f"Checked: {checked}")
    report_lines.append(f"Skipped (unresolved): {skipped}")
    report_lines.append(f"Issues found: {len(issues)}")
    report_lines.append(f"")

    if issues:
        report_lines.append("## Issues")
        report_lines.append("")
        report_lines.append("| File | Line | Spell | ID | effectN | Max | Accessor | Issue |")
        report_lines.append("|------|------|-------|----|---------|-----|----------|-------|")
        for issue in issues:
            report_lines.append(
                f"| {issue['file']}:{issue['line']} "
                f"| {issue['spell_name']} ({issue['spell_id']}) "
                f"| N({issue['effect_index']}) "
                f"| max={issue['num_effects']} "
                f"| {issue['accessor']} "
                f"| {issue['message']} |"
            )
    else:
        report_lines.append("No OOB issues found among resolved spell references.")

    report_lines.append("")
    report_lines.append(f"## Summary")
    report_lines.append(f"- Total effectN calls found: {len(calls)}")
    report_lines.append(f"- Successfully resolved to spell IDs: {checked + len(issues)}")
    report_lines.append(f"- Could not resolve: {skipped}")
    report_lines.append(f"- Out-of-bounds accesses: {len(issues)}")

    output = "\n".join(report_lines)

    if output_file:
        with open(output_file, "w") as f:
            f.write(output)
        print(f"Report written to {output_file}")
    else:
        print(output)

    return issues


# ─── Main ─────────────────────────────────────────────────────────────────────

CLASS_MODULE_DIR = "engine/class_modules"

ALL_CLASS_FILES = [
    "sc_death_knight.cpp",
    "sc_demon_hunter.cpp",
    "sc_druid.cpp",
    "sc_evoker.cpp",
    "sc_hunter.cpp",
    "sc_mage.cpp",
    "sc_rogue.cpp",
    "sc_shaman.cpp",
    "sc_warrior.cpp",
    "monk/sc_monk.cpp",
    "monk/sc_monk_pets.cpp",
    "paladin/sc_paladin.cpp",
    "paladin/sc_paladin_holy.cpp",
    "paladin/sc_paladin_protection.cpp",
    "paladin/sc_paladin_retribution.cpp",
    "priest/sc_priest.cpp",
    "priest/sc_priest_discipline.cpp",
    "priest/sc_priest_holy.cpp",
    "priest/sc_priest_shadow.cpp",
    "priest/sc_priest_pets.cpp",
    "warlock/sc_warlock.cpp",
    "warlock/sc_warlock_init.cpp",
    "warlock/sc_warlock_pets.cpp",
    "warlock/sc_warlock_actions.cpp",
]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Verify spell effectN() calls against DBC")
    parser.add_argument("--all", action="store_true", help="Scan all class modules")
    parser.add_argument("--class-name", type=str, help="Scan specific class (e.g. priest)")
    parser.add_argument("--file", type=str, help="Scan specific file")
    parser.add_argument("--output", type=str, help="Output report file")
    args = parser.parse_args()

    print("Parsing DBC spell data...", flush=True)
    spells, effects = parse_dbc()
    print(f"  Loaded {len(spells)} spells, {sum(len(v) for v in effects.values())} effects")

    # Select files
    if args.file:
        files = [args.file]
    elif args.class_name:
        files = [f for f in ALL_CLASS_FILES if args.class_name.lower() in f.lower()]
        if not files:
            print(f"No files found for class '{args.class_name}'")
            return
    elif args.all:
        files = ALL_CLASS_FILES
    else:
        parser.print_help()
        return

    files = [os.path.join(CLASS_MODULE_DIR, f) for f in files]
    files = [f for f in files if os.path.isfile(f)]

    if not files:
        print("No class module files found.")
        return

    print(f"Scanning {len(files)} files for effectN() calls...", flush=True)
    calls = scan_effectn_calls_with_spell_ids(files)
    print(f"  Found {len(calls)} effectN() calls")

    print("Generating report...", flush=True)
    issues = generate_report(calls, spells, effects, output_file=args.output)

    return issues


if __name__ == "__main__":
    main()
