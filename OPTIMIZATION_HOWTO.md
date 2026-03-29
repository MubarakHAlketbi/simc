# How to Optimize Talents and APL — Step by Step

This guide walks through the exact commands to improve a spec's DPS by
optimizing its talent build and action priority list (APL). Each fight
style (Patchwerk for ST raid, HecticAddCleave for M+/AoE) is optimized
independently — a spec produces TWO optimal builds.

**Related docs:**
- `APL_optimization.md` — APL syntax reference, expression tokens, rules,
  common mistakes. Read this before making manual APL edits.
- `optimization_action_plan.md` — Architecture of the automated optimizer,
  data sources, constraint details, compute estimates.

---

## Prerequisites

```bash
# Build SimC (one time, or after code changes)
cmake -B build -DBUILD_GUI=OFF -DSC_NO_NETWORKING=ON
cmake --build build -j$(nproc)
cp build/simc engine/simc

# Verify build works
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null
```

---

## Step 1: Establish Baseline

Before changing anything, record the current DPS for the spec you want
to optimize. Use 10k+ iterations for reliable numbers.

```bash
# Replace SPEC with the profile name (e.g., MID1_Warrior_Fury)
SPEC=MID1_Warrior_Fury

# Patchwerk baseline (single target, raid)
./engine/simc profiles/MID1/${SPEC}.simc \
  fight_style=Patchwerk target_error=0.1 threads=16 \
  json2=/tmp/${SPEC}_pw_baseline.json output=/dev/null

# HecticAddCleave baseline (M+/AoE)
./engine/simc profiles/MID1/${SPEC}.simc \
  fight_style=HecticAddCleave target_error=0.1 threads=16 \
  json2=/tmp/${SPEC}_hac_baseline.json output=/dev/null

# Read the DPS number
python3 -c "
import json
for style in ['pw', 'hac']:
    with open(f'/tmp/${SPEC}_{style}_baseline.json') as f:
        dps = json.load(f)['sim']['players'][0]['collected_data']['dps']['mean']
    print(f'{style.upper()}: {dps:,.0f} DPS')
"
```

Write these numbers down. Everything below is measured against them.

---

## Step 2: Talent Optimization

Talent builds have the biggest impact. Warrior Fury saw +3.31% from
talent changes vs +0.44% from APL changes. Always do talents first.

### Option A: Automated (recommended)

The hill-climbing optimizer generates valid 1-step mutations from the
current build, sims them through multi-stage filtering, and greedily
accepts improvements. All builds respect tree constraints (point budget,
prerequisites, req_points gates).

```bash
# Single spec, single fight style
python3 scripts/talent_local_search.py \
  --spec warrior_fury --fight-style Patchwerk --max-iter 5

# Single spec, both fight styles
python3 scripts/talent_local_search.py \
  --spec warrior_fury --max-iter 5

# All 33 specs, both fight styles (~8 hours)
python3 scripts/talent_local_search.py --all --max-iter 5
```

The output shows each mutation tested and whether it improved DPS.
If it finds an improvement, it prints the new talent string. Copy it
into the profile's `talents=` line.

After updating talents, validate the build:

```bash
python3 scripts/validate_all_profiles.py
```

This must show 56/56 PASS. If a profile fails, the talent string is
invalid (wrong point budget, missing prerequisites, etc).

### Option B: Manual talent comparison

If you have specific Wowhead builds to test:

```bash
# Get the talent export code from Wowhead talent calculator
# (the base64 string from the URL: wowhead.com/talent-calc/blizzard/CODE)

# Sim with a different talent string
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  talents=NEW_TALENT_STRING_HERE \
  fight_style=Patchwerk iterations=10000 threads=16 \
  json2=/tmp/talent_test.json output=/dev/null

# Compare DPS
python3 -c "
import json
with open('/tmp/talent_test.json') as f:
    dps = json.load(f)['sim']['players'][0]['collected_data']['dps']['mean']
print(f'New build: {dps:,.0f} DPS')
"
```

**Important:** Always validate Wowhead talent strings before using them.
Some Wowhead builds are over-budget (we found Prot Paladin with 35/34
class points). Run the validator:

```bash
python3 -c "
from scripts.lib.talent_validator import TreeConstraints, validate_build, count_points
from scripts.lib.tree_codec_bridge import decode_profile_talents

ts = 'PASTE_TALENT_STRING_HERE'
spec = 'warrior_fury'  # change to your spec

tc = TreeConstraints.build(spec)
sel = decode_profile_talents(ts, spec)
result = validate_build(sel, tc)
cp, sp, hp = count_points(sel, tc)
print(f'class={cp}/34 spec={sp}/34 hero={hp} valid={result.valid}')
for e in result.errors:
    print(f'  ERROR: {e}')
"
```

### Option C: Compare all Wowhead builds for a spec

```bash
python3 scripts/talent_build_compare.py --spec warrior_fury
```

This sims every talent build from `wowhead/warrior/fury/extracted/talents.md`
and picks the best per fight style.

---

## Step 3: APL Optimization

APL optimization adjusts the priority order, thresholds, and routing
of abilities within the current talent build. Gains are smaller than
talent optimization (typically 0-1%) but compound across all specs.

### Option A: Automated (recommended)

```bash
# Single spec, both fight styles
python3 scripts/apl_optimizer.py warrior_fury --max-iter 5

# Single spec, single fight style
python3 scripts/apl_optimizer.py warrior_fury \
  --fight-style Patchwerk --max-iter 5

# All specs
python3 scripts/optimize_all.py --apl --all
```

