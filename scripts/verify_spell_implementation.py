#!/usr/bin/env python3
"""
Automated spell implementation verification against DBC data.

Cross-references every effectN(N) accessor in C++ class modules against
the actual DBC (sc_spell_data.inc) to detect:
  1. OOB effect index (N >= spell.num_effects)
  2. Effect entry existence
  3. Aura type vs accessor sanity

Usage: python3 scripts/verify_spell_implementation.py [--report OUT] [--full] [--spec S]
"""
import os
import re
import sys
from collections import defaultdict

# ─── Aura type reference ──────────────────────────────────────────────────────

AURA_NAMES = {
    0: "NONE", 1: "BIND_SIGHT", 2: "POSSESS", 3: "PERIODIC_DAMAGE",
    4: "SPELL_AURA_DUMMY", 6: "MOD_CHARM", 8: "PERIODIC_HEAL",
    9: "MOD_ATTACKSPEED", 11: "MOD_TAUNT", 12: "STUN",
    13: "MOD_DAMAGE_DONE", 14: "MOD_DAMAGE_TAKEN",
    16: "MOD_DAMAGE_DONE_SCHOOL", 21: "MOD_DAMAGE_PERCENT_TAKEN",
    22: "MOD_REGEN", 23: "SPELL_MOD_DAMAGE_DONE",
    24: "SPELL_MOD_RESIST", 25: "MOD_HEALTH_REGEN",
    26: "PERIODIC_LEECH", 28: "PERIODIC_TRIGGER_SPELL",
    29: "MOD_HEALING", 30: "MOD_HASTE",
    36: "MOD_HEALING_DONE_PCT", 48: "MOD_RESIST_PCT",
    54: "MOD_AURA_DAMAGE", 63: "SCHOOL_ABSORB",
    64: "TRIGGER_SPELL", 76: "MOD_DAMAGE_DONE_VERSUS",
    77: "MOD_DAMAGE_TAKEN_VERSUS", 79: "OBSCURED",
    82: "MOD_DAMAGE_PERCENT_DONE", 87: "MOD_CRIT_CHANCE",
    99: "MOD_SPELL_DAMAGE_OF_STAT_PERCENT",
    107: "ADD_FLAT_MODIFIER", 108: "ADD_PCT_MODIFIER",
    116: "MOD_MELEE_RANGED_ATTACK_POWER",
    123: "MOD_RANGED_ATTACK_POWER_OF_STAT",
    125: "MOD_MELEE_HASTE", 126: "MOD_MELEE_HASTE_PERCENT",
    127: "MOD_RATING", 137: "MOD_SPELL_HEALING_OF_STAT",
    138: "MOD_SPELL_DAMAGE_FROM_CASTER",
    144: "MOD_RATING_PCT", 150: "MOD_HEALING_RECEIVED",
    185: "MOD_COOLDOWN",
    289: "MOD_SPELL_DAMAGE_BY_SCHOOL", 318: "MOD_MASTERY_PCT",
}

def aura_name(aid):
    return AURA_NAMES.get(aid, f"UNKNOWN({aid})")

# ─── DBC Parser ──────────────────────────────────────────────────────────────

SPELL_DATA = "engine/dbc/generated/sc_spell_data.inc"

