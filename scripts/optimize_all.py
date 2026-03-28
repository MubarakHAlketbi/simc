#!/usr/bin/env python3
"""Master Orchestrator — talent discovery -> APL optimization -> validation.

Usage:
  python3 scripts/optimize_all.py --report          # Show current baselines
  python3 scripts/optimize_all.py --apl --all       # APL optimize all specs
  python3 scripts/optimize_all.py --spec warrior_fury --apl  # Single spec
"""

import argparse
import json
import glob
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PROFILE_MAP = {
    "warrior_arms": "MID1_Warrior_Arms", "warrior_fury": "MID1_Warrior_Fury",
    "warrior_protection": "MID1_Warrior_Protection",
    "paladin_protection": "MID1_Paladin_Protection",
    "paladin_retribution": "MID1_Paladin_Retribution",
    "hunter_bm": "MID1_Hunter_Beast_Mastery", "hunter_mm": "MID1_Hunter_Marksmanship",
    "hunter_survival": "MID1_Hunter_Survival",
    "rogue_assassination": "MID1_Rogue_Assassination", "rogue_outlaw": "MID1_Rogue_Outlaw",
    "rogue_subtlety": "MID1_Rogue_Subtlety", "priest_shadow": "MID1_Priest_Shadow",
    "dk_blood": "MID1_Death_Knight_Blood", "dk_frost": "MID1_Death_Knight_Frost",
    "dk_unholy": "MID1_Death_Knight_Unholy",
    "shaman_elemental": "MID1_Shaman_Elemental", "shaman_enhancement": "MID1_Shaman_Enhancement",
    "mage_arcane": "MID1_Mage_Arcane", "mage_fire": "MID1_Mage_Fire", "mage_frost": "MID1_Mage_Frost",
    "warlock_affliction": "MID1_Warlock_Affliction", "warlock_demonology": "MID1_Warlock_Demonology",
    "warlock_destruction": "MID1_Warlock_Destruction",
    "monk_brewmaster": "MID1_Monk_Brewmaster", "monk_windwalker": "MID1_Monk_Windwalker",
    "druid_balance": "MID1_Druid_Balance", "druid_feral": "MID1_Druid_Feral",
    "druid_guardian": "MID1_Druid_Guardian",
    "evoker_devastation": "MID1_Evoker_Devastation", "evoker_augmentation": "MID1_Evoker_Augmentation",
    "dh_havoc": "MID1_Demon_Hunter_Havoc", "dh_vengeance": "MID1_Demon_Hunter_Vengeance",
    "dh_devourer": "MID1_Demon_Hunter_Devourer",
}


def generate_report():
    """Generate summary report from Phase 4 baselines."""
    baselines = []
    for pw_file in sorted(glob.glob("results/phase4/*_patchwerk.json")):
        name = os.path.basename(pw_file).replace("_patchwerk.json", "")
        hac_file = pw_file.replace("_patchwerk.json", "_hecticaddcleave.json")
        if not os.path.exists(hac_file):
            continue
        try:
            with open(pw_file) as f:
                pw_dps = json.load(f)["sim"]["players"][0]["collected_data"]["dps"]["mean"]
            with open(hac_file) as f:
                hac_dps = json.load(f)["sim"]["players"][0]["collected_data"]["dps"]["mean"]
            comp = 0.5 * pw_dps + 0.5 * hac_dps
            baselines.append((name, pw_dps, hac_dps, comp))
        except Exception as e:
            print(f"Error reading {name}: {e}")

    baselines.sort(key=lambda x: -x[3])
    print(f"\n{'Profile':<55} {'Patchwerk':>10} {'HAC':>10} {'Composite':>10}")
    print("-" * 90)
    for name, pw, hac, comp in baselines:
        print(f"{name:<55} {pw:>10,.0f} {hac:>10,.0f} {comp:>10,.0f}")
    print(f"\nTotal: {len(baselines)} profiles")
    return baselines


def main():
    parser = argparse.ArgumentParser(description="SimC Midnight Optimization Pipeline")
    parser.add_argument("--spec", type=str, help="Single spec to optimize")
    parser.add_argument("--all", action="store_true", help="All 33 specs")
    parser.add_argument("--apl", action="store_true", help="Run APL optimization")
    parser.add_argument("--report", action="store_true", help="Show baseline report")
    parser.add_argument("--max-iter", type=int, default=5, help="Max APL optimizer iterations")
    args = parser.parse_args()

    if args.report:
        generate_report()
        return

    specs = list(PROFILE_MAP.keys()) if args.all else ([args.spec] if args.spec else [])
    if not specs:
        parser.print_help()
        return

    print(f"=== SimC Midnight Optimization ===")
    print(f"Specs: {len(specs)}, APL: {args.apl}, Max iter: {args.max_iter}")

    if args.apl:
        from apl_optimizer import optimize_spec
        for i, spec in enumerate(specs):
            profile = f"profiles/MID1/{PROFILE_MAP[spec]}.simc"
            if not os.path.exists(profile):
                print(f"  [{i+1}/{len(specs)}] {spec}: SKIP (no profile)")
                continue
            print(f"  [{i+1}/{len(specs)}] {spec}: optimizing...")
            try:
                optimize_spec(spec, profile, max_iterations=args.max_iter)
                print(f"  [{i+1}/{len(specs)}] {spec}: DONE")
            except Exception as e:
                print(f"  [{i+1}/{len(specs)}] {spec}: ERROR {e}")


if __name__ == "__main__":
    main()