The optimizer applies 4 mutation types:
1. **Adjacent swap** — swap two neighboring actions in priority
2. **Threshold sweep** — change numeric thresholds in if= conditions
3. **Promote** — move an action higher in priority
4. **Route** — change which sub-list an action belongs to

Each mutation is tested via multi-stage filtering (300→3k→10k iterations).

### Option B: Manual APL editing

Read `APL_optimization.md` first — it covers APL syntax, expression
tokens, and common mistakes.

```bash
# Extract the current APL to a file
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  iterations=0 save_actions=/tmp/current_apl.simc output=/dev/null

# View the APL
cat /tmp/current_apl.simc
```

Edit the profile's `actions=` lines directly. Test each change
individually (never combine multiple changes):

```bash
# Test modified profile
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  fight_style=Patchwerk iterations=10000 threads=16 \
  json2=/tmp/apl_test.json output=/dev/null
```

**Critical rule:** Test changes ONE AT A TIME. Combined changes mask
regressions. In our testing, 7 manual APL changes that each seemed
logical all regressed when combined (-1.52% PW, -0.86% HAC).

### Key APL pitfall: action name gotchas

Some actions don't work as expected (see `APL_optimization.md` §5):
- `ravage` is NOT castable — use `maul,if=buff.ravage.up`
- `thrash_bear` → use `thrash`
- `berserk_bear` → use `berserk`
- Moonfire cannot appear in precombat

---

## Step 4: Verify and Commit

After making changes, always verify:

```bash
# 1. Smoke test (catches parse errors)
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc iterations=1 output=/dev/null

# 2. Validate talent build (catches budget/prerequisite violations)
python3 scripts/validate_all_profiles.py

# 3. Run full baseline at 10k+ iterations to confirm improvement
./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  fight_style=Patchwerk target_error=0.1 threads=16 \
  json2=/tmp/final_pw.json output=/dev/null

./engine/simc profiles/MID1/MID1_Warrior_Fury.simc \
  fight_style=HecticAddCleave target_error=0.1 threads=16 \
  json2=/tmp/final_hac.json output=/dev/null

# 4. Compare against baseline
python3 -c "
import json
for style, tag in [('pw', 'Patchwerk'), ('hac', 'HecticAddCleave')]:
    with open(f'/tmp/MID1_Warrior_Fury_{style}_baseline.json') as f:
        old = json.load(f)['sim']['players'][0]['collected_data']['dps']['mean']
    with open(f'/tmp/final_{style}.json') as f:
        new = json.load(f)['sim']['players'][0]['collected_data']['dps']['mean']
    gain = (new - old) / old * 100
    print(f'{tag:20s} {old:>10,.0f} → {new:>10,.0f}  ({gain:+.2f}%)')
"
```

If DPS improved (or stayed the same) for the optimized fight style:

```bash
git add profiles/MID1/MID1_Warrior_Fury.simc
git commit -m "optimize(warrior_fury): +X.XX% PW via talent swap / APL threshold"
```

---

## Step 5: Full Pipeline (All Specs)

To optimize everything at once:

```bash
# Full report of current baselines
python3 scripts/optimize_all.py --report

# Talent optimization for all specs (both fight styles, ~8 hours)
python3 scripts/talent_local_search.py --all --max-iter 5

# APL optimization for all specs (both fight styles, ~4 hours)
python3 scripts/optimize_all.py --apl --all

# Validate all profiles
python3 scripts/validate_all_profiles.py

# Re-baseline everything
for f in profiles/MID1/MID1_*.simc; do
    base=$(basename "$f" .simc)
    echo "Baselining $base..."
    ./engine/simc "$f" fight_style=Patchwerk target_error=0.1 threads=16 \
      json2=results/phase4/${base}_patchwerk.json output=/dev/null
    ./engine/simc "$f" fight_style=HecticAddCleave target_error=0.1 threads=16 \
      json2=results/phase4/${base}_hecticaddcleave.json output=/dev/null
done

# Final report
python3 scripts/optimize_all.py --report
```

---

## Spec Name Reference

Use these names with `--spec`:

```
warrior_fury, warrior_arms, warrior_protection
mage_arcane, mage_fire, mage_frost
warlock_affliction, warlock_demonology, warlock_destruction
rogue_assassination, rogue_outlaw, rogue_subtlety
hunter_bm, hunter_mm, hunter_survival
dk_blood, dk_frost, dk_unholy
dh_havoc, dh_vengeance, dh_devourer
druid_balance, druid_feral, druid_guardian
paladin_retribution, paladin_protection
priest_shadow
shaman_elemental, shaman_enhancement
monk_brewmaster, monk_windwalker
evoker_devastation, evoker_augmentation
```

---

## Key Lessons from Testing

1. **Talent optimization gives bigger gains than APL changes.**
   Warrior Fury: +3.31% from talents, +0.44% from APL.
   Always optimize talents before APL.

2. **Use 10,000+ iterations for valid comparisons.**
   At 1,000 iterations, noise gives ±0.5% false positives.
   You might "improve" DPS that was just noise.

3. **Test APL changes individually, never combined.**
   We tested 7 manual APL changes for Warrior Fury — each seemed
   logical based on sim reports. All 7 regressed when combined.

4. **Upstream APLs are battle-tested.**
   For specs with imported upstream APLs, manual reordering of
   existing actions almost always regresses. The automated optimizer's
   threshold sweeps are safer.

5. **Validate Wowhead talent exports.**
   Some Wowhead builds are over-budget or reference wrong spec nodes.
   Always run `validate_all_profiles.py` after importing.

6. **Each fight style is independent.**
   A talent swap that improves Patchwerk might hurt HecticAddCleave.
   Each spec produces TWO optimal builds, not one compromise.
