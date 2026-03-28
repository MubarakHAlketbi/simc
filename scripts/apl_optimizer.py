#!/usr/bin/env python3
"""M3 — APL Optimization Engine.

Optimizes APLs independently for each fight style (Patchwerk + HecticAddCleave).
Each spec produces TWO optimal APLs — one per fight style.

Usage:
    python3 scripts/apl_optimizer.py warrior_fury
    python3 scripts/apl_optimizer.py warrior_fury --max-iter 5
    python3 scripts/apl_optimizer.py --all --max-iter 3
    python3 scripts/apl_optimizer.py warrior_fury --fight-style Patchwerk  # single style
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.lib.sim_runner import (
    run_sim, SimResult, should_accept_single,
    extract_apl, find_profile
)
from scripts.lib.apl_parser import parse_apl, APL
from scripts.lib.apl_mutations import generate_all_mutations

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"
APL_DIR = Path(__file__).resolve().parent.parent / "ActionPriorityLists" / "default"

FIGHT_STYLES = ["Patchwerk", "HecticAddCleave"]


def get_action_ranking(result: SimResult) -> dict[str, float]:
    """Get action damage ranking from a single fight style result."""
    return dict(result.action_breakdown)


def evaluate_staged_single(
    candidates: list[tuple[APL, str]],
    profile_path: str,
    baseline: SimResult,
    fight_style: str,
    threads: int = 4,
) -> list[tuple[APL, str, SimResult]]:
    """Multi-stage evaluation for a single fight style: 100 -> 1000 -> 10000 iter."""

    if not candidates:
        return []

    # Stage 1: Coarse filter at 100 iterations
    print(f"    Stage 1: {len(candidates)} candidates @ 100 iter...", end="", flush=True)
    stage1_results = []
    for apl, desc in candidates:
        try:
            result = run_sim(profile_path, fight_style, iterations=100, threads=threads,
                            overrides=apl.to_override_lines())
            if result.dps_mean > baseline.dps_mean * 0.98:  # keep within 2%
                stage1_results.append((apl, desc, result))
        except Exception:
            pass  # skip broken APLs silently

    # Keep top 10
    stage1_results.sort(key=lambda x: -x[2].dps_mean)
    survivors = stage1_results[:10]
    print(f" {len(survivors)} survive")

    if not survivors:
        return []

    # Stage 2: Medium filter at 1000 iterations
    print(f"    Stage 2: {len(survivors)} candidates @ 1000 iter...", end="", flush=True)
    stage2_results = []
    for apl, desc, _ in survivors:
        try:
            result = run_sim(profile_path, fight_style, iterations=1000, threads=threads,
                            overrides=apl.to_override_lines())
            improvement = (result.dps_mean - baseline.dps_mean) / baseline.dps_mean
            if improvement > 0.003:  # >0.3% improvement
                stage2_results.append((apl, desc, result))
        except Exception:
            pass

    stage2_results.sort(key=lambda x: -x[2].dps_mean)
    survivors = stage2_results[:3]
    print(f" {len(survivors)} survive")

    if not survivors:
        return []

    # Stage 3: Confirm at 10000 iterations
    print(f"    Stage 3: {len(survivors)} candidates @ 10000 iter...", end="", flush=True)
    stage3_results = []
    for apl, desc, _ in survivors:
        try:
            result = run_sim(profile_path, fight_style, iterations=10000, threads=threads,
                            overrides=apl.to_override_lines())
            if should_accept_single(result, baseline):
                stage3_results.append((apl, desc, result))
        except Exception:
            pass

    stage3_results.sort(key=lambda x: -x[2].dps_mean)
    print(f" {len(stage3_results)} confirmed")

    return stage3_results


def optimize_spec_single_style(
    spec_name: str,
    fight_style: str,
    max_iterations: int = 10,
    threads: int = 4,
) -> dict:
    """Run APL optimization for one spec on one fight style."""

    profile_path = find_profile(spec_name)
    style_tag = "pw" if fight_style == "Patchwerk" else "hac"

    print(f"\n  --- {spec_name} / {fight_style} ---")

    # Extract current APL and run baseline
    print(f"  Extracting APL...", end="", flush=True)
    apl_text = extract_apl(profile_path)
    apl = parse_apl(apl_text)
    print(f" {len(apl.all_actions)} actions across {len(apl.list_names)} lists")

    print(f"  Running baseline @ 10000 iter ({fight_style})...", end="", flush=True)
    baseline = run_sim(profile_path, fight_style, iterations=10000, threads=threads)
    print(f" {baseline.dps_mean:.0f} DPS")

    history = [baseline.dps_mean]
    best_apl = apl
    best_result = baseline

    for iteration in range(max_iterations):
        print(f"\n  --- Iteration {iteration + 1}/{max_iterations} ---")

        # Generate mutations
        ranking = get_action_ranking(best_result)
        candidates = generate_all_mutations(best_apl, ranking)
        print(f"    Generated {len(candidates)} candidates")

        if not candidates:
            print(f"    No candidates generated. Converged.")
            break

        # Evaluate through stages
        winners = evaluate_staged_single(
            candidates, profile_path, best_result, fight_style, threads
        )

        if not winners:
            print(f"    No improvements found. Converged.")
            break

        # Accept best
        new_apl, desc, new_result = winners[0]
        improvement = (new_result.dps_mean - best_result.dps_mean) / best_result.dps_mean * 100

        best_apl = new_apl
        best_result = new_result
        history.append(best_result.dps_mean)

        print(f"    ACCEPTED: {desc}")
        print(f"    {best_result.dps_mean:.0f} DPS ({improvement:+.2f}%)")

        # Convergence check
        if improvement < 0.1:
            print(f"    Improvement < 0.1%. Converged.")
            break

    # Final summary
    total_improvement = (history[-1] - history[0]) / history[0] * 100
    print(f"\n  RESULT [{fight_style}]: {history[0]:.0f} -> {history[-1]:.0f} ({total_improvement:+.2f}%)")

    # Save results
    spec_dir = RESULTS_DIR / spec_name
    spec_dir.mkdir(parents=True, exist_ok=True)

    result_data = {
        "spec": spec_name,
        "fight_style": fight_style,
        "profile": profile_path,
        "baseline_dps": history[0],
        "final_dps": history[-1],
        "improvement_pct": total_improvement,
        "iterations": len(history) - 1,
        "history": history,
    }

    with open(spec_dir / f"apl_optimization_{style_tag}.json", "w") as f:
        json.dump(result_data, f, indent=2)

    # Save optimized APL if it changed
    if total_improvement > 0.1:
        with open(spec_dir / f"optimized_apl_{style_tag}.simc", "w") as f:
            f.write(best_apl.to_simc())

    return result_data


def optimize_spec(
    spec_name: str,
    max_iterations: int = 10,
    threads: int = 4,
    fight_styles: list[str] | None = None,
) -> list[dict]:
    """Run APL optimization for one spec across all fight styles independently.

    Each fight style is optimized separately, producing independent APLs.
    Returns a list of result dicts, one per fight style.
    """
    styles = fight_styles or FIGHT_STYLES

    print(f"\n{'='*60}")
    print(f"  APL OPTIMIZER: {spec_name}")
    print(f"  Optimizing independently for: {', '.join(styles)}")
    print(f"{'='*60}")

    results = []
    for style in styles:
        result = optimize_spec_single_style(
            spec_name, style, max_iterations, threads
        )
        results.append(result)

    # Print cross-style summary
    print(f"\n  === {spec_name} SUMMARY ===")
    for r in results:
        print(f"    {r['fight_style']:20s}: {r['baseline_dps']:.0f} -> {r['final_dps']:.0f} ({r['improvement_pct']:+.2f}%)")

    return results


def main():
    parser = argparse.ArgumentParser(description="APL Optimizer (per-fight-style)")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g. warrior_fury)")
    parser.add_argument("--all", action="store_true", help="Optimize all specs")
    parser.add_argument("--max-iter", type=int, default=5, help="Max iterations per spec per fight style")
    parser.add_argument("--threads", type=int, default=8, help="SimC threads")
    parser.add_argument("--fight-style", type=str, default=None,
                        help="Single fight style (Patchwerk or HecticAddCleave). Default: both")
    args = parser.parse_args()

    from scripts.talent_build_compare import SPEC_MAP

    if args.all:
        specs = sorted(SPEC_MAP.values())
    elif args.spec:
        specs = [args.spec]
    else:
        parser.print_help()
        return

    fight_styles = [args.fight_style] if args.fight_style else None

    start = time.time()
    all_results = []

    for spec in specs:
        try:
            results = optimize_spec(spec, max_iterations=args.max_iter,
                                    threads=args.threads, fight_styles=fight_styles)
            all_results.extend(results)
        except Exception as e:
            print(f"\n  ERROR on {spec}: {e}")
            all_results.append({"spec": spec, "error": str(e)})

    elapsed = time.time() - start

    print(f"\n{'='*60}")
    print(f"  COMPLETE — {len(specs)} specs in {elapsed:.0f}s")
    print(f"{'='*60}")

    improved = [r for r in all_results if r.get("improvement_pct", 0) > 0.1]
    if improved:
        print(f"\n  Specs with APL improvements:")
        for r in sorted(improved, key=lambda x: -x["improvement_pct"]):
            print(f"    {r['spec']:30s} {r['fight_style']:20s} {r['improvement_pct']:+.2f}%")
    else:
        print(f"\n  No APL improvements found (all specs already optimal or converged).")


if __name__ == "__main__":
    main()
