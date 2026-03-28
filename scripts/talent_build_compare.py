#!/usr/bin/env python3
"""M5 — Wowhead Talent Build Comparison.

Sims all Wowhead-recommended talent builds for each spec, ranks by
composite DPS, and identifies if current profile talent is optimal.

Usage:
    python3 scripts/talent_build_compare.py                    # all specs
    python3 scripts/talent_build_compare.py warrior_fury       # one spec
    python3 scripts/talent_build_compare.py --iterations 500   # custom iter
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.lib.sim_runner import (
    run_sim, run_composite, CompositeResult, find_profile, SIMC_BIN
)

WOWHEAD_DIR = Path(__file__).resolve().parent.parent / "wowhead"
RESULTS_DIR = Path(__file__).resolve().parent.parent / "results" / "optimization"

# Map wowhead directory names to SimC spec names
SPEC_MAP = {
    "death-knight/blood": "death_knight_blood",
    "death-knight/frost": "death_knight_frost",
    "death-knight/unholy": "death_knight_unholy",
    "demon-hunter/devourer": "demon_hunter_devourer",
    "demon-hunter/havoc": "demon_hunter_havoc",
    "demon-hunter/vengeance": "demon_hunter_vengeance",
    "druid/balance": "druid_balance",
    "druid/feral": "druid_feral",
    "druid/guardian": "druid_guardian",
    "evoker/augmentation": "evoker_augmentation",
    "evoker/devastation": "evoker_devastation",
    "hunter/beast-mastery": "hunter_beast_mastery",
    "hunter/marksmanship": "hunter_marksmanship",
    "hunter/survival": "hunter_survival",
    "mage/arcane": "mage_arcane",
    "mage/fire": "mage_fire",
    "mage/frost": "mage_frost",
    "monk/brewmaster": "monk_brewmaster",
    "monk/windwalker": "monk_windwalker",
    "paladin/protection": "paladin_protection",
    "paladin/retribution": "paladin_retribution",
    "priest/shadow": "priest_shadow",
    "rogue/assassination": "rogue_assassination",
    "rogue/outlaw": "rogue_outlaw",
    "rogue/subtlety": "rogue_subtlety",
    "shaman/elemental": "shaman_elemental",
    "shaman/enhancement": "shaman_enhancement",
    "warlock/affliction": "warlock_affliction",
    "warlock/demonology": "warlock_demonology",
    "warlock/destruction": "warlock_destruction",
    "warrior/arms": "warrior_arms",
    "warrior/fury": "warrior_fury",
    "warrior/protection": "warrior_protection",
}


def load_wowhead_builds(spec_name: str) -> list[dict]:
    """Load talent builds from Wowhead extraction data.

    Returns list of {hero: str, build_index: int, talent_string: str}
    """
    # Find the wowhead directory for this spec
    wh_dir = None
    for wh_path, simc_name in SPEC_MAP.items():
        if simc_name == spec_name:
            wh_dir = WOWHEAD_DIR / wh_path / "extracted"
            break

    if wh_dir is None or not wh_dir.exists():
        return []

    talents_json = wh_dir / "talents.json"
    if not talents_json.exists():
        return []

    with open(talents_json) as f:
        data = json.load(f)

    builds = []
    content = data.get("content", {})

    for hero_name, hero_data in content.items():
        codes = hero_data.get("talent_codes", [])
        for i, code in enumerate(codes):
            if code and len(code) > 20:  # sanity check
                builds.append({
                    "hero": hero_name,
                    "build_index": i + 1,
                    "talent_string": code,
                    "label": f"{hero_name} #{i+1}",
                })

    return builds


def get_current_talent_string(profile_path: str) -> str:
    """Extract the talents= line from a profile."""
    with open(profile_path) as f:
        for line in f:
            if line.strip().startswith("talents="):
                return line.strip().split("=", 1)[1]
    return ""


def compare_builds_for_spec(
    spec_name: str,
    iterations: int = 1000,
    threads: int = 4,
) -> dict:
    """Compare all Wowhead builds for a spec. Returns results dict."""
    try:
        profile_path = find_profile(spec_name)
    except FileNotFoundError:
        return {"spec": spec_name, "error": "profile not found", "builds": []}

    builds = load_wowhead_builds(spec_name)
    if not builds:
        return {"spec": spec_name, "error": "no wowhead builds found", "builds": []}

    current_talents = get_current_talent_string(profile_path)

    print(f"\n{'='*60}")
    print(f"  {spec_name} — {len(builds)} builds")
    print(f"{'='*60}")

    results = []

    # First: sim current profile (no override)
    print(f"  Simming current profile...", end="", flush=True)
    try:
        current = run_composite(profile_path, iterations=iterations, threads=threads)
        print(f" {current.composite:.0f}")
        results.append({
            "label": "[CURRENT]",
            "hero": "current",
            "talent_string": current_talents,
            "pw": current.pw.dps_mean,
            "hac": current.hac.dps_mean,
            "composite": current.composite,
            "is_current": True,
        })
    except Exception as e:
        print(f" ERROR: {e}")
        results.append({
            "label": "[CURRENT]",
            "error": str(e),
            "is_current": True,
        })

    # Then: sim each Wowhead build
    for build in builds:
        label = build["label"]
        talent_str = build["talent_string"]

        # Skip if identical to current
        if talent_str == current_talents:
            print(f"  {label:30s} = SAME AS CURRENT, skipping")
            if results and results[0].get("composite"):
                results.append({
                    "label": label,
                    "hero": build["hero"],
                    "talent_string": talent_str,
                    "pw": results[0]["pw"],
                    "hac": results[0]["hac"],
                    "composite": results[0]["composite"],
                    "is_current_duplicate": True,
                })
            continue

        print(f"  {label:30s}", end="", flush=True)
        try:
            comp = run_composite(
                profile_path,
                iterations=iterations,
                threads=threads,
                overrides=[f"talents={talent_str}"],
            )
            delta = ""
            if results and results[0].get("composite"):
                pct = (comp.composite - results[0]["composite"]) / results[0]["composite"] * 100
                delta = f" ({pct:+.1f}%)"
            print(f" {comp.composite:.0f}{delta}")
            results.append({
                "label": label,
                "hero": build["hero"],
                "talent_string": talent_str,
                "pw": comp.pw.dps_mean,
                "hac": comp.hac.dps_mean,
                "composite": comp.composite,
            })
        except Exception as e:
            print(f" ERROR: {e}")
            results.append({
                "label": label,
                "hero": build["hero"],
                "talent_string": talent_str,
                "error": str(e),
            })

    # Sort by composite DPS (kept for backward compatibility)
    valid_results = [r for r in results if "composite" in r]
    valid_results.sort(key=lambda x: -x["composite"])

    # Also rank independently per fight style
    pw_ranked = sorted(valid_results, key=lambda x: -x["pw"])
    hac_ranked = sorted(valid_results, key=lambda x: -x["hac"])

    return {
        "spec": spec_name,
        "profile": profile_path,
        "iterations": iterations,
        "build_count": len(builds),
        "results": valid_results,
        "results_pw_ranked": pw_ranked,
        "results_hac_ranked": hac_ranked,
        "best_pw": pw_ranked[0] if pw_ranked else None,
        "best_hac": hac_ranked[0] if hac_ranked else None,
        "errors": [r for r in results if "error" in r and not r.get("is_current")],
    }


def write_report(all_results: list[dict], output_dir: Path):
    """Write summary report with per-fight-style rankings.

    Each spec gets independent best-build identification for Patchwerk and
    HecticAddCleave. The composite column is kept for reference only.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = ["# Wowhead Talent Build Comparison\n"]
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M')}\n")
    lines.append("**Note:** Each spec has independent best builds for Patchwerk and HecticAddCleave.\n")

    summary_rows = []

    for spec_data in sorted(all_results, key=lambda x: x["spec"]):
        spec = spec_data["spec"]
        results = spec_data.get("results", [])

        if not results:
            lines.append(f"\n## {spec}\n\nNo valid results.\n")
            continue

        lines.append(f"\n## {spec} ({spec_data['build_count']} builds)\n")

        # Find current build's DPS for each style
        current_pw = current_hac = None
        for r in results:
            if r.get("is_current") or r.get("is_current_duplicate"):
                current_pw = r["pw"]
                current_hac = r["hac"]
                break

        # Table: ranked by composite (reference), but show per-style bests
        lines.append(f"| Rank | Build | Patchwerk | HecticAC | Composite | vs Current (comp) |")
        lines.append(f"|------|-------|-----------|----------|-----------|-------------------|")

        current_comp = (current_pw + current_hac) * 0.5 if current_pw and current_hac else None
        for rank, r in enumerate(results, 1):
            label = r["label"]
            delta = ""
            if current_comp and not r.get("is_current"):
                pct = (r["composite"] - current_comp) / current_comp * 100
                delta = f"{pct:+.1f}%"
            marker = " **[CURRENT]**" if r.get("is_current") else ""
            if r.get("is_current_duplicate"):
                marker = " (=current)"
            lines.append(
                f"| {rank} | {label}{marker} | {r['pw']:,.0f} | {r['hac']:,.0f} | "
                f"{r['composite']:,.0f} | {delta} |"
            )

        # Per-fight-style bests
        best_pw = spec_data.get("best_pw")
        best_hac = spec_data.get("best_hac")
        if best_pw:
            pw_delta = f" ({(best_pw['pw'] - current_pw) / current_pw * 100:+.1f}%)" if current_pw else ""
            lines.append(f"\n**Best for Patchwerk:** {best_pw['label']} — {best_pw['pw']:,.0f} DPS{pw_delta}")
        if best_hac:
            hac_delta = f" ({(best_hac['hac'] - current_hac) / current_hac * 100:+.1f}%)" if current_hac else ""
            lines.append(f"**Best for HecticAddCleave:** {best_hac['label']} — {best_hac['hac']:,.0f} DPS{hac_delta}")

        # Summary row
        pw_gap = ((best_pw["pw"] - current_pw) / current_pw * 100) if best_pw and current_pw else 0
        hac_gap = ((best_hac["hac"] - current_hac) / current_hac * 100) if best_hac and current_hac else 0

        summary_rows.append({
            "spec": spec,
            "best_pw_build": best_pw["label"] if best_pw else "?",
            "best_pw_dps": best_pw["pw"] if best_pw else 0,
            "pw_gap": pw_gap,
            "best_hac_build": best_hac["label"] if best_hac else "?",
            "best_hac_dps": best_hac["hac"] if best_hac else 0,
            "hac_gap": hac_gap,
        })

    # Write per-spec report
    report_path = output_dir / "wowhead_comparison.md"
    with open(report_path, "w") as f:
        f.write("\n".join(lines))

    # Write summary table — per fight style
    summary_path = output_dir / "talent_summary.md"
    with open(summary_path, "w") as f:
        f.write("# Talent Build Summary (Per Fight Style)\n\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("Each spec is independently ranked for Patchwerk (ST) and HecticAddCleave (AoE/M+).\n\n")

        f.write("## Patchwerk Best Builds\n\n")
        f.write("| Spec | Best Build | DPS | vs Current |\n")
        f.write("|------|-----------|-----|------------|\n")
        for row in sorted(summary_rows, key=lambda x: -x["pw_gap"]):
            f.write(f"| {row['spec']} | {row['best_pw_build']} | {row['best_pw_dps']:,.0f} | {row['pw_gap']:+.1f}% |\n")

        f.write("\n## HecticAddCleave Best Builds\n\n")
        f.write("| Spec | Best Build | DPS | vs Current |\n")
        f.write("|------|-----------|-----|------------|\n")
        for row in sorted(summary_rows, key=lambda x: -x["hac_gap"]):
            f.write(f"| {row['spec']} | {row['best_hac_build']} | {row['best_hac_dps']:,.0f} | {row['hac_gap']:+.1f}% |\n")

        pw_subopt = [r for r in summary_rows if r["pw_gap"] > 0.5]
        hac_subopt = [r for r in summary_rows if r["hac_gap"] > 0.5]
        f.write(f"\n**Patchwerk:** {len(pw_subopt)} specs with suboptimal builds (>0.5% gap)\n")
        f.write(f"**HecticAddCleave:** {len(hac_subopt)} specs with suboptimal builds (>0.5% gap)\n")

    print(f"\nReports written to {output_dir}/")
    return summary_rows


def main():
    parser = argparse.ArgumentParser(description="Compare Wowhead talent builds")
    parser.add_argument("spec", nargs="?", help="Specific spec to test (e.g. warrior_fury)")
    parser.add_argument("--iterations", type=int, default=1000, help="Sim iterations (default: 1000)")
    parser.add_argument("--threads", type=int, default=4, help="SimC threads per sim")
    parser.add_argument("--all", action="store_true", help="Run all specs")
    args = parser.parse_args()

    if args.spec:
        specs = [args.spec]
    elif args.all or not args.spec:
        specs = sorted(SPEC_MAP.values())
    else:
        specs = sorted(SPEC_MAP.values())

    if args.spec and not args.all:
        specs = [args.spec]

    start = time.time()
    all_results = []

    for spec in specs:
        result = compare_builds_for_spec(spec, args.iterations, args.threads)
        all_results.append(result)

        # Save per-spec JSON
        spec_dir = RESULTS_DIR / spec
        spec_dir.mkdir(parents=True, exist_ok=True)
        with open(spec_dir / "wowhead_builds.json", "w") as f:
            json.dump(result, f, indent=2)

    # Write reports
    summary = write_report(all_results, RESULTS_DIR)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  COMPLETE — {len(specs)} specs in {elapsed:.0f}s")
    print(f"{'='*60}")

    # Print quick summary
    if summary:
        pw_sub = [r for r in summary if r["pw_gap"] > 0.5]
        hac_sub = [r for r in summary if r["hac_gap"] > 0.5]
        if pw_sub:
            print(f"\n  Patchwerk — specs with suboptimal builds:")
            for r in sorted(pw_sub, key=lambda x: -x["pw_gap"]):
                print(f"    {r['spec']:35s} {r['pw_gap']:+.1f}%  -> {r['best_pw_build']}")
        if hac_sub:
            print(f"\n  HecticAddCleave — specs with suboptimal builds:")
            for r in sorted(hac_sub, key=lambda x: -x["hac_gap"]):
                print(f"    {r['spec']:35s} {r['hac_gap']:+.1f}%  -> {r['best_hac_build']}")
        if not pw_sub and not hac_sub:
            print(f"\n  All specs are using optimal talent builds for both fight styles!")


if __name__ == "__main__":
    main()