def parse_dbc():
    """Parse sc_spell_data.inc → (spells, effects)

    Main spell entries have a C comment at the end: /* eff_id1, eff_id2, ... */
    We count these to get num_effects, which is reliable.

    Effect entries: { eff_id, spell_id, eff_index, eff_type, aura_type, ...,
                      base_value, misc_a, misc_b, ... }
    """
    spells = {}
    effects = {}

    with open(SPELL_DATA) as f:
        lines = f.readlines()

    # ── Main spell entries (lines ~1 to ~30930) ──────────────────────────
    main_pat = re.compile(
        r'\{\s*"([^"]+)"\s*,\s*(\d+)\s*,'
    )
    eff_ids_in_comment = re.compile(r'/\*\s*([\d\s,]+)\*/')

    for i in range(min(30932, len(lines))):
        line = lines[i]
        m = main_pat.search(line)
        if not m:
            continue
        name = m.group(1)
        sid = int(m.group(2))

        # Extract effect IDs from C++ comment
        eff_ids = []
        cm = eff_ids_in_comment.search(line)
        if cm:
            eff_ids = [int(x) for x in cm.group(1).split(",") if x.strip().isdigit()]

        num_eff = len(eff_ids)  # reliable from the comment

        spells[sid] = {
            "name": name,
            "num_effects": num_eff,
            "effect_ids": eff_ids,
        }

    # ── Effect entries (lines ~30934 to ~82645) ─────────────────────────
    # Format: { eff_id, spell_id, eff_index, eff_type, aura_type, ... }
    # We need: eff_index, aura_type, base_value (field 15), misc_a (16)
    eff_pat = re.compile(
        r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,'
    )

    for i in range(30932, min(82646, len(lines))):
        line = lines[i]
        m = eff_pat.search(line)
        if not m:
            continue

        eff_id = int(m.group(1))
        spell_id = int(m.group(2))
        eff_idx = int(m.group(3))
        eff_type = int(m.group(4))
        aura = int(m.group(5))

        # Parse base_value and misc values
        # Strip leading { and everything up to aura_type, then find
        # the 16th, 17th, 18th comma-separated tokens (0-indexed from after aura_type)
        # Full fields: 0:eff_id 1:spell_id 2:eff_idx 3:eff_type 4:aura_type
        # Then: die_type, dmg_min, dmg_max, dmg_coeff, radius, radius_mod,
        #       trigger_mask, chain_amplitude, bonus_coeff, base_value, misc_a, misc_b
        # base_value is at column 15 (0-indexed in full comma-split, ignoring braces)

        # Strategy: split, tracking brace nesting, then index
        flat = _flat_split_fields(line)
        # After split: [0]={ 1:eff_id 2:spell_id 3:eff_idx 4:eff_type 5:aura_type
        #                 6:die_type 7:dmg_min ...
        # Actually let's just use regex to pull base_value, misc_a, misc_b
        # base_value is the 11th numeric field after aura_type in the simplified structure

        # More reliable: find base_value by looking for the pattern
        # After aura, there are fields until base_value at position 15
        # Use the flat split to get exact column 15
        if len(flat) > 15:
            base_val = _safe_float(flat[15])
            misc_a = _safe_int(flat[16]) if len(flat) > 16 else 0
            # misc_b is flat[17]
            misc_b = _safe_int(flat[17]) if len(flat) > 17 else 0
        else:
            base_val = 0.0
            misc_a = 0
            misc_b = 0

        effects[(spell_id, eff_idx)] = {
            "eff_id": eff_id,
            "spell_id": spell_id,
            "eff_index": eff_idx,
            "eff_type": eff_type,
            "aura_type": aura,
            "base_value": base_val,
            "misc_a": misc_a,
            "misc_b": misc_b,
        }

    print(f"  Parsed {len(spells)} spells, {len(effects)} effects", file=sys.stderr)

    # Sanity check
    if len(spells) < 30000:
        print(f"  WARNING: Expected ~30927 spells, got {len(spells)}", file=sys.stderr)
    if len(effects) < 50000:
        print(f"  WARNING: Expected ~51711 effects, got {len(effects)}", file=sys.stderr)

    return spells, effects


