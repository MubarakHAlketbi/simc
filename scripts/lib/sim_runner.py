"""SimC Runner Module — run sims, parse results, parallel execution."""

import asyncio
import json
import os
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

SIMC_BIN = Path(__file__).resolve().parents[2] / "engine" / "simc"
PROFILES_DIR = Path(__file__).resolve().parents[2] / "profiles" / "MID1"


@dataclass
class SimResult:
    """Result of a single sim run."""
    dps_mean: float
    dps_error: float
    fight_style: str
    action_breakdown: dict[str, float] = field(default_factory=dict)  # name -> compound_amount
    profile_name: str = ""
    raw_json_path: str = ""

    def __repr__(self):
        return f"SimResult(dps={self.dps_mean:.0f}±{self.dps_error:.0f}, fight={self.fight_style})"


@dataclass
class CompositeResult:
    """Combined result across fight styles.

    NOTE: composite is kept for backward compatibility / reporting, but
    optimization should treat Patchwerk and HecticAddCleave independently.
    Each spec should have two optimal talent/APL builds — one per fight style.
    """
    pw: SimResult
    hac: SimResult
    composite: float = 0.0

    def __post_init__(self):
        self.composite = 0.5 * self.pw.dps_mean + 0.5 * self.hac.dps_mean

    def __repr__(self):
        return (f"CompositeResult(pw={self.pw.dps_mean:.0f}, "
                f"hac={self.hac.dps_mean:.0f}, comp={self.composite:.0f})")


def parse_sim_json(json_path: str, fight_style: str) -> SimResult:
    """Parse SimC JSON2 output into SimResult."""
    with open(json_path) as f:
        data = json.load(f)

    player = data["sim"]["players"][0]
    cd = player["collected_data"]

    action_breakdown = {}
    for stat in player.get("stats", []):
        if stat["compound_amount"] > 0:
            action_breakdown[stat["name"]] = stat["compound_amount"]

    return SimResult(
        dps_mean=cd["dps"]["mean"],
        dps_error=cd["dps"].get("mean_std_dev", 0),
        fight_style=fight_style,
        action_breakdown=action_breakdown,
        profile_name=player["name"],
        raw_json_path=json_path,
    )


def run_sim(
    profile_path: str,
    fight_style: str = "Patchwerk",
    iterations: int = 1000,
    threads: int = 4,
    overrides: Optional[list[str]] = None,
    json_out: Optional[str] = None,
    simc_bin: Optional[str] = None,
) -> SimResult:
    """Run a single SimC simulation synchronously.

    Args:
        profile_path: Path to .simc profile file
        fight_style: Patchwerk or HecticAddCleave
        iterations: Number of sim iterations
        threads: SimC thread count
        overrides: Extra lines to append (e.g. ["talents=...", "actions=..."])
        json_out: Path for JSON output (temp file if None)
        simc_bin: Path to simc binary (default: engine/simc)

    Returns:
        SimResult with DPS and action breakdown
    """
    bin_path = simc_bin or str(SIMC_BIN)
    cleanup_json = json_out is None
    if json_out is None:
        fd, json_out = tempfile.mkstemp(suffix=".json", prefix="simc_")
        os.close(fd)

    try:
        # Build the .simc input
        if overrides:
            fd, override_path = tempfile.mkstemp(suffix=".simc", prefix="simc_override_")
            os.close(fd)
            with open(override_path, "w") as f:
                f.write(f"input={profile_path}\n")
                for line in overrides:
                    f.write(line + "\n")
            input_path = override_path
        else:
            input_path = profile_path
            override_path = None

        cmd = [
            bin_path, input_path,
            f"fight_style={fight_style}",
            f"iterations={iterations}",
            f"threads={threads}",
            f"json2={json_out}",
            "output=/dev/null",
        ]

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=300
        )

        if override_path:
            os.unlink(override_path)

        # Check for errors (SimC returns 0 even with errors sometimes)
        if "Error:" in result.stderr or "Error:" in result.stdout:
            error_lines = [l for l in (result.stdout + result.stderr).split("\n")
                          if "Error:" in l]
            raise RuntimeError(f"SimC error: {'; '.join(error_lines)}")

        return parse_sim_json(json_out, fight_style)

    finally:
        if cleanup_json and os.path.exists(json_out):
            os.unlink(json_out)


def run_composite(
    profile_path: str,
    iterations: int = 1000,
    threads: int = 4,
    overrides: Optional[list[str]] = None,
    simc_bin: Optional[str] = None,
) -> CompositeResult:
    """Run Patchwerk + HecticAddCleave and return composite result."""
    pw = run_sim(profile_path, "Patchwerk", iterations, threads, overrides, simc_bin=simc_bin)
    hac = run_sim(profile_path, "HecticAddCleave", iterations, threads, overrides, simc_bin=simc_bin)
    return CompositeResult(pw=pw, hac=hac)


def should_accept(candidate: CompositeResult, baseline: CompositeResult,
                  regression_cap: float = 0.01) -> bool:
    """Check if candidate should replace baseline (composite mode — legacy).

    Rules:
    - Composite must improve
    - Neither fight style may regress more than regression_cap (default 1%)
    """
    if candidate.composite <= baseline.composite:
        return False
    if candidate.pw.dps_mean < baseline.pw.dps_mean * (1 - regression_cap):
        return False
    if candidate.hac.dps_mean < baseline.hac.dps_mean * (1 - regression_cap):
        return False
    return True


