#!/usr/bin/env python3
"""Compare upstream APLs vs our APLs across all specs with differences."""

import subprocess
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

SIMC = "./engine/simc"
ITER = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
RESULTS_DIR = "results/apl_compare"
os.makedirs(RESULTS_DIR, exist_ok=True)

APL_TO_PROFILE = {
    "deathknight_blood": "Death_Knight_Blood",
    "deathknight_frost": "Death_Knight_Frost",
    "deathknight_unholy": "Death_Knight_Unholy",
    "demonhunter_havoc": "Demon_Hunter_Havoc",
    "demonhunter_devourer": "Demon_Hunter_Devourer",
    "demonhunter_vengeance": "Demon_Hunter_Vengeance",
    "druid_balance": "Druid_Balance",
    "druid_feral": "Druid_Feral",
    "druid_guardian": "Druid_Guardian",
    "evoker_augmentation": "Evoker_Augmentation",
    "evoker_devastation": "Evoker_Devastation",
    "hunter_beast_mastery": "Hunter_Beast_Mastery",
    "hunter_marksmanship": "Hunter_Marksmanship",
    "hunter_survival": "Hunter_Survival",
    "mage_arcane": "Mage_Arcane",
    "mage_fire": "Mage_Fire",
    "mage_frost": "Mage_Frost",
    "monk_brewmaster": "Monk_Brewmaster",
    "monk_windwalker": "Monk_Windwalker",
    "paladin_protection": "Paladin_Protection",
    "paladin_retribution": "Paladin_Retribution",
    "priest_shadow": "Priest_Shadow",
    "rogue_assassination": "Rogue_Assassination",
    "rogue_outlaw": "Rogue_Outlaw",
    "rogue_subtlety": "Rogue_Subtlety",
    "shaman_elemental": "Shaman_Elemental",
    "shaman_enhancement": "Shaman_Enhancement",
    "warlock_affliction": "Warlock_Affliction",
    "warlock_demonology": "Warlock_Demonology",
    "warlock_destruction": "Warlock_Destruction",
    "warrior_arms": "Warrior_Arms",
    "warrior_fury": "Warrior_Fury",
    "warrior_protection": "Warrior_Protection",
}

def find_diff_specs():
    """Find specs where APLs actually differ."""
    diff_specs = []
    for apl_spec in APL_TO_PROFILE:
        up = f"ActionPriorityLists/cloned_default/{apl_spec}.simc"
        ours = f"ActionPriorityLists/default/{apl_spec}.simc"
        if os.path.exists(up) and os.path.exists(ours):
            r = subprocess.run(["diff", up, ours], capture_output=True)
            if r.returncode != 0:
                diff_specs.append(apl_spec)
    return sorted(diff_specs)

def run_sim(profile, apl_file, fight_style, json_out):
    """Run a single sim and return mean DPS."""
    cmd = [SIMC, profile, apl_file, 
           f"iterations={ITER}", f"fight_style={fight_style}",
           "desired_targets=1", f"json2={json_out}", "output=/dev/null",
           "threads=4"]
    try:
        subprocess.run(cmd, capture_output=True, timeout=300)
        with open(json_out) as f:
            data = json.load(f)
            return data['sim']['players'][0]['collected_data']['dps']['mean']
    except Exception as e:
        return 0.0

