#!/usr/bin/env python3
"""
talent_tree.py - Parse SimulationCraft's trait_data.inc and build TalentTree objects.

Parses the DBC-generated C++ static arrays into Python dataclasses,
filtering by class and spec to produce a complete talent tree with
nodes, edges, and hero tree information.
"""

import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

# ─── Constants ───────────────────────────────────────────────────────────────

# Node types
NODE_NORMAL = 0
NODE_TIERED = 1
NODE_CHOICE = 2
NODE_SUBTREE_SEL = 3

NODE_TYPE_NAMES = {
    NODE_NORMAL: "NORMAL",
    NODE_TIERED: "TIERED",
    NODE_CHOICE: "CHOICE",
    NODE_SUBTREE_SEL: "SUBTREE_SEL",
}

# Tree indices
TREE_CLASS = 1
TREE_SPEC = 2
TREE_HERO = 3
TREE_SELECTION = 4

TREE_INDEX_NAMES = {
    TREE_CLASS: "CLASS",
    TREE_SPEC: "SPEC",
    TREE_HERO: "HERO",
    TREE_SELECTION: "SELECTION",
}

# Class IDs
CLASS_MAP = {
    1: "Warrior", 2: "Paladin", 3: "Hunter", 4: "Rogue", 5: "Priest",
    6: "Death Knight", 7: "Shaman", 8: "Mage", 9: "Warlock", 10: "Monk",
    11: "Druid", 12: "Demon Hunter", 13: "Evoker",
}

# Spec map: human-readable name -> (class_id, spec_id)
SPEC_MAP = {
    "warrior_arms":         (1, 71),
    "warrior_fury":         (1, 72),
    "warrior_protection":   (1, 73),
    "paladin_holy":         (2, 65),
    "paladin_protection":   (2, 66),
    "paladin_retribution":  (2, 70),
    "hunter_bm":            (3, 253),
    "hunter_mm":            (3, 254),
    "hunter_survival":      (3, 255),
    "rogue_assassination":  (4, 259),
    "rogue_outlaw":         (4, 260),
    "rogue_subtlety":       (4, 261),
    "priest_discipline":    (5, 256),
    "priest_holy":          (5, 257),
    "priest_shadow":        (5, 258),
    "dk_blood":             (6, 250),
    "dk_frost":             (6, 251),
    "dk_unholy":            (6, 252),
    "shaman_elemental":     (7, 262),
    "shaman_enhancement":   (7, 263),
    "shaman_restoration":   (7, 264),
    "mage_arcane":          (8, 62),
    "mage_fire":            (8, 63),
    "mage_frost":           (8, 64),
    "warlock_affliction":   (9, 265),
    "warlock_demonology":   (9, 266),
    "warlock_destruction":  (9, 267),
    "monk_brewmaster":      (10, 268),
    "monk_windwalker":      (10, 269),
    "monk_mistweaver":      (10, 270),
    "druid_balance":        (11, 102),
    "druid_feral":          (11, 103),
    "druid_guardian":       (11, 104),
    "druid_restoration":    (11, 105),
    "dh_havoc":             (12, 577),
    "dh_vengeance":         (12, 581),
    "dh_devourer":          (12, 1480),
    "evoker_devastation":   (13, 1467),
    "evoker_preservation":  (13, 1468),
    "evoker_augmentation":  (13, 1473),
}


# ─── Data Classes ────────────────────────────────────────────────────────────

@dataclass
class TraitEntry:
    """Raw parsed entry from trait_data.inc."""
    tree_index: int
    id_class: int
    id_trait_node_entry: int
    id_node: int
    max_ranks: int
    req_points: int
    id_trait_definition: int
    id_spell: int
    id_replace_spell: int
    id_override_spell: int
    row: int
    col: int
    selection_index: int
    name: str
    id_spec: List[int]        # 4 elements
    id_spec_starter: List[int] # 4 elements
    id_sub_tree: int
    node_type: int


@dataclass
class TalentNodeOption:
    """One option within a talent node (for choice/tiered nodes, there are multiple)."""
    id_trait_node_entry: int
    id_trait_definition: int
    id_spell: int
    id_replace_spell: int
    id_override_spell: int
    max_ranks: int
    selection_index: int
    name: str


