# Talent Engine — Architecture Design

Generated: 2026-03-27

## Problem Statement

33 specs × 4-16 Wowhead builds = 262 pre-made builds. But these are curated
by humans. The actual decision space is much larger: a typical spec has ~60-80
talent nodes across 3 sub-trees, with ~15-20 DPS-relevant decisions. Brute
force is intractable (2^20 = 1M combinations × 4 sims each = 4M sims).

We need a talent engine that:
1. Models the talent tree as a constrained graph
2. Automatically identifies which nodes affect DPS
3. Generates only valid, non-redundant combinations
4. Searches efficiently using multi-stage filtering
5. Produces valid SimC talent strings

---

## Part 1: Talent Tree Graph Model

### Data Source

SimC's DBC (DataBase Client) data contains the full talent tree via
`trait_data_t` records. Each record has:

```
tree_index:          0=CLASS, 1=SPEC, 2=HERO, 3=SELECTION
id_class:            WoW class ID
id_trait_node_entry: unique entry identifier
id_node:             node position in tree (multiple entries share same id_node for choice nodes)
max_ranks:           1-4 (how many points can be spent)
req_points:          minimum total points spent in tree before this unlocks
id_spell:            what spell/passive this grants
id_replace_spell:    spell this replaces (0 if none)
row, col:            position in tree grid
selection_index:     for choice nodes, which option (0-based)
id_spec[4]:          which specs can take this (0 = all)
id_sub_tree:         hero talent tree ID (for hero nodes)
node_type:           0=normal, 1=tiered, 2=choice, 3=sub_tree_selection
```

### Python Data Model

```python
from dataclasses import dataclass, field
from enum import Enum

class NodeType(Enum):
    NORMAL = 0       # standard talent, 1+ ranks
    TIERED = 1       # sequential multi-rank (different spells per tier)
    CHOICE = 2       # pick one of N options
    SUBTREE_SEL = 3  # hero tree selector

class DPSRelevance(Enum):
    DPS = "dps"           # directly affects damage output
    GATING = "gating"     # no DPS itself, but required to reach DPS nodes
    UTILITY = "utility"   # zero DPS impact (movement, CC, defensive)

@dataclass
class TalentOption:
    """One option within a node (choice nodes have multiple options)."""
    entry_id: int           # id_trait_node_entry
    spell_id: int           # id_spell
    replace_spell_id: int   # id_replace_spell
    spell_name: str         # human-readable
    max_ranks: int
    selection_index: int    # 0 for non-choice, 0-N for choice nodes

@dataclass
class TalentNode:
    """A single node in the talent tree."""
    node_id: int                      # id_node
    tree: str                         # "class", "spec", "hero"
    node_type: NodeType
    row: int
    col: int
    req_points: int                   # minimum total points in this tree
    options: list[TalentOption]       # 1 for normal, 2-3 for choice
    dps_relevance: DPSRelevance = DPSRelevance.UTILITY
    
    # Graph edges (computed)
    parent_nodes: list[int] = field(default_factory=list)   # prerequisite node IDs
    child_nodes: list[int] = field(default_factory=list)    # nodes that depend on this

    @property
    def is_choice(self) -> bool:
        return self.node_type == NodeType.CHOICE
    
    @property
    def total_max_ranks(self) -> int:
        if self.node_type == NodeType.TIERED:
            return sum(o.max_ranks for o in self.options)
        return self.options[0].max_ranks if self.options else 1

@dataclass  
class TalentTree:
    """Full talent tree for a spec."""
    spec_name: str                        # e.g. "warrior_fury"
    spec_id: int                          # WoW specialization ID
    class_id: int
    nodes: dict[int, TalentNode]          # node_id -> TalentNode
    hero_trees: dict[str, list[int]]      # hero_name -> [node_ids]
    
    # Computed
    dps_nodes: list[int] = field(default_factory=list)
    utility_nodes: list[int] = field(default_factory=list)
    gating_nodes: list[int] = field(default_factory=list)
    total_points_available: int = 0
    
    def get_nodes_by_tree(self, tree: str) -> list[TalentNode]:
        return [n for n in self.nodes.values() if n.tree == tree]
    
    def get_dps_relevant(self) -> list[TalentNode]:
        return [self.nodes[nid] for nid in self.dps_nodes]
```

