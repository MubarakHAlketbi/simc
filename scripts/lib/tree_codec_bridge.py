#!/usr/bin/env python3
"""Bridge between talent_tree.py and talent_codec.py.

Converts TalentTree objects to the OrderedDict format expected by the codec,
and provides high-level decode/encode functions.
"""

from collections import OrderedDict
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from .talent_tree import (TalentTree, TalentNode, TalentNodeOption, SPEC_MAP,
                          build_talent_tree, TREE_CLASS, TREE_SPEC, TREE_HERO, TREE_SELECTION)
from .talent_codec import decode_talent_string, encode_talent_string, validate_roundtrip

import os
import re


@dataclass
class _CodecEntry:
    """Adapter that makes TalentNodeOption look like what talent_codec expects."""
    node_type: int
    max_ranks: int
    id_trait_node_entry: int
    is_granted: bool = False


def _build_all_class_nodes(class_id: int, spec_id: int) -> OrderedDict:
    """Build codec nodes from ALL DBC entries for a class (not filtered by spec).
    
    CRITICAL: SimC's generate_tree_nodes() iterates ALL traits for a class across
    all talent_tree types. It does NOT filter by spec. The bitstream includes bits
    for every node in the class, even those not available to the current spec.
    Our tree builder filters by spec, which causes bitstream position mismatch.
    
    This function parses trait_data.inc directly to get the complete node set.
    """
    # Find trait_data.inc
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    trait_path = os.path.join(base, "engine", "dbc", "generated", "trait_data.inc")
    
    # Parse regex for each line
    line_re = re.compile(
        r'\s*\{\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),'
        r'\s*(\d+),\s*(\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*"(.*?)",'
        r'\s*\{([^}]*)\},\s*\{([^}]*)\},\s*(\d+),\s*(\d+)'
    )
    
    # Group entries by id_node (like SimC's std::map)
    from collections import defaultdict
    node_entries = defaultdict(list)
    
    with open(trait_path) as f:
        for line in f:
            m = line_re.match(line)
            if not m:
                continue
            tree_idx = int(m.group(1))
            cid = int(m.group(2))
            
            if cid != class_id:
                continue
            # SimC iterates talent_tree::INVALID(0) to MAX(5), but only 1-4 have real data
            if tree_idx not in (TREE_CLASS, TREE_SPEC, TREE_HERO, TREE_SELECTION):
                continue
            
            id_node = int(m.group(4))
            max_ranks = int(m.group(5))
            node_type = int(m.group(18))
            id_trait_node_entry = int(m.group(3))
            
            # Parse row/col for hero grant check
            row = int(m.group(11))
            col = int(m.group(12))
            
            # Parse id_spec_starter to check granted status
            starter_str = m.group(16).strip()
            starters = [int(x.strip()) for x in starter_str.split(',') if x.strip()]
            # Parse id_spec for hero availability check
            spec_str = m.group(15).strip()
            id_specs = [int(x.strip()) for x in spec_str.split(',') if x.strip()]
            id_sub_tree = int(m.group(17))
            
            # SimC's is_granted() logic (from trait_data.cpp:261-276):
            # 1. Hero talent starting node: granted when hero tree selected
            #    C++ checks row==1 && col==1 but in Midnight DBC build 12.0.1.66384,
            #    hero starting nodes are at (row=1, col=3). We check row==1 which is
            #    the root row of all hero sub-trees.
            # 2. Class talent with spec in id_spec_starter: granted
            is_granted = False
            if tree_idx == TREE_HERO and row == 1:
                # Starting hero node — auto-granted when hero path selected
                is_granted = True
            elif starters and spec_id in [s for s in starters if s != 0]:
                is_granted = True
            
            entry = _CodecEntry(
                node_type=node_type,
                max_ranks=max_ranks,
                id_trait_node_entry=id_trait_node_entry,
                is_granted=is_granted,
            )
            node_entries[id_node].append((entry, 0))
    
    # Sort by id_node (ascending) to match SimC's std::map iteration
    result = OrderedDict()
    for node_id in sorted(node_entries.keys()):
        result[node_id] = node_entries[node_id]
    
    return result