@dataclass
class TalentNode:
    """A single node in the talent tree. May contain multiple options for choice nodes."""
    id_node: int
    tree_index: int       # 1=CLASS, 2=SPEC, 3=HERO, 4=SELECTION
    node_type: int        # 0=NORMAL, 1=TIERED, 2=CHOICE, 3=SUBTREE_SEL
    row: int
    col: int
    req_points: int
    id_sub_tree: int      # non-zero for hero tree nodes
    id_class: int
    id_spec: List[int]    # spec filter from first entry
    id_spec_starter: List[int]
    options: List[TalentNodeOption] = field(default_factory=list)

    @property
    def name(self) -> str:
        """Primary name (first option)."""
        return self.options[0].name if self.options else "Unknown"

    @property
    def names(self) -> List[str]:
        """All option names."""
        return [o.name for o in self.options]

    @property
    def id_spell(self) -> int:
        """Primary spell ID."""
        return self.options[0].id_spell if self.options else 0

    @property
    def max_ranks(self) -> int:
        """Max ranks from first option."""
        return self.options[0].max_ranks if self.options else 1

    @property
    def tree_type(self) -> str:
        return TREE_INDEX_NAMES.get(self.tree_index, "UNKNOWN")

    @property
    def type_name(self) -> str:
        return NODE_TYPE_NAMES.get(self.node_type, "UNKNOWN")

    def is_choice(self) -> bool:
        return self.node_type == NODE_CHOICE

    def is_available_for_spec(self, spec_id: int) -> bool:
        """Check if this node is available for a given spec."""
        specs = [s for s in self.id_spec if s != 0]
        return len(specs) == 0 or spec_id in specs


@dataclass
class TalentEdge:
    """An edge (prerequisite) between two nodes."""
    from_node: int  # id_node of prerequisite
    to_node: int    # id_node of dependent


@dataclass
class HeroTree:
    """A hero talent sub-tree."""
    id_sub_tree: int
    name: str
    id_class: int
    node_ids: List[int] = field(default_factory=list)


@dataclass
class TalentTree:
    """Complete talent tree for a spec."""
    spec_name: str
    class_id: int
    spec_id: int
    nodes: Dict[int, TalentNode] = field(default_factory=dict)         # id_node -> TalentNode
    edges: List[TalentEdge] = field(default_factory=list)
    hero_trees: Dict[int, HeroTree] = field(default_factory=dict)      # id_sub_tree -> HeroTree
    selection_nodes: Dict[int, TalentNode] = field(default_factory=dict)  # selection nodes

    @property
    def class_nodes(self) -> Dict[int, TalentNode]:
        return {nid: n for nid, n in self.nodes.items() if n.tree_index == TREE_CLASS}

    @property
    def spec_nodes(self) -> Dict[int, TalentNode]:
        return {nid: n for nid, n in self.nodes.items() if n.tree_index == TREE_SPEC}

    @property
    def hero_nodes(self) -> Dict[int, TalentNode]:
        return {nid: n for nid, n in self.nodes.items() if n.tree_index == TREE_HERO}

    def get_node_by_name(self, name: str) -> Optional[TalentNode]:
        """Find a node by name (case-insensitive)."""
        name_lower = name.lower()
        for node in self.nodes.values():
            for opt in node.options:
                if opt.name.lower() == name_lower:
                    return node
        return None

    def get_nodes_at_row(self, row: int) -> List[TalentNode]:
        return [n for n in self.nodes.values() if n.row == row]

    def get_children(self, node_id: int) -> List[int]:
        """Get all node IDs that depend on this node."""
        return [e.to_node for e in self.edges if e.from_node == node_id]

    def get_parents(self, node_id: int) -> List[int]:
        """Get all node IDs that this node depends on."""
        return [e.from_node for e in self.edges if e.to_node == node_id]

    def summary(self) -> str:
        lines = []
        lines.append(f"TalentTree: {self.spec_name} (class={self.class_id}, spec={self.spec_id})")
        lines.append(f"  Total nodes: {len(self.nodes)}")
        lines.append(f"  Class tree nodes: {len(self.class_nodes)}")
        lines.append(f"  Spec tree nodes: {len(self.spec_nodes)}")
        lines.append(f"  Hero tree nodes: {len(self.hero_nodes)}")
        lines.append(f"  Selection nodes: {len(self.selection_nodes)}")
        lines.append(f"  Edges: {len(self.edges)}")

        choice_count = sum(1 for n in self.nodes.values() if n.is_choice())
        lines.append(f"  Choice nodes: {choice_count}")

        if self.hero_trees:
            lines.append(f"  Hero trees:")
            for ht in self.hero_trees.values():
                lines.append(f"    - {ht.name} (id={ht.id_sub_tree}, nodes={len(ht.node_ids)})")

        return "\n".join(lines)


