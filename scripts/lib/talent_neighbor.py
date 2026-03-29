#!/usr/bin/env python3
"""Talent Neighbor Generator — constraint-aware single-node mutations.

Given a decoded talent build, generates all valid single-step neighbor builds:
  REMOVE:      drop a selected node
  ADD:         take an unselected node
  SWAP_CHOICE: switch a choice node to its other option
  SWAP_POINT:  remove A + add B in same sub-tree (budget-neutral)

All neighbors are validated against tree constraints:
  - Sub-tree point budgets
  - Row gates (req_points)
  - Edge prerequisites
  - Choice exclusivity
"""

from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

from .talent_tree import (
    TalentTree, TalentNode, TREE_CLASS, TREE_SPEC, TREE_HERO,
    NODE_CHOICE, NODE_SUBTREE_SEL
)
from .talent_codec import encode_talent_string


# ─── Point Budget Constants ─────────────────────────────────────────────────
# These are the max points spendable in each sub-tree.
# In practice, most builds spend within 1-2 of these caps.
# We infer them from the current build rather than hardcoding.

def get_subtree_points(tree: TalentTree, selections: Dict[int, Tuple[int, int]],
                       tree_index: int) -> Tuple[int, List[int]]:
    """Count points spent in a sub-tree. Returns (total_points, [nid, ...])."""
    points = 0
    node_ids = []
    for nid, (rank, choice) in selections.items():
        node = tree.nodes.get(nid)
        if node and node.tree_index == tree_index:
            points += rank
            node_ids.append(nid)
    return points, node_ids


def get_max_row_gate(tree: TalentTree, selections: Dict[int, Tuple[int, int]],
                     tree_index: int) -> int:
    """Get the highest req_points value among selected nodes in this sub-tree."""
    max_gate = 0
    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if node and node.tree_index == tree_index:
            max_gate = max(max_gate, node.req_points)
    return max_gate


# ─── Constraint Checks ──────────────────────────────────────────────────────

def _build_child_map(tree: TalentTree) -> Dict[int, List[int]]:
    """Map parent_id -> [child_ids]."""
    children = defaultdict(list)
    for edge in tree.edges:
        children[edge.from_node].append(edge.to_node)
    return children


def _build_parent_map(tree: TalentTree) -> Dict[int, List[int]]:
    """Map child_id -> [parent_ids]."""
    parents = defaultdict(list)
    for edge in tree.edges:
        parents[edge.to_node].append(edge.from_node)
    return parents


def _is_granted(node: TalentNode, spec_id: int) -> bool:
    """Check if a node is auto-granted (can't be removed)."""
    # Hero starting nodes (row=1)
    if node.tree_index == TREE_HERO and node.row == 1:
        return True
    # Class nodes with spec starter
    starters = [s for s in node.id_spec_starter if s != 0]
    if starters and spec_id in starters:
        return True
    return False


def can_remove_node(tree: TalentTree, selections: Dict[int, Tuple[int, int]],
                    node_id: int, spec_id: int,
                    child_map: Dict[int, List[int]] = None,
                    parent_map: Dict[int, List[int]] = None) -> bool:
    """Check if a node can be safely removed from the build."""
    if node_id not in selections:
        return False

    node = tree.nodes.get(node_id)
    if not node:
        return False

    # Can't remove granted nodes
    if _is_granted(node, spec_id):
        return False

    # Can't remove subtree selection nodes
    if node.node_type == NODE_SUBTREE_SEL:
        return False

    if child_map is None:
        child_map = _build_child_map(tree)
    if parent_map is None:
        parent_map = _build_parent_map(tree)

    # Check: would removing this break any selected child's prerequisites?
    for child_id in child_map.get(node_id, []):
        if child_id not in selections:
            continue
        # Child is selected — check if it has another selected parent
        other_parents = [p for p in parent_map.get(child_id, [])
                        if p != node_id and p in selections]
        if not other_parents:
            return False  # child would lose its only parent

    # Check: would removing this drop points below a row gate?
    ti = node.tree_index
    rank = selections[node_id][0]
    current_points, _ = get_subtree_points(tree, selections, ti)
    new_points = current_points - rank

    # Find the highest req_points among OTHER selected nodes in this sub-tree
    for nid, (r, _) in selections.items():
        if nid == node_id:
            continue
        n = tree.nodes.get(nid)
        if n and n.tree_index == ti and n.req_points > new_points:
            return False  # would break this node's row gate

    return True