def _flat_split_fields(line):
    """Split a DBC line by commas, flattening { a, b, c } groups inline.
    Returns a list of string field values."""
    result = [line.lstrip(" {").rstrip(" },}\n")]
    # Split by comma outside braces
    fields = []
    current = []
    depth = 0
    for ch in result[0]:
        if ch == "{":
            depth += 1
            current.append("{")
        elif ch == "}":
            depth -= 1
            current.append("}")
        elif ch == "," and depth == 0:
            fields.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        fields.append("".join(current).strip())
    # Flatten brace groups
    flat = []
    for f in fields:
        if f.startswith("{") and f.endswith("}"):
            inner = f[1:-1]
            for sub in inner.split(","):
                flat.append(sub.strip())
        else:
            flat.append(f)
    # Remove the leading { if it's in the first field
    if flat and flat[0] == "{":
        flat = flat[1:]
    # Remove trailing } if present
    while flat and flat[-1] in ("}", ""):
        flat.pop()
    return flat


def _safe_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return 0.0

def _safe_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return 0


# ─── C++ Scanner ─────────────────────────────────────────────────────────────

CLASS_FILES = [
    "engine/class_modules/sc_death_knight.cpp",
    "engine/class_modules/sc_demon_hunter.cpp",
    "engine/class_modules/sc_druid.cpp",
    "engine/class_modules/sc_evoker.cpp",
    "engine/class_modules/sc_hunter.cpp",
    "engine/class_modules/sc_mage.cpp",
    "engine/class_modules/sc_rogue.cpp",
    "engine/class_modules/sc_shaman.cpp",
    "engine/class_modules/sc_warrior.cpp",
    "engine/class_modules/monk/sc_monk.cpp",
    "engine/class_modules/monk/sc_monk_pets.cpp",
    "engine/class_modules/monk/sc_monk.hpp",
    "engine/class_modules/paladin/sc_paladin.cpp",
    "engine/class_modules/paladin/sc_paladin.hpp",
    "engine/class_modules/paladin/sc_paladin_holy.cpp",
    "engine/class_modules/paladin/sc_paladin_protection.cpp",
    "engine/class_modules/paladin/sc_paladin_retribution.cpp",
    "engine/class_modules/priest/sc_priest.cpp",
    "engine/class_modules/priest/sc_priest.hpp",
    "engine/class_modules/priest/sc_priest_discipline.cpp",
    "engine/class_modules/priest/sc_priest_holy.cpp",
    "engine/class_modules/priest/sc_priest_pets.cpp",
    "engine/class_modules/priest/sc_priest_shadow.cpp",
    "engine/class_modules/warlock/sc_warlock.cpp",
    "engine/class_modules/warlock/sc_warlock.hpp",
    "engine/class_modules/warlock/sc_warlock_init.cpp",
    "engine/class_modules/warlock/sc_warlock_pets.cpp",
    "engine/class_modules/warlock/sc_warlock_actions.cpp",
]

ACCESSOR_LIST = [
    "percent", "base_value", "time_value", "resource",
    "ap_coeff", "sp_coeff", "average", "damage_multiplier",
    "chain_amplitude", "value", "trigger_spell", "amplitude",
]

