#!/usr/bin/env python3
"""
update_talents_from_extracted.py

After re-running extract_wowhead_tabs.py --all --pages talents,
this script reads the talent codes from extracted/talents.md files
and updates the talents= line in each matching MID1 profile.

Usage:
    python3 update_talents_from_extracted.py [--dry-run]

For hero-tree variant profiles (e.g. MID1_Warrior_Fury_Slayer.simc),
it picks the code matching that hero tree. For base profiles, it picks
the first code from the first/primary hero tree.
"""
import re, os, glob, argparse, sys

def extract_talent_codes_from_md(md_path):
    """
    Parse a talents.md file and return a dict:
      hero_name -> [list of talent code strings]
    If no hero switches, key is "default".
    """
    if not os.path.exists(md_path):
        return {}

    with open(md_path) as f:
        content = f.read()

    result = {}
    current_hero = "default"

    for line in content.split("\n"):
        # Detect hero section headers: "## Hero Talent: Slayer" or "## Default"
        m = re.match(r"^## Hero Talent: (.+)$", line)
        if m:
            current_hero = m.group(1).strip()
            result.setdefault(current_hero, [])
            continue
        m2 = re.match(r"^## Default", line)
        if m2:
            current_hero = "default"
            result.setdefault(current_hero, [])
            continue

        # Detect talent code lines: "Build N: `CODE`"
        m3 = re.match(r"^Build \d+: `([A-Za-z0-9+/]{40,}={0,2})`$", line)
        if m3:
            code = m3.group(1)
            result.setdefault(current_hero, []).append(code)

    return result

# Mapping: spec slug -> wowhead class/spec path
SPEC_TO_WOWHEAD = {
    "blood":         "death-knight/blood",
    "unholy":        "death-knight/unholy",
    "havoc":         "demon-hunter/havoc",
    "vengeance":     "demon-hunter/vengeance",
    "balance":       "druid/balance",
    "feral":         "druid/feral",
    "guardian":      "druid/guardian",
    "devastation":   "evoker/devastation",
    "augmentation":  "evoker/augmentation",
    "beast_mastery": "hunter/beast-mastery",
    "marksmanship":  "hunter/marksmanship",
    "survival":      "hunter/survival",
    "arcane":        "mage/arcane",
    "fire":          "mage/fire",
    "brewmaster":    "monk/brewmaster",
    "windwalker":    "monk/windwalker",
    "retribution":   "paladin/retribution",
    "shadow":        "priest/shadow",
    "assassination": "rogue/assassination",
    "outlaw":        "rogue/outlaw",
    "subtlety":      "rogue/subtlety",
    "elemental":     "shaman/elemental",
    "enhancement":   "shaman/enhancement",
    "affliction":    "warlock/affliction",
    "demonology":    "warlock/demonology",
    "destruction":   "warlock/destruction",
    "arms":          "warrior/arms",
    "fury":          "warrior/fury",
}

def get_wowhead_key(pname, spec):
    n = pname.lower()
    if spec == "frost":
        return "mage/frost" if "mage" in n else "death-knight/frost"
    if spec == "protection":
        return "paladin/protection" if "paladin" in n else "warrior/protection"
    if "devourer" in n:
        return "demon-hunter/havoc"
    return SPEC_TO_WOWHEAD.get(spec)

def guess_hero_from_filename(pname, codes_by_hero):
    """Try to match hero tree name from profile filename to codes_by_hero keys."""
    pname_lower = pname.lower()
    for hero_name in codes_by_hero:
        if hero_name == "default":
            continue
        # Normalize hero name for comparison
        hero_norm = re.sub(r"[^a-z0-9]", "", hero_name.lower())
        if hero_norm in pname_lower or any(w in pname_lower for w in hero_norm.split()):
            return hero_name
    return None

def main():
    parser = argparse.ArgumentParser(description="Update profile talents= from extracted talent codes")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--wowhead-dir", default="wowhead", help="Wowhead directory")
    parser.add_argument("--profiles-dir", default="profiles/MID1", help="Profiles directory")
    args = parser.parse_args()

    profiles = sorted(glob.glob(os.path.join(args.profiles_dir, "*.simc")))
    updated = 0
    skipped_no_codes = 0
    skipped_same = 0

    for pf in profiles:
        pname = os.path.basename(pf)
        with open(pf) as f:
            content = f.read()

        spec_m = re.search(r"^spec=(\w+)", content, re.M)
        if not spec_m:
            continue
        spec = spec_m.group(1)

        wk = get_wowhead_key(pname, spec)
        if not wk:
            continue

        md_path = os.path.join(args.wowhead_dir, wk, "extracted", "talents.md")
        codes_by_hero = extract_talent_codes_from_md(md_path)

        if not codes_by_hero:
            skipped_no_codes += 1
            continue

        # Pick the right hero tree
        # 1. Try to match filename to a hero name in the extracted codes
        # 2. Fall back to first available hero / default
        hero_match = guess_hero_from_filename(pname, codes_by_hero)

        if hero_match and codes_by_hero.get(hero_match):
            codes = codes_by_hero[hero_match]
        elif "default" in codes_by_hero and codes_by_hero["default"]:
            codes = codes_by_hero["default"]
        else:
            # Use first available
            codes = next((v for v in codes_by_hero.values() if v), None)

        if not codes:
            skipped_no_codes += 1
            continue

        new_talent = codes[0]  # Use first (primary) build

        # Check current talents= line
        cur_m = re.search(r"^talents=(.+)$", content, re.M)
        if cur_m and cur_m.group(1).strip() == new_talent:
            skipped_same += 1
            continue

        new_content = re.sub(r"^talents=.+$", f"talents={new_talent}", content, flags=re.M)
        cur_val = cur_m.group(1).strip() if cur_m else "(none)"

        print(f"  UPDATE {pname}")
        print(f"    old: {cur_val[:60]}...")
        print(f"    new: {new_talent[:60]}...")

        if not args.dry_run:
            with open(pf, "w") as f:
                f.write(new_content)
        updated += 1

    print(f"\nSummary: {updated} updated, {skipped_same} already correct, {skipped_no_codes} skipped (no codes extracted yet)")
    if skipped_no_codes > 0:
        print(f"  -> Run: python3 wowhead/extract_wowhead_tabs.py --all --pages talents")
        print(f"     then re-run this script to update remaining profiles.")

if __name__ == "__main__":
    main()