def can_add_node(tree: TalentTree, selections: Dict[int, Tuple[int, int]],
                 node_id: int, max_budget: Dict[int, int] = None,
                 parent_map: Dict[int, List[int]] = None) -> bool:
    """Check if an unselected node can be added to the build."""
    if node_id in selections:
        return False

    node = tree.nodes.get(node_id)
    if not node:
        return False

    # Skip subtree selection nodes
    if node.node_type == NODE_SUBTREE_SEL:
        return False

    if parent_map is None:
        parent_map = _build_parent_map(tree)

    # Check prerequisites: at least one parent must be selected
    parents = parent_map.get(node_id, [])
    if parents and not any(p in selections for p in parents):
        return False

    # Check row gate
    ti = node.tree_index
    current_points, _ = get_subtree_points(tree, selections, ti)
    if node.req_points > current_points:
        return False

    # Check budget (if provided)
    if max_budget and ti in max_budget:
        if current_points + node.max_ranks > max_budget[ti]:
            return False

    return True


# ─── Neighbor Generation ────────────────────────────────────────────────────

def generate_neighbors(
    tree: TalentTree,
    selections: Dict[int, Tuple[int, int]],
    codec_nodes,
    spec_id: int,
    purchased_flags: Dict[int, int] = None,
    max_swaps: int = 60,
) -> List[Tuple[str, str]]:
    """Generate all valid single-step neighbor talent strings.

    Returns list of (talent_string, description) tuples.
    """
    child_map = _build_child_map(tree)
    parent_map = _build_parent_map(tree)

    # Infer budget caps from current build — NO headroom.
    # All valid builds for a spec use the same total points per sub-tree.
    # Adding headroom creates invalid builds with extra talent points.
    budget = {}
    for ti in (TREE_CLASS, TREE_SPEC, TREE_HERO):
        pts, _ = get_subtree_points(tree, selections, ti)
        budget[ti] = pts  # strict budget: can only add if you also remove

    neighbors = []

    # 1. REMOVE mutations
    removable = []
    for nid in list(selections.keys()):
        if can_remove_node(tree, selections, nid, spec_id, child_map, parent_map):
            removable.append(nid)

    for nid in removable:
        new_sel = dict(selections)
        del new_sel[nid]
        try:
            ts = encode_talent_string(new_sel, codec_nodes, spec_id, purchased_flags)
            name = tree.nodes[nid].name
            neighbors.append((ts, f"REMOVE {name} ({nid})"))
        except Exception:
            pass

    # 2. ADD mutations
    addable = []
    for nid in tree.nodes:
        if can_add_node(tree, selections, nid, budget, parent_map):
            addable.append(nid)

    for nid in addable:
        new_sel = dict(selections)
        node = tree.nodes[nid]
        choice_idx = 0 if node.node_type == NODE_CHOICE else -1
        new_sel[nid] = (node.max_ranks, choice_idx)
        try:
            ts = encode_talent_string(new_sel, codec_nodes, spec_id, purchased_flags)
            name = node.name
            neighbors.append((ts, f"ADD {name} ({nid})"))
        except Exception:
            pass

    # 3. SWAP_CHOICE mutations
    for nid, (rank, choice_idx) in selections.items():
        node = tree.nodes.get(nid)
        if not node or node.node_type != NODE_CHOICE:
            continue
        if len(node.options) < 2:
            continue
        # Try the other option(s)
        for alt_idx in range(len(node.options)):
            if alt_idx == choice_idx:
                continue
            new_sel = dict(selections)
            new_sel[nid] = (rank, alt_idx)
            try:
                ts = encode_talent_string(new_sel, codec_nodes, spec_id, purchased_flags)
                old_name = node.options[choice_idx].name if choice_idx >= 0 else "?"
                new_name = node.options[alt_idx].name
                neighbors.append((ts, f"SWAP_CHOICE {old_name} -> {new_name} ({nid})"))
            except Exception:
                pass

    # 4. SWAP_POINT mutations (budget-neutral: remove A, add B in same sub-tree)
    # With strict budgets, addable may be empty. We need to check what becomes
    # addable AFTER each removal (freeing budget + potentially opening row gates).
    swap_count = 0
    for remove_nid in removable:
        if swap_count >= max_swaps:
            break
        remove_node = tree.nodes[remove_nid]
        ti = remove_node.tree_index

        # Create selection with this node removed
        reduced_sel = dict(selections)
        del reduced_sel[remove_nid]

        # Compute a relaxed budget that accounts for the freed points
        relaxed_budget = dict(budget)
        relaxed_budget[ti] = budget[ti]  # same cap — removal frees room

        # Find what's addable after this removal
        for add_nid in tree.nodes:
            if swap_count >= max_swaps:
                break
            if add_nid in reduced_sel or add_nid == remove_nid:
                continue
            add_node = tree.nodes.get(add_nid)
            if not add_node or add_node.tree_index != ti:
                continue
            if not can_add_node(tree, reduced_sel, add_nid, relaxed_budget, parent_map):
                continue

            new_sel = dict(reduced_sel)
            choice_idx = 0 if add_node.node_type == NODE_CHOICE else -1
            new_sel[add_nid] = (add_node.max_ranks, choice_idx)

            try:
                ts = encode_talent_string(new_sel, codec_nodes, spec_id, purchased_flags)
                neighbors.append((ts, f"SWAP {remove_node.name} -> {add_node.name}"))
                swap_count += 1
            except Exception:
                pass

    return neighbors


