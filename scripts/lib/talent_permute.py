#!/usr/bin/env python3
"""Talent Permutation Engine — pivot sweep + tuning hill-climb."""

import itertools
from typing import Dict, Set, Tuple, Iterator

from .talent_tree import TalentTree, build_talent_tree, SPEC_MAP
from .talent_codec import encode_talent_string
from .tree_codec_bridge import tree_to_codec_nodes


def generate_pivot_combinations(tree: TalentTree, pivots: Set[int],
                                 base_selections: Dict[int, Tuple[int, int]],
                                 max_combos: int = 500) -> Iterator[Dict[int, Tuple[int, int]]]:
    """Generate talent builds by varying pivot nodes, fixing everything else."""
    pivot_options = {}
    for nid in pivots:
        node = tree.nodes.get(nid)
        if not node:
            continue
        options = [(0, -1)]  # not taken
        if node.node_type == 2:  # CHOICE
            for i in range(len(node.options)):
                options.append((1, i))
        else:
            for rank in range(1, node.max_ranks + 1):
                options.append((rank, -1))
        pivot_options[nid] = options

    pivot_ids = sorted(pivot_options.keys())
    option_lists = [pivot_options[nid] for nid in pivot_ids]

    count = 0
    for combo in itertools.product(*option_lists):
        if count >= max_combos:
            break
        build = dict(base_selections)
        for nid, (rank, choice) in zip(pivot_ids, combo):
            if rank > 0:
                build[nid] = (rank, choice)
            else:
                build.pop(nid, None)
        count += 1
        yield build


def tuning_hill_climb(tree: TalentTree, base_build: Dict[int, Tuple[int, int]],
                       tuning_nodes: Set[int], sim_func=None) -> Dict[int, Tuple[int, int]]:
    """Hill-climb tuning nodes. sim_func(build) -> composite_dps."""
    if sim_func is None:
        return base_build
    
    current = dict(base_build)
    current_dps = sim_func(current)
    
    improved = True
    while improved:
        improved = False
        for nid in sorted(tuning_nodes):
            node = tree.nodes.get(nid)
            if not node:
                continue
            original = current.get(nid)
            if nid not in current:
                current[nid] = (node.max_ranks, -1)
                new_dps = sim_func(current)
                if new_dps > current_dps * 1.001:
                    current_dps = new_dps
                    improved = True
                else:
                    current.pop(nid, None)
            else:
                del current[nid]
                new_dps = sim_func(current)
                if new_dps > current_dps * 1.001:
                    current_dps = new_dps
                    improved = True
                else:
                    current[nid] = original
    
    return current


def encode_build(build: Dict[int, Tuple[int, int]], spec_name: str,
                  purchased_flags: Dict[int, int] = None) -> str:
    """Encode a talent build to a SimC talent string."""
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    return encode_talent_string(build, codec_nodes, spec_id, purchased_flags)
