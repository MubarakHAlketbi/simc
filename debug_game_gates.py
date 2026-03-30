#!/usr/bin/env python3
"""
Dissect the game's REAL gating system from DB2 tables.

The game uses:
- TraitNodeGroup: groups of nodes (a "gate tier")
- TraitNodeGroupXTraitNode: which nodes belong to each group
- TraitNodeGroupXTraitCond: conditions applied to each group
- TraitCond: the actual condition (CondType, SpentAmountRequired, etc.)

CondType values (from Blizzard UI code):
  0 = ???
  1 = Spent amount required (the gate!)
  2 = Quest required
  3 = Achievement required
  ...
"""

import csv, os, sys, re
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scripts.lib.talent_tree import SPEC_MAP
from scripts.lib.tree_codec_bridge import decode_profile_talents

BASE = "engine/dbc/generated"

# ── 1. Parse TraitCond ────────────────────────────────────────────────
conds = {}  # ID -> row
with open(f"{BASE}/TraitCond.csv") as f:
    for row in csv.DictReader(f):
        conds[int(row['ID'])] = row

# ── 2. Parse TraitNodeGroup ──────────────────────────────────────────
groups = {}  # ID -> row
with open(f"{BASE}/TraitNodeGroup.csv") as f:
    for row in csv.DictReader(f):
        groups[int(row['ID'])] = row

# ── 3. Parse TraitNodeGroupXTraitNode ────────────────────────────────
group_nodes = defaultdict(list)  # group_id -> [node_id, ...]
node_groups = defaultdict(list)  # node_id -> [group_id, ...]
with open(f"{BASE}/TraitNodeGroupXTraitNode.csv") as f:
    for row in csv.DictReader(f):
        gid = int(row['TraitNodeGroupID'])
        nid = int(row['TraitNodeID'])
        group_nodes[gid].append(nid)
        node_groups[nid].append(gid)

# ── 4. Parse TraitNodeGroupXTraitCond ────────────────────────────────
group_conds = defaultdict(list)  # group_id -> [cond_id, ...]
with open(f"{BASE}/TraitNodeGroupXTraitCond.csv") as f:
    for row in csv.DictReader(f):
        gid = int(row['TraitNodeGroupID'])
        cid = int(row['TraitCondID'])
        group_conds[gid].append(cid)

# ── 5. Parse TraitTree to get tree IDs ───────────────────────────────
trees = {}  # ID -> row
with open(f"{BASE}/TraitTree.csv") as f:
    for row in csv.DictReader(f):
        trees[int(row['ID'])] = row

# ── 6. Parse trait_data.inc to get node->tree mapping ────────────────
line_re = re.compile(
    r'\s*\{\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),'
    r'\s*(\d+),\s*(\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*"(.*?)",'
    r'\s*\{([^}]*)\},\s*\{([^}]*)\},\s*(\d+),\s*(\d+)'
)

node_info = {}  # node_id -> {name, req_points, tree_idx, class_id, row, ...}
with open(f"{BASE}/trait_data.inc") as f:
    for line in f:
        m = line_re.match(line)
        if not m:
            continue
        nid = int(m.group(4))
        if nid not in node_info:  # first entry for this node
            node_info[nid] = {
                'tree_idx': int(m.group(1)),
                'class_id': int(m.group(2)),
                'req_points': int(m.group(6)),
                'name': m.group(14),
                'row': int(m.group(11)),
            }

# ── 7. Find Warrior (class_id=1) gate conditions ─────────────────────
print("=" * 70)
print("WARRIOR GATE ANALYSIS (from DB2 TraitCond/TraitNodeGroup)")
print("=" * 70)

# First find which TraitTree IDs belong to Warrior
# Warrior class tree nodes have tree_idx=1, class_id=1
warrior_class_nodes = set()
warrior_spec_nodes = defaultdict(set)  # spec_name -> nodes
for nid, info in node_info.items():
    if info['class_id'] == 1:
        if info['tree_idx'] == 1:
            warrior_class_nodes.add(nid)
        elif info['tree_idx'] == 2:
            warrior_spec_nodes[info['tree_idx']].add(nid)

# Find groups that contain warrior nodes
warrior_groups = set()
for nid in warrior_class_nodes:
    for gid in node_groups.get(nid, []):
        warrior_groups.add(gid)

print(f"\nWarrior class tree nodes: {len(warrior_class_nodes)}")
print(f"Node groups containing warrior nodes: {len(warrior_groups)}")

