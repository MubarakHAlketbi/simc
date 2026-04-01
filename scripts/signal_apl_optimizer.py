#!/usr/bin/env python3
"""signal_apl_optimizer.py — Layer 2 + Layer 3 APL optimizer.

Layer 2: Signal-guided mutations from sim data (APS inversion, buff waste,
         resource overcap, interval gap). ~20-40 targeted candidates.
Layer 3: LLM semantic advisor for signals that require mechanic knowledge
         (missing buff consumers, wrong condition types, synergy gaps).

Both layers feed into the same multi-stage evaluation funnel as Layer 1
(300 → 3k → 10k iterations). DPS delta is the final arbiter.

Usage:
    python3 scripts/signal_apl_optimizer.py warrior_fury
    python3 scripts/signal_apl_optimizer.py warrior_fury --fight-style Patchwerk
    python3 scripts/signal_apl_optimizer.py warrior_fury --llm
    python3 scripts/signal_apl_optimizer.py --all
    python3 scripts/signal_apl_optimizer.py --all --llm
"""

import argparse
import json
import sys
import time
import tempfile
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.lib.sim_runner import (
    run_sim, SimResult, should_accept_single,
    extract_apl, find_profile,
)
from scripts.lib.apl_parser import parse_apl, APL
from scripts.lib.apl_mutations import generate_all_mutations
from scripts.lib.apl_signal_extractor import (
    extract_signals, signals_needing_llm, format_signals_report,
)
from scripts.lib.apl_signal_mutations import generate_signal_mutations
from scripts.lib.llm_apl_advisor import get_llm_mutations

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"
FIGHT_STYLES = ["Patchwerk", "HecticAddCleave"]


# ---------------------------------------------------------------------------
# Multi-stage evaluator (shared with apl_optimizer.py)
# ---------------------------------------------------------------------------

