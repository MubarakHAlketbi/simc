# Optimization Action Plan

Updated: 2026-03-31 — v0.3 full pass complete (33/33 specs)

## Context

This document covers the optimization phase of SimC maintenance. Optimization is
ONE activity among many — see `AGENTS.md` for the full scope (upstream sync,
engine fixes, bug hunting, feature implementation, testing, APL work, profiles).

**Optimization is only meaningful when the engine is correct.** Before running
any optimization:

1. **Upstream is synced** — no pending engine fixes or DBC updates
2. **Engine is verified** — proc chains, scaling formulas, tier set math checked
3. **Baselines are fresh** — reflect current engine state

Our 2026-03-29 review found 181 upstream commits missing, including proc chain
fixes, scaling bugs, tier set math errors, crash fixes, and event sequencing bugs.
All optimization results from before the upstream sync are PROVISIONAL.
See `FORK_VS_UPSTREAM_REVIEW.md`.

---

## Architecture

Three phases per spec, in strict order:

```
PHASE 0: ENGINE VERIFICATION         PHASE 1: TALENT OPT           PHASE 2: APL OPT
  Upstream sync                        Wowhead seeds                  Extract current APL
       |                                    |                              |
  Rebuild + re-validate                Screen at 1k iter             Generate mutations
       |                                    |                              |
  C++ code review (proc chains)        Local search (swaps)          Multi-stage eval
       |                                    |                              |
  Multi-target sweep                   Hill-climb                    Accept best
       |                                    |                              |
  Tier set value check                 Confirm at 10k iter           Confirm at 10k iter
```

Each spec produces TWO independent optimal talent/APL builds — one for Patchwerk, one for HecticAddCleave.
File convention: `<Base>.simc` = PW-optimized, `<Base>_HAC.simc` = HAC-optimized.
All specs get both profiles, including tanks. See `OPTIMIZATION_HOWTO.md` § "Profile File Convention" for details.

---

## Phase 0 — Engine Verification (NEW — added 2026-03-31)

Before optimizing a spec, verify the engine is correct for that spec:

| Check | How | What It Catches |
|-------|-----|-----------------|
| Upstream sync | `git fetch upstream && git log HEAD..upstream/midnight` | All engine-layer fixes |
| C++ TODO/FIXME | `grep -n 'TODO\|FIXME' sc_{class}.cpp` | Known incomplete implementations |
| Multi-target sweep | Sim at 1,3,5,10 targets, compare per-target DPS | AoE scaling bugs (Void Ray) |
| Tier set delta | Sim with/without tier, compare vs tooltip | Tier math errors (Enh 4PC halving) |
| Proc rate check | Compare JSON proc counts vs expected RPPM/ICD | Broken proc chains (Star Cascade) |

**If any check fails, fix the engine BEFORE optimizing.** Optimizing on broken
simulation math produces sharper wrong answers.

---

## Phase 1 — Talent Optimization

Two independent optimization loops per spec, each producing results per fight style.

---

## Talent Optimization — Real Edges + Validated Neighbors

### Data Sources

| Data | Source | Details |
|------|--------|---------|
| Node definitions | `engine/dbc/generated/trait_data.inc` | 3,420 entries, build 12.0.1.66384 |
| Prerequisite edges | `engine/dbc/generated/TraitEdge.csv` | 6,409 Type 2 edges (class/spec/hero) |
| Edge origin | DB2 `TraitEdge` table via wago.tools | Build 12.0.1.66384 (release) |

Old heuristic edges (row-adjacency, col-distance ≤ 1) had 77.7% precision, 90.1% recall.
Replaced with real DB2 edges. 40 nodes have no edges (33 apex row-11, row-1 roots) — use req_points gates only.

### Constraints (enforced by `talent_validator.py`)

| Constraint | Rule |
|------------|------|
| Class budget | ≤ 34 purchased points (granted nodes free) |
| Spec budget | ≤ 34 purchased points |
| Hero tree | Auto-granted (15 points), one tree selected |
| req_points | Node requires N total points in sub-tree before unlocking |
| Prerequisites | At least 1 parent must be selected (real TraitEdge.csv edges) |
| Choice nodes | Exactly 1 option selected |
| Granted nodes | Auto-detected via id_spec_starter + undocumented grants (warlock Soul Leech) |

### Granted Class Talents

Not all specs have 1 free talent. Actual counts:

| Grants | Specs |
|--------|-------|
| 0 | Warlock (Soul Leech undocumented, hardcoded in validator) |
| 1 | DH, DK, Hunter, Mage, Rogue, Shaman (18 specs) |
| 2 | Evoker, Monk, Priest, Warrior (13 specs) |
| 3 | Druid, Paladin (10 specs) |

### Hero Tree Handling

Hero trees are shared between 2 specs. Key discoveries:
- Internal hero nodes may have id_spec tagging for only one spec (Scalecommander nodes tagged Devastation-only, but Aug can use them)
- SimC's parser skips spec validation for hero talents (player.cpp ~line 2929)
- Selection nodes identify available sub-trees (fixes Evoker Aug + Chronowarden which has no Aug-tagged starting node)
- Each hero tree has 2 different row-1 starting nodes (one per spec), rest are shared

### Search Pipeline

**Phase 1 — Seed Screening** (`talent_build_compare.py`):
- Sim all Wowhead builds (4-16 per spec) at 1000 iter × both fight styles
- Rank per fight style independently, pick top 3 seeds

