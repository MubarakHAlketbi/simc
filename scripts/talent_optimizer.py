#!/usr/bin/env python3
"""Batch 4 — Talent Permutation Optimizer (per fight style).

Wires: talent_tree → node_classifier → talent_permute → sim_runner
Each spec gets independent optimization for Patchwerk and HecticAddCleave.

Usage:
    python3 scripts/talent_optimizer.py warrior_fury
    python3 scripts/talent_optimizer.py warrior_fury --fight-style Patchwerk
    python3 scripts/talent_optimizer.py --all
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.lib.talent_tree import build_talent_tree, SPEC_MAP
from scripts.lib.talent_codec import decode_talent_string, encode_talent_string
from scripts.lib.tree_codec_bridge import (
    tree_to_codec_nodes, decode_profile_talents, encode_profile_talents
)
from scripts.lib.node_classifier import classify_all_nodes, get_pivot_nodes, DPSRelevance
from scripts.lib.talent_permute import generate_pivot_combinations, tuning_hill_climb
from scripts.lib.sim_runner import run_sim, extract_apl, find_profile, SimResult

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"
FIGHT_STYLES = ["Patchwerk", "HecticAddCleave"]


def get_current_talents(profile_path: str) -> str:
    """Extract talents= line from a .simc profile."""
    with open(profile_path) as f:
        for line in f:
            if line.startswith("talents="):
                return line.strip().split("=", 1)[1]
    raise ValueError(f"No talents= line in {profile_path}")


def optimize_spec_talents(
    spec_name: str,
    fight_styles: list[str] | None = None,
    max_pivots: int = 200,
    threads: int = 8,
) -> list[dict]:
    """Run talent optimization for one spec, independently per fight style."""
    styles = fight_styles or FIGHT_STYLES
    profile_path = find_profile(spec_name)

    print(f"\n{'='*60}")
    print(f"  TALENT OPTIMIZER: {spec_name}")
    print(f"{'='*60}")

    # Step 1: Build tree and classify
    print(f"  Building talent tree...", end="", flush=True)
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    print(f" {len(tree.nodes)} nodes")

    print(f"  Extracting APL for classification...", end="", flush=True)
    apl_text = extract_apl(profile_path)
    print(f" done")

    print(f"  Classifying nodes...", end="", flush=True)
    classification = classify_all_nodes(tree, apl_text, spec_name)
    dps_count = sum(1 for v in classification.values() if v == DPSRelevance.DPS)
    gate_count = sum(1 for v in classification.values() if v == DPSRelevance.GATING)
    util_count = sum(1 for v in classification.values() if v == DPSRelevance.UTILITY)
    print(f" {dps_count} DPS, {gate_count} GATING, {util_count} UTILITY")

    pivots = get_pivot_nodes(tree, classification)
    tuning = {nid for nid, rel in classification.items()
              if rel == DPSRelevance.DPS and nid not in pivots}
    print(f"  Pivots: {len(pivots)}, Tuning: {len(tuning)}")

    # Decode current build
    current_talent_str = get_current_talents(profile_path)
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    _, current_selections, purchased_flags = decode_talent_string(current_talent_str, codec_nodes)

    all_results = []

    for style in styles:
        style_tag = "pw" if style == "Patchwerk" else "hac"
        print(f"\n  --- {style} ---")

        # Baseline
        print(f"  Baseline @ 1000 iter...", end="", flush=True)
        baseline = run_sim(profile_path, style, iterations=1000, threads=threads)
        print(f" {baseline.dps_mean:.0f} DPS")

        # Step 2: Pivot sweep
        print(f"  Pivot sweep ({max_pivots} max combos) @ 200 iter...", end="", flush=True)
        combos = list(generate_pivot_combinations(tree, pivots, current_selections, max_pivots))
        print(f" {len(combos)} combos generated")

        if len(combos) <= 1:
            print(f"  No pivot variation possible, skipping.")
            all_results.append({
                "spec": spec_name, "fight_style": style,
                "baseline_dps": baseline.dps_mean, "best_dps": baseline.dps_mean,
                "improvement_pct": 0, "phase": "pivot", "best_talent_str": current_talent_str,
            })
            continue

        # Sim each combo
        pivot_results = []
        for i, build in enumerate(combos):
            try:
                talent_str = encode_talent_string(build, codec_nodes, spec_id, purchased_flags)
                result = run_sim(profile_path, style, iterations=200, threads=threads,
                                overrides=[f"talents={talent_str}"])
                pivot_results.append((build, talent_str, result.dps_mean))
                if (i + 1) % 50 == 0:
                    print(f"    [{i+1}/{len(combos)}]...", end="", flush=True)
            except Exception:
                pass

        if not pivot_results:
            print(f"  All pivot combos failed.")
            all_results.append({
                "spec": spec_name, "fight_style": style,
                "baseline_dps": baseline.dps_mean, "best_dps": baseline.dps_mean,
                "improvement_pct": 0, "phase": "pivot_failed",
            })
            continue

        pivot_results.sort(key=lambda x: -x[2])
        best_pivot_dps = pivot_results[0][2]
        pivot_improvement = (best_pivot_dps - baseline.dps_mean) / baseline.dps_mean * 100
        print(f"\n  Pivot sweep best: {best_pivot_dps:.0f} ({pivot_improvement:+.1f}% vs baseline)")

        # Keep top 10 for confirmation
        top10 = pivot_results[:10]
        print(f"  Confirming top {len(top10)} @ 1000 iter...", end="", flush=True)
        confirmed = []
        for build, talent_str, _ in top10:
            try:
                result = run_sim(profile_path, style, iterations=1000, threads=threads,
                                overrides=[f"talents={talent_str}"])
                confirmed.append((build, talent_str, result.dps_mean))
            except Exception:
                pass

        if not confirmed:
            print(f" all failed")
            all_results.append({
                "spec": spec_name, "fight_style": style,
                "baseline_dps": baseline.dps_mean, "best_dps": baseline.dps_mean,
                "improvement_pct": 0, "phase": "confirm_failed",
            })
            continue

        confirmed.sort(key=lambda x: -x[2])
        best_build, best_talent_str, best_dps = confirmed[0]
        print(f" best: {best_dps:.0f}")

        # Step 3: Tuning hill-climb on best pivot build
        print(f"  Tuning hill-climb ({len(tuning)} nodes)...", end="", flush=True)

        def sim_build(build_dict):
            try:
                ts = encode_talent_string(build_dict, codec_nodes, spec_id, purchased_flags)
                r = run_sim(profile_path, style, iterations=1000, threads=threads,
                           overrides=[f"talents={ts}"])
                return r.dps_mean
            except Exception:
                return 0

        tuned_build = tuning_hill_climb(tree, best_build, tuning, sim_func=sim_build)
        tuned_str = encode_talent_string(tuned_build, codec_nodes, spec_id, purchased_flags)
        tuned_dps = sim_build(tuned_build)
        tuning_gain = (tuned_dps - best_dps) / best_dps * 100 if best_dps > 0 else 0
        print(f" {tuned_dps:.0f} ({tuning_gain:+.2f}% from tuning)")

        # Step 4: Final confirmation @ 10k iter
        if tuned_dps > best_dps:
            best_build, best_talent_str, best_dps = tuned_build, tuned_str, tuned_dps

        print(f"  Final confirm @ 10000 iter...", end="", flush=True)
        final = run_sim(profile_path, style, iterations=10000, threads=threads,
                       overrides=[f"talents={best_talent_str}"])
        final_baseline = run_sim(profile_path, style, iterations=10000, threads=threads)
        print(f" {final.dps_mean:.0f} vs {final_baseline.dps_mean:.0f}")

        total_improvement = (final.dps_mean - final_baseline.dps_mean) / final_baseline.dps_mean * 100

        print(f"  RESULT [{style}]: {final_baseline.dps_mean:.0f} -> {final.dps_mean:.0f} ({total_improvement:+.2f}%)")

        # Save
        spec_dir = RESULTS_DIR / spec_name
        spec_dir.mkdir(parents=True, exist_ok=True)

        result_data = {
            "spec": spec_name,
            "fight_style": style,
            "baseline_dps": final_baseline.dps_mean,
            "best_dps": final.dps_mean,
            "improvement_pct": total_improvement,
            "best_talent_str": best_talent_str,
            "current_talent_str": current_talent_str,
            "pivot_combos_tested": len(combos),
            "pivot_nodes": len(pivots),
            "tuning_nodes": len(tuning),
            "classification": {"dps": dps_count, "gating": gate_count, "utility": util_count},
        }

        with open(spec_dir / f"talent_optimization_{style_tag}.json", "w") as f:
            json.dump(result_data, f, indent=2)

        if total_improvement > 0.5:
            with open(spec_dir / f"best_build_{style_tag}.txt", "w") as f:
                f.write(best_talent_str + "\n")

        all_results.append(result_data)

    # Summary
    print(f"\n  === {spec_name} TALENT SUMMARY ===")
    for r in all_results:
        imp = r.get("improvement_pct", 0)
        print(f"    {r['fight_style']:20s}: {r.get('baseline_dps',0):.0f} -> {r.get('best_dps',0):.0f} ({imp:+.2f}%)")

    return all_results


def main():
    parser = argparse.ArgumentParser(description="Talent Optimizer (per-fight-style)")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g. warrior_fury)")
    parser.add_argument("--all", action="store_true", help="Optimize all specs")
    parser.add_argument("--fight-style", type=str, default=None)
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--max-pivots", type=int, default=200)
    args = parser.parse_args()

    if args.all:
        from scripts.talent_build_compare import SPEC_MAP as S
        specs = sorted(S.values())
    elif args.spec:
        specs = [args.spec]
    else:
        parser.print_help()
        return

    styles = [args.fight_style] if args.fight_style else None
    start = time.time()

    for spec in specs:
        try:
            optimize_spec_talents(spec, fight_styles=styles,
                                 max_pivots=args.max_pivots, threads=args.threads)
        except Exception as e:
            print(f"\n  ERROR on {spec}: {e}")
            import traceback; traceback.print_exc()

    print(f"\nDone in {time.time() - start:.0f}s")


if __name__ == "__main__":
    main()
