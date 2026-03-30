#!/usr/bin/env python3
"""optimize_spec.py — Full optimization pipeline for a single spec.

Each spec produces TWO independent optimal profiles:
  - profiles/MID1/<Base>.simc          → PW-optimized (talent + APL best for Patchwerk)
  - profiles/MID1/<Base>_HAC.simc      → HAC-optimized (talent + APL best for HecticAddCleave)

Flow per spec:
  1. Talent optimize for Patchwerk   → best PW talent string
  2. Talent optimize for HAC         → best HAC talent string
  3. Apply PW talent to base profile → APL optimize for Patchwerk
  4. Create HAC profile copy         → apply HAC talent → APL optimize for HAC
  5. Smoke test both → validate → commit

Usage:
  python3 scripts/optimize_spec.py dk_unholy
  python3 scripts/optimize_spec.py --all
  python3 scripts/optimize_spec.py --all --dry-run
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.lib.sim_runner import find_profile

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
SIMC_BIN = os.path.join(ROOT, "engine", "simc")


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_profile_talent(path: str) -> str | None:
    with open(path) as f:
        for line in f:
            if line.startswith("talents="):
                return line.strip().split("=", 1)[1]
    return None


def set_profile_talent(path: str, talent_str: str):
    with open(path) as f:
        content = f.read()
    content = re.sub(r"^talents=.*$", f"talents={talent_str}", content, flags=re.MULTILINE)
    with open(path, "w") as f:
        f.write(content)


def apply_apl_file(profile_path: str, apl_path: str):
    """Replace all actions= lines in profile with those from APL file."""
    with open(profile_path) as f:
        lines = f.readlines()
    with open(apl_path) as f:
        apl_lines = f.readlines()
    non_action = [l for l in lines if not l.lstrip().startswith("actions")]
    if non_action and not non_action[-1].endswith("\n"):
        non_action[-1] += "\n"
    with open(profile_path, "w") as f:
        f.writelines(non_action)
        f.writelines(apl_lines)


def smoke_test(path: str) -> bool:
    r = subprocess.run(
        [SIMC_BIN, path, "iterations=1", "output=/dev/null"],
        capture_output=True, timeout=60, cwd=ROOT,
    )
    return r.returncode == 0


def find_opt_dir(spec: str, base_name: str) -> str:
    """Find or create the results/optimization/<spec> directory."""
    # apl_optimizer uses the full class name from find_profile, so the dir
    # may be under various aliases. Try common patterns.
    candidates = [
        spec,
        base_name.replace("MID1_", "").lower().replace(" ", "_"),
        spec.replace("dk_", "death_knight_").replace("dh_", "demon_hunter_")
            .replace("hunter_bm", "hunter_beast_mastery")
            .replace("hunter_mm", "hunter_marksmanship"),
    ]
    for name in candidates:
        d = os.path.join(RESULTS_DIR, name)
        if os.path.isdir(d):
            return d
    # Fallback: create using first candidate
    d = os.path.join(RESULTS_DIR, candidates[0])
    os.makedirs(d, exist_ok=True)
    return d


# ── Talent search ────────────────────────────────────────────────────────────

def run_talent_search(spec: str, fight_style: str, max_iter: int = 5) -> tuple[str | None, float]:
    """Run talent local search. Returns (talent_string, dps) or (None, 0)."""
    cmd = [
        sys.executable, os.path.join(ROOT, "scripts", "talent_local_search.py"),
        "--spec", spec, "--fight-style", fight_style, "--max-iter", str(max_iter),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200, cwd=ROOT)
    print(result.stdout)
    if result.returncode != 0:
        print(f"  TALENT ERROR: {result.stderr[-500:]}")
        return None, 0.0

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


# ── APL optimization ─────────────────────────────────────────────────────────

def run_apl_optimizer_single(spec: str, fight_style: str, max_iter: int = 5):
    """Run APL optimizer for a single fight style."""
    cmd = [
        sys.executable, os.path.join(ROOT, "scripts", "apl_optimizer.py"),
        spec, "--fight-style", fight_style, "--max-iter", str(max_iter),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600, cwd=ROOT)
    print(result.stdout)
    if result.returncode != 0:
        print(f"  APL ERROR: {result.stderr[-500:]}")


# ── Main pipeline ────────────────────────────────────────────────────────────

def optimize_one_spec(spec: str, max_iter: int = 5, dry_run: bool = False):
    base_name = PROFILE_MAP.get(spec)
    if not base_name:
        print(f"  SKIP: {spec} not in PROFILE_MAP")
        return

    pw_profile = os.path.join(PROFILES_DIR, f"{base_name}.simc")
    hac_profile = os.path.join(PROFILES_DIR, f"{base_name}_HAC.simc")

    if not os.path.exists(pw_profile):
        print(f"  SKIP: {pw_profile} does not exist")
        return

    print(f"\n{'='*70}")
    print(f"  OPTIMIZING: {spec}")
    print(f"  PW  profile: {base_name}.simc")
    print(f"  HAC profile: {base_name}_HAC.simc")
    print(f"{'='*70}")

    if dry_run:
        print("  [DRY RUN] would create two optimized profiles")
        return

    start = time.time()

    # ── 1. Talent optimization (independent per style) ───────────────────
    print(f"\n--- Step 1a: Talent optimization (Patchwerk) ---")
    pw_talent, pw_dps = run_talent_search(spec, "Patchwerk", max_iter)

    print(f"\n--- Step 1b: Talent optimization (HecticAddCleave) ---")
    hac_talent, hac_dps = run_talent_search(spec, "HecticAddCleave", max_iter)

    # ── 2. Apply PW talent to base profile ───────────────────────────────
    if pw_talent:
        print(f"\n--- Step 2a: Applying PW-optimized talent to {base_name}.simc ---")
        set_profile_talent(pw_profile, pw_talent)
        print(f"  PW talent applied ({pw_dps:,.0f} DPS)")
    else:
        print(f"\n--- Step 2a: No PW talent improvement, keeping original ---")

    # ── 3. Create HAC profile (copy base, then override talent) ──────────
    print(f"\n--- Step 2b: Creating HAC profile {base_name}_HAC.simc ---")
    shutil.copy2(pw_profile, hac_profile)
    if hac_talent:
        set_profile_talent(hac_profile, hac_talent)
        print(f"  HAC talent applied ({hac_dps:,.0f} DPS)")
    else:
        print(f"  No HAC talent improvement, HAC profile uses PW talent")

    # ── 4. APL optimization (independent per style) ──────────────────────
    print(f"\n--- Step 3a: APL optimization (Patchwerk) ---")
    run_apl_optimizer_single(spec, "Patchwerk", max_iter)

    # Apply PW APL to base profile if it exists
    opt_dir = find_opt_dir(spec, base_name)
    pw_apl = os.path.join(opt_dir, "optimized_apl_pw.simc")
    if os.path.exists(pw_apl):
        apply_apl_file(pw_profile, pw_apl)
        print(f"  Applied PW APL to {base_name}.simc")

    # For HAC APL: temporarily point find_profile at the HAC profile
    # We need to set the HAC profile talent first, then run APL optimizer
    # But apl_optimizer uses find_profile which finds the base. So we swap:
    print(f"\n--- Step 3b: APL optimization (HecticAddCleave) ---")
    # Backup base, put HAC in its place, run optimizer, restore
    pw_backup = pw_profile + ".pw_backup"
    shutil.copy2(pw_profile, pw_backup)
    shutil.copy2(hac_profile, pw_profile)
    run_apl_optimizer_single(spec, "HecticAddCleave", max_iter)
    # Restore base profile
    shutil.copy2(pw_backup, pw_profile)
    os.unlink(pw_backup)

    # Apply HAC APL to HAC profile if it exists
    hac_apl = os.path.join(opt_dir, "optimized_apl_hac.simc")
    if os.path.exists(hac_apl):
        apply_apl_file(hac_profile, hac_apl)
        print(f"  Applied HAC APL to {base_name}_HAC.simc")

    # ── 5. Smoke test ────────────────────────────────────────────────────
    print(f"\n--- Step 4: Smoke test ---")
    all_pass = True
    for label, path in [("PW", pw_profile), ("HAC", hac_profile)]:
        ok = smoke_test(path)
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: {label} — {os.path.basename(path)}")
        if not ok:
            all_pass = False

    if not all_pass:
        print("  WARNING: Some profiles failed smoke test!")
        return

    # ── 6. Git commit ────────────────────────────────────────────────────
    print(f"\n--- Step 5: Commit ---")
    subprocess.run(["git", "add", pw_profile, hac_profile], cwd=ROOT)
    diff = subprocess.run(["git", "diff", "--cached", "--stat"],
                          capture_output=True, text=True, cwd=ROOT)
    if diff.stdout.strip():
        parts = []
        if pw_talent:
            parts.append(f"PW talent {pw_dps:,.0f}")
        if hac_talent:
            parts.append(f"HAC talent {hac_dps:,.0f}")
        if os.path.exists(pw_apl):
            parts.append("PW APL improved")
        if os.path.exists(hac_apl):
            parts.append("HAC APL improved")
        detail = "; ".join(parts) if parts else "no changes"
        msg = f"optimize({spec}): {detail}"
        subprocess.run(["git", "commit", "-m", msg], cwd=ROOT)
        print(f"  Committed: {msg}")
    else:
        print("  No changes to commit")

    elapsed = time.time() - start
    print(f"\n  Done in {elapsed:.0f}s")


def main():
    parser = argparse.ArgumentParser(
        description="Full spec optimization — produces two profiles per spec (PW + HAC)")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g., dk_unholy)")
    parser.add_argument("--all", action="store_true", help="Optimize all specs")
    parser.add_argument("--max-iter", type=int, default=5, help="Max iterations per optimizer")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without running")
    args = parser.parse_args()

    if args.all:
        specs = sorted(PROFILE_MAP.keys())
        print(f"Optimizing {len(specs)} specs — each gets PW + HAC profiles...")
        for i, spec in enumerate(specs, 1):
            print(f"\n[{i}/{len(specs)}]")
            optimize_one_spec(spec, args.max_iter, args.dry_run)
    elif args.spec:
        optimize_one_spec(args.spec, args.max_iter, args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
