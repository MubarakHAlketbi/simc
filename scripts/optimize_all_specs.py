#!/usr/bin/env python3
"""
Full optimization pass for all 33 specs.
Per spec:
  1. Talent search PW
  2. Talent search HAC
  3. Apply PW talent -> base profile, HAC talent -> _HAC profile
  4. APL opt PW on base profile, APL opt HAC on _HAC profile
  5. Apply improved APLs
  6. Validate + smoke test
  7. Commit
  8. Print short report
"""

import subprocess
import sys
import json
import re
import shutil
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "profiles" / "MID1"
OPT = ROOT / "results" / "optimization"
SIMC = ROOT / "engine" / "simc"

SPECS = [
    "warrior_arms",
    "warrior_fury",
    "warrior_protection",
    "paladin_protection",
    "paladin_retribution",
    "hunter_bm",
    "hunter_mm",
    "hunter_survival",
    "rogue_assassination",
    "rogue_outlaw",
    "rogue_subtlety",
    "priest_shadow",
    "dk_blood",
    "dk_frost",
    "dk_unholy",
    "shaman_elemental",
    "shaman_enhancement",
    "mage_arcane",
    "mage_fire",
    "mage_frost",
    "warlock_affliction",
    "warlock_demonology",
    "warlock_destruction",
    "monk_brewmaster",
    "monk_windwalker",
    "druid_balance",
    "druid_feral",
    "druid_guardian",
    "dh_havoc",
    "dh_vengeance",
    "dh_devourer",
    "evoker_devastation",
    "evoker_augmentation",
]


def run(cmd, timeout=3600):
    """Run a command, return (stdout+stderr, returncode)."""
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True,
        cwd=str(ROOT), timeout=timeout
    )
    return result.stdout + result.stderr, result.returncode


def find_profile(spec):
    """Return base profile path for a spec name."""
    out, rc = run(f"python3 -c \"import sys; sys.path.insert(0,'.'); from scripts.lib.sim_runner import find_profile; print(find_profile('{spec}'))\"")
    if rc != 0:
        return None
    path = out.strip()
    return path if Path(path).exists() else None


def hac_profile_path(base_path):
    """Derive _HAC profile path from base profile path."""
    p = Path(base_path)
    return str(p.parent / (p.stem + "_HAC" + p.suffix))


def get_talents_line(profile_path):
    """Extract current talents= value from a profile."""
    with open(profile_path) as f:
        for line in f:
            if line.strip().startswith("talents="):
                return line.strip().split("=", 1)[1]
    return None


def set_talents(profile_path, talent_string):
    """Replace talents= line in a profile."""
    lines = []
    with open(profile_path) as f:
        lines = f.readlines()
    replaced = False
    with open(profile_path, "w") as f:
        for line in lines:
            if line.strip().startswith("talents="):
                f.write(f"talents={talent_string}\n")
                replaced = True
            else:
                f.write(line)
    if not replaced:
        with open(profile_path, "a") as f:
            f.write(f"\ntalents={talent_string}\n")


def apply_apl(profile_path, apl_path):
    """Replace all actions lines in profile with those from apl_path."""
    with open(profile_path) as f:
        non_action_lines = [l for l in f.readlines() if not l.strip().startswith("actions")]
    with open(apl_path) as f:
        apl_lines = f.readlines()
    with open(profile_path, "w") as f:
        f.writelines(non_action_lines)
        if non_action_lines and not non_action_lines[-1].endswith("\n"):
            f.write("\n")
        f.writelines(apl_lines)


def parse_talent_result(output):
    """Extract (talent_string, dps) from talent_local_search output.
    Returns (None, baseline_dps) if no improvement found."""
    talent = None
    final_dps = None
    baseline_dps = None

    for line in output.splitlines():
        m = re.search(r"Talent string:\s*(\S+)", line)
        if m:
            talent = m.group(1)
        m = re.search(r"Final:\s*([\d,]+)\s*DPS", line)
        if m:
            final_dps = float(m.group(1).replace(",", ""))
        m = re.search(r"Result:\s*([\d,]+)\s*DPS", line)
        if m and final_dps is None:
            final_dps = float(m.group(1).replace(",", ""))
        m = re.search(r"Baseline DPS:\s*([\d,]+)", line)
        if m:
            baseline_dps = float(m.group(1).replace(",", ""))

    return talent, (final_dps or baseline_dps)


