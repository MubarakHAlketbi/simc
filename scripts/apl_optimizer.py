#!/usr/bin/env python3
"""M3 — APL Optimization Engine.

Iteratively improves APLs using mutation operators and multi-stage evaluation.

Usage:
    python3 scripts/apl_optimizer.py warrior_fury
    python3 scripts/apl_optimizer.py warrior_fury --max-iter 5
    python3 scripts/apl_optimizer.py --all --max-iter 3
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.lib.sim_runner import (
    run_sim, run_composite, CompositeResult, should_accept,
    extract_apl, find_profile
)
from scripts.lib.apl_parser import parse_apl, APL
from scripts.lib.apl_mutations import generate_all_mutations

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"
APL_DIR = Path(__file__).resolve().parent.parent / "ActionPriorityLists" / "default"


def get_action_ranking(result: CompositeResult) -> dict[str, float]:
    """Merge action breakdowns from both fight styles."""
    ranking = {}
    for name, dmg in result.pw.action_breakdown.items():
        ranking[name] = ranking.get(name, 0) + dmg
    for name, dmg in result.hac.action_breakdown.items():
        ranking[name] = ranking.get(name, 0) + dmg
    return ranking


def evaluate_staged(
    candidates: list[tuple[APL, str]],
    profile_path: str,
    baseline: CompositeResult,
    threads: int = 4,
) -> list[tuple[APL, str, CompositeResult]]:
    """Multi-stage evaluation: 100 iter -> 1000 iter -> 10000 iter."""
    
    if not candidates:
        return []
    
    # Stage 1: Coarse filter at 100 iterations
    print(f"    Stage 1: {len(candidates)} candidates @ 100 iter...", end="", flush=True)
    stage1_results = []
    for apl, desc in candidates:
        try:
            comp = run_composite(profile_path, iterations=100, threads=threads,
                               overrides=apl.to_override_lines())
            if comp.composite > baseline.composite * 0.98:  # keep anything within 2%
                stage1_results.append((apl, desc, comp))
        except Exception as e:
            pass  # skip broken APLs silently
    
    # Keep top 10 by composite
    stage1_results.sort(key=lambda x: -x[2].composite)
    survivors = stage1_results[:10]
    print(f" {len(survivors)} survive")
    
    if not survivors:
        return []
    
    # Stage 2: Medium filter at 1000 iterations
    print(f"    Stage 2: {len(survivors)} candidates @ 1000 iter...", end="", flush=True)
    stage2_results = []
    for apl, desc, _ in survivors:
        try:
            comp = run_composite(profile_path, iterations=1000, threads=threads,
                               overrides=apl.to_override_lines())
            improvement = (comp.composite - baseline.composite) / baseline.composite
            if improvement > 0.003:  # >0.3% improvement
                stage2_results.append((apl, desc, comp))
        except Exception:
            pass
    
    stage2_results.sort(key=lambda x: -x[2].composite)
    survivors = stage2_results[:3]
    print(f" {len(survivors)} survive")
    
    if not survivors:
        return []
    
    # Stage 3: Confirm at 10000 iterations
    print(f"    Stage 3: {len(survivors)} candidates @ 10000 iter...", end="", flush=True)
    stage3_results = []
    for apl, desc, _ in survivors:
        try:
            comp = run_composite(profile_path, iterations=10000, threads=threads,
                               overrides=apl.to_override_lines())
            if should_accept(comp, baseline, regression_cap=0.01):
                stage3_results.append((apl, desc, comp))
        except Exception:
            pass
    
    stage3_results.sort(key=lambda x: -x[2].composite)
    print(f" {len(stage3_results)} confirmed")
    
    return stage3_results


def optimize_spec(
    spec_name: str,
    max_iterations: int = 10,
    threads: int = 4,
) -> dict:
    """Run the full APL optimization loop for one spec."""
    
    profile_path = find_profile(spec_name)
    
    print(f"\n{'='*60}")
    print(f"  APL OPTIMIZER: {spec_name}")
    print(f"{'='*60}")
    
    # Step 0: Extract current APL and run baseline
    print(f"  Extracting APL...", end="", flush=True)
    apl_text = extract_apl(profile_path)
    apl = parse_apl(apl_text)
    print(f" {len(apl.all_actions)} actions across {len(apl.list_names)} lists")
    
    print(f"  Running baseline @ 10000 iter...", end="", flush=True)
    baseline = run_composite(profile_path, iterations=10000, threads=threads)
    print(f" {baseline}")
    
    history = [baseline.composite]
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
        winners = evaluate_staged(candidates, profile_path, best_result, threads)
        
        if not winners:
            print(f"    No improvements found. Converged.")
            break
        
        # Accept best
        new_apl, desc, new_result = winners[0]
        improvement = (new_result.composite - best_result.composite) / best_result.composite * 100
        
        best_apl = new_apl
        best_result = new_result
        history.append(best_result.composite)
        
        print(f"    ACCEPTED: {desc}")
        print(f"    {best_result.composite:.0f} ({improvement:+.2f}%)")
        
        # Convergence check
        if improvement < 0.1:
            print(f"    Improvement < 0.1%. Converged.")
            break
    
    # Final summary
    total_improvement = (history[-1] - history[0]) / history[0] * 100
    print(f"\n  RESULT: {history[0]:.0f} -> {history[-1]:.0f} ({total_improvement:+.2f}%)")
    print(f"  Iterations: {len(history) - 1}")
    
    # Save results
    spec_dir = RESULTS_DIR / spec_name
    spec_dir.mkdir(parents=True, exist_ok=True)
    
    result_data = {
        "spec": spec_name,
        "profile": profile_path,
        "baseline_composite": history[0],
        "final_composite": history[-1],
        "improvement_pct": total_improvement,
        "iterations": len(history) - 1,
        "history": history,
    }
    
    with open(spec_dir / "apl_optimization.json", "w") as f:
        json.dump(result_data, f, indent=2)
    
    # Save optimized APL if it changed
    if total_improvement > 0.1:
        with open(spec_dir / "optimized_apl.simc", "w") as f:
            f.write(best_apl.to_simc())
    
    return result_data


def main():
    parser = argparse.ArgumentParser(description="APL Optimizer")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g. warrior_fury)")
    parser.add_argument("--all", action="store_true", help="Optimize all specs")
    parser.add_argument("--max-iter", type=int, default=5, help="Max iterations per spec")
    parser.add_argument("--threads", type=int, default=8, help="SimC threads")
    args = parser.parse_args()
    
    from scripts.talent_build_compare import SPEC_MAP
    
    if args.all:
        specs = sorted(SPEC_MAP.values())
    elif args.spec:
        specs = [args.spec]
    else:
        parser.print_help()
        return
    
    start = time.time()
    all_results = []
    
    for spec in specs:
        try:
            result = optimize_spec(spec, max_iterations=args.max_iter, threads=args.threads)
            all_results.append(result)
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
            print(f"    {r['spec']:35s} {r['improvement_pct']:+.2f}%")
    else:
        print(f"\n  No APL improvements found (all specs already optimal or converged).")


if __name__ == "__main__":
    main()
