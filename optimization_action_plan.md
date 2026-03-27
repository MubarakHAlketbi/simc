# Optimization System — Full Action Plan

Generated: 2026-03-27
Based on: `apl_optimizer_plan.md` + `talent_engine_design.md`

## Overview

A unified system to find the best talent build AND the best APL for every
spec. Two engines (talent + APL) work in sequence, with shared infrastructure.

**Total estimated effort:** ~18 hours implementation + ~8 hours compute
**Deliverables:** Optimized profiles for all 33 specs with validated talent
builds and APLs, plus reusable automation tooling for future patches.

---

## Prerequisites (before starting)

These must be true before optimization work begins:

- [x] 56/56 profiles compile and sim (DONE)
- [x] 112/112 Phase 4 baselines exist (DONE)
- [x] Guardian Druid APL fixed (DONE 2026-03-27)
- [x] All 8 upstream APL fixes applied (DONE)
- [x] Wowhead extraction pipeline working (DONE, 33/33 specs)
- [ ] Phase 4b: re-run gen_apl_diff.py with fresh data (10 min)

---

## Milestone 1: Shared Infrastructure
**Estimate: 3 hours | Priority: CRITICAL | Blocks everything**

All subsequent milestones depend on this core plumbing.

### Task 1.1 — SimC Runner Module
**File:** `scripts/lib/sim_runner.py`

A reusable Python module that runs SimC sims and parses results.

```
Inputs:  profile path, optional overrides (talents=, actions=), 
         fight_style, iterations, threads
Output:  SimResult(dps_mean, dps_error, action_breakdown, fight_style)
```

Capabilities:
- Write temp .simc override files (input= + overrides)
- Run simc binary, parse JSON2 output
- Parallel execution (asyncio subprocess pool, configurable concurrency)
- Composite DPS scoring (50% PW + 50% HAC)
- Acceptance logic (composite improves, no fight style regresses >1%)

Acceptance test: Run Warrior Fury with default APL vs a deliberately
worse APL override, verify DPS difference matches expectations.

### Task 1.2 — APL Parser/Serializer
**File:** `scripts/lib/apl_parser.py`

Parse .simc APL text into structured data, serialize back to text.

```
Input:   raw .simc text (from save_actions or .simc file)
Output:  APL object (dict of action lists, each a list of APLAction)
```

Capabilities:
- Parse actions.{list}+=/action,if=condition,key=value format
- Preserve ordering within each sub-list
- Deep copy for mutation
- Serialize back to valid .simc text
- Extract all talent/buff/debuff references from conditions

Acceptance test: Parse a saved APL, serialize it, run both — DPS identical.

### Task 1.3 — Talent String Codec
**File:** `scripts/lib/talent_codec.py`

Decode and encode SimC base64 talent strings.

```
Input:   base64 talent string + spec info
Output:  dict of {node_id: (rank, choice_index)}
```