def scan_effectn_calls(filepaths):
    """Extract all ->effectN(N).accessor() calls."""
    results = []

    pat = re.compile(
        r'->effectN\s*\(\s*(\d+)\s*\)'
        r'(\s*\.\s*(' + "|".join(ACCESSOR_LIST) + r')\s*\()'
    )

    # Patterns for resolving spell references
    assign_id_pat = re.compile(r'find_spell\s*\(\s*(\d+)\s*\)')
    assign_name_id_pat = re.compile(
        r'(?:find_(?:talent_)?spell|ST|GST|find_class_spell'
        r'|find_specialization_spell|find_pet_spell|find_talent_spell)\s*\(\s*'
        r'(?:"([^"]+)"|(?:talent_tree::\w+,\s*)?"([^"]+)")'
    )

    for fpath in filepaths:
        if not os.path.isfile(fpath):
            continue
        try:
            with open(fpath) as f:
                all_lines = f.readlines()
        except Exception:
            continue

        for lineno, line in enumerate(all_lines, 1):
            stripped = line.strip()
            if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
                continue

            for m in pat.finditer(line):
                idx = int(m.group(1))
                accessor = m.group(3)

                # Extract variable chain
                before = line[:m.start()]
                var_m = re.search(r'(\w+(?:->\w+)*)$', before)
                var_chain = var_m.group(1) if var_m else "?"

                # Resolve spell: scan backward
                spell_ref_id = None
                spell_ref_name = None
                for lb in range(1, min(31, lineno)):
                    prev = all_lines[lineno - lb - 1]
                    im = assign_id_pat.search(prev)
                    if im:
                        spell_ref_id = int(im.group(1))
                        break
                    nm = assign_name_id_pat.search(prev)
                    if nm:
                        name_val = nm.group(1) or nm.group(2)
                        if name_val:
                            spell_ref_name = name_val
                        break

                results.append({
                    "file": fpath,
                    "line": lineno,
                    "var_chain": var_chain,
                    "idx": idx,
                    "accessor": accessor,
                    "spell_ref_id": spell_ref_id,
                    "spell_ref_name": spell_ref_name,
                    "context": stripped,
                })

    return results


# ─── Verification ─────────────────────────────────────────────────────────────

ACCESSOR_AURA_WHITELIST = {
    "percent": {0, 3, 4, 6, 13, 14, 16, 21, 23, 36, 48, 64, 76, 77, 82, 99, 108, 138, 150, 289, 318},
    "base_value": {0, 2, 4, 6, 11, 22, 30, 64, 107, 108, 127, 144, 185},
    "time_value": {0, 4, 6, 64, 185},
    "resource": {0, 4, 6, 64, 107, 108},
    "ap_coeff": {0, 2, 4, 6},
    "sp_coeff": {0, 2, 4, 6},
    "average": {0, 2, 4, 6},
    "value": {0, 2, 4, 6},
    "trigger_spell": {28, 42, 64},
    "damage_multiplier": {0, 2, 4, 6, 108},
    "chain_amplitude": {0, 2, 4, 6},
    "amplitude": {0, 3, 8, 28},
}

def verify(calls, spells, effects):
    # Build name→id map
    name_to_id = {}
    for sid, s in spells.items():
        name_to_id[s["name"].lower()] = sid
        clean = re.sub(r"[':\u2019]", "", s["name"]).lower().replace(" ", "_")
        name_to_id[clean] = sid
        for prefix in ["cast_", "damage_", "heal_", "buff_", "aura_", "proc_"]:
            if s["name"].lower().startswith(prefix):
                name_to_id[s["name"][len(prefix):].lower()] = sid

    verified = []
    for c in calls:
        spell_id = c.get("spell_ref_id")
        spell_name = "<unresolved>"

        if spell_id:
            s = spells.get(spell_id)
            spell_name = s["name"] if s else f"<unknown id={spell_id}>"
        elif c.get("spell_ref_name"):
            ref = c["spell_ref_name"].lower()
            # Direct match first
            if ref in name_to_id:
                spell_id = name_to_id[ref]
                s = spells[spell_id]
                spell_name = s["name"]
            else:
                # Containment match
                for name, sid in name_to_id.items():
                    if ref in name or name in ref:
                        spell_id = sid
                        s = spells[spell_id]
                        spell_name = s["name"]
                        break

        spell_info = spells.get(spell_id) if spell_id else None
        eff_info = effects.get((spell_id, c["idx"])) if spell_id else None
        num_eff = spell_info["num_effects"] if spell_info else None

        flag = None
        severity = "OK"
        detail = ""

        # Check 1: Bounds
        # effectN() is 1-indexed: effectN(1) → effects()[0]
        # Valid: N >= 1 && N <= num_effects
        if spell_info:
            if c["idx"] < 1:
                flag = "ZERO_INDEX"
                severity = "CRITICAL"
                detail = (
                    f"effectN({c['idx']}) is 0 or negative — SimC effectN is 1-indexed"
                )
            elif c["idx"] > num_eff:
                flag = "OOB"
                severity = "CRITICAL"
                detail = (
                    f"effectN({c['idx']}) but spell {spell_info['name']} ({spell_id}) "
                    f"has only {num_eff} effects (IDs: {spell_info['effect_ids']})"
                )
        elif not spell_info and spell_id:
            flag = "UNKNOWN_SPELL"
            severity = "WARNING"
            detail = f"Spell ID {spell_id} not found in DBC"

        # Check 2: Aura/accessor compatibility
        if not flag and eff_info:
            aura = eff_info["aura_type"]
            eff_type = eff_info["eff_type"]
            bv = eff_info["base_value"]
            good = ACCESSOR_AURA_WHITELIST.get(c["accessor"])
            if good is not None and aura not in good:
                flag = "AURA_MISMATCH"
                severity = "WARNING"
                detail = (
                    f".{c['accessor']}() on aura {aura} ({aura_name(aura)}), "
                    f"type {eff_type}, base_value={bv} — "
                    f"expected one of {sorted(good)}"
                )

        verified.append({
            **c,
            "spell_id": spell_id,
            "spell_name": spell_name,
            "spell_num_effects": num_eff,
            "effect_found": eff_info is not None,
            "aura_type": eff_info["aura_type"] if eff_info else None,
            "aura_name": aura_name(eff_info["aura_type"]) if eff_info else None,
            "eff_type": eff_info["eff_type"] if eff_info else None,
            "base_value": eff_info["base_value"] if eff_info else None,
            "misc_a": eff_info["misc_a"] if eff_info else None,
            "flag": flag,
            "severity": severity,
            "detail": detail,
        })

    return verified