**Phase 2 — Neighborhood Generation** (`talent_validator.py :: generate_neighbors()`):

| Mutation | Description | Count (Fury) |
|----------|-------------|-------------|
| SWAP_CLASS | Remove class leaf + add eligible class node | ~100 |
| SWAP_SPEC | Remove spec leaf + add eligible spec node | ~100 |
| CHOICE_SWAP | Switch a choice node to its other option | ~9 |
| RANK_CHANGE | Adjust tiered node rank up or down | ~1 |
| **Total** | | **~216** |

All neighbors are valid by construction — budget, prerequisites, and req_points checked during generation.

**Phase 3 — Hill-Climb** (`talent_local_search.py`):
- Per seed: generate neighbors → Stage 1 (300 iter) → Stage 2 (3k iter) → Stage 3 (10k iter)
- Accept best improvement, repeat until no gain
- Typically converges in 1-2 passes

### Test Results — Warrior Fury (2026-03-29)

| Style | Baseline | Optimized | Gain | Passes | Key Finding |
|-------|----------|-----------|------|--------|-------------|
| Patchwerk | 86,897 | 89,777 | +3.31% | 2 | -Reckless Abandon +Wrath and Fury, -Pain and Gain +Stance Mastery |

---

## APL Optimization — Mutation + Multi-Stage

Implemented in `apl_optimizer.py`. Per fight style:

1. Extract current APL via `save_actions`
2. Generate mutations: adjacent swap, threshold sweep, routing changes
3. Three-stage funnel: 300 iter → 3,000 iter → 10,000 iter
4. Accept if DPS improves for that fight style

### Test Results — Warrior Fury (2026-03-28)

| Style | Result | Detail |
|-------|--------|--------|
| Patchwerk | +0.00% | Converged immediately — APL already optimal |
| HecticAddCleave | +0.44% | Rampage threshold 100→80 in thane_aoe |

Manual APL changes all regressed. Upstream APLs are at their ceiling for well-tuned specs.

---

## Files

### Active Pipeline

| Script | Purpose |
|--------|---------|
| `scripts/lib/sim_runner.py` | SimC runner, JSON parse, scoring; AbilityStats/BuffStats/ResourceStats |
| `scripts/lib/apl_parser.py` | APL parse/serialize; insert_action, replace_condition, make_action |
| `scripts/lib/apl_mutations.py` | Layer 1 blind mutation operators: swap, sweep, promote, route |
| `scripts/lib/apl_signal_extractor.py` | Layer 2: APS inversion, buff waste, resource overcap, interval gap signals |
| `scripts/lib/apl_signal_mutations.py` | Layer 2: targeted mutations from signals (S-M1 through S-M4) |
| `scripts/lib/llm_apl_advisor.py` | Layer 3: LLM prompt builder, CHANGE block parser, APL converter |
| `scripts/lib/talent_tree.py` | DBC tree parser + real TraitEdge.csv edges |
| `scripts/lib/talent_codec.py` | Base64 talent string encode/decode |
| `scripts/lib/tree_codec_bridge.py` | Tree↔codec bridge |
| `scripts/lib/talent_validator.py` | Build validation + neighbor generation |
| `scripts/apl_optimizer.py` | Layer 1 APL optimization loop |
| `scripts/signal_apl_optimizer.py` | Layer 2+3 unified runner |
| `scripts/talent_local_search.py` | Talent seed + hill-climb |
| `scripts/talent_build_compare.py` | Wowhead build comparison |
| `scripts/validate_all_profiles.py` | Full profile validation |
| `scripts/optimize_all.py` | Master orchestrator |
| `scripts/optimize_all_specs.py` | Full per-spec talent+APL orchestrator |

### Deprecated (kept, not called)

| Script | Reason |
|--------|--------|
| `scripts/lib/node_classifier.py` | Wrong regex, wrong abstraction |
| `scripts/lib/talent_permute.py` | Generates 0 combos with correct budgets |
| `scripts/lib/talent_neighbor.py` | Superseded by talent_validator.py |

---

## Compute Estimates

Per spec, per fight style:

| Phase | Sims | Time |
|-------|------|------|
| Seed screening (12 builds × 1k iter) | 12 | 36s |
| Neighborhood screen (~216 × 300 iter) | 216 | ~120s |
| Stage 2 (top 20% × 3k iter) | ~43 | ~90s |
| Stage 3 (top 3 × 10k iter) | 3 | ~30s |
| Hill-climb pass 2 | ~200 | ~150s |
| **Total per style** | **~474** | **~7 min** |

All 33 specs × 2 styles: ~8 hours. With 2x parallelism: ~4 hours.

---

## Success Criteria

0. **Engine is current** — upstream synced, no pending class fixes, build number matches
1. **Engine is correct** — multi-target sweep + tier set delta + proc rate checks pass for all specs
2. Every spec's PW-best talent build ≥ best Wowhead build for PW — **MET (v0.3)**
3. Every spec's HAC-best talent build ≥ best Wowhead build for HAC — **MET (v0.3)**
4. All talent strings pass `validate_all_profiles.py` — **89/89 PASS (v0.3)**
5. All generated builds pass SimC smoke test — **MET (v0.3)**
6. Pipeline runs end-to-end: `python3 scripts/optimize_all_specs.py` — **MET (v0.3)**
