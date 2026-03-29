#!/usr/bin/env python3
"""
talent_validator.py — Validate and generate legal talent builds.

Uses real TraitEdge.csv prerequisite data + point budget enforcement
to ensure every build respects the talent tree constraints.

Two main APIs:
  - validate_build(): check if a build is legal, return errors
  - generate_neighbors(): yield valid 1-step mutations for hill-climbing
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple, Iterator
from collections import defaultdict

from .talent_tree import (
    TalentTree, TalentNode, build_talent_tree, SPEC_MAP,
    TREE_CLASS, TREE_SPEC, TREE_HERO, TREE_SELECTION,
    NODE_CHOICE, NODE_TIERED, NODE_NORMAL, NODE_SUBTREE_SEL,
)
from .tree_codec_bridge import (
    decode_profile_talents, encode_profile_talents,
)

# ─── Constants ────────────────────────────────────────────────────────────────

# Midnight expansion point budgets (level 90)
CLASS_POINT_BUDGET = 34
SPEC_POINT_BUDGET = 34
HERO_POINTS_GRANTED = 15  # all hero nodes auto-granted

# Undocumented granted nodes — always active, cost 0 points.
# These nodes have no id_spec_starter in the DBC but are granted in-game.
UNDOCUMENTED_GRANTS = {
    71933,  # Warlock Soul Leech — always granted for all warlock specs
}


# ─── Precomputed Tree Data ────────────────────────────────────────────────────

@dataclass
class TreeConstraints:
    """Precomputed constraint data for fast validation."""
    tree: TalentTree
    spec_id: int

    # Edge lookups
    parents_of: Dict[int, List[int]] = field(default_factory=dict)   # node -> [parent nodes]
    children_of: Dict[int, List[int]] = field(default_factory=dict)  # node -> [child nodes]

    # Node classification
    granted_nodes: Set[int] = field(default_factory=set)   # auto-granted (free) nodes
    class_nodes: Set[int] = field(default_factory=set)     # purchasable class tree nodes
    spec_nodes: Set[int] = field(default_factory=set)      # purchasable spec tree nodes
    hero_nodes: Dict[int, Set[int]] = field(default_factory=dict)  # sub_tree_id -> node set

    # Nodes with no incoming edges (roots, apex talents)
    root_nodes: Set[int] = field(default_factory=set)

    @staticmethod
    def build(spec_name: str) -> 'TreeConstraints':
        """Build constraint data for a spec."""
        tree = build_talent_tree(spec_name)
        _, spec_id = SPEC_MAP[spec_name.lower()]

        tc = TreeConstraints(tree=tree, spec_id=spec_id)

        # Build edge lookups
        for edge in tree.edges:
            tc.parents_of.setdefault(edge.to_node, []).append(edge.from_node)
            tc.children_of.setdefault(edge.from_node, []).append(edge.to_node)

        # Classify nodes
        for nid, node in tree.nodes.items():
            # Check if granted
            is_granted = False
            starters = [s for s in node.id_spec_starter if s != 0]
            if starters and spec_id in starters:
                is_granted = True
            elif node.tree_index == TREE_HERO and node.row == 1:
                is_granted = True
            elif nid in UNDOCUMENTED_GRANTS:
                is_granted = True

            if is_granted:
                tc.granted_nodes.add(nid)

            if node.tree_index == TREE_CLASS:
                if not is_granted:
                    tc.class_nodes.add(nid)
            elif node.tree_index == TREE_SPEC:
                tc.spec_nodes.add(nid)
            elif node.tree_index == TREE_HERO:
                st = node.id_sub_tree
                if st not in tc.hero_nodes:
                    tc.hero_nodes[st] = set()
                tc.hero_nodes[st].add(nid)

            # Root nodes = no incoming edges
            if nid not in tc.parents_of:
                tc.root_nodes.add(nid)

        return tc


# ─── Validator ────────────────────────────────────────────────────────────────

@dataclass
class ValidationResult:
    valid: bool
    errors: List[str] = field(default_factory=list)

    def __bool__(self):
        return self.valid


def validate_build(
    selections: Dict[int, Tuple[int, int]],
    tc: TreeConstraints,
) -> ValidationResult:
    """
    Validate a talent build against all tree constraints.

    Args:
        selections: dict of node_id -> (rank, choice_index)
                    choice_index is -1 for non-choice nodes
        tc: precomputed TreeConstraints

    Returns:
        ValidationResult with .valid bool and .errors list
    """
    errors = []
    tree = tc.tree

    # ── 1. Point budget ──────────────────────────────────────────────────
    class_pts = 0
    spec_pts = 0
    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if not node:
            continue
        if node.tree_index == TREE_CLASS and nid not in tc.granted_nodes:
            class_pts += rank
        elif node.tree_index == TREE_SPEC:
            spec_pts += rank

    if class_pts > CLASS_POINT_BUDGET:
        errors.append(f"Class points {class_pts} exceeds budget {CLASS_POINT_BUDGET}")
    if spec_pts > SPEC_POINT_BUDGET:
        errors.append(f"Spec points {spec_pts} exceeds budget {SPEC_POINT_BUDGET}")

    # ── 2. Rank validity ─────────────────────────────────────────────────
    for nid, (rank, choice_idx) in selections.items():
        node = tree.nodes.get(nid)
        if not node:
            # Selection nodes (hero tree picker) are in selection_nodes, not nodes
            if nid in tree.selection_nodes:
                continue  # Valid — hero tree selection
            errors.append(f"Node {nid} not found in tree")
            continue

        if node.node_type == NODE_TIERED:
            # Tiered: total max_ranks is sum of all options
            total_max = sum(o.max_ranks for o in node.options)
            if rank < 1 or rank > total_max:
                errors.append(f"{node.name}: rank {rank} out of range [1, {total_max}]")
        else:
            if rank < 1 or rank > node.max_ranks:
                errors.append(f"{node.name}: rank {rank} out of range [1, {node.max_ranks}]")

        # Choice node validation
        if node.node_type == NODE_CHOICE:
            if choice_idx < 0 or choice_idx >= len(node.options):
                errors.append(f"{node.name}: invalid choice index {choice_idx} (has {len(node.options)} options)")

    # ── 3. req_points gates ──────────────────────────────────────────────
    # Count points spent per sub-tree (class, spec)
    class_spent = 0
    spec_spent = 0
    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if not node:
            continue
        if node.tree_index == TREE_CLASS:
            # Granted nodes still count toward the gate threshold
            class_spent += rank
        elif node.tree_index == TREE_SPEC:
            spec_spent += rank

    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if not node or node.req_points == 0:
            continue
        # Skip selection nodes
        if nid in tree.selection_nodes:
            continue

        if node.tree_index == TREE_CLASS:
            if class_spent < node.req_points:
                # More precise: count points in nodes with LOWER req_points
                pts_before = sum(
                    r for n, (r, _) in selections.items()
                    if tree.nodes.get(n) and tree.nodes[n].tree_index == TREE_CLASS
                    and tree.nodes[n].req_points < node.req_points
                )
                # Include same-tier nodes? No — req_points means "points in earlier tiers"
                # Actually, req_points just means total points spent, so we use class_spent
                # But we need to exclude THIS node's own points from the check
                # The gate is: total class points (excluding this node) >= req_points
                # Actually in-game it's just: total points spent >= req_points (including granted)
                pass  # Use the simple check below

        if node.tree_index == TREE_CLASS and class_spent < node.req_points:
            errors.append(f"{node.name}: requires {node.req_points} class points, only {class_spent} spent")
        elif node.tree_index == TREE_SPEC and spec_spent < node.req_points:
            errors.append(f"{node.name}: requires {node.req_points} spec points, only {spec_spent} spent")

    # ── 4. Prerequisite edges ────────────────────────────────────────────
    for nid in selections:
        node = tree.nodes.get(nid)
        if not node:
            continue
        # Skip selection nodes
        if nid in tree.selection_nodes:
            continue

        # Skip nodes with no parent edges (roots, apex talents, etc.)
        parents = tc.parents_of.get(nid)
        if not parents:
            continue

        # At least ONE parent must be selected (OR logic)
        if not any(p in selections for p in parents):
            parent_names = [tree.nodes[p].name for p in parents if p in tree.nodes]
            errors.append(
                f"{node.name}: no prerequisite selected "
                f"(needs one of: {', '.join(parent_names)})"
            )

    return ValidationResult(valid=len(errors) == 0, errors=errors)


# ─── Point counting helpers ───────────────────────────────────────────────────

def count_points(
    selections: Dict[int, Tuple[int, int]],
    tc: TreeConstraints,
) -> Tuple[int, int, int]:
    """Return (class_purchased, spec_purchased, hero_points)."""
    tree = tc.tree
    cp = sp = hp = 0
    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if not node:
            continue
        if node.tree_index == TREE_CLASS:
            if nid not in tc.granted_nodes:
                cp += rank
            # Granted nodes don't count toward purchased budget
        elif node.tree_index == TREE_SPEC:
            sp += rank
        elif node.tree_index == TREE_HERO:
            hp += rank
    return cp, sp, hp


def points_spent_in_tree(
    selections: Dict[int, Tuple[int, int]],
    tree: TalentTree,
    tree_index: int,
) -> int:
    """Total points (including granted) spent in a sub-tree. Used for req_points checks."""
    total = 0
    for nid, (rank, _) in selections.items():
        node = tree.nodes.get(nid)
        if node and node.tree_index == tree_index:
            total += rank
    return total


# ─── Neighbor Generator ──────────────────────────────────────────────────────

def _is_removable(
    nid: int,
    selections: Dict[int, Tuple[int, int]],
    tc: TreeConstraints,
) -> bool:
    """
    Check if a node can be removed without breaking any child's prerequisites.
    A node is removable if every selected child has at least one OTHER selected parent.
    Also checks that removal doesn't break req_points gates for remaining nodes.
    """
    tree = tc.tree
    node = tree.nodes.get(nid)
    if not node:
        return False

    # Can't remove granted nodes
    if nid in tc.granted_nodes:
        return False

    # Check children: each selected child must have another parent still selected
    children = tc.children_of.get(nid, [])
    for child_id in children:
        if child_id not in selections:
            continue
        # Does this child have another selected parent?
        parents = tc.parents_of.get(child_id, [])
        other_parents = [p for p in parents if p != nid and p in selections]
        if not other_parents:
            return False  # Child would be orphaned

    # Check req_points: would removal break any remaining node's gate?
    rank = selections[nid][0]
    tree_idx = node.tree_index
    current_pts = points_spent_in_tree(selections, tree, tree_idx)
    new_pts = current_pts - rank

    for other_nid, (_, _) in selections.items():
        if other_nid == nid:
            continue
        other = tree.nodes.get(other_nid)
        if other and other.tree_index == tree_idx and other.req_points > 0:
            if new_pts < other.req_points:
                return False

    return True


def _can_add(
    nid: int,
    rank: int,
    choice_idx: int,
    selections: Dict[int, Tuple[int, int]],
    tc: TreeConstraints,
) -> bool:
    """Check if a node can be added to the build."""
    tree = tc.tree
    node = tree.nodes.get(nid)
    if not node:
        return False

    # Already selected?
    if nid in selections:
        return False

    # Budget check
    if node.tree_index == TREE_CLASS and nid not in tc.granted_nodes:
        cp, _, _ = count_points(selections, tc)
        if cp + rank > CLASS_POINT_BUDGET:
            return False
    elif node.tree_index == TREE_SPEC:
        _, sp, _ = count_points(selections, tc)
        if sp + rank > SPEC_POINT_BUDGET:
            return False

    # req_points check
    if node.req_points > 0:
        current_pts = points_spent_in_tree(selections, tree, node.tree_index)
        # New node's own points count toward the total, but req_points is checked
        # against points BEFORE adding this node (you need X points to unlock the tier)
        if current_pts < node.req_points:
            return False

    # Prerequisite check
    parents = tc.parents_of.get(nid)
    if parents:
        if not any(p in selections for p in parents):
            return False

    return True


def generate_neighbors(
    selections: Dict[int, Tuple[int, int]],
    tc: TreeConstraints,
    purchased_flags: Optional[Dict[int, int]] = None,
) -> Iterator[Tuple[str, Dict[int, Tuple[int, int]]]]:
    """
    Generate valid 1-step neighbor builds for hill-climbing.

    Yields (description, new_selections) tuples.
    Each neighbor differs by exactly one swap/toggle/choice change.

    Mutation types:
      - SWAP: remove one leaf + add one eligible node (same sub-tree)
      - CHOICE_SWAP: switch which option is selected in a choice node
      - RANK_CHANGE: adjust rank of a tiered node (up or down)
    """
    tree = tc.tree

    # ── Precompute removable set ─────────────────────────────────────────
    removable_class = []
    removable_spec = []
    for nid in selections:
        node = tree.nodes.get(nid)
        if not node:
            continue
        if not _is_removable(nid, selections, tc):
            continue
        if node.tree_index == TREE_CLASS and nid not in tc.granted_nodes:
            removable_class.append(nid)
        elif node.tree_index == TREE_SPEC:
            removable_spec.append(nid)

    # ── SWAP mutations (class tree) ──────────────────────────────────────
    for rm_nid in removable_class:
        rm_node = tree.nodes[rm_nid]
        rm_rank = selections[rm_nid][0]

        # Build without this node
        trial = dict(selections)
        del trial[rm_nid]

        # Find all eligible additions in class tree
        for add_nid in tc.class_nodes:
            if add_nid in trial or add_nid == rm_nid:
                continue
            add_node = tree.nodes[add_nid]
            add_rank = add_node.max_ranks
            choice_idx = -1
            if add_node.node_type == NODE_CHOICE:
                add_rank = 1
                choice_idx = 0  # Default to first choice

            if _can_add(add_nid, add_rank, choice_idx, trial, tc):
                new_build = dict(trial)
                new_build[add_nid] = (add_rank, choice_idx)
                desc = f"swap_class: -{rm_node.name} +{add_node.name}"
                yield desc, new_build

    # ── SWAP mutations (spec tree) ───────────────────────────────────────
    for rm_nid in removable_spec:
        rm_node = tree.nodes[rm_nid]
        rm_rank = selections[rm_nid][0]

        trial = dict(selections)
        del trial[rm_nid]

        for add_nid in tc.spec_nodes:
            if add_nid in trial or add_nid == rm_nid:
                continue
            add_node = tree.nodes[add_nid]
            add_rank = add_node.max_ranks
            choice_idx = -1
            if add_node.node_type == NODE_CHOICE:
                add_rank = 1
                choice_idx = 0

            if _can_add(add_nid, add_rank, choice_idx, trial, tc):
                new_build = dict(trial)
                new_build[add_nid] = (add_rank, choice_idx)
                desc = f"swap_spec: -{rm_node.name} +{add_node.name}"
                yield desc, new_build

    # ── CHOICE_SWAP mutations ────────────────────────────────────────────
    for nid, (rank, choice_idx) in selections.items():
        node = tree.nodes.get(nid)
        if not node or node.node_type != NODE_CHOICE:
            continue
        for alt_idx in range(len(node.options)):
            if alt_idx == choice_idx:
                continue
            new_build = dict(selections)
            new_build[nid] = (rank, alt_idx)
            alt_name = node.options[alt_idx].name
            desc = f"choice_swap: {node.name} -> {alt_name}"
            yield desc, new_build

    # ── RANK_CHANGE mutations (tiered nodes) ─────────────────────────────
    for nid, (rank, choice_idx) in selections.items():
        node = tree.nodes.get(nid)
        if not node or node.node_type != NODE_TIERED:
            continue
        if nid in tc.granted_nodes:
            continue

        total_max = sum(o.max_ranks for o in node.options)

        # Rank down (frees a point)
        if rank > 1:
            new_build = dict(selections)
            new_build[nid] = (rank - 1, choice_idx)
            # Check req_points aren't broken
            result = validate_build(new_build, tc)
            if result.valid:
                desc = f"rank_down: {node.name} {rank}->{rank-1}"
                yield desc, new_build

        # Rank up (costs a point)
        if rank < total_max:
            new_build = dict(selections)
            new_build[nid] = (rank + 1, choice_idx)
            result = validate_build(new_build, tc)
            if result.valid:
                desc = f"rank_up: {node.name} {rank}->{rank+1}"
                yield desc, new_build


# ─── Convenience ──────────────────────────────────────────────────────────────

def validate_profile(profile_path: str, spec_name: str) -> ValidationResult:
    """Validate a .simc profile's talent build."""
    talent_str = None
    with open(profile_path) as f:
        for line in f:
            if line.startswith("talents="):
                talent_str = line.strip().split("=", 1)[1]
                break

    if not talent_str:
        return ValidationResult(valid=False, errors=["No talents= line found"])

    tc = TreeConstraints.build(spec_name)
    selections = decode_profile_talents(talent_str, spec_name)
    return validate_build(selections, tc)


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    import sys
    import glob

    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        # Validate all profiles
        profiles = sorted(glob.glob("profiles/MID1/MID1_*.simc"))
        pass_count = 0
        fail_count = 0

        for p in profiles:
            basename = os.path.basename(p)
            # Extract spec from profile
            with open(p) as f:
                spec_line = None
                class_line = None
                for line in f:
                    if line.startswith("spec="):
                        spec_line = line.strip().split("=", 1)[1]
                    if line.startswith("class=") or line.strip().startswith('"class='):
                        # Handle class= which might be quoted
                        class_line = line.strip().replace('"', '').split("=", 1)[1]

            if not spec_line:
                print(f"  SKIP  {basename} (no spec= line)")
                continue

            # Find matching spec_name
            found = None
            for s in SPEC_MAP:
                parts = s.split("_")
                if spec_line.lower() == parts[-1] or spec_line.lower() == s.split("_", 1)[-1]:
                    found = s
                    break

            if not found:
                # Try harder
                for s in SPEC_MAP:
                    if spec_line.lower() in s:
                        found = s
                        break

            if not found:
                print(f"  SKIP  {basename} (can't map spec={spec_line})")
                continue

            result = validate_profile(p, found)
            if result.valid:
                tc = TreeConstraints.build(found)
                sel = decode_profile_talents(
                    open(p).read().split("talents=")[1].split("\n")[0].strip(),
                    found,
                )
                cp, sp, hp = count_points(sel, tc)
                print(f"  PASS  {basename:50s}  class={cp:2d}/34  spec={sp:2d}/34  hero={hp:2d}")
                pass_count += 1
            else:
                print(f"  FAIL  {basename}")
                for err in result.errors[:5]:
                    print(f"        {err}")
                fail_count += 1

        print(f"\n{pass_count} passed, {fail_count} failed out of {pass_count + fail_count}")

    elif len(sys.argv) > 1:
        # Validate single spec and show neighbors
        spec = sys.argv[1]
        tc = TreeConstraints.build(spec)

        # Load from profile
        profile_map = {
            s: f"profiles/MID1/MID1_{'_'.join(w.title() for w in s.split('_'))}.simc"
            for s in SPEC_MAP
        }
        # Handle special names
        profile_map["dk_blood"] = "profiles/MID1/MID1_Death_Knight_Blood.simc"
        profile_map["dk_frost"] = "profiles/MID1/MID1_Death_Knight_Frost.simc"
        profile_map["dk_unholy"] = "profiles/MID1/MID1_Death_Knight_Unholy.simc"
        profile_map["dh_havoc"] = "profiles/MID1/MID1_Demon_Hunter_Havoc.simc"
        profile_map["dh_vengeance"] = "profiles/MID1/MID1_Demon_Hunter_Vengeance.simc"
        profile_map["dh_devourer"] = "profiles/MID1/MID1_Demon_Hunter_Devourer.simc"
        profile_map["hunter_bm"] = "profiles/MID1/MID1_Hunter_Beast_Mastery.simc"
        profile_map["hunter_mm"] = "profiles/MID1/MID1_Hunter_Marksmanship.simc"

        ppath = profile_map.get(spec)
        if not ppath or not os.path.exists(ppath):
            print(f"Profile not found for {spec}")
            return

        with open(ppath) as f:
            for line in f:
                if line.startswith("talents="):
                    talent_str = line.strip().split("=", 1)[1]
                    break

        selections = decode_profile_talents(talent_str, spec)
        result = validate_build(selections, tc)
        cp, sp, hp = count_points(selections, tc)

        print(f"Spec: {spec}")
        print(f"Points: class={cp}/34  spec={sp}/34  hero={hp}")
        print(f"Valid: {result.valid}")
        if result.errors:
            for err in result.errors:
                print(f"  ERROR: {err}")

        # Count neighbors
        neighbor_count = 0
        for desc, _ in generate_neighbors(selections, tc):
            neighbor_count += 1
        print(f"Valid neighbors: {neighbor_count}")

    else:
        print("Usage:")
        print("  python -m scripts.lib.talent_validator --all")
        print("  python -m scripts.lib.talent_validator warrior_fury")


if __name__ == "__main__":
    main()