### Building the Tree from DBC

```python
def build_talent_tree(spec: str) -> TalentTree:
    """Extract talent tree from SimC DBC data.
    
    Approach: Run SimC with a special query that dumps trait_data,
    or parse the generated DBC .inc files directly.
    """
    # Method: use simc to dump all traits for a spec
    # simc spell_query outputs are limited, so instead we parse
    # the DBC generated data files
    
    # Alternative: run a minimal sim and inspect the debug output
    # which logs "X tree nodes generated for spec Y"
    
    # Build adjacency from row/req_points:
    # Node B depends on Node A if:
    #   1. B.req_points > 0 and A is in a prior row
    #   2. B is directly below A in the grid (col match or adjacent)
    #   3. The DBC has explicit prerequisite links (id_node connections)
```

### Prerequisite Resolution

WoW talent trees use TWO prerequisite systems:
1. **Point gates**: `req_points` = minimum total points spent in tree before
   this node unlocks. This is row-based (row 1 = 0 req, row 4 = 8 req, etc.)
2. **Direct edges**: some nodes require specific parent nodes (pathing arrows
   visible in the talent calculator). These are in the DBC but need to be
   extracted from the tree connection data.

For the engine, we need both. Point gates determine valid total-point
allocations. Direct edges determine which specific nodes must be taken.

---

## Part 2: DPS-Node Identification

### Three-Source Classification

#### Source A: APL Reference Scan
Any talent referenced in the APL is DPS-relevant:
```python
def classify_from_apl(apl_text: str, tree: TalentTree) -> set[int]:
    """Find all talent.X references in APL conditions."""
    dps_nodes = set()
    # Match patterns: talent.X, talent.X.enabled, talent.X.rank
    for match in re.finditer(r'talent\.(\w+)', apl_text):
        talent_name = match.group(1)
        for node in tree.nodes.values():
            for opt in node.options:
                if tokenize(opt.spell_name) == talent_name:
                    dps_nodes.add(node.node_id)
    return dps_nodes
```

#### Source B: Spell Data Damage Classification
Any talent whose spell_data has damage/stat modification effects:
```python
def classify_from_spell_data(tree: TalentTree) -> set[int]:
    """Check if talent spell modifies damage or stats."""
    dps_nodes = set()
    for node in tree.nodes.values():
        for opt in node.options:
            # Query spell effects for:
            # - Direct damage (A_SCHOOL_DAMAGE, A_WEAPON_DAMAGE)
            # - Damage modifiers (A_ADD_PCT_MODIFIER on damage)
            # - Stat buffs (A_MOD_STAT, A_MOD_RATING)
            # - Resource generation (more resources = more casts)
            # - Cooldown reduction
            # - Proc effects that deal damage
            if spell_has_dps_effect(opt.spell_id):
                dps_nodes.add(node.node_id)
    return dps_nodes
```

#### Source C: Action Registration Scan
Any talent that creates/modifies an action in the class module:
```python
def classify_from_code(spec: str, tree: TalentTree) -> set[int]:
    """Grep class module for talent references in action creation."""
    dps_nodes = set()
    # Search sc_{class}.cpp for talent.X usage in:
    # - Action constructors
    # - Damage multiplier calculations
    # - Proc trigger checks
    # - Resource calculations
    code = read_class_module(spec)
    for match in re.finditer(r'talent\.(?:spec|class|hero)\w*\.(\w+)', code):
        # Map back to tree node
        ...
    return dps_nodes
```