def tree_to_codec_nodes(tree: TalentTree, spec_id: int) -> OrderedDict:
    """Convert a TalentTree to the OrderedDict format expected by talent_codec.
    
    Uses _build_all_class_nodes() to get ALL class nodes (not just spec-filtered),
    matching SimC's bitstream layout exactly.
    """
    return _build_all_class_nodes(tree.class_id, spec_id)


def decode_profile_talents(talent_str: str, spec_name: str) -> Dict[int, Tuple[int, int]]:
    """High-level: decode a talent string given a spec name.
    
    Returns dict of node_id -> (rank, choice_index).
    """
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    _, selections, _ = decode_talent_string(talent_str, codec_nodes)
    return selections


def encode_profile_talents(selections: Dict[int, Tuple[int, int]], spec_name: str,
                           purchased_flags: Optional[Dict[int, int]] = None) -> str:
    """High-level: encode talent selections to a talent string."""
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    return encode_talent_string(selections, codec_nodes, spec_id, purchased_flags)


def validate_profile_roundtrip(talent_str: str, spec_name: str) -> Tuple[bool, str]:
    """High-level: validate round-trip encoding for a profile talent string."""
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    try:
        spec, selections, purchased_flags = decode_talent_string(talent_str, codec_nodes)
        reencoded = encode_talent_string(selections, codec_nodes, spec_id, purchased_flags)
        if reencoded == talent_str:
            return True, "Round-trip successful"
        else:
            for i in range(min(len(talent_str), len(reencoded))):
                if talent_str[i] != reencoded[i]:
                    return False, f"Mismatch at position {i}/{len(talent_str)}"
            return False, f"Length mismatch: {len(talent_str)} vs {len(reencoded)}"
    except Exception as e:
        return False, f"Error: {e}"


def get_selected_talent_names(talent_str: str, spec_name: str) -> List[str]:
    """Decode a talent string and return human-readable talent names."""
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    _, selections, _ = decode_talent_string(talent_str, codec_nodes)
    
    names = []
    for node_id, (rank, choice_idx) in sorted(selections.items()):
        node = tree.nodes.get(node_id)
        if node:
            if choice_idx >= 0 and choice_idx < len(node.options):
                name = node.options[choice_idx].name
            else:
                name = node.name
            names.append(f"{name} (rank {rank})")
    return names


def modify_talent(talent_str: str, spec_name: str, 
                  node_id: int, new_rank: int, new_choice: int = -1) -> str:
    """Modify a single talent node in an existing talent string.
    
    Returns the new talent string with the modification applied.
    """
    tree = build_talent_tree(spec_name)
    class_id, spec_id = SPEC_MAP[spec_name]
    codec_nodes = tree_to_codec_nodes(tree, spec_id)
    _, selections, purchased_flags = decode_talent_string(talent_str, codec_nodes)
    
    if new_rank <= 0:
        selections.pop(node_id, None)
    else:
        selections[node_id] = (new_rank, new_choice)
    
    return encode_talent_string(selections, codec_nodes, spec_id, purchased_flags)


if __name__ == "__main__":
    import sys
    
    spec = sys.argv[1] if len(sys.argv) > 1 else "warrior_fury"
    
    # Read talent string from profile
    profile_map = {
        "warrior_fury": "MID1_Warrior_Fury",
        "warrior_arms": "MID1_Warrior_Arms",
        "warrior_protection": "MID1_Warrior_Protection",
    }
    
    # Try to read from profile
    profile_name = profile_map.get(spec, f"MID1_{spec.replace('_', '_').title()}")
    profile_path = f"profiles/MID1/{profile_name}.simc"
    
    talent_str = None
    try:
        with open(profile_path) as f:
            for line in f:
                if line.startswith("talents="):
                    talent_str = line.strip().split("=", 1)[1]
                    break
    except FileNotFoundError:
        pass
    
    if talent_str:
        print(f"Testing round-trip for {spec}...")
        print(f"  Talent string: {talent_str[:60]}...")
        success, msg = validate_profile_roundtrip(talent_str, spec)
        print(f"  Result: {'PASS' if success else 'FAIL'}")
        if not success:
            print(f"  {msg}")
        
        print(f"\nSelected talents ({spec}):")
        for name in get_selected_talent_names(talent_str, spec):
            print(f"  - {name}")
    else:
        print(f"Could not find talent string for {spec}")