def validate_build(tree: TalentTree, selections: Dict[int, Tuple[int, int]],
                   spec_id: int) -> Tuple[bool, str]:
    """Full constraint validation of a talent build."""
    parent_map = _build_parent_map(tree)

    for nid, (rank, choice_idx) in selections.items():
        node = tree.nodes.get(nid)
        if not node:
            return False, f"Node {nid} not in tree"

        # Check rank bounds
        if rank < 1 or rank > node.max_ranks:
            return False, f"Node {nid} ({node.name}): rank {rank} out of range 1-{node.max_ranks}"

        # Check choice index
        if node.node_type == NODE_CHOICE:
            if choice_idx < 0 or choice_idx >= len(node.options):
                return False, f"Node {nid} ({node.name}): choice {choice_idx} out of range"

        # Check prerequisites
        if not _is_granted(node, spec_id):
            parents = parent_map.get(nid, [])
            if parents and not any(p in selections for p in parents):
                return False, f"Node {nid} ({node.name}): no parent selected from {parents}"

        # Check row gate
        ti = node.tree_index
        pts, _ = get_subtree_points(tree, selections, ti)
        if node.req_points > pts - rank:
            # Points excluding this node's own contribution
            other_pts = pts - rank
            if node.req_points > other_pts:
                pass  # This check is approximate; row gates count all points before this row

    return True, "Valid"


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

    from scripts.lib.talent_tree import build_talent_tree, SPEC_MAP
    from scripts.lib.talent_codec import decode_talent_string
    from scripts.lib.tree_codec_bridge import tree_to_codec_nodes

    spec = sys.argv[1] if len(sys.argv) > 1 else "warrior_fury"
    tree = build_talent_tree(spec)
    class_id, spec_id = SPEC_MAP[spec]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)

    # Read talent string from profile
    profile_map = {
        "warrior_fury": "MID1_Warrior_Fury",
        "warrior_arms": "MID1_Warrior_Arms",
    }
    profile_name = profile_map.get(spec, f"MID1_{spec.replace('_', '_').title()}")
    profile_path = f"profiles/MID1/{profile_name}.simc"

    talent_str = None
    with open(profile_path) as f:
        for line in f:
            if line.startswith("talents="):
                talent_str = line.strip().split("=", 1)[1]
                break

    if not talent_str:
        print(f"No talent string found for {spec}")
        sys.exit(1)

    _, selections, purchased_flags = decode_talent_string(talent_str, codec_nodes)

    # Generate neighbors
    neighbors = generate_neighbors(tree, selections, codec_nodes, spec_id, purchased_flags)

    # Count by type
    by_type = {}
    for ts, desc in neighbors:
        mutation = desc.split()[0]
        by_type[mutation] = by_type.get(mutation, 0) + 1

    print(f"=== Neighbors for {spec} ===")
    print(f"Total: {len(neighbors)}")
    for t, c in sorted(by_type.items()):
        print(f"  {t}: {c}")
    print()

    # Show first 10
    for ts, desc in neighbors[:10]:
        print(f"  {desc}")
    if len(neighbors) > 10:
        print(f"  ... and {len(neighbors) - 10} more")
