#!/usr/bin/env python3
"""dump_llm_prompts.py — Print the exact prompts sent to Layer 3 LLM for a spec.

Runs a real baseline sim, extracts signals, builds the prompt for each fight
style, and prints them to stdout. Does NOT call the LLM or modify any files.

Usage:
    python3 scripts/dump_llm_prompts.py warlock_affliction
    python3 scripts/dump_llm_prompts.py warlock_affliction --fight-style Patchwerk
    python3 scripts/dump_llm_prompts.py warrior_fury --iterations 3000
"""

import argparse
import sys
import os
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.lib.sim_runner import run_sim, extract_apl, find_profile
from scripts.lib.apl_parser import parse_apl
from scripts.lib.apl_signal_extractor import extract_signals, format_signals_report
from scripts.lib.llm_apl_advisor import build_llm_prompt

FIGHT_STYLES = ["Patchwerk", "HecticAddCleave"]

DIVIDER     = "=" * 80
SUBDIV      = "-" * 80


def dump_prompt(spec: str, fight_style: str, iterations: int, threads: int) -> None:
    # Resolve profile path (HAC uses _HAC.simc)
    profile_path = find_profile(spec)
    if fight_style == "HecticAddCleave":
        hac = profile_path.replace(".simc", "_HAC.simc")
        if Path(hac).exists():
            profile_path = hac

    print(f"\n{DIVIDER}")
    print(f"  SPEC: {spec}   FIGHT STYLE: {fight_style}")
    print(f"  PROFILE: {Path(profile_path).name}")
    print(f"  Running baseline ({iterations} iter)...")
    print(DIVIDER)

    fd, json_path = tempfile.mkstemp(suffix=".json", prefix="simc_dump_")
    os.close(fd)
    try:
        baseline = run_sim(profile_path, fight_style,
                           iterations=iterations, threads=threads,
                           json_out=json_path)
    finally:
        if os.path.exists(json_path):
            os.unlink(json_path)

    print(f"  Baseline DPS: {baseline.dps_mean:,.0f}")
    print(f"  Ability stats: {len(baseline.ability_stats)}")
    print(f"  Buff stats:    {len(baseline.buff_stats)}")
    print(f"  Resource stats:{len(baseline.resource_stats)}")

    apl_text = extract_apl(profile_path)
    apl      = parse_apl(apl_text)
    signals  = extract_signals(baseline, apl)

    print(f"\n  Signals detected: {len(signals)}")
    print(format_signals_report(signals))

    prompt = build_llm_prompt(spec, fight_style, baseline, apl_text, signals)

    print(f"\n{DIVIDER}")
    print(f"  PROMPT  ({len(prompt)} chars, ~{len(prompt)//4} tokens)")
    print(DIVIDER)
    print(prompt)
    print(DIVIDER)
    print(f"  END OF PROMPT — {spec} / {fight_style}")
    print(DIVIDER)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print Layer 3 LLM prompts for a spec without calling the LLM"
    )
    parser.add_argument("spec", help="Spec name, e.g. warlock_affliction")
    parser.add_argument(
        "--fight-style", default=None,
        choices=["Patchwerk", "HecticAddCleave"],
        help="Single fight style (default: both)",
    )
    parser.add_argument(
        "--iterations", type=int, default=5000,
        help="Sim iterations for baseline (default: 5000)",
    )
    parser.add_argument(
        "--threads", type=int, default=16,
        help="SimC threads (default: 16)",
    )
    args = parser.parse_args()

    styles = [args.fight_style] if args.fight_style else FIGHT_STYLES
    for fs in styles:
        dump_prompt(args.spec, fs, args.iterations, args.threads)


if __name__ == "__main__":
    main()