def read_apl_result(spec, style_tag):
    """Read APL optimization JSON result."""
    path = OPT / spec / f"apl_optimization_{style_tag}.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def smoke_test(profile_path):
    """Return True if profile parses without crash."""
    out, rc = run(f"./engine/simc \"{profile_path}\" iterations=1 output=/dev/null 2>&1", timeout=60)
    return rc == 0


def validate():
    """Run validate_all_profiles.py, return (passed, failed, output)."""
    out, rc = run("python3 scripts/validate_all_profiles.py", timeout=120)
    m = re.search(r"(\d+) passed, (\d+) failed", out)
    if m:
        return int(m.group(1)), int(m.group(2)), out
    return 0, 1, out


def optimize_spec(spec):
    report = {
        "spec": spec,
        "pw_talent_changed": False, "hac_talent_changed": False,
        "pw_dps": None, "hac_dps": None,
        "pw_apl": "no gain", "hac_apl": "no gain",
        "errors": [], "committed": False,
        "unchanged": False,
    }

    print(f"\n{'='*60}")
    print(f"  {spec.upper()}")
    print(f"{'='*60}")

    base_profile = find_profile(spec)
    if not base_profile:
        report["errors"].append("profile not found")
        return report
    hac_profile = hac_profile_path(base_profile)

    # Ensure HAC profile exists
    if not Path(hac_profile).exists():
        shutil.copy(base_profile, hac_profile)
        print(f"  Created HAC profile: {Path(hac_profile).name}")

    orig_pw_talent = get_talents_line(base_profile)
    orig_hac_talent = get_talents_line(hac_profile)

    # ── Step 1: Talent opt PW ─────────────────────────────────────────────
    print(f"  [1/4] Talent search PW...")
    out, rc = run(
        f"python3 scripts/talent_local_search.py "
        f"--spec {spec} --fight-style Patchwerk --max-iter 5 --threads 16",
        timeout=2400
    )
    pw_talent, pw_dps = parse_talent_result(out)
    report["pw_dps"] = pw_dps
    if pw_talent and pw_talent != orig_pw_talent:
        report["pw_talent_changed"] = True
        set_talents(base_profile, pw_talent)
        print(f"        New talent -> {pw_dps:,.0f} DPS")
    else:
        if not pw_talent:
            pw_talent = orig_pw_talent
        print(f"        No improvement -> {pw_dps:,.0f} DPS" if pw_dps else "        No result")
    report["pw_final_talent"] = pw_talent

    # ── Step 2: Talent opt HAC ────────────────────────────────────────────
    print(f"  [2/4] Talent search HAC...")
    out, rc = run(
        f"python3 scripts/talent_local_search.py "
        f"--spec {spec} --fight-style HecticAddCleave --max-iter 5 --threads 16",
        timeout=2400
    )
    hac_talent, hac_dps = parse_talent_result(out)
    report["hac_dps"] = hac_dps
    if hac_talent and hac_talent != orig_hac_talent:
        report["hac_talent_changed"] = True
        set_talents(hac_profile, hac_talent)
        print(f"        New talent -> {hac_dps:,.0f} DPS")
    else:
        if not hac_talent:
            hac_talent = orig_hac_talent
        print(f"        No improvement -> {hac_dps:,.0f} DPS" if hac_dps else "        No result")
    report["hac_final_talent"] = hac_talent

    # Ensure HAC profile has the HAC talent (even if same as PW)
    if hac_talent:
        set_talents(hac_profile, hac_talent)

    # ── Step 3: APL opt PW ────────────────────────────────────────────────
    print(f"  [3/4] APL opt PW...")
    out, rc = run(
        f"python3 scripts/apl_optimizer.py {spec} --fight-style Patchwerk "
        f"--max-iter 5 --threads 16",
        timeout=2400
    )
    pw_apl_result = read_apl_result(spec, "pw")
    pw_apl_pct = pw_apl_result.get("improvement_pct", 0) if pw_apl_result else 0
    if pw_apl_pct > 0.1:
        report["pw_apl"] = f"+{pw_apl_pct:.2f}%"
        apl_file = OPT / spec / "optimized_apl_pw.simc"
        if apl_file.exists():
            apply_apl(base_profile, str(apl_file))
            print(f"        Applied: {report['pw_apl']}")
        else:
            print(f"        Improved {report['pw_apl']} but optimized_apl_pw.simc missing")
    else:
        report["pw_apl"] = f"+{pw_apl_pct:.2f}%" if pw_apl_pct > 0 else "no gain"
        print(f"        {report['pw_apl']}")

    # ── Step 4: APL opt HAC ───────────────────────────────────────────────
    print(f"  [4/4] APL opt HAC...")
    # APL optimizer uses find_profile which returns base profile.
    # Temporarily swap HAC talent into base profile so APL optimizer
    # runs HAC sims with the HAC talent build.
    if hac_talent and hac_talent != get_talents_line(base_profile):
        set_talents(base_profile, hac_talent)
        swapped = True
    else:
        swapped = False

    out, rc = run(
        f"python3 scripts/apl_optimizer.py {spec} --fight-style HecticAddCleave "
        f"--max-iter 5 --threads 16",
        timeout=2400
    )

    # Restore PW talent to base profile
    if swapped and pw_talent:
        set_talents(base_profile, pw_talent)

    hac_apl_result = read_apl_result(spec, "hac")
    hac_apl_pct = hac_apl_result.get("improvement_pct", 0) if hac_apl_result else 0
    if hac_apl_pct > 0.1:
        report["hac_apl"] = f"+{hac_apl_pct:.2f}%"
        apl_file = OPT / spec / "optimized_apl_hac.simc"
        if apl_file.exists():
            apply_apl(hac_profile, str(apl_file))
            print(f"        Applied: {report['hac_apl']}")
        else:
            print(f"        Improved {report['hac_apl']} but optimized_apl_hac.simc missing")
    else:
        report["hac_apl"] = f"+{hac_apl_pct:.2f}%" if hac_apl_pct > 0 else "no gain"
        print(f"        {report['hac_apl']}")

    # ── Step 5: Smoke test ────────────────────────────────────────────────
    for path, label in [(base_profile, "PW"), (hac_profile, "HAC")]:
        if not smoke_test(path):
            report["errors"].append(f"smoke failed: {label}")

    # ── Step 6: Validate ──────────────────────────────────────────────────
    passed, failed, val_out = validate()
    if failed > 0:
        report["errors"].append(f"validate: {failed} failed")
        for line in val_out.splitlines():
            if "FAIL" in line:
                print(f"  VALIDATION: {line.strip()}")

    # ── Step 7: Commit ────────────────────────────────────────────────────
    talent_changed = report["pw_talent_changed"] or report["hac_talent_changed"]
    apl_changed = (report["pw_apl"] not in ("no gain", "+0.00%") or
                   report["hac_apl"] not in ("no gain", "+0.00%"))
    changes = []
    if report["pw_talent_changed"]:
        changes.append(f"PW talent {report['pw_dps']:,.0f}" if report["pw_dps"] else "PW talent")
    if report["hac_talent_changed"]:
        changes.append(f"HAC talent {report['hac_dps']:,.0f}" if report["hac_dps"] else "HAC talent")
    if report["pw_apl"] not in ("no gain", "+0.00%"):
        changes.append(f"PW APL {report['pw_apl']}")
    if report["hac_apl"] not in ("no gain", "+0.00%"):
        changes.append(f"HAC APL {report['hac_apl']}")

    if not report["errors"]:
        if not changes:
            report["unchanged"] = True
            report["committed"] = True
            print(f"  Already optimal — no changes")
        else:
            pw_s = f"{report['pw_dps']:,.0f}" if report["pw_dps"] else "?"
            hac_s = f"{report['hac_dps']:,.0f}" if report["hac_dps"] else "?"
            msg = f"optimize({spec}): PW {pw_s}; HAC {hac_s}; {', '.join(changes)}"
            git_out, rc = run(f"git add profiles/MID1/ && git commit -m \"{msg}\"")
            if rc == 0:
                report["committed"] = True
                print(f"  Committed: {msg}")
            elif "nothing to commit" in git_out:
                report["committed"] = True
                report["unchanged"] = True
                print(f"  Nothing changed (already optimal)")
            else:
                report["errors"].append("git commit failed")
                print(f"  Commit failed: {git_out[:200]}")
    else:
        print(f"  Skipping commit: {report['errors']}")

    return report


