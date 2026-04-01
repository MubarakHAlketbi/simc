#!/usr/bin/env python3
"""
One-time comparison: reference profiles (simulationcraft.org) vs our PW profiles.

For each matching pair we run FOUR sims on OUR simc binary, all with OUR gear:
  A. Our profile as-is (or use existing phase4 baseline if fresh)
  B. Our profile + reference talent string substituted
  C. Our profile + reference APL substituted
  D. Our profile + ref talents + ref APL

This holds gear constant and isolates whether talents or APL drive any delta.

We also note the reference site-reported DPS so we can detect engine divergence.

Output:
  docs/analysis/reference_profile_comparison.md
"""

import re
import sys
import json
import time
import subprocess
import tempfile
import shutil
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SIMC       = Path("engine/simc")
PROFILES   = Path("profiles/MID1")
REF_BASE   = Path("reference/simulationcraft_org")
PHASE4     = Path("results/phase4")
OUT_MD     = Path("docs/analysis/reference_profile_comparison.md")
THREADS    = 16
TARGET_ERR = 0.1   # ~7500 iter equivalent
MAX_PAR    = 3     # parallel sims (×THREADS each)

# ---------------------------------------------------------------------------
# Explicit mapping: reference_dir -> our_profile (without .simc)
# Key = relative path under reference/simulationcraft_org
# Val = MID1 profile stem (without profiles/MID1/ and .simc)
# ---------------------------------------------------------------------------
MAPPING = {
    "death_knight/blood_deathbringer":       "MID1_Death_Knight_Blood_Deathbringer",
    "death_knight/blood_sanlayn":            "MID1_Death_Knight_Blood",
    "death_knight/frost":                    "MID1_Death_Knight_Frost",
    "death_knight/frost_rider":              "MID1_Death_Knight_Frost_Rider",
    "death_knight/unholy_rider":             "MID1_Death_Knight_Unholy",
    "death_knight/unholy_sanlayn":           "MID1_Death_Knight_Unholy_San'layn",
    "demon_hunter/devourer_annihilator":     "MID1_Demon_Hunter_Devourer",
    "demon_hunter/devourer_void-scarred":    "MID1_Demon_Hunter_Devourer_Void-Scarred",
    "demon_hunter/havoc_fel-scarred":        "MID1_Demon_Hunter_Havoc",
    "demon_hunter/vengeance_aldrachi_reaver":"MID1_Demon_Hunter_Vengeance_Aldrachi_Reaver",
    "demon_hunter/vengeance_annihilator":    "MID1_Demon_Hunter_Vengeance",
    "druid/feral_wildstalker":              "MID1_Druid_Feral",
    "druid/guardian":                       "MID1_Druid_Guardian",
    "evoker/devastation_fs":                "MID1_Evoker_Devastation_FS",
    "evoker/devastation_sc":                "MID1_Evoker_Devastation",
    "hunter/beast_mastery":                 "MID1_Hunter_Beast_Mastery",
    "hunter/marksmanship":                  "MID1_Hunter_Marksmanship",
    "hunter/survival_pl_dw":               "MID1_Hunter_Survival_PL_DW",
    "hunter/survival_sentinel_2h":          "MID1_Hunter_Survival",
    "mage/arcane_spellslinger":             "MID1_Mage_Arcane",
    "mage/arcane_sunfury":                  "MID1_Mage_Arcane_Sunfury",
    "mage/fire_frostfire":                  "MID1_Mage_Fire_Frostfire",
    "mage/fire_sunfury":                    "MID1_Mage_Fire",
    "mage/frost_frostfire":                 "MID1_Mage_Frost_Frostfire",
    "mage/frost_spellslinger":              "MID1_Mage_Frost",
    "monk/brewmaster":                      "MID1_Monk_Brewmaster",
    "monk/windwalker":                      "MID1_Monk_Windwalker",
    "monk/windwalker_conduit":              "MID1_Monk_Windwalker_Conduit",
    "paladin/protection":                   "MID1_Paladin_Protection",
    "paladin/protection_lightsmith":        "MID1_Paladin_Protection_Lightsmith",
    "paladin/retribution":                  "MID1_Paladin_Retribution",
    "paladin/retribution_herald":           "MID1_Paladin_Retribution_Herald",
    "priest/shadow_archon":                 "MID1_Priest_Shadow_Archon",
    "priest/shadow_voidweaver":             "MID1_Priest_Shadow",
    "rogue/assassination":                  "MID1_Rogue_Assassination",
    "rogue/outlaw_fatebound":               "MID1_Rogue_Outlaw",
    "rogue/outlaw_trickster":               "MID1_Rogue_Outlaw_Trickster",
    "rogue/subtlety":                       "MID1_Rogue_Subtlety",
    "shaman/elemental_stormbringer":        "MID1_Shaman_Elemental",
    "shaman/enhancement_stormbringer":      "MID1_Shaman_Enhancement_Stormbringer",
    "shaman/enhancement_totemic":           "MID1_Shaman_Enhancement",
    "warlock/affliction_hellcaller":        "MID1_Warlock_Affliction_Hellcaller",
    "warlock/affliction_soul_harvester":    "MID1_Warlock_Affliction",
    "warlock/demonology_soul_harvester":    "MID1_Warlock_Demonology_Soul_Harvester",
    "warlock/destruction_diabolist":        "MID1_Warlock_Destruction_Diabolist",
    "warlock/destruction_hellcaller":       "MID1_Warlock_Destruction",
    "warrior/protection":                   "MID1_Warrior_Protection",
}