# ─── Parsing ─────────────────────────────────────────────────────────────────

# Regex to parse a single trait_data entry line
# Matches: { fields..., "name", { spec[4] }, { starter[4] }, sub_tree, node_type },
_ENTRY_RE = re.compile(
    r'\{\s*'
    r'(\d+)\s*,\s*'            # tree_index
    r'(\d+)\s*,\s*'            # id_class
    r'(\d+)\s*,\s*'            # id_trait_node_entry
    r'(\d+)\s*,\s*'            # id_node
    r'(\d+)\s*,\s*'            # max_ranks
    r'(\d+)\s*,\s*'            # req_points
    r'(\d+)\s*,\s*'            # id_trait_definition
    r'(\d+)\s*,\s*'            # id_spell
    r'(\d+)\s*,\s*'            # id_replace_spell
    r'(\d+)\s*,\s*'            # id_override_spell
    r'(\d+)\s*,\s*'            # row
    r'(\d+)\s*,\s*'            # col
    r'(\d+)\s*,\s*'            # selection_index
    r'"([^"]*)"\s*,\s*'        # name
    r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\}\s*,\s*'  # id_spec[4]
    r'\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\}\s*,\s*'  # id_spec_starter[4]
    r'(\d+)\s*,\s*'            # id_sub_tree
    r'(\d+)\s*'                # node_type
    r'\}'
)

# Regex for sub_tree data: { id, "name", class_id }
_SUBTREE_RE = re.compile(
    r'\{\s*(\d+)\s*,\s*"([^"]*)"\s*,\s*(\d+)\s*\}'
)


def _default_inc_path() -> str:
    """Find trait_data.inc relative to this script or from home."""
    # Try relative to script location (scripts/lib/ -> engine/dbc/generated/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    simc_root = os.path.dirname(os.path.dirname(script_dir))
    candidate = os.path.join(simc_root, "engine", "dbc", "generated", "trait_data.inc")
    if os.path.exists(candidate):
        return candidate
    # Fallback
    home = os.path.expanduser("~")
    return os.path.join(home, "simc", "engine", "dbc", "generated", "trait_data.inc")


def parse_trait_data(filepath: Optional[str] = None) -> Tuple[List[TraitEntry], Dict[int, Tuple[str, int]]]:
    """
    Parse trait_data.inc and return:
      - list of TraitEntry objects
      - dict of sub_tree_id -> (name, class_id)
    """
    if filepath is None:
        filepath = _default_inc_path()

    with open(filepath, 'r') as f:
        content = f.read()

    # Parse trait entries
    entries = []
    for m in _ENTRY_RE.finditer(content):
        g = m.groups()
        entry = TraitEntry(
            tree_index=int(g[0]),
            id_class=int(g[1]),
            id_trait_node_entry=int(g[2]),
            id_node=int(g[3]),
            max_ranks=int(g[4]),
            req_points=int(g[5]),
            id_trait_definition=int(g[6]),
            id_spell=int(g[7]),
            id_replace_spell=int(g[8]),
            id_override_spell=int(g[9]),
            row=int(g[10]),
            col=int(g[11]),
            selection_index=int(g[12]),
            name=g[13],
            id_spec=[int(g[14]), int(g[15]), int(g[16]), int(g[17])],
            id_spec_starter=[int(g[18]), int(g[19]), int(g[20]), int(g[21])],
            id_sub_tree=int(g[22]),
            node_type=int(g[23]),
        )
        entries.append(entry)

    # Parse sub_tree data
    sub_trees = {}
    # Find the sub_tree section
    st_start = content.find("__trait_sub_tree_data")
    if st_start != -1:
        st_section = content[st_start:]
        for m in _SUBTREE_RE.finditer(st_section):
            st_id = int(m.group(1))
            st_name = m.group(2)
            st_class = int(m.group(3))
            sub_trees[st_id] = (st_name, st_class)

    return entries, sub_trees


