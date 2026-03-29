#!/usr/bin/env python3
"""Talent Local Search — Wowhead seeds + neighborhood hill-climb.

Optimizes talent builds per fight style independently:
1. Screen Wowhead builds (seeds) at medium precision
2. From top seeds, generate single-node neighbors
3. Hill-climb: screen neighbors, adopt best, repeat
4. Confirm winner at high precision

Usage:
    python3 scripts/talent_local_search.py warrior_fury
    python3 scripts/talent_local_search.py warrior_fury --fight-style Patchwerk
    python3 scripts/talent_local_search.py --all
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
from scripts.lib.tree_codec_bridge import tree_to_codec_nodes
from scripts.lib.talent_neighbor import generate_neighbors
from scripts.lib.sim_runner import run_sim, find_profile
from scripts.talent_build_compare import load_wowhead_builds

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"
FIGHT_STYLES = ["Patchwerk", "HecticAddCleave"]


def _get_current_talents(profile_path: str) -> str:
    with open(profile_path) as f:
        for line in f:
            if line.startswith("talents="):
                return line.strip().split("=", 1)[1]
    raise ValueError(f"No talents= in {profile_path}")


def screen_seeds(
    profile_path: str,
    fight_style: str,
    seeds: list[tuple[str, str]],  # [(label, talent_string), ...]
    iterations: int = 1000,
    threads: int = 8,
) -> list[tuple[str, str, float]]:
    """Sim all seeds, return sorted by DPS descending."""
    results = []
    for label, talent_str in seeds:
        try:
            r = run_sim(profile_path, fight_style, iterations=iterations,
                       threads=threads, overrides=[f"talents={talent_str}"])
            results.append((label, talent_str, r.dps_mean))
        except Exception as e:
            pass  # skip broken builds
    results.sort(key=lambda x: -x[2])
    return results


def search_one_pass(
    profile_path: str,
    fight_style: str,
    base_talent_str: str,
    base_dps: float,
    tree, codec_nodes, spec_id, purchased_flags,
    threads: int = 8,
) -> tuple[str, float, str]:
    """One hill-climb pass: generate neighbors, screen, confirm.

    Returns (best_talent_str, best_dps, best_desc) or (base_talent_str, base_dps, "")
    if no improvement found.
    """
    # Decode current build
    _, selections, pf = decode_talent_string(base_talent_str, codec_nodes)
    if purchased_flags is None:
        purchased_flags = pf

    # Generate neighbors
    neighbors = generate_neighbors(tree, selections, codec_nodes, spec_id, purchased_flags)
    if not neighbors:
        return base_talent_str, base_dps, ""

    # Quick screen at 500 iter
    screened = []
    for talent_str, desc in neighbors:
        try:
            r = run_sim(profile_path, fight_style, iterations=500,
                       threads=threads, overrides=[f"talents={talent_str}"])
            screened.append((talent_str, desc, r.dps_mean))
        except Exception:
            pass

    if not screened:
        return base_talent_str, base_dps, ""

    # Keep top 5
    screened.sort(key=lambda x: -x[2])
    top5 = screened[:5]

    # Confirm at 2000 iter
    confirmed = []
    for talent_str, desc, _ in top5:
        try:
            r = run_sim(profile_path, fight_style, iterations=2000,
                       threads=threads, overrides=[f"talents={talent_str}"])
            if r.dps_mean > base_dps:
                confirmed.append((talent_str, desc, r.dps_mean))
        except Exception:
            pass

    if not confirmed:
        return base_talent_str, base_dps, ""

    confirmed.sort(key=lambda x: -x[2])
    best_ts, best_desc, best_dps = confirmed[0]
    return best_ts, best_dps, best_desc


def optimize_from_seeds(
    spec_name: str,
    fight_style: str,
    seeds: list[tuple[str, str]],
    threads: int = 8,
    max_passes: int = 5,
    top_seeds: int = 3,
) -> dict:
    """Full local search from Wowhead seeds for one spec + one fight style."""

    profile_path = find_profile(spec_name)
    style_tag = "pw" if fight_style == "Patchwerk" else "hac"

    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)

    print(f"\n  --- {spec_name} / {fight_style} ---")

    # Screen seeds
    print(f"  Screening {len(seeds)} seeds @ 1000 iter...", end="", flush=True)
    seed_results = screen_seeds(profile_path, fight_style, seeds, iterations=1000, threads=threads)
    if not seed_results:
        print(f" all failed")
        return {"spec": spec_name, "fight_style": fight_style, "error": "all seeds failed"}

    print(f" best: {seed_results[0][0]} ({seed_results[0][2]:.0f})")
    for label, ts, dps in seed_results[:5]:
        print(f"    {label:30s} {dps:>10,.0f}")

    # Also sim current profile as baseline
    current_ts = _get_current_talents(profile_path)
    baseline = run_sim(profile_path, fight_style, iterations=1000, threads=threads)
    print(f"  Current profile baseline: {baseline.dps_mean:.0f}")

    # Pick top seeds (include current if not already best)
    top = seed_results[:top_seeds]
    current_in_top = any(ts == current_ts for _, ts, _ in top)
    if not current_in_top:
        top.append(("current", current_ts, baseline.dps_mean))

    # Get purchased_flags from current build
    _, _, purchased_flags = decode_talent_string(current_ts, codec_nodes)

    # Hill-climb from each top seed
    overall_best_ts = seed_results[0][1]
    overall_best_dps = seed_results[0][2]
    overall_best_label = seed_results[0][0]
    total_neighbors = 0

    for seed_label, seed_ts, seed_dps in top:
        current_ts_local = seed_ts
        current_dps = seed_dps

        for pass_num in range(1, max_passes + 1):
            # Decode for neighbor count
            _, sel, _ = decode_talent_string(current_ts_local, codec_nodes)
            nbrs = generate_neighbors(tree, sel, codec_nodes, spec_id, purchased_flags)
            total_neighbors += len(nbrs)

            print(f"  [{seed_label}] Pass {pass_num}: {len(nbrs)} neighbors...", end="", flush=True)

            new_ts, new_dps, new_desc = search_one_pass(
                profile_path, fight_style, current_ts_local, current_dps,
                tree, codec_nodes, spec_id, purchased_flags, threads
            )

            if new_dps > current_dps * 1.001:  # >0.1% improvement
                improvement = (new_dps - current_dps) / current_dps * 100
                print(f" +{improvement:.2f}% ({new_desc})")
                current_ts_local = new_ts
                current_dps = new_dps
            else:
                print(f" converged")
                break

        if current_dps > overall_best_dps:
            overall_best_ts = current_ts_local
            overall_best_dps = current_dps
            overall_best_label = seed_label

    # Final confirmation at 10k iter
    print(f"  Final confirm @ 10000 iter...", end="", flush=True)
    final = run_sim(profile_path, fight_style, iterations=10000, threads=threads,
                   overrides=[f"talents={overall_best_ts}"])
    final_baseline = run_sim(profile_path, fight_style, iterations=10000, threads=threads)
    total_improvement = (final.dps_mean - final_baseline.dps_mean) / final_baseline.dps_mean * 100
    print(f" {final.dps_mean:.0f} vs baseline {final_baseline.dps_mean:.0f} ({total_improvement:+.2f}%)")

    # Save results
    spec_dir = RESULTS_DIR / spec_name
    spec_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "spec": spec_name,
        "fight_style": fight_style,
        "baseline_dps": final_baseline.dps_mean,
        "best_dps": final.dps_mean,
        "improvement_pct": total_improvement,
        "best_talent_str": overall_best_ts,
        "best_seed": overall_best_label,
        "seeds_tested": len(seeds),
        "neighbors_tested": total_neighbors,
        "current_talent_str": _get_current_talents(profile_path),
    }

    with open(spec_dir / f"talent_local_search_{style_tag}.json", "w") as f:
        json.dump(result, f, indent=2)

    if total_improvement > 0.5:
        with open(spec_dir / f"best_build_{style_tag}.txt", "w") as f:
            f.write(overall_best_ts + "\n")

    return result


def optimize_spec(
    spec_name: str,
    fight_styles: list[str] | None = None,
    threads: int = 8,
    max_passes: int = 5,
) -> list[dict]:
    """Top-level: load Wowhead builds, run local search per fight style."""
    styles = fight_styles or FIGHT_STYLES

    print(f"\n{'='*60}")
    print(f"  TALENT LOCAL SEARCH: {spec_name}")
    print(f"{'='*60}")

    # Load seeds
    try:
        builds = load_wowhead_builds(spec_name)
        seeds = [(b["label"], b["talent_string"]) for b in builds]
        print(f"  Loaded {len(seeds)} Wowhead builds")
    except Exception as e:
        print(f"  No Wowhead builds available ({e}), using current profile only")
        profile_path = find_profile(spec_name)
        current_ts = _get_current_talents(profile_path)
        seeds = [("current", current_ts)]

    results = []
    for style in styles:
        result = optimize_from_seeds(spec_name, style, seeds, threads, max_passes)
        results.append(result)

    # Summary
    print(f"\n  === {spec_name} TALENT SUMMARY ===")
    for r in results:
        if "error" in r:
            print(f"    {r['fight_style']:20s}: ERROR — {r['error']}")
        else:
            print(f"    {r['fight_style']:20s}: {r['baseline_dps']:.0f} -> {r['best_dps']:.0f} ({r['improvement_pct']:+.2f}%) seed={r['best_seed']}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Talent Local Search Optimizer")
    parser.add_argument("spec", nargs="?", help="Spec to optimize")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--fight-style", type=str, default=None)
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--max-passes", type=int, default=5)
    args = parser.parse_args()

    if args.all:
        from scripts.talent_build_compare import SPEC_MAP as SM
        specs = sorted(SM.values())
    elif args.spec:
        specs = [args.spec]
    else:
        parser.print_help()
        return

    styles = [args.fight_style] if args.fight_style else None
    start = time.time()

    all_results = []
    for spec in specs:
        try:
            results = optimize_spec(spec, fight_styles=styles,
                                    threads=args.threads, max_passes=args.max_passes)
            all_results.extend(results)
        except Exception as e:
            print(f"\n  ERROR on {spec}: {e}")
            import traceback; traceback.print_exc()

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  DONE — {len(specs)} specs in {elapsed:.0f}s")
    print(f"{'='*60}")

    improved = [r for r in all_results if r.get("improvement_pct", 0) > 0.3]
    if improved:
        print(f"\n  Improved specs:")
        for r in sorted(improved, key=lambda x: -x["improvement_pct"]):
            print(f"    {r['spec']:30s} {r['fight_style']:20s} {r['improvement_pct']:+.2f}%")


if __name__ == "__main__":
    main()