def print_short_report(report):
    spec = report["spec"]
    pw = f"{report['pw_dps']:,.0f}" if report["pw_dps"] else "N/A"
    hac = f"{report['hac_dps']:,.0f}" if report["hac_dps"] else "N/A"
    t_pw = "Y" if report.get("pw_talent_changed") else "-"
    t_hac = "Y" if report.get("hac_talent_changed") else "-"
    pw_apl = report.get("pw_apl", "-")
    hac_apl = report.get("hac_apl", "-")
    if report["errors"]:
        status = "ERR:" + "|".join(report["errors"])[:30]
    elif report.get("unchanged"):
        status = "already-optimal"
    else:
        status = "OK"
    print(f"  {spec:30s}  PW={pw:>10}  HAC={hac:>10}  T={t_pw}/{t_hac}  APL={pw_apl}/{hac_apl}  [{status}]")


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list":
            for s in SPECS:
                print(s)
            return
        specs_to_run = sys.argv[1:]
    else:
        specs_to_run = SPECS

    all_reports = []
    for i, spec in enumerate(specs_to_run):
        print(f"\n\n[{i+1}/{len(specs_to_run)}] >>> {spec.upper()} <<<")
        try:
            report = optimize_spec(spec)
        except subprocess.TimeoutExpired:
            report = {"spec": spec, "pw_dps": None, "hac_dps": None,
                      "pw_talent_changed": False, "hac_talent_changed": False,
                      "pw_apl": "-", "hac_apl": "-",
                      "errors": ["TIMEOUT"], "committed": False, "unchanged": False}
            print(f"  TIMEOUT")
        except Exception as e:
            report = {"spec": spec, "pw_dps": None, "hac_dps": None,
                      "pw_talent_changed": False, "hac_talent_changed": False,
                      "pw_apl": "-", "hac_apl": "-",
                      "errors": [str(e)[:60]], "committed": False, "unchanged": False}
            print(f"  EXCEPTION: {e}")
        all_reports.append(report)

        # Immediate short report after each spec
        print(f"\n  --- REPORT ---")
        print_short_report(report)

    # Final summary table
    print(f"\n\n{'='*100}")
    print(f"  FULL OPTIMIZATION COMPLETE — {len(all_reports)} specs")
    print(f"{'='*100}")
    print(f"  {'Spec':30s}  {'PW DPS':>10}  {'HAC DPS':>10}  T=PW/HAC  APL=PW/HAC              Status")
    print(f"  {'-'*30}  {'-'*10}  {'-'*10}  --------  ----------------------  ------")
    for r in all_reports:
        print_short_report(r)

    ok = sum(1 for r in all_reports if r["committed"] and not r["errors"])
    changed = sum(1 for r in all_reports if not r.get("unchanged") and r["committed"])
    err = sum(1 for r in all_reports if r["errors"])
    print(f"\n  {ok} committed ({changed} with changes, {ok-changed} already optimal), {err} errors")


if __name__ == "__main__":
    main()
