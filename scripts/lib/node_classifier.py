#!/usr/bin/env python3
"""Node Classifier — classify talent nodes as DPS / GATING / UTILITY.

Three-source classification:
1. APL scan: talents referenced in APL conditions
2. Code scan: talents referenced in class module damage calculations
"""

import os
import re
from enum import Enum
from typing import Dict, Set

from .talent_tree import TalentTree, build_talent_tree, SPEC_MAP


class DPSRelevance(Enum):
    DPS = "dps"
    GATING = "gating"
    UTILITY = "utility"


def _tokenize_name(name: str) -> str:
    return re.sub(r'[^a-z0-9]', '_', name.lower()).strip('_')


def classify_from_apl(apl_text: str, tree: TalentTree) -> Set[int]:
    """Find all talent references in APL conditions."""
    dps_nodes = set()
    for match in re.finditer(r'talent\.(\w+)', apl_text):
        talent_name = match.group(1).lower()
        for nid, node in tree.nodes.items():
            for opt in node.options:
                if _tokenize_name(opt.name) == talent_name:
                    dps_nodes.add(nid)
    return dps_nodes


def classify_from_code(spec_name: str, tree: TalentTree) -> Set[int]:
    """Grep class module for talent references in damage calculations."""
    dps_nodes = set()
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    class_name = spec_name.split('_')[0]
    module_map = {
        'warrior': 'sc_warrior.cpp', 'paladin': 'paladin/sc_paladin.cpp',
        'hunter': 'sc_hunter.cpp', 'rogue': 'sc_rogue.cpp',
        'priest': 'sc_priest.cpp', 'dk': 'sc_death_knight.cpp',
        'shaman': 'sc_shaman.cpp', 'mage': 'sc_mage.cpp',
        'warlock': 'warlock/sc_warlock.cpp', 'monk': 'sc_monk.cpp',
        'druid': 'sc_druid.cpp', 'dh': 'sc_demon_hunter.cpp',
        'evoker': 'sc_evoker.cpp',
    }
    
    module_file = module_map.get(class_name)
    if not module_file:
        return dps_nodes
    
    module_path = os.path.join(base, 'engine', 'class_modules', module_file)
    if not os.path.exists(module_path):
        return dps_nodes
    
    try:
        with open(module_path) as f:
            code = f.read()
    except:
        return dps_nodes
    
    for match in re.finditer(r'talent\.(?:spec|class_|hero)?\w*\.(\w+)', code):
        talent_ref = match.group(1).lower()
        for nid, node in tree.nodes.items():
            for opt in node.options:
                if _tokenize_name(opt.name) == talent_ref:
                    dps_nodes.add(nid)
    
    return dps_nodes


def classify_all_nodes(tree: TalentTree, apl_text: str = '', spec_name: str = '') -> Dict[int, DPSRelevance]:
    """Classify all nodes in a talent tree."""
    apl_dps = classify_from_apl(apl_text, tree) if apl_text else set()
    code_dps = classify_from_code(spec_name, tree) if spec_name else set()
    
    all_dps = apl_dps | code_dps
    
    gating = set()
    if hasattr(tree, 'edges'):
        edge_map = {}
        for edge in tree.edges:
            edge_map.setdefault(edge.to_node, []).append(edge.from_node)
        for nid in all_dps:
            for parent_id in edge_map.get(nid, []):
                if parent_id not in all_dps:
                    gating.add(parent_id)
    
    result = {}
    for nid in tree.nodes:
        if nid in all_dps:
            result[nid] = DPSRelevance.DPS
        elif nid in gating:
            result[nid] = DPSRelevance.GATING
        else:
            result[nid] = DPSRelevance.UTILITY
    
    return result


def get_pivot_nodes(tree: TalentTree, classification: Dict[int, DPSRelevance]) -> Set[int]:
    """Identify pivot nodes (rotation-changing) vs tuning nodes."""
    pivots = set()
    for nid, relevance in classification.items():
        if relevance != DPSRelevance.DPS:
            continue
        node = tree.nodes[nid]
        if node.node_type == 2:
            pivots.add(nid)
            continue
        for opt in node.options:
            if hasattr(opt, 'id_replace_spell') and opt.id_replace_spell != 0:
                pivots.add(nid)
                break
    return pivots
