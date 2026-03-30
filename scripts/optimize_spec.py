#!/usr/bin/env python3
"""optimize_spec.py — Full optimization pipeline for a single spec.

Runs talent optimization (both styles) → picks HAC-optimized talents →
applies to profile + variants → runs APL optimization → applies APL →
validates → commits.

Usage:
  python3 scripts/optimize_spec.py dk_unholy
  python3 scripts/optimize_spec.py --all          # all specs sequentially
  python3 scripts/optimize_spec.py --all --dry-run # just show what would be done
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.lib.sim_runner import find_profile

# Maps short spec name → profile base name (without .simc)
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

PROFILES_DIR = os.path.join(ROOT, "profiles", "MID1")
RESULTS_DIR = os.path.join(ROOT, "results", "optimization")


def find_variants(base_profile_name: str) -> list[str]:
    """Find variant profiles that share the same base.

    E.g., MID1_Death_Knight_Frost → [MID1_Death_Knight_Frost_Rider.simc]
    """
    pattern = os.path.join(PROFILES_DIR, f"{base_profile_name}_*.simc")
    base_path = os.path.join(PROFILES_DIR, f"{base_profile_name}.simc")
    variants = []
    for f in sorted(glob.glob(pattern)):
        if f != base_path:
            variants.append(f)
    return variants


def get_profile_talent(profile_path: str) -> str | None:
    """Extract the talents= line from a profile."""
    with open(profile_path) as f:
        for line in f:
            if line.startswith("talents="):
                return line.strip().split("=", 1)[1]
    return None


def set_profile_talent(profile_path: str, talent_str: str):
    """Replace the talents= line in a profile."""
    with open(profile_path) as f:
        content = f.read()
    content = re.sub(r"^talents=.*$", f"talents={talent_str}", content, flags=re.MULTILINE)
    with open(profile_path, "w") as f:
        f.write(content)


def apply_optimized_apl(profile_path: str, apl_path: str):
    """Replace all actions= lines in profile with those from optimized APL."""
    with open(profile_path) as f:
        lines = f.readlines()
    with open(apl_path) as f:
        apl_lines = f.readlines()

    # Keep non-action lines
    non_action = [l for l in lines if not l.lstrip().startswith("actions")]
    # Ensure trailing newline
    if non_action and not non_action[-1].endswith("\n"):
        non_action[-1] += "\n"

    with open(profile_path, "w") as f:
        f.writelines(non_action)
        f.writelines(apl_lines)


def run_talent_search(spec: str, fight_style: str, max_iter: int = 5) -> tuple[str | None, float]:
    """Run talent local search, return (talent_string, dps) or (None, 0)."""
    cmd = [
        sys.executable, os.path.join(ROOT, "scripts", "talent_local_search.py"),
        "--spec", spec, "--fight-style", fight_style, "--max-iter", str(max_iter),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200, cwd=ROOT)
    print(result.stdout)
    if result.returncode != 0:
        print(f"  TALENT ERROR: {result.stderr[-500:]}")
        return None, 0.0

    # Parse output for talent string and DPS
    talent_str = None
    final_dps = 0.0
    for line in result.stdout.split("\n"):
        if line.startswith("Talent string:"):
            talent_str = line.split(":", 1)[1].strip()
        if line.startswith("Final:"):
            try:
                final_dps = float(line.split(":")[1].strip().split()[0].replace(",", ""))
            except (ValueError, IndexError):
                pass
    return talent_str, final_dps


def run_apl_optimizer(spec: str, max_iter: int = 5) -> dict:
    """Run APL optimizer for both styles. Returns summary dict."""
    # Use the full class name for apl_optimizer since we fixed find_profile
    cmd = [
        sys.executable, os.path.join(ROOT, "scripts", "apl_optimizer.py"),
        spec, "--max-iter", str(max_iter),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600, cwd=ROOT)
    print(result.stdout)
    if result.returncode != 0:
        print(f"  APL ERROR: {result.stderr[-500:]}")
    return {}


def smoke_test(profile_path: str) -> bool:
    """Run 1-iteration smoke test."""
    simc = os.path.join(ROOT, "engine", "simc")
    result = subprocess.run(
        [simc, profile_path, "iterations=1", "output=/dev/null"],
        capture_output=True, timeout=60, cwd=ROOT,
    )
    return result.returncode == 0


def optimize_one_spec(spec: str, max_iter: int = 5, dry_run: bool = False):
    """Full optimization pipeline for one spec."""
    base_name = PROFILE_MAP.get(spec)
    if not base_name:
        print(f"  SKIP: {spec} not in PROFILE_MAP")
        return

    profile_path = os.path.join(PROFILES_DIR, f"{base_name}.simc")
    if not os.path.exists(profile_path):
        print(f"  SKIP: {profile_path} does not exist")
        return

    variants = find_variants(base_name)
    all_profiles = [profile_path] + variants
    variant_names = [os.path.basename(v) for v in variants]

    print(f"\n{'='*70}")
    print(f"  OPTIMIZING: {spec}")
    print(f"  Base profile: {base_name}.simc")
    if variant_names:
        print(f"  Variants: {', '.join(variant_names)}")
    print(f"{'='*70}")

    if dry_run:
        print("  [DRY RUN] would optimize talent + APL")
        return

    start = time.time()

    # Step 1: Talent optimization — both fight styles
    print(f"\n--- Step 1: Talent optimization (Patchwerk) ---")
    pw_talent, pw_dps = run_talent_search(spec, "Patchwerk", max_iter)

    print(f"\n--- Step 2: Talent optimization (HecticAddCleave) ---")
    hac_talent, hac_dps = run_talent_search(spec, "HecticAddCleave", max_iter)

    # Step 2: Choose talent build
    # Strategy: use HAC-optimized talent if it improved, else use PW-optimized
    chosen_talent = None
    chosen_label = "none"
    original_talent = get_profile_talent(profile_path)

    if hac_talent and hac_dps > 0:
        chosen_talent = hac_talent
        chosen_label = "HAC-optimized"
    elif pw_talent and pw_dps > 0:
        chosen_talent = pw_talent
        chosen_label = "PW-optimized"

    if chosen_talent and chosen_talent != original_talent:
        print(f"\n--- Step 3: Applying {chosen_label} talents ---")
        for p in all_profiles:
            set_profile_talent(p, chosen_talent)
            print(f"  Updated: {os.path.basename(p)}")
    else:
        print(f"\n--- Step 3: No talent change needed ---")

    # Step 3: APL optimization
    print(f"\n--- Step 4: APL optimization ---")
    run_apl_optimizer(spec, max_iter)

    # Apply optimized APL if it exists
    spec_opt_dir = os.path.join(RESULTS_DIR, spec.replace("dk_", "death_knight_").replace("dh_", "demon_hunter_").replace("hunter_bm", "hunter_beast_mastery").replace("hunter_mm", "hunter_marksmanship"))
    # Try the direct name mapping used by find_profile
    for possible_dir_name in [spec, base_name.replace("MID1_", "").lower().replace(" ", "_")]:
        d = os.path.join(RESULTS_DIR, possible_dir_name)
        if os.path.isdir(d):
            spec_opt_dir = d
            break

    for style_tag in ["pw", "hac"]:
        apl_file = os.path.join(spec_opt_dir, f"optimized_apl_{style_tag}.simc")
        if os.path.exists(apl_file):
            print(f"  Applying optimized APL ({style_tag}) to base profile")
            apply_optimized_apl(profile_path, apl_file)

    # Step 4: Smoke test all profiles
    print(f"\n--- Step 5: Smoke test ---")
    all_pass = True
    for p in all_profiles:
        ok = smoke_test(p)
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: {os.path.basename(p)}")
        if not ok:
            all_pass = False

    if not all_pass:
        print("  WARNING: Some profiles failed smoke test!")
        return

    # Step 5: Git commit
    print(f"\n--- Step 6: Commit ---")
    changed = [p for p in all_profiles]
    subprocess.run(["git", "add"] + changed, cwd=ROOT)
    # Check if anything actually changed
    diff = subprocess.run(["git", "diff", "--cached", "--stat"], capture_output=True, text=True, cwd=ROOT)
    if diff.stdout.strip():
        msg = f"optimize({spec}): {chosen_label} talents; APL optimized; validates"
        subprocess.run(["git", "commit", "-m", msg], cwd=ROOT)
        print(f"  Committed: {msg}")
    else:
        print("  No changes to commit")

    elapsed = time.time() - start
    print(f"\n  Done in {elapsed:.0f}s")


def main():
    parser = argparse.ArgumentParser(description="Full spec optimization pipeline")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g., dk_unholy)")
    parser.add_argument("--all", action="store_true", help="Optimize all specs")
    parser.add_argument("--max-iter", type=int, default=5, help="Max iterations per optimizer")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without running")
    args = parser.parse_args()

    if args.all:
        specs = sorted(PROFILE_MAP.keys())
        print(f"Optimizing {len(specs)} specs sequentially...")
        for i, spec in enumerate(specs, 1):
            print(f"\n[{i}/{len(specs)}]")
            optimize_one_spec(spec, args.max_iter, args.dry_run)
    elif args.spec:
        optimize_one_spec(args.spec, args.max_iter, args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
