# Optimization Action Plan

Last updated: 2026-03-28

## Architecture

Two independent optimization loops, each producing results per fight style:

```
TALENT OPTIMIZATION                    APL OPTIMIZATION
  Wowhead builds (seeds)                Extract current APL
       |                                     |
  Screen at 1k iter                     Generate mutations
       |                                     |
  Local search (neighbors)              Multi-stage evaluation
       |                                     |
  Hill-climb to convergence             Accept best per style
       |                                     |
  Confirm at 10k iter                   Confirm at 10k iter
```

Each spec produces TWO independent optimal talent/APL builds — one for Patchwerk, one for HecticAddCleave.

---

## Talent Optimization — Seed + Local Search

### Why Not Classify-Then-Permute

The old approach (node_classifier.py + talent_permute.py) is broken:

1. **Code scanner regex wrong** — matches `talent.spec.X` but C++ uses `talents.fury.X` (plural, spec-name prefix). Result: 0 code-classified DPS nodes for Warrior.
2. **APL scanner too narrow** — only finds talents in `if=` conditions (5/106 for Fury). Core abilities never appear in conditions because they're always taken.
3. **Wrong abstraction** — talent optimization is DAG budget allocation across competing sub-tree paths, not independent node toggles. Even a perfect classifier can't decompose this correctly.

### New Approach: Seed + Local Search

**Phase 1 — Seed Screening** (already implemented in `talent_build_compare.py`):
- Sim all Wowhead builds (4-16 per spec) at 1000 iter × both fight styles
- Rank per fight style independently
- Pick top 3 seeds per fight style

**Phase 2 — Neighborhood Generation** (NEW: `scripts/lib/talent_neighbor.py`):
Starting from a decoded talent build (dict of node_id → rank/choice), generate all single-step neighbors:

| Mutation | Description | Constraint |
|----------|-------------|-----------|
| REMOVE | Drop a selected non-granted node (rank → 0) | No child depends solely on it; row-gate still met |
| ADD | Take an unselected node (0 → max_ranks) | Prerequisites met; sub-tree budget allows |
| SWAP_CHOICE | Switch a choice node to its other option | Always valid (same point cost) |
| SWAP_POINT | Remove node A + add node B in same sub-tree | Budget-neutral; both individually valid |

Each build has ~15-25 flexible nodes → ~30-50 single-step neighbors.

**Phase 3 — Hill-Climb** (NEW: `scripts/talent_local_search.py`):
```
for each seed (top 3 per fight style):
    current = seed
    for iteration in range(5):
        neighbors = generate_neighbors(current)
        screen at 500 iter → keep top 5
        confirm at 2000 iter → keep best
        if best > current + 0.1%:
            current = best
        else:
            break  # converged
    confirm winner at 10000 iter
```

### Constraint Rules

A talent build must satisfy:
1. **Sub-tree point budgets**: CLASS ≤ 31, SPEC ≤ 30, HERO ≤ ~10 (varies)
2. **Row gates**: `req_points` on each node — must spend N points in sub-tree before this row unlocks
3. **Edge prerequisites**: every parent edge must have at least one selected parent
4. **Choice exclusivity**: only one option per choice node
5. **Granted nodes**: hero starting nodes (row=1) and spec-starter class nodes are auto-granted, always present

### Validation Strategy

Belt-and-suspenders:
1. `validate_build()` checks all 5 constraint rules in Python
2. `encode_talent_string()` → SimC will error on invalid builds (catches edge cases)
3. Skip neighbors with DPS within noise threshold (±0.2% at 500 iter)

---

## APL Optimization — Mutation + Multi-Stage

Already implemented and working (`scripts/apl_optimizer.py`). Per fight style:

1. Extract current APL via `save_actions`
2. Generate 4 mutation types: adjacent swap, threshold sweep, promotion, routing
3. Three-stage funnel: 100 iter (coarse) → 1000 iter (medium) → 10000 iter (confirm)
4. Accept if DPS improves for that fight style
5. Converge when <0.1% improvement

Warrior Fury test: PW +0.00% (optimal), HAC +0.44% (rampage threshold 100→80).

---

## Files to Create

### `scripts/lib/talent_neighbor.py` (~250 lines)

```python
# Core functions:

def get_subtree_budget(tree, selections, tree_index) -> (spent, max_budget):
    """Count points spent in a sub-tree vs max allowed."""

def can_remove_node(tree, selections, node_id) -> bool:
    """Check if removing a node breaks any child prerequisites or row gates."""

def can_add_node(tree, selections, node_id) -> bool:
    """Check if adding a node is valid (prereqs met, budget allows)."""

def find_removable_nodes(tree, selections) -> set[int]:
    """All nodes that can be safely removed."""

def find_addable_nodes(tree, selections) -> set[int]:
    """All unselected nodes whose prerequisites are satisfied and budget allows."""

def generate_neighbors(tree, selections, codec_nodes, spec_id, purchased_flags)
    -> list[tuple[str, str]]:  # [(talent_string, description), ...]
    """Generate all single-step neighbor talent strings."""
    # 1. REMOVE: for each removable node, drop it
    # 2. ADD: for each addable node, take it at max ranks
    # 3. SWAP_CHOICE: for each selected choice node, switch to other option
    # 4. SWAP_POINT: for each (removable, addable) pair in same sub-tree, swap
    #    (capped at ~50 swaps to avoid combinatorial explosion)

def validate_build(tree, selections) -> tuple[bool, str]:
    """Full constraint validation. Returns (valid, reason)."""
```