def _node_available_for_spec(entry: TraitEntry, class_id: int, spec_id: int) -> bool:
    """Check if a trait entry is available for the given class/spec."""
    if entry.id_class != class_id:
        return False
    specs = [s for s in entry.id_spec if s != 0]
    if len(specs) == 0:
        return True
    return spec_id in specs


def _build_edges(nodes: Dict[int, TalentNode]) -> List[TalentEdge]:
    """
    Build edges between nodes based on row adjacency and column proximity.

    Heuristic: A node at row R depends on nodes at row R-1 that are
    within column distance <= 1. For nodes with req_points > 0, the
    prerequisite is the point gate rather than a specific node, but we
    still build structural edges for the tree topology.
    """
    edges = []
    seen = set()

    # Group nodes by (tree_index, row)
    by_tree_row: Dict[Tuple[int, int], List[TalentNode]] = {}
    for node in nodes.values():
        key = (node.tree_index, node.row)
        by_tree_row.setdefault(key, []).append(node)

    for node in nodes.values():
        if node.row <= 1:
            continue  # Root row, no parents

        # Look for potential parents in the previous row(s) within same tree
        prev_key = (node.tree_index, node.row - 1)
        candidates = by_tree_row.get(prev_key, [])

        # For hero trees, also filter by sub_tree
        if node.tree_index == TREE_HERO and node.id_sub_tree != 0:
            candidates = [c for c in candidates
                         if c.id_sub_tree == node.id_sub_tree or c.id_sub_tree == 0]

        for cand in candidates:
            col_dist = abs(cand.col - node.col)
            if col_dist <= 1:
                edge_key = (cand.id_node, node.id_node)
                if edge_key not in seen:
                    seen.add(edge_key)
                    edges.append(TalentEdge(from_node=cand.id_node, to_node=node.id_node))

    return edges