# ─── Report ───────────────────────────────────────────────────────────────────

def _short_file(p):
    return os.path.basename(p)

def report(verified, outpath=None):
    stats = defaultdict(int)
    for v in verified:
        stats["total"] += 1
        if v["flag"]:
            stats[v["severity"]] += 1
        if v["spell_id"]:
            stats["resolved"] += 1
        else:
            stats["unresolved"] += 1
        if v["effect_found"]:
            stats["eff_found"] += 1

    flagged = [v for v in verified if v["flag"]]
    flagged.sort(key=lambda x: (
        {"CRITICAL": 0, "WARNING": 1}.get(x["severity"], 2),
        x["file"], x["line"]
    ))

    lines = []
    lines.append("# Spell Implementation Verification Report")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total effectN() calls scanned | {stats['total']} |")
    lines.append(f"| Resolved to spell ID | {stats['resolved']} |")
    lines.append(f"| Unresolved (variable) | {stats['unresolved']} |")
    lines.append(f"| DBC effect entry found | {stats['eff_found']} |")
    lines.append(f"| **CRITICAL** issues | {stats['CRITICAL']} |")
    lines.append(f"| WARNING issues | {stats['WARNING']} |")
    lines.append("")

    # Critical
    critical = [v for v in flagged if v["severity"] == "CRITICAL"]
    if critical:
        lines.append("## CRITICAL Issues (OOB / Unknown Spells)")
        lines.append("")
        lines.append("| # | File | Line | Spell | ID | Call | Detail |")
        lines.append("|---|------|------|-------|----|------|--------|")
        for i, v in enumerate(critical, 1):
            call_str = f"`{v['var_chain']}->effectN({v['idx']}).{v['accessor']}()`"
            lines.append(
                f"| {i} | `{_short_file(v['file'])}:{v['line']}` "
                f"| {v['spell_name']} | `{v['spell_id']}`"
                f"| {call_str} | {v['detail']} |"
            )
        lines.append("")

    # Warnings
    warns = [v for v in flagged if v["severity"] == "WARNING"]
    if warns:
        lines.append(f"## Warning Issues (Aura/accessor mismatch, {len(warns)} total)")
        lines.append("")
        lines.append("| # | File | Line | Spell | Accessor | Aura | Type | BV | Detail |")
        lines.append("|---|------|------|-------|----------|------|------|----|--------|")
        # Show first 50 to avoid huge output
        for i, v in enumerate(warns[:50], 1):
            aura_s = f"{v['aura_type']} ({v['aura_name']})" if v['aura_type'] else "?"
            type_s = str(v['eff_type']) if v['eff_type'] is not None else "?"
            bv_s = f"{v['base_value']:.4f}" if v['base_value'] is not None else "?"
            lines.append(
                f"| {i} | `{_short_file(v['file'])}:{v['line']}`"
                f"| {v['spell_name']} | .{v['accessor']}()"
                f"| {aura_s} | {type_s} | {bv_s} | {v['detail']} |"
            )
        if len(warns) > 50:
            lines.append(f"\n... and {len(warns) - 50} more warnings. See full output for details.")
        lines.append("")

    # Per-file summary
    lines.append("## Per-File Summary")
    lines.append("")
    lines.append("| File | Total | Resolved | CRIT | WARN |")
    lines.append("|------|-------|----------|------|------|")
    fs = defaultdict(lambda: defaultdict(int))
    for v in verified:
        f = _short_file(v["file"])
        fs[f]["total"] += 1
        if v["spell_id"]:
            fs[f]["resolved"] += 1
        if v["flag"]:
            fs[f][v["severity"]] += 1
    for fn in sorted(fs):
        s = fs[fn]
        lines.append(f"| {fn} | {s['total']} | {s['resolved']} | {s['CRITICAL']} | {s['WARNING']} |")

    txt = "\n".join(lines)
    if outpath:
        with open(outpath, "w") as f:
            f.write(txt)
        print(f"Report → {outpath}")
    else:
        print(txt)

    return flagged


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    import argparse
    p = argparse.ArgumentParser(description="Verify spell effectN() calls vs DBC")
    p.add_argument("--report", help="Output report path (markdown)")
    p.add_argument("--full", action="store_true", help="Include APL files")
    p.add_argument("--class-only", help="Comma-separated class filters")
    args = p.parse_args()

    files = [f for f in CLASS_FILES if os.path.isfile(f)]

    if args.class_only:
        keywords = [k.strip().lower() for k in args.class_only.split(",")]
        files = [f for f in files if any(k in f.lower() for k in keywords)]

    if args.full:
        for root, _, fnames in os.walk("engine/class_modules/apl"):
            for fn in sorted(fnames):
                if fn.endswith(".cpp"):
                    fp = os.path.join(root, fn)
                    if os.path.isfile(fp):
                        files.append(fp)

    print(f"Parsing DBC ...", file=sys.stderr)
    spells, effects = parse_dbc()

    print(f"Scanning {len(files)} files ...", file=sys.stderr)
    calls = scan_effectn_calls(files)
    print(f"  Found {len(calls)} effectN() calls", file=sys.stderr)

    print("Verifying ...", file=sys.stderr)
    verified = verify(calls, spells, effects)
    flagged = report(verified, args.report)

    n_crit = len([f for f in flagged if f["severity"] == "CRITICAL"])
    n_warn = len([f for f in flagged if f["severity"] == "WARNING"])
    if n_crit:
        print(f"\n*** {n_crit} CRITICAL, {n_warn} WARNING ***\n", file=sys.stderr)
        for f in flagged:
            if f["severity"] == "CRITICAL":
                print(f"  {f['file']}:{f['line']}  {f['spell_name']} ({f['spell_id']})  "
                      f"{f['detail']}", file=sys.stderr)
    else:
        print(f"\nNo critical issues. {n_warn} warnings.", file=sys.stderr)

    return n_crit


if __name__ == "__main__":
    sys.exit(main())
