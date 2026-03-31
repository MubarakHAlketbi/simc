# How to Optimize Talents and APL — Step by Step

This guide covers the optimization phase of SimC maintenance. Optimization is
ONE activity among many — see `AGENTS.md` for the full scope (upstream sync,
engine fixes, bug hunting, feature implementation, testing, APL work, profiles).

**Optimization is only meaningful when the engine is correct.** Always complete
Steps 0a-0c below before optimizing. If upstream has pending engine fixes, or
if proc chains / scaling / tier set math haven't been verified, optimization
results will be wrong.

Each fight style (Patchwerk for ST raid, HecticAddCleave for M+/AoE) is
optimized independently — a spec produces TWO optimal builds.

**Related docs:**
- `AGENTS.md` — Full maintenance scope, session workflow, engine verification methods
- `APL_optimization.md` — APL syntax reference, expression tokens, rules, common mistakes
- `optimization_action_plan.md` — Optimizer architecture, data sources, constraints

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

## Step 0: Upstream Sync + Engine Verification (MANDATORY)

**Do this BEFORE any optimization.** Optimization on a broken engine produces
sharper wrong answers. We learned this the hard way — see `FORK_VS_UPSTREAM_REVIEW.md`.

### 0a. Sync upstream

```bash
git fetch upstream midnight
git log --oneline HEAD..upstream/midnight | head -30   # review new commits
git rebase upstream/midnight
cmake --build build -j$(nproc) && cp build/simc engine/simc
python3 scripts/validate_all_profiles.py               # must still pass
```

### 0b. Review upstream changes for the spec you're optimizing

```bash
# What changed in the class module?
git log --oneline upstream/midnight ^HEAD -- engine/class_modules/sc_{class}.cpp
# What changed in the APL generator?
git log --oneline upstream/midnight ^HEAD -- engine/class_modules/apl/apl_{class}.cpp
# What changed in DBC data?
git log --oneline upstream/midnight ^HEAD -- engine/dbc/generated/
```

If upstream has engine fixes for your spec (proc chains, scaling, tier set math),
your previous baselines are INVALID. Re-run Step 1 after syncing.

### 0c. Verify engine correctness for your spec

```bash
CLASS=warrior  # change to your class
SPEC=MID1_Warrior_Fury

# Check for TODOs/FIXMEs
grep -n 'TODO\|FIXME\|HACK' engine/class_modules/sc_${CLASS}.cpp | head -20

# Multi-target sweep (catches AoE scaling bugs invisible to PW+HAC tests)
for N in 1 3 5 10; do
  ./engine/simc profiles/MID1/${SPEC}.simc fight_style=Patchwerk \
    desired_targets=$N iterations=1000 threads=16 \
    json2=/tmp/${SPEC}_${N}t.json output=/dev/null
  python3 -c "
import json
with open('/tmp/${SPEC}_${N}t.json') as f:
    dps = json.load(f)['sim']['players'][0]['collected_data']['dps']['mean']
print(f'  {N} targets: {dps:,.0f} DPS ({dps/$N if $N > 0 else 0:,.0f} per target)')
"
done

# Tier set on/off comparison
./engine/simc profiles/MID1/${SPEC}.simc iterations=3000 threads=16 \
  json2=/tmp/${SPEC}_tier_on.json output=/dev/null
./engine/simc profiles/MID1/${SPEC}.simc iterations=3000 threads=16 \
  set_bonus=tier33_2pc=0 set_bonus=tier33_4pc=0 \
  json2=/tmp/${SPEC}_tier_off.json output=/dev/null
```

If per-target DPS scales suspiciously (e.g., ST ability damage doubles at 2 targets)
or tier set provides 0% gain, there's likely an engine bug. Check upstream first.

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

## Profile File Convention

Each spec produces TWO independent optimal profiles with distinct talent
builds and APLs — one for Patchwerk (ST raid), one for HecticAddCleave (M+/AoE).

### Naming Rules

| File | Purpose |
|------|---------|
| `MID1_{Class}_{Spec}.simc` | PW-optimized (default — raid/ST) |
| `MID1_{Class}_{Spec}_HAC.simc` | HAC-optimized (M+/AoE) |

Variant profiles (hero talent alternatives) follow the same pattern:

| File | Purpose |
|------|---------|
| `MID1_{Class}_{Spec}_{Variant}.simc` | PW-optimized variant |
| `MID1_{Class}_{Spec}_{Variant}_HAC.simc` | HAC-optimized variant |

### Rules

1. **Every optimized spec gets BOTH files.** The base `.simc` is PW-optimized,
   the `_HAC.simc` copy has the HAC-optimized talent string and APL.
2. **Tank specs skip HAC** — they only produce PW profiles (no `_HAC.simc`).
3. **_HAC profiles are full copies**, not references. They duplicate gear,
   consumables, and other non-talent lines so they can be simmed standalone.
4. **Variant profiles get _HAC too** if their talent/APL differs between
   fight styles. If PW and HAC produce the same talent string, skip _HAC.
5. **Profile count grows** as optimization proceeds. Track total via
   `ls profiles/MID1/*.simc | wc -l` and `python3 scripts/validate_all_profiles.py`.
6. **optimize_spec.py automates this** — it creates both files, applies the
   right talent string to each, and runs APL optimization independently.

### Example: DK Unholy (first spec fully optimized)

```
MID1_Death_Knight_Unholy.simc       → PW talents (107,884 DPS)
MID1_Death_Knight_Unholy_HAC.simc   → HAC talents (236,310 DPS)
MID1_Death_Knight_Unholy_San'layn.simc → variant (not yet optimized)
```

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

0. **Sync upstream BEFORE optimizing. Engine correctness > optimization.**
   We spent 331 commits optimizing APLs and talents while upstream fixed
   181 commits of engine bugs (proc chains, segfaults, scaling formulas,
   tier set math). Our baselines were precise measurements of INCORRECT
   simulations. The Enhancement 4PC mastery bug halved the value — every
   Enhancement optimization result was based on wrong numbers.
   See `FORK_VS_UPSTREAM_REVIEW.md` for the full post-mortem.

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

7. **SimC is lenient, the game is strict about talent gates.**
   SimC accepts any talent string that passes its parser. The game client
   enforces req_points gates using a currency system — only PURCHASED nodes
   (not granted) count toward gate thresholds. Always verify talent strings
   import into the actual game client, not just SimC.

8. **Granted nodes don't count toward gates.**
   Classes with granted talents (Warrior: 2, Druid/Paladin: 3) effectively
   have fewer points to meet higher gates. For Warrior (2 granted), the
   game sees 32 purchasable class points, and 23 must be spent before the
   second gate — leaving only 9 for the final tier. The optimizer must
   respect this tighter budget.

9. **"Implemented" ≠ "correct". "Non-zero DPS" ≠ "correct DPS".**
   Our tier set audit declared "33/33 implemented" based on DBC entry
   existence and non-zero baselines. But the Enhancement 4PC was implemented
   with the WRONG mastery value. A baseline is a MEASUREMENT, not a
   VALIDATION. Always verify behavior (mechanic + numeric values) against
   tooltips, not just existence.

10. **APL optimization is the 10% above water. Engine code is the 90% below.**
    Our APL optimizer has 4 mutation types, multi-stage filtering, and
    multi-target evaluation. But it cannot detect that a proc chain is
    broken, a scaling formula is wrong, or a timer is missing. C++ code
    review and upstream sync are the only ways to catch engine-layer bugs.