def sim_spec(apl_spec):
    """Run all 4 sims for a spec (upstream PW, ours PW, upstream HAC, ours HAC)."""
    profile_base = APL_TO_PROFILE[apl_spec]
    profile = f"profiles/MID1/MID1_{profile_base}.simc"
    
    if not os.path.exists(profile):
        return apl_spec, None
    
    upstream = f"ActionPriorityLists/cloned_default/{apl_spec}.simc"
    ours = f"ActionPriorityLists/default/{apl_spec}.simc"
    
    up_pw = run_sim(profile, upstream, "Patchwerk", 
                    f"{RESULTS_DIR}/{apl_spec}_up_pw.json")
    ours_pw = run_sim(profile, ours, "Patchwerk",
                      f"{RESULTS_DIR}/{apl_spec}_ours_pw.json")
    up_hac = run_sim(profile, upstream, "HecticAddCleave",
                     f"{RESULTS_DIR}/{apl_spec}_up_hac.json")
    ours_hac = run_sim(profile, ours, "HecticAddCleave",
                       f"{RESULTS_DIR}/{apl_spec}_ours_hac.json")
    
    return apl_spec, {
        'up_pw': up_pw, 'ours_pw': ours_pw,
        'up_hac': up_hac, 'ours_hac': ours_hac,
        'up_comp': 0.5 * up_pw + 0.5 * up_hac,
        'ours_comp': 0.5 * ours_pw + 0.5 * ours_hac,
    }

def main():
    diff_specs = find_diff_specs()
    print(f"Found {len(diff_specs)} specs with APL differences")
    print(f"Running {ITER} iterations per sim, 4 sims per spec = {len(diff_specs)*4} total sims")
    print(f"Using 4 threads per sim, {min(8, len(diff_specs))} parallel specs")
    print()
    
    results = {}
    # Run 8 specs in parallel (each uses 4 threads = 32 total)
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(sim_spec, spec): spec for spec in diff_specs}
        for future in as_completed(futures):
            spec, data = future.result()
            if data is None:
                print(f"  SKIP {spec} — no profile")
                continue
            results[spec] = data
            
            up_c = data['up_comp']
            ours_c = data['ours_comp']
            if up_c > 0:
                delta = (ours_c - up_c) / up_c * 100
            else:
                delta = 0
            
            if abs(delta) < 0.5:
                tag = "TIE"
            elif delta > 0:
                tag = f"OURS +{delta:.1f}%"
            else:
                tag = f"UPSTREAM +{-delta:.1f}%"
            
            print(f"  {spec:28s} UP={up_c:>10.0f}  OURS={ours_c:>10.0f}  {tag}")
    
    # Print summary table
    print()
    print("=" * 120)
    print(f"{'SPEC':<28s} {'UP_PW':>10s} {'OURS_PW':>10s} {'PW_Δ%':>8s} {'UP_HAC':>10s} {'OURS_HAC':>10s} {'HAC_Δ%':>8s} {'UP_COMP':>10s} {'OURS_COMP':>10s} {'WINNER':>12s}")
    print("-" * 120)
    
    up_wins = ours_wins = ties = 0
    
    for spec in sorted(results.keys()):
        d = results[spec]
        pw_delta = ((d['ours_pw'] - d['up_pw']) / d['up_pw'] * 100) if d['up_pw'] > 0 else 0
        hac_delta = ((d['ours_hac'] - d['up_hac']) / d['up_hac'] * 100) if d['up_hac'] > 0 else 0
        comp_delta = ((d['ours_comp'] - d['up_comp']) / d['up_comp'] * 100) if d['up_comp'] > 0 else 0
        
        if abs(comp_delta) < 0.5:
            winner = "TIE"
            ties += 1
        elif comp_delta > 0:
            winner = f"OURS +{comp_delta:.1f}%"
            ours_wins += 1
        else:
            winner = f"UP +{-comp_delta:.1f}%"
            up_wins += 1
        
        print(f"{spec:<28s} {d['up_pw']:>10.0f} {d['ours_pw']:>10.0f} {pw_delta:>+7.1f}% {d['up_hac']:>10.0f} {d['ours_hac']:>10.0f} {hac_delta:>+7.1f}% {d['up_comp']:>10.0f} {d['ours_comp']:>10.0f} {winner:>12s}")
    
    print("-" * 120)
    print(f"UPSTREAM wins: {up_wins}  |  OURS wins: {ours_wins}  |  TIES (<0.5%): {ties}")
    print(f"Total specs compared: {len(results)}")

if __name__ == "__main__":
    main()