#### Combined Classification
```python
def classify_all_nodes(tree: TalentTree, apl: str, spec: str):
    apl_dps = classify_from_apl(apl, tree)
    spell_dps = classify_from_spell_data(tree)
    code_dps = classify_from_code(spec, tree)
    
    all_dps = apl_dps | spell_dps | code_dps
    
    # Mark gating nodes: utility nodes that are prerequisites of DPS nodes
    gating = set()
    for nid in all_dps:
        for parent_id in tree.nodes[nid].parent_nodes:
            if parent_id not in all_dps:
                gating.add(parent_id)
    
    for node in tree.nodes.values():
        if node.node_id in all_dps:
            node.dps_relevance = DPSRelevance.DPS
        elif node.node_id in gating:
            node.dps_relevance = DPSRelevance.GATING
        else:
            node.dps_relevance = DPSRelevance.UTILITY
    
    tree.dps_nodes = sorted(all_dps)
    tree.gating_nodes = sorted(gating)
    tree.utility_nodes = sorted(
        set(tree.nodes.keys()) - all_dps - gating
    )
```

### Expected Reduction

Typical spec has ~70 nodes total. Expected classification:
- DPS: ~15-25 nodes (talents that affect rotation or damage)
- GATING: ~5-10 nodes (must take to reach DPS nodes)
- UTILITY: ~35-50 nodes (CC, movement, defensives)

This reduces the search space from ~70 to ~15-25 variable nodes.

---

## Part 3: Smart Permutation Generator

### Constraint System

A valid talent build must satisfy:
1. **Point budget**: Class tree gets ~31 points, Spec tree gets ~30 points,
   Hero tree gets all nodes (fixed path). Total varies by spec.
2. **Row gates**: Can only take row N nodes after spending req_points in
   prior rows.
3. **Pathing**: Must take at least one parent node to reach a child.
4. **Choice exclusivity**: For choice nodes, exactly one option selected.
5. **Hero tree lock-in**: Once a hero tree is selected, all hero nodes are
   from that tree (the other tree is unavailable).

### Pivot vs Tuning Nodes

**Pivot nodes** change the rotation fundamentally:
- Enable/disable entire abilities (e.g., Bladestorm vs Ravager)
- Change resource economy (e.g., Massacre changes Execute threshold)
- Alter AoE/ST balance (e.g., Improved Whirlwind)
- Choice nodes are almost always pivots

**Tuning nodes** provide % modifiers:
- +X% damage to ability Y
- +X seconds duration to buff Z
- Flat damage/stat increases

Detection heuristic:
```python
def is_pivot_node(node: TalentNode, apl: str) -> bool:
    """Pivot = changes which abilities exist or APL structure."""
    for opt in node.options:
        # Grants a new castable ability?
        if opt.replace_spell_id != 0:
            return True  # replaces an ability
        # Referenced in APL routing conditions?
        if f"talent.{tokenize(opt.spell_name)}" in apl:
            # Check if it's in an if= condition (not just a damage mod)
            return True
    # Choice nodes are always pivots
    if node.is_choice:
        return True
    return False
```

### Two-Phase Search Algorithm

```
Phase 1: PIVOT SWEEP (coarse)
  Fix all tuning nodes to their Wowhead-recommended values.
  Enumerate all valid combinations of pivot nodes.
  Typical: 5-8 pivot nodes × 2-3 options each = 100-500 combinations.
  Sim each at 200 iterations (coarse).
  Keep top 10 pivot combinations.

Phase 2: TUNING SWEEP (fine)
  For each of the top 10 pivot combos:
    Enumerate tuning node variations (toggle each on/off).
    Typical: 10-15 tuning nodes, but many are rank 1-2 (not toggleable).
    Use greedy hill-climbing: toggle one node at a time, keep if DPS improves.
    Sim at 1000 iterations.
  
  Confirm winner at 10,000 iterations.
```

### Complexity Estimate

