# Optimization Action Plan

Updated: 2026-03-29

## Architecture

Two independent optimization loops per spec, each producing results per fight style:

```
TALENT OPTIMIZATION                    APL OPTIMIZATION
  Wowhead builds (seeds)                Extract current APL
       |                                     |
  Screen at 1k iter per style           Generate mutations (swap/sweep/route)
       |                                     |
  Local search (single-node swaps)      Multi-stage eval (300→3k→10k iter)
       |                                     |
  Hill-climb to convergence             Accept best per style
       |                                     |
  Confirm at 10k iter                   Confirm at 10k iter
```

Each spec produces TWO independent optimal talent/APL builds — one for Patchwerk, one for HecticAddCleave.
File convention: `<Base>.simc` = PW-optimized, `<Base>_HAC.simc` = HAC-optimized.
Tank specs skip HAC. See `OPTIMIZATION_HOWTO.md` § "Profile File Convention" for details.

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
| `scripts/lib/sim_runner.py` | SimC runner, JSON parse, scoring |
| `scripts/lib/apl_parser.py` | APL parse/serialize |
| `scripts/lib/apl_mutations.py` | Mutation operators: swap, sweep, route |
| `scripts/lib/talent_tree.py` | DBC tree parser + real TraitEdge.csv edges |
| `scripts/lib/talent_codec.py` | Base64 talent string encode/decode |
| `scripts/lib/tree_codec_bridge.py` | Tree↔codec bridge |
| `scripts/lib/talent_validator.py` | Build validation + neighbor generation (NEW) |
| `scripts/apl_optimizer.py` | APL optimization loop |
| `scripts/talent_local_search.py` | Talent seed + hill-climb (NEW) |
| `scripts/talent_build_compare.py` | Wowhead build comparison |
| `scripts/validate_all_profiles.py` | Full profile validation (NEW) |
| `scripts/optimize_all.py` | Master orchestrator |

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

1. Every spec's PW-best talent build ≥ best Wowhead build for PW
2. Every spec's HAC-best talent build ≥ best Wowhead build for HAC
3. All talent strings pass `validate_all_profiles.py` (56/56)
4. All generated builds pass SimC smoke test
5. Pipeline runs end-to-end: `python3 scripts/optimize_all.py --talent --apl --all`
