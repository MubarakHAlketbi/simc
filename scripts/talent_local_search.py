#!/usr/bin/env python3
"""
talent_local_search.py — Hill-climbing talent optimizer using valid neighbors.

Starts from a seed build (Wowhead/profile), generates valid 1-step mutations,
sims them in multi-stage filtering, and greedily accepts improvements.

Usage:
  python3 scripts/talent_local_search.py --spec warrior_fury [--fight-style Patchwerk]
  python3 scripts/talent_local_search.py --spec warrior_fury --max-iter 3
  python3 scripts/talent_local_search.py --all
"""

import argparse
import json
import os
import subprocess
import sys
import time
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.lib.talent_tree import SPEC_MAP, build_talent_tree
from scripts.lib.talent_validator import (
    TreeConstraints, validate_build, count_points, generate_neighbors,
)
from scripts.lib.tree_codec_bridge import (
    decode_profile_talents, encode_profile_talents,
)
from scripts.lib.talent_codec import decode_talent_string, encode_talent_string

# ─── Constants ────────────────────────────────────────────────────────────────

SIMC_BIN = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "engine", "simc")

PROFILE_MAP = {}
for _spec in SPEC_MAP:
    parts = _spec.split("_")
    # Build profile path from spec name
    if _spec.startswith("dk_"):
        cls = "Death_Knight"
        spc = parts[1].title()
    elif _spec.startswith("dh_"):
        cls = "Demon_Hunter"
        spc = parts[1].title()
    elif _spec.startswith("hunter_bm"):
        cls = "Hunter"
        spc = "Beast_Mastery"
    elif _spec.startswith("hunter_mm"):
        cls = "Hunter"
        spc = "Marksmanship"
    else:
        cls = parts[0].title()
        spc = "_".join(p.title() for p in parts[1:])
    PROFILE_MAP[_spec] = f"profiles/MID1/MID1_{cls}_{spc}.simc"


# ─── Sim Runner ───────────────────────────────────────────────────────────────

def run_sim(
    profile_path: str,
    talent_override: str,
    fight_style: str = "Patchwerk",
    iterations: int = 1000,
    threads: int = 16,
) -> Optional[float]:
    """Run SimC and return DPS. Returns None on error."""
    cmd = [
        SIMC_BIN,
        profile_path,
        f"talents={talent_override}",
        f"fight_style={fight_style}",
        f"iterations={iterations}",
        f"threads={threads}",
        "json2=/tmp/talent_search_result.json",
        "output=/dev/null",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, timeout=120)
        if result.returncode != 0:
            return None
        with open("/tmp/talent_search_result.json") as f:
            data = json.load(f)
        return data["sim"]["players"][0]["collected_data"]["dps"]["mean"]
    except (subprocess.TimeoutExpired, json.JSONDecodeError, KeyError, FileNotFoundError):
        return None


# ─── Multi-Stage Filter ──────────────────────────────────────────────────────

