#!/bin/bash
# APL Comparison: upstream (cloned_default) vs ours (default)
# Runs both APLs on each profile and compares DPS
# Usage: bash scripts/apl_compare.sh [iterations]

set -e
cd "$(dirname "$0")/.."

ITER=${1:-1000}
SIMC="./engine/simc"
RESULTS_DIR="results/apl_compare"
mkdir -p "$RESULTS_DIR"

# Mapping: apl_spec_name -> profile_base_name (without MID1_ prefix)
declare -A APL_TO_PROFILE=(
  ["deathknight_blood"]="Death_Knight_Blood"
  ["deathknight_frost"]="Death_Knight_Frost"
  ["deathknight_unholy"]="Death_Knight_Unholy"
  ["demonhunter_havoc"]="Demon_Hunter_Havoc"
  ["demonhunter_devourer"]="Demon_Hunter_Devourer"
  ["demonhunter_vengeance"]="Demon_Hunter_Vengeance"
  ["druid_balance"]="Druid_Balance"
  ["druid_feral"]="Druid_Feral"
  ["druid_guardian"]="Druid_Guardian"
  ["evoker_augmentation"]="Evoker_Augmentation"
  ["evoker_devastation"]="Evoker_Devastation"
  ["hunter_beast_mastery"]="Hunter_Beast_Mastery"
  ["hunter_marksmanship"]="Hunter_Marksmanship"
  ["hunter_survival"]="Hunter_Survival"
  ["mage_arcane"]="Mage_Arcane"
  ["mage_fire"]="Mage_Fire"
  ["mage_frost"]="Mage_Frost"
  ["monk_brewmaster"]="Monk_Brewmaster"
  ["monk_windwalker"]="Monk_Windwalker"
  ["paladin_protection"]="Paladin_Protection"
  ["paladin_retribution"]="Paladin_Retribution"
  ["priest_shadow"]="Priest_Shadow"
  ["rogue_assassination"]="Rogue_Assassination"
  ["rogue_outlaw"]="Rogue_Outlaw"
  ["rogue_subtlety"]="Rogue_Subtlety"
  ["shaman_elemental"]="Shaman_Elemental"
  ["shaman_enhancement"]="Shaman_Enhancement"
  ["warlock_affliction"]="Warlock_Affliction"
  ["warlock_demonology"]="Warlock_Demonology"
  ["warlock_destruction"]="Warlock_Destruction"
  ["warrior_arms"]="Warrior_Arms"
  ["warrior_fury"]="Warrior_Fury"
  ["warrior_protection"]="Warrior_Protection"
)

# Find specs that actually differ
DIFF_SPECS=()
for apl_spec in "${!APL_TO_PROFILE[@]}"; do
  apl_file="ActionPriorityLists/cloned_default/${apl_spec}.simc"
  our_file="ActionPriorityLists/default/${apl_spec}.simc"
  if [ -f "$apl_file" ] && [ -f "$our_file" ]; then
    lines=$(diff "$apl_file" "$our_file" 2>/dev/null | wc -l)
    if [ "$lines" -gt "0" ]; then
      DIFF_SPECS+=("$apl_spec")
    fi
  fi
done

echo "=============================================="
echo "APL COMPARISON: Upstream vs Ours"
echo "Iterations: $ITER per sim (x2 fight styles)"
echo "Specs with differences: ${#DIFF_SPECS[@]}"
echo "=============================================="
echo ""

# Results array
declare -A UPSTREAM_PW UPSTREAM_HAC OURS_PW OURS_HAC

run_sim() {
  local profile="$1"
  local apl_override="$2"
  local fight_style="$3"
  local output_json="$4"
  
  local cmd="$SIMC \"$profile\" iterations=$ITER fight_style=$fight_style desired_targets=1 json2=$output_json output=/dev/null"
  if [ -n "$apl_override" ]; then
    cmd="$cmd \"$apl_override\""
  fi
  
  eval $cmd 2>/dev/null
  
  # Extract DPS from JSON
  python3 -c "
import json, sys
with open('$output_json') as f:
    data = json.load(f)
    dps = data['sim']['players'][0]['collected_data']['dps']['mean']
    print(f'{dps:.1f}')
" 2>/dev/null
}

printf "%-28s %12s %12s %12s %12s %12s %8s\n" \
  "SPEC" "UP_PW" "OURS_PW" "UP_HAC" "OURS_HAC" "UP_COMP" "WINNER"
printf "%-28s %12s %12s %12s %12s %12s %8s\n" \
  "---" "---" "---" "---" "---" "---" "---"

TOTAL_UP=0
TOTAL_OURS=0
UP_WINS=0
OURS_WINS=0
TIES=0

for apl_spec in $(echo "${DIFF_SPECS[@]}" | tr ' ' '\n' | sort); do
  profile_base="${APL_TO_PROFILE[$apl_spec]}"
  profile="profiles/MID1/MID1_${profile_base}.simc"
  
  if [ ! -f "$profile" ]; then
    echo "SKIP $apl_spec — no profile $profile"
    continue
  fi
  
  upstream_apl="ActionPriorityLists/cloned_default/${apl_spec}.simc"
  ours_apl="ActionPriorityLists/default/${apl_spec}.simc"
  
  # Run all 4 sims
  up_pw=$(run_sim "$profile" "$upstream_apl" "Patchwerk" "$RESULTS_DIR/${apl_spec}_upstream_pw.json")
  ours_pw=$(run_sim "$profile" "$ours_apl" "Patchwerk" "$RESULTS_DIR/${apl_spec}_ours_pw.json")
  up_hac=$(run_sim "$profile" "$upstream_apl" "HecticAddCleave" "$RESULTS_DIR/${apl_spec}_upstream_hac.json")
  ours_hac=$(run_sim "$profile" "$ours_apl" "HecticAddCleave" "$RESULTS_DIR/${apl_spec}_ours_hac.json")
  
  # Calculate composites
  up_comp=$(python3 -c "print(f'{0.5*${up_pw:-0}+0.5*${up_hac:-0}:.1f}')")
  ours_comp=$(python3 -c "print(f'{0.5*${ours_pw:-0}+0.5*${ours_hac:-0}:.1f}')")
  
  # Determine winner
  winner=$(python3 -c "
up=$up_comp; ours=$ours_comp
diff_pct = (ours - up) / up * 100 if up > 0 else 0
if abs(diff_pct) < 0.5: print('TIE')
elif ours > up: print(f'OURS +{diff_pct:.1f}%')
else: print(f'UP +{-diff_pct:.1f}%')
")
  
  printf "%-28s %12s %12s %12s %12s %12s %s\n" \
    "$apl_spec" "$up_pw" "$ours_pw" "$up_hac" "$ours_hac" "$up_comp/$ours_comp" "$winner"
done

echo ""
echo "=============================================="
echo "DONE"
echo "=============================================="