| Phase | Combinations | Iterations | Sims | Time (est.) |
|-------|-------------|-----------|------|-------------|
| Pivot sweep | ~200 | 200 | 400 (×2 fights) | ~3 min |
| Tuning sweep (10 pivots × 15 toggles) | ~150 | 1000 | 300 | ~5 min |
| Confirmation | 3 | 10000 | 6 | ~30 sec |
| **Total per spec** | | | **~706** | **~9 min** |
| **Total all 33 specs** | | | **~23,000** | **~5 hours** |

Vs brute force: 2^20 × 4 sims = 4,194,304 sims = weeks.

### Generating Valid Builds

```python
def generate_valid_builds(tree: TalentTree, 
                          fixed_nodes: dict[int, int],  # node_id -> rank
                          variable_nodes: list[int],     # nodes to permute
                          ) -> Iterator[dict[int, int]]:
    """
    Yield all valid talent allocations where:
    - fixed_nodes have their assigned ranks
    - variable_nodes are permuted (on/off/choice)
    - Point budget and prerequisite constraints are satisfied
    """
    # Use backtracking search with constraint propagation
    # Process nodes in topological order (parents before children)
    
    topo_order = topological_sort(variable_nodes, tree)
    
    def backtrack(idx: int, current: dict[int, int], points_spent: dict[str, int]):
        if idx == len(topo_order):
            if is_valid_allocation(current, points_spent, tree):
                yield dict(current)
            return
        
        node = tree.nodes[topo_order[idx]]
        
        # Option 1: don't take this node (rank 0)
        if not is_required_for_children(node, current, tree):
            current[node.node_id] = 0
            yield from backtrack(idx + 1, current, points_spent)
        
        # Option 2+: take this node at each valid rank
        for rank in range(1, node.total_max_ranks + 1):
            if can_afford(node, rank, points_spent, tree):
                current[node.node_id] = rank
                new_points = dict(points_spent)
                new_points[node.tree] = new_points.get(node.tree, 0) + rank
                yield from backtrack(idx + 1, current, new_points)
        
        del current[node.node_id]
    
    yield from backtrack(0, dict(fixed_nodes), count_fixed_points(fixed_nodes, tree))
```

---

## Part 4: Talent String Encoder/Decoder

### Decoder (base64 → node selections)

SimC's `parse_traits_hash` reads the base64 string bit-by-bit:
```
version(8) + spec_id(16) + tree_hash(128) + per_node_data(variable)

Per node (in tree_nodes order):
  selected(1 bit):  0 = not taken, 1 = taken
  if selected:
    purchased(1 bit): 0 = granted (rank 1), 1 = purchased
    if purchased:
      partially_ranked(1 bit): 0 = max rank, 1 = partial
      if partially_ranked:
        rank(6 bits): how many ranks
      if choice node:
        choice_index(2 bits): which option (0-based)
```

Python implementation:
```python
def decode_talent_string(talent_str: str, tree: TalentTree) -> dict[int, tuple[int, int]]:
    """Decode talent string to {node_id: (rank, choice_index)}."""
    bits = base64_to_bits(talent_str)
    head = 0
    
    version = read_bits(bits, head, 8); head += 8
    spec_id = read_bits(bits, head, 16); head += 16
    tree_hash = read_bits(bits, head, 128); head += 128
    
    result = {}
    for node_id in sorted(tree.nodes.keys()):  # must match SimC's tree_nodes order
        node = tree.nodes[node_id]
        selected = read_bits(bits, head, 1); head += 1
        
        if selected:
            rank = node.total_max_ranks  # default: max
            choice = 0
            
            purchased = read_bits(bits, head, 1); head += 1
            if purchased:
                partial = read_bits(bits, head, 1); head += 1
                if partial:
                    rank = read_bits(bits, head, 6); head += 6
                if node.is_choice:
                    choice = read_bits(bits, head, 2); head += 2
            else:
                rank = 1  # granted
            
            result[node_id] = (rank, choice)
    
    return result
```