# For each warrior group, show its gate condition
print(f"\n--- Gate conditions for warrior class tree ---\n")
for gid in sorted(warrior_groups):
    group = groups.get(gid, {})
    tree_id = group.get('TraitTreeID', '?')
    flags = group.get('Flags', '?')
    
    # Get conditions for this group
    cond_ids = group_conds.get(gid, [])
    
    # Get nodes in this group
    gnodes = group_nodes.get(gid, [])
    warrior_gnodes = [n for n in gnodes if n in warrior_class_nodes]
    
    if not warrior_gnodes:
        continue
    
    # Get gate info from conditions
    gate_info = []
    for cid in cond_ids:
        cond = conds.get(cid, {})
        cond_type = int(cond.get('CondType', 0))
        spent_req = int(cond.get('SpentAmountRequired', 0))
        spec_set = int(cond.get('SpecSetID', 0))
        grants = int(cond.get('GrantedRanks', 0))
        cond_flags = int(cond.get('Flags', 0))
        gate_info.append({
            'cond_id': cid, 'type': cond_type, 'spent': spent_req,
            'spec_set': spec_set, 'grants': grants, 'flags': cond_flags,
        })
    
    # Only show groups with spending gates
    spending_gates = [g for g in gate_info if g['type'] == 1]
    if spending_gates or True:  # Show all for now
        node_names = []
        for n in sorted(warrior_gnodes):
            info = node_info.get(n, {})
            node_names.append(f"{n}({info.get('name','?')},row={info.get('row','?')},req={info.get('req_points','?')})")
        
        print(f"Group {gid} (tree={tree_id}, flags={flags}):")
        print(f"  Nodes ({len(warrior_gnodes)}): {', '.join(node_names[:8])}")
        if len(warrior_gnodes) > 8:
            print(f"    ... and {len(warrior_gnodes) - 8} more")
        for g in gate_info:
            type_name = {0: "UNAVAILABLE", 1: "SPENT_AMOUNT", 2: "QUEST", 3: "ACHIEVEMENT", 
                        4: "LEVEL", 5: "GRANTED"}.get(g['type'], f"TYPE_{g['type']}")
            print(f"  Condition {g['cond_id']}: {type_name} spent={g['spent']} "
                  f"spec_set={g['spec_set']} grants={g['grants']} flags={g['flags']}")
        print()

# ── 8. Now do the SAME for Prot Warrior spec tree ────────────────────
print("\n" + "=" * 70)
print("PROT WARRIOR SPEC TREE GATES")
print("=" * 70)

# Prot warrior spec nodes
prot_spec_nodes = set()
for nid, info in node_info.items():
    if info['class_id'] == 1 and info['tree_idx'] == 2:
        # Check if spec is Prot (spec_id=73)
        prot_spec_nodes.add(nid)

prot_groups = set()
for nid in prot_spec_nodes:
    for gid in node_groups.get(nid, []):
        prot_groups.add(gid)

print(f"\nProt spec tree node groups: {len(prot_groups)}")

for gid in sorted(prot_groups):
    group = groups.get(gid, {})
    cond_ids = group_conds.get(gid, [])
    gnodes = [n for n in group_nodes.get(gid, []) if n in prot_spec_nodes]
    
    if not gnodes:
        continue
    
    gate_info = []
    for cid in cond_ids:
        cond = conds.get(cid, {})
        gate_info.append({
            'cond_id': cid,
            'type': int(cond.get('CondType', 0)),
            'spent': int(cond.get('SpentAmountRequired', 0)),
            'spec_set': int(cond.get('SpecSetID', 0)),
            'grants': int(cond.get('GrantedRanks', 0)),
            'flags': int(cond.get('Flags', 0)),
            'currency': int(cond.get('TraitCurrencyID', 0)),
        })
    
    spending_gates = [g for g in gate_info if g['spent'] > 0]
    if spending_gates:
        names = [f"{n}({node_info.get(n,{}).get('name','?')},row={node_info.get(n,{}).get('row','?')})" 
                 for n in sorted(gnodes)]
        print(f"\nGroup {gid}:")
        print(f"  Nodes: {', '.join(names[:6])}")
        if len(names) > 6:
            print(f"    ... and {len(names) - 6} more")
        for g in gate_info:
            type_name = {0: "UNAVAILABLE", 1: "SPENT_AMOUNT", 2: "QUEST", 3: "ACHIEVEMENT",
                        4: "LEVEL", 5: "GRANTED"}.get(g['type'], f"TYPE_{g['type']}")
            print(f"  Cond {g['cond_id']}: {type_name} spent={g['spent']} currency={g['currency']} "
                  f"spec_set={g['spec_set']} flags={g['flags']}")

# ── 9. Compare DB2 gates vs our req_points ────────────────────────────
print("\n" + "=" * 70)
print("COMPARISON: DB2 SpentAmountRequired vs trait_data.inc req_points")
print("=" * 70)

# For each node, compare the DB2 gate with our req_points
mismatches = []
for nid in sorted(warrior_class_nodes | prot_spec_nodes):
    our_req = node_info.get(nid, {}).get('req_points', 0)
    
    # Find DB2 gate for this node
    db2_gate = 0
    for gid in node_groups.get(nid, []):
        for cid in group_conds.get(gid, []):
            cond = conds.get(cid, {})
            if int(cond.get('CondType', 0)) == 1:  # SPENT_AMOUNT
                spent = int(cond.get('SpentAmountRequired', 0))
                if spent > db2_gate:
                    db2_gate = spent
    
    if our_req != db2_gate:
        name = node_info.get(nid, {}).get('name', '?')
        row = node_info.get(nid, {}).get('row', '?')
        tidx = node_info.get(nid, {}).get('tree_idx', '?')
        mismatches.append((nid, name, row, tidx, our_req, db2_gate))

print(f"\nMismatches: {len(mismatches)}")
for nid, name, row, tidx, ours, db2 in mismatches:
    tree = "CLASS" if tidx == 1 else "SPEC"
    print(f"  node {nid} ({name}, row={row}, {tree}): req_points={ours} DB2_gate={db2}")