Capabilities:
- Decode: base64 → node selections (matching SimC's bit layout exactly)
- Encode: node selections → base64 (with zero-filled tree hash)
- Must replicate SimC's `generate_tree_nodes` node ordering
- Round-trip validation: decode(encode(decode(s))) == decode(s)

Acceptance test: Decode an existing profile's talent string, re-encode,
run sim — DPS identical to original.

### Task 1.4 — DBC Tree Extractor
**File:** `scripts/lib/talent_tree.py`

Build the talent tree graph from SimC's DBC data.

```
Input:   spec name
Output:  TalentTree object (nodes, edges, constraints)
```

Approach options (try in order):
1. Parse `engine/dbc/generated/trait_data.inc` directly (static data)
2. Run SimC in debug mode and capture tree node dump
3. Write a minimal C++ tool that queries trait_data_t::data()

Capabilities:
- Build TalentTree with all nodes, types, prerequisites, spell IDs
- Resolve prerequisite edges (point gates + direct pathing)
- Identify hero tree options per spec
- Map spell_id → tokenized SimC name

Acceptance test: Build tree for Warrior Fury, verify it has ~70 nodes,
verify known talents (Rampage, Bloodthirst, etc.) appear with correct data.

---

## Milestone 2: Node Classification Engine
**Estimate: 2 hours | Priority: HIGH | Blocks Milestones 4-5**

### Task 2.1 — APL Talent Reference Scanner
**File:** `scripts/lib/node_classifier.py`

Scan saved APL text for all `talent.X` references.

```
Input:   APL text (from save_actions)
Output:  set of talent names referenced
```

Method: regex scan for `talent.{name}` patterns in if= conditions
and action names.

### Task 2.2 — Spell Effect Scanner

Check each talent's spell_data for DPS-relevant effects.

```
Input:   TalentTree
Output:  set of node_ids with damage/stat effects
```

Method: Use SimC's spell_query or parse DBC effect data for:
- A_SCHOOL_DAMAGE, A_WEAPON_DAMAGE (direct damage)
- A_ADD_PCT_MODIFIER on damage amounts
- A_MOD_STAT, A_MOD_RATING (stat buffs)
- A_ADD_PCT_LABEL_MODIFIER (label-based damage mods)
- Proc effects that trigger damage spells
- Resource generation/cost reduction (indirect DPS)
- Cooldown reduction effects

### Task 2.3 — Combined Classifier

Merge all sources and classify: DPS / GATING / UTILITY.

```
Input:   TalentTree + APL text + class module code
Output:  TalentTree with dps_relevance set on all nodes
```

Additional logic:
- GATING: utility nodes required to path to a DPS node
- Pivot detection: choice nodes, ability-granting nodes, APL-routing nodes
- Per-spec classification report (human-readable .md)

### Task 2.4 — Validation

Spot-check 3 specs manually:
- Warrior Fury: verify Rampage, Bladestorm, Odyn's Fury = DPS
- Rogue Assassination: verify Mutilate, Garrote = DPS; Cloak = UTILITY
- Mage Frost: verify Glacial Spike, Icy Veins = DPS

Fix any misclassifications, tune heuristics.

---

## Milestone 3: APL Optimization Engine
**Estimate: 3 hours | Priority: HIGH | Independent of Milestones 4-5**

### Task 3.1 — Mutation Generators
**File:** `scripts/lib/apl_mutations.py`

Six mutation operators:

| ID | Mutation | Description |
|----|----------|-------------|
| M1 | Adjacent Swap | Swap two adjacent actions in same sub-list |
| M2 | Condition Tightening | Add condition to unconditional action |
| M3 | Condition Loosening | Remove/simplify a condition clause |
| M4 | Threshold Sweep | Vary numeric thresholds ±30% |
| M5 | Promotion/Demotion | Move action up/down N positions |
| M6 | Sub-list Routing | Change AoE breakpoint or list entry condition |

Each generator takes an APL + action_breakdown ranking and yields
candidate (APL, mutation_description) pairs.

### Task 3.2 — Multi-Stage Evaluation Pipeline
**File:** `scripts/lib/evaluator.py`

Three-stage filtering to reduce sim cost:

| Stage | Iterations | Purpose | Keep |
|-------|-----------|---------|------|
| 1 | 100 | Coarse filter all candidates | Top 20% or top 10 |
| 2 | 1,000 | Medium filter survivors | >0.3% improvement |
| 3 | 10,000 | Confirm top 3 | Best with regression check |

### Task 3.3 — Optimization Loop Controller
**File:** `scripts/apl_optimizer.py`

Main loop: baseline → generate → evaluate → accept → converge.

Features:
- Checkpoint/resume (saves state per iteration)
- Per-spec timeout (max 10 iterations)
- Convergence: stop when <0.1% improvement
- Report generation per spec

### Task 3.4 — Smoke Test

Run on Warrior Fury (well-understood APL, fast sims):
- Verify loop completes in ~10 min
- Verify accepted mutations are sensible
- Verify no regression in either fight style
- Verify output APL is valid and sims correctly

---

## Milestone 4: Talent Permutation Engine
**Estimate: 3 hours | Priority: HIGH | Depends on Milestones 1-2**

### Task 4.1 — Pivot Node Identifier
**File:** `scripts/lib/talent_permute.py`

Classify DPS nodes into PIVOT (rotation-changing) vs TUNING (% modifier).

Heuristics:
- Choice nodes = always PIVOT
- Nodes with replace_spell_id != 0 = PIVOT (grants/replaces ability)
- Nodes referenced in APL call_action_list routing = PIVOT
- Nodes with only A_ADD_PCT_MODIFIER effects = TUNING
- Everything else = TUNING by default

### Task 4.2 — Constraint-Aware Build Generator

Backtracking generator that produces valid talent builds:
- Respects point budgets per tree (class ~31, spec ~30)
- Respects row gates (req_points)
- Respects direct prerequisite edges
- Handles choice exclusivity
- Fixes utility nodes to current values
- Fixes gating nodes to required values

### Task 4.3 — Two-Phase Search

Phase 1 — Pivot Sweep:
- Fix tuning nodes to Wowhead defaults
- Enumerate all valid pivot combinations (~100-500 per spec)
- Sim each at 200 iterations × 2 fight styles
- Keep top 10

Phase 2 — Tuning Sweep:
- Per winning pivot combo, hill-climb tuning nodes
- Toggle one tuning node at a time, keep if DPS improves
- Sim at 1000 iterations
- Confirm winner at 10,000 iterations

### Task 4.4 — DPS Fingerprint Cache

Before simming any build, compute DPS-fingerprint (hash of only
DPS+GATING node selections). Skip if fingerprint already simmed.

### Task 4.5 — Smoke Test

Run on Warrior Fury:
- Verify tree extraction produces ~70 nodes
- Verify classification: ~20 DPS, ~5 GATING, ~45 UTILITY
- Verify generated builds are all valid (iterations=0 test)
- Verify pivot sweep finds ~200 combinations
- Verify best build DPS >= Wowhead #1 build DPS
- Total runtime < 15 minutes

---

## Milestone 5: Wowhead Build Comparison (Quick Win)
**Estimate: 1 hour | Priority: MEDIUM | Depends on Milestone 1**

### Task 5.1 — Build Extractor
**File:** `scripts/talent_build_compare.py`

Parse all `wowhead/{class}/{spec}/extracted/talents.json` files.
Extract: hero path, build name/description, talent string.

### Task 5.2 — Batch Sim Runner

For each spec:
- Load all Wowhead builds (4-16 per spec)
- Sim each with default APL at 1,000 iterations × 2 fight styles
- Compute composite DPS
- Rank builds

### Task 5.3 — Report

Output per spec:
```
Warrior Fury (12 builds):
  #1  Slayer Build 1       PW: 87,400  HAC: 145,200  Comp: 116,300  [CURRENT]
  #2  Slayer Build 4       PW: 86,900  HAC: 146,800  Comp: 116,850  +0.5%
  #3  Mountain Thane B2    PW: 83,100  HAC: 151,400  Comp: 117,250  +0.8%
  ...
```

This is the fastest win — tells us immediately if current profile
talent strings are optimal, before any permutation search.

**Total: 262 builds × 2 fight styles × 1k iter ≈ 9 minutes all specs.**

---

## Milestone 6: Full Integration Run
**Estimate: 2 hours coding + 8 hours compute | Priority: MEDIUM**

### Task 6.1 — Master Orchestrator
**File:** `scripts/optimize_all.py`

Runs the full pipeline for all 33 specs:

```
For each spec:
  Step 1: Wowhead build comparison (Task 5.2)
          → identify best Wowhead build
          
  Step 2: Talent engine pivot sweep (Task 4.3 Phase 1)
          → identify best pivot combination
          
  Step 3: Talent engine tuning sweep (Task 4.3 Phase 2)
          → refine best build
          
  Step 4: APL optimization (Task 3.3)
          → optimize APL for winning talent build
          
  Step 5: Cross-validation
          → sim winning APL × top 3 talent builds
          → sim winning build × current APL (before optimization)
          → verify improvement is from talent AND APL combined
          
  Step 6: If APLs differ between builds → merge with talent gates
```

### Task 6.2 — Parallel Execution

Run 4 specs concurrently (each uses 8 threads for SimC):
- 33 specs / 4 parallel = ~8 batches
- ~1 hour per batch (talent sweep + APL optimization)
- Total: ~8 hours compute

### Task 6.3 — Profile Updates

For each spec where improvement > 0.5%:
- Update `talents=` in MID1 profile
- Update APL in `ActionPriorityLists/default/` if changed
- Create hero-variant profiles if second hero path is >2% different
- Re-run baselines (Patchwerk + HecticAddCleave at target_error=0.1)

### Task 6.4 — Final Validation Matrix

```
For each spec:
  For each Wowhead build (all 4-16):
    For each fight style (PW, HAC):
      Sim at 10,000 iterations
      
  Assert: no build regresses >2% vs pre-optimization
  Assert: best build improved or within 0.1%
  Assert: average across builds improved
```

### Task 6.5 — Summary Report

```
results/optimization/summary.md

Spec                    | Before  | After   | Δ     | Source
Warrior Fury            | 116,300 | 118,900 | +2.2% | talent + APL
Rogue Assassination     |  13,400 |  58,200 | +334% | talent (was broken)
Druid Balance           |  11,200 |  45,600 | +307% | talent (was wrong)
...
Total average           |  XX,XXX |  XX,XXX | +X.X%
```

---

## Milestone 7: Documentation and Skill Save
**Estimate: 1 hour | Priority: LOW**

### Task 7.1 — Update project_progress.md
- Phase 4d status → COMPLETE
- New baseline numbers
- Per-spec improvements

### Task 7.2 — Save as Hermes Skill
- Save the optimization workflow as a reusable skill
- Includes: how to re-run after patch changes, common pitfalls

### Task 7.3 — Update APL_optimization.md
- Section 13 tooling checklist → mark completed items
- Add talent engine documentation

---

## Execution Schedule

| Day | Milestones | Hours | Output |
|-----|-----------|-------|--------|
| 1 | M1 (infrastructure) + M5 (Wowhead compare) | 4h code + 10min compute | SimC runner, APL parser, talent codec, build comparison for all 33 specs |
| 2 | M2 (classification) + M3 (APL optimizer) | 5h code + 30min testing | Node classifier, 6 mutation operators, multi-stage evaluator, loop controller |
| 3 | M4 (talent permutation) | 3h code + 30min testing | Pivot/tuning split, constraint generator, two-phase search |
| 4 | M6 (full run) | 2h code + 8h compute | All 33 specs optimized, profiles updated, baselines re-run |
| 5 | M7 (docs) + fixes | 1h + buffer | Progress doc, skill save, any regressions fixed |

**Total: ~15h coding + ~9h compute = 4-5 working days**

---

## File Structure

```
scripts/
  lib/
    __init__.py
    sim_runner.py          # M1.1 — run sims, parse JSON
    apl_parser.py          # M1.2 — parse/serialize APLs
    talent_codec.py        # M1.3 — encode/decode talent strings
    talent_tree.py         # M1.4 — build tree from DBC
    node_classifier.py     # M2.1-2.3 — classify DPS/GATING/UTILITY
    apl_mutations.py       # M3.1 — 6 mutation operators
    evaluator.py           # M3.2 — multi-stage sim evaluation
    talent_permute.py      # M4.1-4.4 — pivot/tuning search
  apl_optimizer.py         # M3.3 — APL optimization loop
  talent_engine.py         # M4 entry point
  talent_build_compare.py  # M5 — Wowhead build comparison
  optimize_all.py          # M6 — master orchestrator

results/
  optimization/
    {spec}/
      tree.json
      classification.md
      wowhead_comparison.md
      pivot_sweep.json
      tuning_sweep.json
      apl_iterations/
      best_build.txt
      best_apl.simc
      report.md
    summary.md
    checkpoint.json
```

---

## Success Criteria

1. **All 33 specs have a validated best talent build** with composite DPS
   >= best Wowhead build (or within 0.3% if Wowhead is already optimal)

2. **All 33 specs have an optimized APL** for their best build, with
   composite DPS >= current APL (or within 0.1% if already optimal)

3. **No regression**: no spec's DPS drops >1% on any fight style vs
   current baselines

4. **Automation**: the full pipeline can be re-run with a single command
   (`python3 scripts/optimize_all.py`) after any patch/data update

5. **56/56 profiles still pass** compilation and smoke tests after updates