### `scripts/talent_local_search.py` (~250 lines)

```python
def screen_seeds(spec_name, fight_style, seeds, threads) -> list:
    """Sim all seeds at 1000 iter, return sorted by DPS."""

def search_neighborhood(spec_name, fight_style, base_ts, tree, codec_nodes,
                        spec_id, purchased_flags, threads) -> tuple[str, float]:
    """One hill-climb pass: generate neighbors, screen, confirm."""

def optimize_from_seeds(spec_name, fight_style, seeds, threads=8,
                        max_passes=5) -> dict:
    """Full local search from Wowhead seeds.
    Returns {talent_string, dps, improvement_pct, passes, neighbors_tested}."""

def optimize_spec(spec_name, fight_styles=None, threads=8) -> list[dict]:
    """Top-level: load Wowhead builds, run local search per fight style."""
```

### Modify `scripts/talent_optimizer.py`

Replace the classify → permute pipeline with:
```python
1. Load Wowhead builds via talent_build_compare.load_wowhead_builds()
2. For each fight style:
   a. optimize_from_seeds() — screens seeds + local search
   b. Save results per fight style
3. Compare PW-best vs HAC-best — report if they differ
```

### Modify `scripts/optimize_all.py`

Add `--talent` flag alongside existing `--apl`:
```
python3 scripts/optimize_all.py --talent --all          # talent optimize all specs
python3 scripts/optimize_all.py --talent --apl --all    # both talent + APL
python3 scripts/optimize_all.py --talent --spec warrior_fury --fight-style Patchwerk
```

---

## Files to Deprecate

| File | Reason | Action |
|------|--------|--------|
| `scripts/lib/node_classifier.py` | Wrong regex, wrong abstraction | Keep in repo, remove from pipeline |
| `scripts/lib/talent_permute.py` | Generates 0 combos, structurally limited | Keep in repo, remove from pipeline |

---

## Results Structure

```
results/optimization/{spec}/
  wowhead_builds.json               # all Wowhead builds per-style ranked
  talent_local_search_pw.json       # PW local search results
  talent_local_search_hac.json      # HAC local search results
  best_build_pw.txt                 # PW-optimal talent string
  best_build_hac.txt                # HAC-optimal talent string
  apl_optimization_pw.json          # PW APL optimizer results
  apl_optimization_hac.json         # HAC APL optimizer results
  optimized_apl_pw.simc             # PW-optimal APL (if improved)
  optimized_apl_hac.simc            # HAC-optimal APL (if improved)
```

---

## Compute Estimates

Per spec, per fight style:
| Phase | Sims | Time |
|-------|------|------|
| Seed screening (8-12 builds × 1k iter) | 12 | 36s |
| Neighborhood gen + screen (40 neighbors × 500 iter) | 40 | 60s |
| Confirmation (top 5 × 2k iter) | 5 | 25s |
| Hill-climb pass 2 (if improved) | 45 | 85s |
| Hill-climb pass 3 (diminishing) | 30 | 50s |
| Final confirm (10k iter) | 2 | 14s |
| **Total per style** | **~134** | **~4.5 min** |

Per spec (2 styles): ~9 min
All 33 specs: ~5 hours
With 2x parallelism: ~2.5 hours

Combined with APL optimization (~6 min/spec/style):
All 33 specs, talent + APL: ~10 hours
With 2x parallelism: ~5 hours

---

## Implementation Order

| Step | What | Effort | Blocks |
|------|------|--------|--------|
| 1 | `talent_neighbor.py` — constraint validation + neighbor generation | 2h | Steps 2-3 |
| 2 | `talent_local_search.py` — screen + hill-climb + optimize_from_seeds | 1.5h | Step 3 |
| 3 | Rewrite `talent_optimizer.py` — wire seeds → local search | 0.5h | Step 4 |
| 4 | Update `optimize_all.py` — add --talent flag | 0.5h | — |
| 5 | Test on warrior_fury (both styles) | 0.5h | Step 6 |
| 6 | Full 33-spec run | 5h compute | Step 7 |
| 7 | Apply results — update profiles, create _M+ variants | 1h | — |

**Total: ~6h coding + ~5h compute**

---

## Success Criteria

1. Every spec's PW-best talent build DPS ≥ best Wowhead build for PW
2. Every spec's HAC-best talent build DPS ≥ best Wowhead build for HAC
3. Local search finds ≥ 0.1% improvement over Wowhead for ≥ 5 specs
4. All generated talent strings pass encode → SimC smoke test
5. Pipeline runs end-to-end: `python3 scripts/optimize_all.py --talent --all`
