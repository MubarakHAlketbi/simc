#!/usr/bin/env python3
"""Compare upstream APLs vs our APLs vs C++ default across ALL specs."""

import subprocess
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

SIMC = "./engine/simc"
ITER = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
RESULTS_DIR = "results/apl_compare_all"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Complete mapping of all APL specs to base profile names
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

# Skip healer specs that have no DPS profile
SKIP_SPECS = {"druid_restoration", "monk_mistweaver"}

def run_sim(profile, apl_file, fight_style, json_out):
    """Run a single sim and return mean DPS. If apl_file is None, use C++ default."""
    cmd = [SIMC, profile]
    if apl_file:
        cmd.append(apl_file)
    cmd += [f"iterations={ITER}", f"fight_style={fight_style}",
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
    """Run 6 sims: upstream PW/HAC, ours PW/HAC, C++ default PW/HAC."""
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
    cpp_pw = run_sim(profile, None, "Patchwerk",
                     f"{RESULTS_DIR}/{apl_spec}_cpp_pw.json")
    
    up_hac = run_sim(profile, upstream, "HecticAddCleave",
                     f"{RESULTS_DIR}/{apl_spec}_up_hac.json")
    ours_hac = run_sim(profile, ours, "HecticAddCleave",
                       f"{RESULTS_DIR}/{apl_spec}_ours_hac.json")
    cpp_hac = run_sim(profile, None, "HecticAddCleave",
                      f"{RESULTS_DIR}/{apl_spec}_cpp_hac.json")
    
    return apl_spec, {
        'up_pw': up_pw, 'ours_pw': ours_pw, 'cpp_pw': cpp_pw,
        'up_hac': up_hac, 'ours_hac': ours_hac, 'cpp_hac': cpp_hac,
        'up_comp': 0.5 * up_pw + 0.5 * up_hac,
        'ours_comp': 0.5 * ours_pw + 0.5 * ours_hac,
        'cpp_comp': 0.5 * cpp_pw + 0.5 * cpp_hac,
    }

def main():
    specs = sorted([s for s in APL_TO_PROFILE if s not in SKIP_SPECS])
    print(f"Testing ALL {len(specs)} specs (3 APL variants x 2 fight styles = 6 sims each)")
    print(f"Total sims: {len(specs)*6} at {ITER} iterations each")
    print(f"APL variants: UPSTREAM (.simc override) | OURS (.simc override) | C++ (engine default)")
    print()
    
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(sim_spec, spec): spec for spec in specs}
        done = 0
        for future in as_completed(futures):
            spec, data = future.result()
            done += 1
            if data is None:
                print(f"  [{done}/{len(specs)}] SKIP {spec} — no profile")
                continue
            results[spec] = data
            best = max(data['up_comp'], data['ours_comp'], data['cpp_comp'])
            tag = ""
            if best == data['up_comp'] and best > 0: tag = "UP"
            elif best == data['ours_comp'] and best > 0: tag = "OURS"
            elif best == data['cpp_comp'] and best > 0: tag = "C++"
            print(f"  [{done}/{len(specs)}] {spec:28s} UP={data['up_comp']:>9.0f}  OURS={data['ours_comp']:>9.0f}  C++={data['cpp_comp']:>9.0f}  best={tag}")
    
    # Summary table
    print()
    print("=" * 155)
    hdr = f"{'SPEC':<28s} {'UP_PW':>9s} {'OURS_PW':>9s} {'C++_PW':>9s} {'UP_HAC':>9s} {'OURS_HAC':>9s} {'C++_HAC':>9s} {'UP_COMP':>9s} {'OURS_COMP':>9s} {'C++_COMP':>9s} {'BEST':>6s} {'Δ vs 2nd':>9s}"
    print(hdr)
    print("-" * 155)
    
    winners = {"UP": 0, "OURS": 0, "C++": 0, "TIE": 0}
    
    for spec in sorted(results.keys()):
        d = results[spec]
        comps = [("UP", d['up_comp']), ("OURS", d['ours_comp']), ("C++", d['cpp_comp'])]
        # Filter out zeros
        valid = [(n, v) for n, v in comps if v > 0]
        if not valid:
            continue
        valid.sort(key=lambda x: -x[1])
        best_name, best_val = valid[0]
        second_val = valid[1][1] if len(valid) > 1 else 0
        
        if second_val > 0:
            delta_pct = (best_val - second_val) / second_val * 100
        else:
            delta_pct = 0
            
        if delta_pct < 0.5:
            winner = "TIE"
            winners["TIE"] += 1
        else:
            winner = best_name
            winners[best_name] += 1
        
        print(f"{spec:<28s} {d['up_pw']:>9.0f} {d['ours_pw']:>9.0f} {d['cpp_pw']:>9.0f} {d['up_hac']:>9.0f} {d['ours_hac']:>9.0f} {d['cpp_hac']:>9.0f} {d['up_comp']:>9.0f} {d['ours_comp']:>9.0f} {d['cpp_comp']:>9.0f} {winner:>6s} {f'+{delta_pct:.1f}%':>9s}")
    
    print("-" * 155)
    print(f"UPSTREAM wins: {winners['UP']}  |  OURS wins: {winners['OURS']}  |  C++ wins: {winners['C++']}  |  TIES: {winners['TIE']}  |  Total: {len(results)}")

if __name__ == "__main__":
    main()