def build_talent_tree(spec_name: str, filepath: Optional[str] = None) -> TalentTree:
    """
    Build a complete TalentTree for the given spec.

    Args:
        spec_name: Key from SPEC_MAP (e.g., 'warrior_fury')
        filepath: Optional path to trait_data.inc

    Returns:
        TalentTree with all nodes, edges, and hero trees for the spec.
    """
    spec_name_lower = spec_name.lower()
    if spec_name_lower not in SPEC_MAP:
        available = ", ".join(sorted(SPEC_MAP.keys()))
        raise ValueError(f"Unknown spec '{spec_name}'. Available: {available}")

    class_id, spec_id = SPEC_MAP[spec_name_lower]

    entries, sub_trees = parse_trait_data(filepath)

    # Filter entries for this class/spec
    filtered: List[TraitEntry] = []
    for e in entries:
        if e.id_class != class_id:
            continue
        if e.tree_index == TREE_SELECTION:
            # Selection nodes: filter by spec in id_spec
            specs = [s for s in e.id_spec if s != 0]
            if specs and spec_id not in specs:
                continue
            filtered.append(e)
        elif e.tree_index == TREE_HERO:
            # Hero nodes: available if spec is in id_spec or id_spec is all zeros
            specs = [s for s in e.id_spec if s != 0]
            if specs and spec_id not in specs:
                continue
            filtered.append(e)
        else:
            # Class/Spec nodes
            if _node_available_for_spec(e, class_id, spec_id):
                filtered.append(e)

    # Group entries by id_node to build TalentNode objects
    node_entries: Dict[int, List[TraitEntry]] = {}
    for e in filtered:
        node_entries.setdefault(e.id_node, []).append(e)

    nodes: Dict[int, TalentNode] = {}
    selection_nodes: Dict[int, TalentNode] = {}

    for id_node, elist in node_entries.items():
        # Sort by selection_index for consistent ordering
        elist.sort(key=lambda x: x.selection_index)
        first = elist[0]

        options = []
        for e in elist:
            opt = TalentNodeOption(
                id_trait_node_entry=e.id_trait_node_entry,
                id_trait_definition=e.id_trait_definition,
                id_spell=e.id_spell,
                id_replace_spell=e.id_replace_spell,
                id_override_spell=e.id_override_spell,
                max_ranks=e.max_ranks,
                selection_index=e.selection_index,
                name=e.name,
            )
            options.append(opt)

        node = TalentNode(
            id_node=id_node,
            tree_index=first.tree_index,
            node_type=first.node_type,
            row=first.row,
            col=first.col,
            req_points=first.req_points,
            id_sub_tree=first.id_sub_tree,
            id_class=first.id_class,
            id_spec=first.id_spec,
            id_spec_starter=first.id_spec_starter,
            options=options,
        )

        if first.tree_index == TREE_SELECTION:
            selection_nodes[id_node] = node
        else:
            nodes[id_node] = node

    # Build edges
    edges = _build_edges(nodes)

    # Build hero trees
    hero_trees: Dict[int, HeroTree] = {}
    for node in nodes.values():
        if node.tree_index == TREE_HERO and node.id_sub_tree != 0:
            st_id = node.id_sub_tree
            if st_id not in hero_trees:
                st_info = sub_trees.get(st_id, (f"SubTree-{st_id}", class_id))
                hero_trees[st_id] = HeroTree(
                    id_sub_tree=st_id,
                    name=st_info[0],
                    id_class=st_info[1],
                )
            hero_trees[st_id].node_ids.append(node.id_node)

    return TalentTree(
        spec_name=spec_name_lower,
        class_id=class_id,
        spec_id=spec_id,
        nodes=nodes,
        edges=edges,
        hero_trees=hero_trees,
        selection_nodes=selection_nodes,
    )


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    import sys

    spec = sys.argv[1] if len(sys.argv) > 1 else "warrior_fury"

    print(f"Building talent tree for: {spec}")
    print()

    tree = build_talent_tree(spec)
    print(tree.summary())
    print()

    # Print class tree nodes
    print("=== CLASS TREE ===")
    class_nodes = sorted(tree.class_nodes.values(), key=lambda n: (n.row, n.col))
    for node in class_nodes:
        choice_str = ""
        if node.is_choice():
            choice_str = f" [CHOICE: {' / '.join(node.names)}]"
        elif node.node_type == NODE_TIERED:
            choice_str = " [TIERED]"
        print(f"  Row {node.row:2d} Col {node.col:2d} | {node.name:40s} | ranks={node.max_ranks} req={node.req_points} spell={node.id_spell}{choice_str}")

    print()
    print("=== SPEC TREE ===")
    spec_nodes = sorted(tree.spec_nodes.values(), key=lambda n: (n.row, n.col))
    for node in spec_nodes:
        choice_str = ""
        if node.is_choice():
            choice_str = f" [CHOICE: {' / '.join(node.names)}]"
        print(f"  Row {node.row:2d} Col {node.col:2d} | {node.name:40s} | ranks={node.max_ranks} req={node.req_points} spell={node.id_spell}{choice_str}")

    if tree.hero_trees:
        for ht in tree.hero_trees.values():
            print()
            print(f"=== HERO TREE: {ht.name} (id={ht.id_sub_tree}) ===")
            hero_nodes = sorted(
                [tree.nodes[nid] for nid in ht.node_ids if nid in tree.nodes],
                key=lambda n: (n.row, n.col)
            )
            for node in hero_nodes:
                choice_str = ""
                if node.is_choice():
                    choice_str = f" [CHOICE: {' / '.join(node.names)}]"
                print(f"  Row {node.row:2d} Col {node.col:2d} | {node.name:40s} | ranks={node.max_ranks} spell={node.id_spell}{choice_str}")

    if tree.selection_nodes:
        print()
        print("=== SELECTION NODES ===")
        for node in tree.selection_nodes.values():
            print(f"  Node {node.id_node} | {' / '.join(node.names)} | sub_trees: {[o.selection_index for o in node.options]}")

    # Edge stats
    print()
    print(f"Total edges: {len(tree.edges)}")
    if tree.edges:
        print("Sample edges (first 10):")
        for edge in tree.edges[:10]:
            from_name = tree.nodes[edge.from_node].name if edge.from_node in tree.nodes else "?"
            to_name = tree.nodes[edge.to_node].name if edge.to_node in tree.nodes else "?"
            print(f"  {from_name} -> {to_name}")


if __name__ == "__main__":
    main()