### Encoder (node selections → base64)

Reverse of decode:
```python
def encode_talent_string(selections: dict[int, tuple[int, int]], 
                         tree: TalentTree) -> str:
    """Encode node selections back to SimC talent string."""
    bits = []
    
    write_bits(bits, tree.spec_id, 8)   # version = 2
    write_bits(bits, tree.spec_id, 16)  # spec_id
    write_bits(bits, 0, 128)            # tree_hash = 0 (SimC accepts this)
    
    for node_id in sorted(tree.nodes.keys()):
        node = tree.nodes[node_id]
        
        if node_id in selections:
            rank, choice = selections[node_id]
            write_bits(bits, 1, 1)  # selected
            
            if rank == 1 and is_granted(node):
                write_bits(bits, 0, 1)  # not purchased (granted)
            else:
                write_bits(bits, 1, 1)  # purchased
                if rank < node.total_max_ranks:
                    write_bits(bits, 1, 1)   # partially ranked
                    write_bits(bits, rank, 6) # rank value
                else:
                    write_bits(bits, 0, 1)   # full rank
                
                if node.is_choice:
                    write_bits(bits, choice, 2)
        else:
            write_bits(bits, 0, 1)  # not selected
    
    return bits_to_base64(bits)
```

### Critical: Node Ordering Must Match SimC

The encoder/decoder MUST iterate nodes in the EXACT same order as SimC's
`generate_tree_nodes()`. SimC sorts by `id_node` within each tree. The
ordering is:
1. All CLASS tree nodes, sorted by id_node
2. All SPEC tree nodes, sorted by id_node
3. All SELECTION nodes (hero tree selectors)
4. All HERO tree nodes for the selected hero path

We must replicate this ordering exactly or the bit positions will be wrong.

---

## Part 5: Caching and Deduplication

### DPS-Equivalence Classes

Two builds that differ ONLY in utility nodes produce IDENTICAL DPS.
Detect and skip:

```python
def dps_fingerprint(selections: dict[int, tuple[int, int]], 
                    tree: TalentTree) -> tuple:
    """Hash only DPS-relevant node selections."""
    return tuple(
        (nid, selections.get(nid, (0, 0)))
        for nid in sorted(tree.dps_nodes + tree.gating_nodes)
    )
```

Before simming a build, check:
```python
seen_fingerprints = {}
fp = dps_fingerprint(build, tree)
if fp in seen_fingerprints:
    # Skip — DPS identical to a previously tested build
    result = seen_fingerprints[fp]
else:
    result = run_sim(build)
    seen_fingerprints[fp] = result
```

### Incremental Encoding

When sweeping tuning nodes (one toggle at a time), don't re-encode from
scratch. Cache the base bit string and flip only the changed node's bits.

---

## Part 6: Integration Architecture

### Full Pipeline

```
┌──────────────────────────────────────────────────────┐
│                  talent_engine.py                      │
│                                                        │
│  1. Build tree from DBC ─────────────────────────────┐│
│  2. Classify nodes (DPS/GATING/UTILITY) ────────────┐││
│  3. Decode current build ──────────────────────────┐│││
│  4. Generate pivot combinations ─────────────────┐ ││││
│  5. Pivot sweep (coarse sims) ─────────────────┐ │ ││││
│  6. Tuning sweep (per winning pivot) ────────┐ │ │ ││││
│  7. Encode winning build ──────────────────┐ │ │ │ ││││
│  8. Feed into APL optimizer ─────────────┐ │ │ │ │ ││││
│                                          ▼ ▼ ▼ ▼ ▼ ▼▼▼│
│                                      SimC Runner       │
└──────────────────────────────────────────────────────┘

Output per spec:
  - Best talent build (SimC talent string)
  - DPS by fight style
  - Comparison to current profile build
  - Comparison to all Wowhead builds
  - Node sensitivity report (which nodes matter most)
```