# Reference-reported DPS (from index.md / site) — used only for engine divergence check
REF_REPORTED_DPS = {
    "death_knight/blood_deathbringer":       54717,
    "death_knight/blood_sanlayn":            59890,
    "death_knight/frost":                    116066,
    "death_knight/frost_rider":              112231,
    "death_knight/unholy_rider":             130435,
    "death_knight/unholy_sanlayn":           124990,
    "demon_hunter/devourer_annihilator":     108625,
    "demon_hunter/devourer_void-scarred":    109837,
    "demon_hunter/havoc_fel-scarred":        114804,
    "demon_hunter/vengeance_aldrachi_reaver":62207,
    "demon_hunter/vengeance_annihilator":    68737,
    "druid/feral_wildstalker":               120320,
    "druid/guardian":                        88270,
    "evoker/devastation_fs":                 104551,
    "evoker/devastation_sc":                 109070,
    "hunter/beast_mastery":                  113980,
    "hunter/marksmanship":                   108733,
    "hunter/survival_pl_dw":                 110339,
    "hunter/survival_sentinel_2h":           108605,
    "mage/arcane_spellslinger":              101622,
    "mage/arcane_sunfury":                   96253,
    "mage/fire_frostfire":                   105174,
    "mage/fire_sunfury":                     102438,
    "mage/frost_frostfire":                  95610,
    "mage/frost_spellslinger":               113638,
    "monk/brewmaster":                       72321,
    "monk/windwalker":                       114446,
    "monk/windwalker_conduit":               109083,
    "paladin/protection":                    69620,
    "paladin/protection_lightsmith":         55406,
    "paladin/retribution":                   112984,
    "paladin/retribution_herald":            104924,
    "priest/shadow_archon":                  107607,
    "priest/shadow_voidweaver":              105184,
    "rogue/assassination":                   104072,
    "rogue/outlaw_fatebound":                107724,
    "rogue/outlaw_trickster":                102142,
    "rogue/subtlety":                        109256,
    "shaman/elemental_stormbringer":         124290,
    "shaman/enhancement_stormbringer":       91989,
    "shaman/enhancement_totemic":            101146,
    "warlock/affliction_hellcaller":         99300,
    "warlock/affliction_soul_harvester":     104004,
    "warlock/demonology_soul_harvester":     120997,
    "warlock/destruction_diabolist":         108723,
    "warlock/destruction_hellcaller":        109082,
    "warrior/protection":                    77889,
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def run_sim(simc_file: str, label: str, tmpdir: Path) -> float | None:
    """Run simc on a .simc file, return mean DPS."""
    json_out = tmpdir / f"{label}.json"
    cmd = [
        str(SIMC), simc_file,
        f"fight_style=Patchwerk",
        f"target_error={TARGET_ERR}",
        f"threads={THREADS}",
        f"json2={json_out}",
        "output=/dev/null",
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=600)
        if not json_out.exists():
            return None
        with open(json_out) as f:
            data = json.load(f)
        players = data.get("players") or data.get("sim", {}).get("players", [])
        if not players:
            return None
        return float(players[0].get("collected_data", {}).get("dps", {}).get("mean", 0))
    except Exception as e:
        print(f"    [ERROR] {label}: {e}", flush=True)
        return None


def read_talent_string(ref_dir: str) -> str:
    path = REF_BASE / ref_dir / "talents.md"
    if not path.exists():
        return ""
    txt = path.read_text()
    # talents string is the line after ```
    m = re.search(r'## Talent Export String\n```\n([A-Za-z0-9+/=]+)', txt)
    return m.group(1).strip() if m else ""


def read_ref_apl(ref_dir: str) -> list[str]:
    """
    Return full APL lines (actions.*=...) from profile.simc — the authoritative
    source with correct actions.LISTNAME+=/ syntax.
    """
    path = REF_BASE / ref_dir / "profile.simc"
    if not path.exists():
        return []
    lines = path.read_text().splitlines()
    # Skip bare "actions" lines with no = (artifact of HTML extraction)
    return [l for l in lines if l.startswith("actions") and "=" in l]


def read_our_profile(profile_stem: str) -> str:
    p = PROFILES / f"{profile_stem}.simc"
    if not p.exists():
        return ""
    return p.read_text()


def extract_talent_from_profile(profile_text: str) -> str:
    m = re.search(r'^talents=([A-Za-z0-9+/=]+)', profile_text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def substitute_talents(profile_text: str, new_talents: str) -> str:
    return re.sub(r'^(talents=)[A-Za-z0-9+/=]+', f'talents={new_talents}',
                  profile_text, flags=re.MULTILINE)


def substitute_apl(profile_text: str, ref_apl_lines: list[str]) -> str:
    """
    Replace all actions.* lines in profile_text with ref_apl_lines.
    """
    # Remove all existing action lines
    cleaned = re.sub(r'^actions[^\n]*\n', '', profile_text, flags=re.MULTILINE)
    apl_block = "\n".join(ref_apl_lines) + "\n"
    return cleaned + apl_block


def diff_talents(our: str, ref: str) -> str:
    if our == ref:
        return "IDENTICAL"
    if not our or not ref:
        return "MISSING"
    return f"DIFFER (our={our[:20]}... ref={ref[:20]}...)"


def diff_apl_summary(our_text: str, ref_lines: list[str]) -> str:
    our_actions = set(re.findall(r'^actions[^\n]*', our_text, re.MULTILINE))
    ref_actions = set(ref_lines)
    same      = len(our_actions & ref_actions)
    only_ours = len(our_actions - ref_actions)
    only_ref  = len(ref_actions - our_actions)
    return f"ours={len(our_actions)} ref={len(ref_actions)} shared={same} only_ours={only_ours} only_ref={only_ref}"


# ---------------------------------------------------------------------------
# Per-spec work (run in a separate process via executor)
# ---------------------------------------------------------------------------
def process_spec(ref_dir: str, profile_stem: str) -> dict:
    label = ref_dir.replace("/", "_")
    tmpdir = Path(tempfile.mkdtemp(prefix=f"simc_cmp_{label}_"))

    result = {
        "ref_dir": ref_dir,
        "profile": profile_stem,
        "ref_reported": REF_REPORTED_DPS.get(ref_dir, 0),
        "dps_ours": None,
        "dps_ref_talents": None,
        "dps_ref_apl": None,
        "dps_ref_both": None,
        "talent_diff": "",
        "apl_diff": "",
        "error": None,
    }

    try:
        our_text = read_our_profile(profile_stem)
        if not our_text:
            result["error"] = f"profile not found: {profile_stem}.simc"
            return result

        ref_talent = read_talent_string(ref_dir)
        ref_apl    = read_ref_apl(ref_dir)
        our_talent = extract_talent_from_profile(our_text)

        result["talent_diff"] = diff_talents(our_talent, ref_talent)
        result["apl_diff"]    = diff_apl_summary(our_text, ref_apl)

        # Write profile variants to tmpdir
        ours_path = tmpdir / "ours.simc"
        ours_path.write_text(our_text)

        if ref_talent and ref_talent != our_talent:
            ref_t_text = substitute_talents(our_text, ref_talent)
            ref_t_path = tmpdir / "ref_talents.simc"
            ref_t_path.write_text(ref_t_text)
        else:
            ref_t_path = None

        if ref_apl:
            ref_a_text = substitute_apl(our_text, ref_apl)
            ref_a_path = tmpdir / "ref_apl.simc"
            ref_a_path.write_text(ref_a_text)
        else:
            ref_a_path = None

        if ref_talent and ref_apl and ref_talent != our_talent:
            ref_both_text = substitute_apl(substitute_talents(our_text, ref_talent), ref_apl)
            ref_both_path = tmpdir / "ref_both.simc"
            ref_both_path.write_text(ref_both_text)
        else:
            ref_both_path = None

        # --- Run sims ---
        print(f"  [{label}] running ours...", flush=True)
        result["dps_ours"] = run_sim(str(ours_path), "ours", tmpdir)

        if ref_t_path:
            print(f"  [{label}] running ref_talents...", flush=True)
            result["dps_ref_talents"] = run_sim(str(ref_t_path), "ref_t", tmpdir)

        if ref_a_path:
            print(f"  [{label}] running ref_apl...", flush=True)
            result["dps_ref_apl"] = run_sim(str(ref_a_path), "ref_a", tmpdir)

        if ref_both_path:
            print(f"  [{label}] running ref_both...", flush=True)
            result["dps_ref_both"] = run_sim(str(ref_both_path), "ref_both", tmpdir)

    except Exception as e:
        result["error"] = str(e)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    return result


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def pct(a, b):
    if a and b and b > 0:
        return f"{(a-b)/b*100:+.2f}%"
    return "N/A"


def engine_div(our_dps, reported):
    if our_dps and reported:
        d = (our_dps - reported) / reported * 100
        return f"{d:+.1f}%"
    return "N/A"


def write_report(results: list[dict]):
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reference Profile Comparison — simulationcraft.org vs Ours",
        "",
        "Source: https://simulationcraft.org/reports/MID1_Raid.html  ",
        "Their build: 86712bd5dd (12.0.1.66709, hotfix 2026-03-31)  ",
        f"Our build: midnight branch | Compared: {time.strftime('%Y-%m-%d')}  ",
        "Method: All sims use OUR gear + OUR simc binary. Only talents/APL substituted.",
        "",
        "## Quick Legend",
        "- **dps_ours**: our profile on our engine",
        "- **dps_ref_T**: our gear + their talent string",
        "- **dps_ref_A**: our gear + their APL",
        "- **dps_ref_TA**: our gear + their talents + their APL",
        "- **reported**: DPS from simulationcraft.org (different engine/gear)",
        "- **engine_div**: (dps_ours - reported) / reported — detects engine divergence",
        "",
        "## Summary Table",
        "",
        "| Spec | ours | ref_T | ref_A | ref_TA | reported | engine_div | winner |",
        "|------|------|-------|-------|--------|----------|------------|--------|",
    ]

    for r in sorted(results, key=lambda x: x["ref_dir"]):
        if r.get("error"):
            lines.append(f"| {r['ref_dir']} | ERROR: {r['error']} | | | | | | |")
            continue
        o   = r["dps_ours"]
        rt  = r["dps_ref_talents"]
        ra  = r["dps_ref_apl"]
        rta = r["dps_ref_both"]
        rep = r["ref_reported"]

        # Best overall
        candidates = {"ours": o, "ref_T": rt, "ref_A": ra, "ref_TA": rta}
        candidates = {k: v for k, v in candidates.items() if v}
        winner = max(candidates, key=candidates.get) if candidates else "?"

        def fmt(v): return f"{int(v):,}" if v else "-"
        def d(v): return pct(v, o) if v and o else "-"

        lines.append(
            f"| {r['ref_dir']} "
            f"| {fmt(o)} "
            f"| {fmt(rt)} ({d(rt)}) "
            f"| {fmt(ra)} ({d(ra)}) "
            f"| {fmt(rta)} ({d(rta)}) "
            f"| {fmt(rep)} "
            f"| {engine_div(o, rep)} "
            f"| **{winner}** |"
        )

    lines += [
        "",
        "## Engine Divergence Analysis",
        "",
        "Specs where our engine DPS differs from reported by more than ±5%:",
        "",
    ]
    divs = []
    for r in results:
        o = r.get("dps_ours")
        rep = r.get("ref_reported")
        if o and rep:
            d = (o - rep) / rep * 100
            if abs(d) > 5:
                divs.append((r["ref_dir"], o, rep, d))
    if divs:
        lines.append("| Spec | our_engine_DPS | reported_DPS | delta |")
        lines.append("|------|---------------|-------------|-------|")
        for spec, o, rep, d in sorted(divs, key=lambda x: abs(x[3]), reverse=True):
            lines.append(f"| {spec} | {int(o):,} | {int(rep):,} | {d:+.1f}% |")
    else:
        lines.append("None — engine parity within ±5% for all specs.")

    lines += [
        "",
        "## Talent Differences",
        "",
        "Specs where reference talent string differs from ours:",
        "",
        "| Spec | Our Talent String | Ref Talent String | DPS Impact |",
        "|------|------------------|-------------------|------------|",
    ]
    for r in sorted(results, key=lambda x: x["ref_dir"]):
        if r.get("error") or r["talent_diff"] == "IDENTICAL":
            continue
        our_t = extract_talent_from_profile(read_our_profile(r["profile"]))
        ref_t = read_talent_string(r["ref_dir"])
        dps_delta = pct(r.get("dps_ref_talents"), r.get("dps_ours"))
        lines.append(f"| {r['ref_dir']} | `{our_t[:40]}` | `{ref_t[:40]}` | {dps_delta} |")

    lines += [
        "",
        "## APL Differences",
        "",
        "| Spec | APL diff summary | DPS impact (ref_A vs ours) |",
        "|------|-----------------|---------------------------|",
    ]
    for r in sorted(results, key=lambda x: x["ref_dir"]):
        if r.get("error"):
            continue
        dps_delta = pct(r.get("dps_ref_apl"), r.get("dps_ours"))
        lines.append(f"| {r['ref_dir']} | {r['apl_diff']} | {dps_delta} |")

    lines += [
        "",
        "## Key Findings & Lessons",
        "",
        "*(Auto-generated — fill in manual analysis after reviewing the table above)*",
        "",
        "### Talent Lessons",
    ]

    # Auto-generate talent winners / losers
    talent_better_ours, talent_better_ref = [], []
    for r in results:
        if r.get("error") or not r.get("dps_ours") or not r.get("dps_ref_talents"):
            continue
        delta_pct = (r["dps_ref_talents"] - r["dps_ours"]) / r["dps_ours"] * 100
        if delta_pct > 0.5:
            talent_better_ref.append((r["ref_dir"], delta_pct))
        elif delta_pct < -0.5:
            talent_better_ours.append((r["ref_dir"], delta_pct))

    if talent_better_ref:
        lines.append("")
        lines.append("Reference talents beat ours (>0.5% gain) — investigate these builds:")
        for spec, d in sorted(talent_better_ref, key=lambda x: -x[1]):
            lines.append(f"- {spec}: ref_T is {d:+.2f}% vs ours")
    if talent_better_ours:
        lines.append("")
        lines.append("Our talents beat reference (>0.5% lead) — our optimizer working:")
        for spec, d in sorted(talent_better_ours, key=lambda x: x[1]):
            lines.append(f"- {spec}: our talents lead by {-d:.2f}%")

    lines += [
        "",
        "### APL Lessons",
    ]
    apl_better_ours, apl_better_ref = [], []
    for r in results:
        if r.get("error") or not r.get("dps_ours") or not r.get("dps_ref_apl"):
            continue
        delta_pct = (r["dps_ref_apl"] - r["dps_ours"]) / r["dps_ours"] * 100
        if delta_pct > 0.5:
            apl_better_ref.append((r["ref_dir"], delta_pct))
        elif delta_pct < -0.5:
            apl_better_ours.append((r["ref_dir"], delta_pct))

    if apl_better_ref:
        lines.append("")
        lines.append("Reference APL beats ours (>0.5%) — consider adopting or investigating:")
        for spec, d in sorted(apl_better_ref, key=lambda x: -x[1]):
            lines.append(f"- {spec}: ref_A is {d:+.2f}% vs ours")
    if apl_better_ours:
        lines.append("")
        lines.append("Our APL beats reference (>0.5%) — our optimization paying off:")
        for spec, d in sorted(apl_better_ours, key=lambda x: x[1]):
            lines.append(f"- {spec}: our APL leads by {-d:.2f}%")

    lines += [
        "",
        "### Engine Divergence Lessons",
        "*(Fill in after reviewing engine_div column — large divergences indicate bugs or missing features)*",
        "",
        "---",
        f"*Generated by scripts/compare_reference_profiles.py on {time.strftime('%Y-%m-%d %H:%M')}*",
    ]

    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"\n[done] Report written to {OUT_MD}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    import os
    os.chdir(Path(__file__).parent.parent)

    pairs = [(ref_dir, stem) for ref_dir, stem in MAPPING.items()
             if (PROFILES / f"{stem}.simc").exists()
             and (REF_BASE / ref_dir / "profile.simc").exists()]

    missing_ours = [(r, s) for r, s in MAPPING.items()
                    if not (PROFILES / f"{s}.simc").exists()]
    missing_ref  = [(r, s) for r, s in MAPPING.items()
                    if not (REF_BASE / r / "profile.simc").exists()]

    print(f"[compare] {len(pairs)} pairs to compare")
    if missing_ours:
        print(f"[skip - no our profile] {[s for _,s in missing_ours]}")
    if missing_ref:
        print(f"[skip - no ref profile] {[r for r,_ in missing_ref]}")

    results = []
    # Process in parallel batches
    with ProcessPoolExecutor(max_workers=MAX_PAR) as ex:
        futs = {ex.submit(process_spec, ref_dir, stem): ref_dir
                for ref_dir, stem in pairs}
        for fut in as_completed(futs):
            ref_dir = futs[fut]
            try:
                r = fut.result()
                o = r.get("dps_ours")
                rt = r.get("dps_ref_talents")
                ra = r.get("dps_ref_apl")
                err = r.get("error")
                if err:
                    print(f"  [FAIL] {ref_dir}: {err}")
                else:
                    print(f"  [done] {ref_dir}  ours={int(o or 0):,}  "
                          f"ref_T={int(rt or 0):,} ({pct(rt,o)})  "
                          f"ref_A={int(ra or 0):,} ({pct(ra,o)})")
                results.append(r)
            except Exception as e:
                print(f"  [EXCEPTION] {ref_dir}: {e}")
                results.append({"ref_dir": ref_dir, "profile": MAPPING[ref_dir],
                                 "ref_reported": REF_REPORTED_DPS.get(ref_dir,0),
                                 "error": str(e)})

    write_report(results)

    # Save raw JSON for future reference
    raw_json = OUT_MD.with_suffix(".json")
    raw_json.write_text(json.dumps(results, indent=2))
    print(f"[done] Raw data: {raw_json}")


if __name__ == "__main__":
    main()