def should_accept_single(candidate: SimResult, baseline: SimResult) -> bool:
    """Check if candidate improves DPS for a single fight style.

    Used by per-fight-style optimization (the primary mode).
    Each spec should be optimized independently for Patchwerk and
    HecticAddCleave, producing two optimal talent/APL builds.
    """
    return candidate.dps_mean > baseline.dps_mean


async def run_sim_async(
    profile_path: str,
    fight_style: str = "Patchwerk",
    iterations: int = 1000,
    threads: int = 4,
    overrides: Optional[list[str]] = None,
    simc_bin: Optional[str] = None,
) -> SimResult:
    """Async version of run_sim for parallel execution."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, run_sim, profile_path, fight_style, iterations, threads,
        overrides, None, simc_bin
    )


async def run_composite_async(
    profile_path: str,
    iterations: int = 1000,
    threads: int = 4,
    overrides: Optional[list[str]] = None,
    simc_bin: Optional[str] = None,
) -> CompositeResult:
    """Async composite — runs both fight styles concurrently."""
    pw_task = run_sim_async(profile_path, "Patchwerk", iterations, threads, overrides, simc_bin)
    hac_task = run_sim_async(profile_path, "HecticAddCleave", iterations, threads, overrides, simc_bin)
    pw, hac = await asyncio.gather(pw_task, hac_task)
    return CompositeResult(pw=pw, hac=hac)


async def batch_composite(
    jobs: list[tuple[str, Optional[list[str]]]],  # [(profile_path, overrides), ...]
    iterations: int = 1000,
    threads: int = 4,
    max_concurrent: int = 4,
    simc_bin: Optional[str] = None,
) -> list[CompositeResult]:
    """Run multiple composite sims with concurrency limit."""
    semaphore = asyncio.Semaphore(max_concurrent)
    results = []

    async def limited_run(profile, overrides):
        async with semaphore:
            return await run_composite_async(profile, iterations, threads, overrides, simc_bin)

    tasks = [limited_run(p, o) for p, o in jobs]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Convert exceptions to None with warning
    final = []
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            print(f"  WARNING: sim failed for job {i}: {r}")
            final.append(None)
        else:
            final.append(r)
    return final


def extract_apl(profile_path: str, simc_bin: Optional[str] = None) -> str:
    """Extract the full APL that SimC would run for a profile.

    Uses save_actions to dump the generated APL (works for both
    .simc override APLs and C++ generated APLs).
    """
    bin_path = simc_bin or str(SIMC_BIN)
    fd, actions_path = tempfile.mkstemp(suffix=".simc", prefix="simc_actions_")
    os.close(fd)

    try:
        cmd = [
            bin_path, profile_path,
            "iterations=0",
            f"save_actions={actions_path}",
            "output=/dev/null",
        ]
        subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        with open(actions_path) as f:
            return f.read()
    finally:
        if os.path.exists(actions_path):
            os.unlink(actions_path)


_CLASS_ALIASES = {
    "dk": "Death_Knight",
    "dh": "Demon_Hunter",
}

_SPEC_ALIASES = {
    "bm": "Beast_Mastery",
    "mm": "Marksmanship",
    "ww": "Windwalker",
}


def find_profile(spec_name: str) -> str:
    """Find MID1 profile path for a spec name like 'warrior_fury' or 'dk_unholy'."""
    parts = spec_name.split("_")

    # Resolve class alias (dk -> Death_Knight, dh -> Demon_Hunter)
    cls_key = parts[0].lower()
    if cls_key in _CLASS_ALIASES:
        cls = _CLASS_ALIASES[cls_key]
        spec_parts = parts[1:]
    else:
        cls = parts[0].capitalize()
        spec_parts = parts[1:]

    # Resolve spec alias (bm -> Beast_Mastery, mm -> Marksmanship)
    if len(spec_parts) == 1 and spec_parts[0].lower() in _SPEC_ALIASES:
        spc = _SPEC_ALIASES[spec_parts[0].lower()]
    else:
        spc = "_".join(p.capitalize() for p in spec_parts)

    profile_name = f"MID1_{cls}_{spc}"
    path = PROFILES_DIR / f"{profile_name}.simc"
    if path.exists():
        return str(path)

    # Try fuzzy match as fallback
    for p in PROFILES_DIR.glob("MID1_*.simc"):
        if spec_name.replace("_", "").lower() in p.stem.replace("_", "").lower():
            return str(p)

    raise FileNotFoundError(f"No profile found for spec '{spec_name}' in {PROFILES_DIR}")


if __name__ == "__main__":
    import sys
    # Quick test
    spec = sys.argv[1] if len(sys.argv) > 1 else "warrior_fury"
    profile = find_profile(spec)
    print(f"Testing {spec} -> {profile}")

    result = run_sim(profile, "Patchwerk", iterations=100, threads=8)
    print(f"  Patchwerk:  {result}")

    result2 = run_sim(profile, "HecticAddCleave", iterations=100, threads=8)
    print(f"  HecticAC:   {result2}")

    comp = CompositeResult(pw=result, hac=result2)
    print(f"  Composite:  {comp}")

    print(f"\n  Top 5 actions by damage:")
    for name, dmg in sorted(result.action_breakdown.items(), key=lambda x: -x[1])[:5]:
        print(f"    {name:30s} {dmg:>12,.0f}")