### CLI Interface

```bash
# Discover best build for one spec
python3 scripts/talent_engine.py --spec warrior_fury

# Run all specs
python3 scripts/talent_engine.py --all

# Just classify nodes (no sims)
python3 scripts/talent_engine.py --spec warrior_fury --classify-only

# Compare Wowhead builds only (no permutation search)
python3 scripts/talent_engine.py --spec warrior_fury --wowhead-only

# Show tree structure
python3 scripts/talent_engine.py --spec warrior_fury --show-tree
```

### Output Artifacts

Per spec:
```
results/talents/{spec}/
  tree.json           # full tree with classifications
  classification.md   # human-readable node classification report
  pivot_sweep.json    # all pivot combinations tested
  tuning_sweep.json   # tuning results per winning pivot
  best_build.txt      # SimC talent= string
  comparison.md       # vs current profile vs Wowhead builds
  sensitivity.md      # per-node DPS impact ranking
```

---

## Part 7: Implementation Plan

### Phase A: DBC Tree Extraction (2 hours)
1. Write Python script to parse SimC's DBC trait_data
   - Option 1: Parse the .inc generated files directly
   - Option 2: Run SimC in debug mode to dump tree nodes
   - Option 3: Use the existing trait_data query functions
2. Build TalentTree objects for all 33 specs
3. Validate: decode an existing talent string and verify node selections match

### Phase B: Node Classification (2 hours)
4. APL scanner: extract all talent.X references from save_actions output
5. Spell data scanner: check DBC effect types for damage/stat mods
6. Code scanner: grep class modules for talent usage in damage calculations
7. Combined classifier with DPS/GATING/UTILITY output
8. Validate against a few specs manually (spot-check known DPS talents)

### Phase C: Encoder/Decoder (3 hours)
9. Implement decode_talent_string matching SimC's parse_traits_hash exactly
10. Implement encode_talent_string matching SimC's generate_traits_hash exactly
11. Round-trip test: decode(encode(decode(existing_string))) == original
12. Validate: encoded strings produce identical sim results

### Phase D: Permutation Engine (3 hours)
13. Pivot node identification
14. Constraint-aware backtracking generator
15. DPS fingerprint deduplication
16. Multi-stage sim pipeline (coarse → fine → confirm)

### Phase E: Full Run (variable)
17. Run on 1 spec as proof of concept (Warrior Fury — well-understood)
18. Run on all 33 specs
19. Compare results to Wowhead builds
20. Feed winning builds into APL optimizer (Component 5 integration)

### Estimated Total: ~10 hours implementation + ~5 hours runtime

---

## Part 8: Risk Analysis

### Risk: DBC Node Order Mismatch
The encoder/decoder must iterate nodes in the exact same order as SimC.
If our order differs by even one node, all subsequent bits shift and the
string is garbage.
**Mitigation**: Round-trip test is mandatory before any optimization.
Decode a known-good string, re-encode, verify bytes match.

### Risk: Constraint Violations
Generated builds might violate hidden prerequisites not captured in
req_points.
**Mitigation**: Every generated build is validated by running `iterations=0`
in SimC — if it fails to parse the talent string, it's invalid. Fast check
(<0.1s per build).

### Risk: APL Mismatch
The default APL may not support a talent combo well (e.g., APL doesn't use
an ability granted by a talent we toggled on).
**Mitigation**: This is why talent engine feeds INTO the APL optimizer.
Phase 4d-1 finds best talents with current APL, Phase 4d-2 optimizes APL
for winning talents. Iterate if needed.

### Risk: Overfitting to Fight Style
Talent X is great for Patchwerk but terrible for HecticAddCleave.
**Mitigation**: Composite scoring (50/50) + regression cap prevents this.
Also output per-fight-style results so users can pick fight-appropriate builds.