def evaluate_candidates(
    candidates: list[tuple[APL, str]],
    profile_path: str,
    baseline: SimResult,
    fight_style: str,
    threads: int = 16,
) -> list[tuple[APL, str, SimResult]]:
    """3-stage funnel: 100 → 1000 → 10000 iter."""

    if not candidates:
        return []

    # Stage 1: 100 iter, keep within 2% of baseline and top 15%
    print(f"    Stage 1: {len(candidates)} candidates @ 100 iter...", end="", flush=True)
    s1 = []
    for apl, desc in candidates:
        try:
            r = run_sim(profile_path, fight_style, iterations=100, threads=threads,
                        overrides=apl.to_override_lines())
            if r.dps_mean >= baseline.dps_mean * 0.98:
                s1.append((apl, desc, r))
        except Exception:
            pass
    s1.sort(key=lambda x: -x[2].dps_mean)
    cutoff = max(1, len(s1) // 5)  # top 20%
    s1 = s1[:max(cutoff, 10)]
    print(f" {len(s1)} survive")
    if not s1:
        return []

    # Stage 2: 1000 iter, keep >0.3% improvement
    print(f"    Stage 2: {len(s1)} candidates @ 1000 iter...", end="", flush=True)
    s2 = []
    for apl, desc, _ in s1:
        try:
            r = run_sim(profile_path, fight_style, iterations=1000, threads=threads,
                        overrides=apl.to_override_lines())
            if (r.dps_mean - baseline.dps_mean) / baseline.dps_mean > 0.003:
                s2.append((apl, desc, r))
        except Exception:
            pass
    s2.sort(key=lambda x: -x[2].dps_mean)
    s2 = s2[:3]
    print(f" {len(s2)} survive")
    if not s2:
        return []

    # Stage 3: 10000 iter confirmation
    print(f"    Stage 3: {len(s2)} candidates @ 10000 iter...", end="", flush=True)
    s3 = []
    for apl, desc, _ in s2:
        try:
            r = run_sim(profile_path, fight_style, iterations=10000, threads=threads,
                        overrides=apl.to_override_lines())
            if should_accept_single(r, baseline):
                s3.append((apl, desc, r))
        except Exception:
            pass
    s3.sort(key=lambda x: -x[2].dps_mean)
    print(f" {len(s3)} confirmed")
    return s3


# ---------------------------------------------------------------------------
# Profile APL apply
# ---------------------------------------------------------------------------

def apply_apl_to_profile(profile_path: str, apl: APL) -> None:
    """Replace APL actions in profile with optimized APL."""
    with open(profile_path) as f:
        lines = [l for l in f.readlines() if not l.strip().startswith("actions")]
    with open(profile_path, "w") as f:
        f.writelines(lines)
        if lines and not lines[-1].endswith("\n"):
            f.write("\n")
        f.write(apl.to_simc() + "\n")


# ---------------------------------------------------------------------------
# Single spec, single fight style
# ---------------------------------------------------------------------------

def optimize_one(
    spec: str,
    fight_style: str,
    max_iter: int = 3,
    threads: int = 16,
    use_llm: bool = False,
    use_blind: bool = True,
) -> dict:
    """Run Layer 2 (+ optionally Layer 3 LLM) for one spec/fight style."""

    result = {
        "spec": spec,
        "fight_style": fight_style,
        "baseline_dps": 0.0,
        "final_dps": 0.0,
        "improvement_pct": 0.0,
        "iterations": 0,
        "changes": [],
        "signals_found": 0,
        "llm_called": False,
    }

    try:
        profile_path = find_profile(spec)
    except FileNotFoundError as e:
        print(f"  ERROR: {e}")
        result["error"] = str(e)
        return result

    # Resolve HAC profile path
    if fight_style == "HecticAddCleave":
        hac = profile_path.replace(".simc", "_HAC.simc")
        if Path(hac).exists():
            profile_path = hac

    print(f"\n  Profile: {Path(profile_path).name}")
    print(f"  Running baseline ({fight_style}, 10k iter)...")

    # Save JSON for signal extraction
    fd, json_path = tempfile.mkstemp(suffix=".json", prefix="simc_signal_")
    os.close(fd)
    try:
        baseline = run_sim(profile_path, fight_style, iterations=10000,
                           threads=threads, json_out=json_path)
        result["baseline_dps"] = baseline.dps_mean
        print(f"  Baseline: {baseline.dps_mean:,.0f} DPS")

        best_dps = baseline.dps_mean
        best_apl_text = extract_apl(profile_path)
        current_apl = parse_apl(best_apl_text)
        tested_descs: list[str] = []

        for iteration in range(max_iter):
            print(f"\n  === Iteration {iteration + 1}/{max_iter} ===")

            # --- Extract signals ---
            signals = extract_signals(baseline, current_apl)
            result["signals_found"] = len(signals)
            print(f"  Signals detected: {len(signals)}")
            if signals:
                print(format_signals_report(signals[:5]))

            # --- Generate candidates ---
            candidates: list[tuple[APL, str]] = []

            # Layer 2: signal mutations
            sig_muts = generate_signal_mutations(signals, current_apl, max_total=40)
            print(f"  Signal mutations: {len(sig_muts)}")
            candidates += sig_muts

            # Layer 1 blind mutations (optional)
            if use_blind:
                blind_muts = generate_all_mutations(current_apl, baseline.action_breakdown)
                print(f"  Blind mutations: {len(blind_muts)}")
                candidates += blind_muts

            # Layer 3: LLM mutations
            llm_needed = signals_needing_llm(signals)
            if use_llm and (llm_needed or (iteration == 0 and len(sig_muts) == 0)):
                print(f"  [LLM] Calling advisor ({len(llm_needed)} unresolved signals)...")
                result["llm_called"] = True
                llm_muts = get_llm_mutations(
                    spec_name=spec,
                    fight_style=fight_style,
                    sim=baseline,
                    apl_text=best_apl_text,
                    signals=signals,
                    already_tested=tested_descs,
                )
                print(f"  LLM mutations: {len(llm_muts)}")
                candidates += llm_muts

            if not candidates:
                print("  No candidates generated. Converged.")
                break

            # Deduplicate by description
            seen = set()
            unique = []
            for c in candidates:
                if c[1] not in seen and c[1] not in tested_descs:
                    seen.add(c[1])
                    unique.append(c)
            print(f"  Unique candidates: {len(unique)}")

            # --- Evaluate ---
            confirmed = evaluate_candidates(unique, profile_path, baseline,
                                            fight_style, threads)
            tested_descs += [c[1] for c in unique]

            if not confirmed:
                print("  No improvement found. Converged.")
                break

            best_apl, best_desc, best_result = confirmed[0]
            gain = (best_result.dps_mean - baseline.dps_mean) / baseline.dps_mean * 100
            print(f"  IMPROVEMENT: {best_desc}")
            print(f"    {baseline.dps_mean:,.0f} → {best_result.dps_mean:,.0f} (+{gain:.2f}%)")

            # Apply
            apply_apl_to_profile(profile_path, best_apl)
            baseline = best_result
            current_apl = best_apl
            best_apl_text = best_apl.to_simc()
            result["changes"].append({"desc": best_desc, "gain_pct": gain})
            result["iterations"] += 1

        result["final_dps"] = baseline.dps_mean
        result["improvement_pct"] = (
            (baseline.dps_mean - result["baseline_dps"]) / result["baseline_dps"] * 100
        )

        # Save result JSON
        spec_dir = RESULTS_DIR / spec
        spec_dir.mkdir(parents=True, exist_ok=True)
        style_tag = "pw" if fight_style == "Patchwerk" else "hac"
        with open(spec_dir / f"signal_apl_{style_tag}.json", "w") as f:
            json.dump(result, f, indent=2)

    finally:
        if os.path.exists(json_path):
            os.unlink(json_path)

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Layer 2+3 APL Optimizer (signal-guided + LLM)")
    parser.add_argument("spec", nargs="?", help="Spec to optimize (e.g. warrior_fury)")
    parser.add_argument("--all", action="store_true", help="Run on all specs")
    parser.add_argument("--fight-style", default=None,
                        choices=["Patchwerk", "HecticAddCleave"],
                        help="Single fight style (default: both)")
    parser.add_argument("--max-iter", type=int, default=3, help="Max iterations per style")
    parser.add_argument("--threads", type=int, default=16, help="SimC threads")
    parser.add_argument("--llm", action="store_true", help="Enable Layer 3 LLM advisor")
    parser.add_argument("--no-blind", action="store_true",
                        help="Disable Layer 1 blind mutations (signal-only)")
    args = parser.parse_args()

    fight_styles = [args.fight_style] if args.fight_style else FIGHT_STYLES

    if args.all:
        from scripts.lib.talent_tree import SPEC_MAP
        specs = sorted(SPEC_MAP.keys())
    elif args.spec:
        specs = [args.spec]
    else:
        parser.print_help()
        return

    all_results = []
    start = time.time()

    for spec in specs:
        print(f"\n{'='*60}")
        print(f"  {spec.upper()}")
        print(f"{'='*60}")
        for fs in fight_styles:
            r = optimize_one(
                spec=spec,
                fight_style=fs,
                max_iter=args.max_iter,
                threads=args.threads,
                use_llm=args.llm,
                use_blind=not args.no_blind,
            )
            all_results.append(r)
            imp = r.get("improvement_pct", 0)
            llm_flag = " [LLM]" if r.get("llm_called") else ""
            print(f"\n  {spec} {fs}: {r['baseline_dps']:,.0f} → {r['final_dps']:,.0f} "
                  f"({imp:+.2f}%){llm_flag}")

    elapsed = time.time() - start
    print(f"\n\n{'='*70}")
    print(f"  SIGNAL APL OPTIMIZER COMPLETE — {len(specs)} specs × {len(fight_styles)} styles")
    print(f"  Wall time: {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"{'='*70}")

    improved = [r for r in all_results if r.get("improvement_pct", 0) > 0.1]
    print(f"\n  Specs with improvements (>{0.1}%):")
    for r in sorted(improved, key=lambda x: -x.get("improvement_pct", 0)):
        print(f"    {r['spec']:30s}  {r['fight_style']:20s}  "
              f"+{r['improvement_pct']:.2f}%  "
              f"({len(r.get('changes', []))} changes)")

    if not improved:
        print("    None — all specs already at signal optimum.")


if __name__ == "__main__":
    main()