def multi_stage_eval(
    candidates: List[Tuple[str, str]],  # (description, talent_string)
    profile_path: str,
    fight_style: str,
    baseline_dps: float,
    threads: int = 16,
) -> List[Tuple[str, str, float]]:
    """
    Multi-stage filtering of candidates.
    Stage 1: 300 iter on all -> keep top 20% or > -0.5%
    Stage 2: 3000 iter on survivors -> keep > 0% improvement
    Stage 3: 10000 iter on top 3 -> confirm improvement
    """
    if not candidates:
        return []

    # Stage 1: coarse filter
    stage1 = []
    for desc, tstr in candidates:
        dps = run_sim(profile_path, tstr, fight_style, iterations=300, threads=threads)
        if dps is not None:
            stage1.append((desc, tstr, dps))

    if not stage1:
        return []

    # Keep top 20% or those within 0.5% of best
    stage1.sort(key=lambda x: -x[2])
    cutoff = max(len(stage1) // 5, 3)
    best_s1 = stage1[0][2]
    survivors = [x for x in stage1[:cutoff] if x[2] >= best_s1 * 0.995]
    # Also keep anything that beats baseline
    for x in stage1[cutoff:]:
        if x[2] > baseline_dps:
            survivors.append(x)

    if not survivors:
        return []

    # Stage 2: medium filter
    stage2 = []
    for desc, tstr, _ in survivors:
        dps = run_sim(profile_path, tstr, fight_style, iterations=3000, threads=threads)
        if dps is not None and dps > baseline_dps:
            stage2.append((desc, tstr, dps))

    if not stage2:
        return []

    # Stage 3: confirm top 3
    stage2.sort(key=lambda x: -x[2])
    stage3 = []
    for desc, tstr, _ in stage2[:3]:
        dps = run_sim(profile_path, tstr, fight_style, iterations=10000, threads=threads)
        if dps is not None:
            stage3.append((desc, tstr, dps))

    stage3.sort(key=lambda x: -x[2])
    return stage3


# ─── Main Search Loop ────────────────────────────────────────────────────────

def local_search(
    spec_name: str,
    fight_style: str = "Patchwerk",
    max_iterations: int = 5,
    threads: int = 16,
) -> Tuple[Optional[str], float, str]:
    """
    Hill-climbing talent optimization.

    Returns (best_talent_string, best_dps, description).
    """
    profile_path = PROFILE_MAP.get(spec_name)
    if not profile_path or not os.path.exists(profile_path):
        print(f"ERROR: Profile not found for {spec_name}")
        return None, 0.0, "no profile"

    # Load seed build
    with open(profile_path) as f:
        content = f.read()
    talent_str = None
    for line in content.split("\n"):
        if line.startswith("talents="):
            talent_str = line.strip().split("=", 1)[1]
            break

    if not talent_str:
        print(f"ERROR: No talents= in {profile_path}")
        return None, 0.0, "no talents"

    # Build constraint data
    tc = TreeConstraints.build(spec_name)
    selections = decode_profile_talents(talent_str, spec_name)

    # Validate seed
    result = validate_build(selections, tc)
    if not result.valid:
        print(f"ERROR: Seed build is invalid: {result.errors[:3]}")
        return None, 0.0, "invalid seed"

    cp, sp, hp = count_points(selections, tc)
    print(f"Seed: class={cp}/34 spec={sp}/34 hero={hp}")

    # Baseline DPS
    print(f"Running baseline ({fight_style}, 10k iter)...")
    baseline_dps = run_sim(profile_path, talent_str, fight_style, iterations=10000, threads=threads)
    if baseline_dps is None:
        print("ERROR: Baseline sim failed")
        return None, 0.0, "sim failed"

    print(f"Baseline DPS: {baseline_dps:,.0f}")

    best_str = talent_str
    best_dps = baseline_dps
    best_desc = "seed"

    for iteration in range(max_iterations):
        print(f"\n=== Iteration {iteration + 1}/{max_iterations} ===")

        # Decode current best
        selections = decode_profile_talents(best_str, spec_name)

        # Generate all valid neighbors
        neighbors = list(generate_neighbors(selections, tc))
        print(f"Generated {len(neighbors)} valid neighbors")

        if not neighbors:
            print("No neighbors to explore. Done.")
            break

        # Encode neighbors to talent strings
        # We need purchased_flags for round-trip safety
        class_id, spec_id = SPEC_MAP[spec_name]
        from scripts.lib.tree_codec_bridge import tree_to_codec_nodes
        codec_nodes = tree_to_codec_nodes(tc.tree, spec_id)
        _, _, purchased_flags = decode_talent_string(best_str, codec_nodes)

        candidates = []
        for desc, new_selections in neighbors:
            try:
                new_str = encode_profile_talents(new_selections, spec_name, purchased_flags)
                candidates.append((desc, new_str))
            except Exception:
                continue

        print(f"Encoded {len(candidates)} candidates")

        # Multi-stage evaluation
        results = multi_stage_eval(candidates, profile_path, fight_style, best_dps, threads)

        if results and results[0][2] > best_dps:
            desc, new_str, new_dps = results[0]
            gain = (new_dps - best_dps) / best_dps * 100
            print(f"IMPROVEMENT: {desc}")
            print(f"  {best_dps:,.0f} -> {new_dps:,.0f} (+{gain:.2f}%)")
            best_str = new_str
            best_dps = new_dps
            best_desc = desc
        else:
            print("No improvement found. Local optimum reached.")
            break

    return best_str, best_dps, best_desc


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Talent hill-climbing optimizer")
    parser.add_argument("--spec", type=str, help="Spec to optimize (e.g., warrior_fury)")
    parser.add_argument("--fight-style", type=str, default="Patchwerk",
                        help="Fight style (Patchwerk or HecticAddCleave)")
    parser.add_argument("--max-iter", type=int, default=5, help="Max hill-climb iterations")
    parser.add_argument("--threads", type=int, default=16, help="Sim threads")
    parser.add_argument("--all", action="store_true", help="Run on all valid specs")

    args = parser.parse_args()

    if args.all:
        specs = sorted(SPEC_MAP.keys())
        for spec in specs:
            profile = PROFILE_MAP.get(spec)
            if not profile or not os.path.exists(profile):
                continue
            print(f"\n{'='*60}")
            print(f"  {spec} — {args.fight_style}")
            print(f"{'='*60}")
            best_str, best_dps, desc = local_search(
                spec, args.fight_style, args.max_iter, args.threads,
            )
            if best_str:
                print(f"\nResult: {best_dps:,.0f} DPS ({desc})")
    elif args.spec:
        best_str, best_dps, desc = local_search(
            args.spec, args.fight_style, args.max_iter, args.threads,
        )
        if best_str:
            print(f"\n{'='*60}")
            print(f"Final: {best_dps:,.0f} DPS")
            print(f"Mutation: {desc}")
            print(f"Talent string: {best_str}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
