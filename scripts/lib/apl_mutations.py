"""APL Mutation Generators — produce candidate APL variants for optimization."""

import re
from typing import Iterator
from .apl_parser import APL, APLAction, swap_actions, move_action, add_condition, modify_threshold


def _is_mutable_action(action: APLAction) -> bool:
    """Actions that should be considered for mutations."""
    # Skip variable definitions, auto_attack, call_action_list routing
    if action.is_variable:
        return False
    if action.action in ("auto_attack", "snapshot_stats", "potion", "use_items"):
        return False
    if action.action in ("blood_fury", "berserking", "fireblood", "ancestral_call",
                         "lights_judgment", "bag_of_tricks"):
        return False
    return True


def _is_routing_action(action: APLAction) -> bool:
    """Actions that route to sub-lists."""
    return action.is_call


def _extract_numeric_thresholds(condition: str) -> list[tuple[str, str, float]]:
    """Extract numeric thresholds from a condition.
    
    Returns: [(full_match, operator+number, numeric_value), ...]
    """
    results = []
    for m in re.finditer(r'([<>=!]+)(\d+(?:\.\d+)?)', condition):
        op = m.group(1)
        num_str = m.group(2)
        try:
            num = float(num_str)
            results.append((m.group(0), num_str, num))
        except ValueError:
            pass
    return results


# ============================================================
# M1: Adjacent Swap
# ============================================================

def generate_adjacent_swaps(
    apl: APL,
    action_ranking: dict[str, float],
    max_candidates: int = 15,
) -> Iterator[tuple[APL, str]]:
    """M1: Swap adjacent actions within the same sub-list.
    
    Prioritizes swaps involving high-damage actions.
    """
    candidates = []
    
    for list_name, actions in apl.lists.items():
        for i in range(len(actions) - 1):
            a, b = actions[i], actions[i + 1]
            if not _is_mutable_action(a) or not _is_mutable_action(b):
                continue
            if _is_routing_action(a) or _is_routing_action(b):
                continue
            
            # Score by combined damage contribution
            score = (action_ranking.get(a.action, 0) + 
                    action_ranking.get(b.action, 0))
            candidates.append((list_name, i, i + 1, score,
                              f"M1: swap {list_name}[{i}] {a.action} <-> [{i+1}] {b.action}"))
    
    # Sort by score descending, take top N
    candidates.sort(key=lambda x: -x[3])
    for list_name, idx_a, idx_b, _, desc in candidates[:max_candidates]:
        yield swap_actions(apl, list_name, idx_a, idx_b), desc


# ============================================================
# M4: Threshold Sweep
# ============================================================

def generate_threshold_sweeps(
    apl: APL,
    action_ranking: dict[str, float],
    max_candidates: int = 21,
) -> Iterator[tuple[APL, str]]:
    """M4: Vary numeric thresholds ±30% in 10% steps."""
    candidates = []
    
    for list_name, actions in apl.lists.items():
        for i, action in enumerate(actions):
            if not action.conditions or not _is_mutable_action(action):
                continue
            
            thresholds = _extract_numeric_thresholds(action.conditions)
            score = action_ranking.get(action.action, 0)
            
            for full_match, num_str, num_val in thresholds:
                if num_val == 0 or num_val > 1000:
                    continue  # skip zeros and huge numbers
                
                # Generate sweep values: -30%, -20%, -10%, +10%, +20%, +30%
                for pct in [-30, -20, -10, 10, 20, 30]:
                    new_val = num_val * (1 + pct / 100)
                    if num_val == int(num_val):
                        new_str = str(int(round(new_val)))
                    else:
                        new_str = f"{new_val:.1f}"
                    
                    if new_str == num_str:
                        continue
                    
                    candidates.append((
                        list_name, i, num_str, new_str, score,
                        f"M4: {list_name}[{i}] {action.action} threshold {num_str}->{new_str} ({pct:+d}%)"
                    ))
    
    # Sort by action importance
    candidates.sort(key=lambda x: -x[4])
    for list_name, idx, old_val, new_val, _, desc in candidates[:max_candidates]:
        yield modify_threshold(apl, list_name, idx, old_val, new_val), desc


# ============================================================
# M5: Action Promotion/Demotion
# ============================================================

def generate_promotions(
    apl: APL,
    action_ranking: dict[str, float],
    max_candidates: int = 20,
) -> Iterator[tuple[APL, str]]:
    """M5: Move high-damage actions up by 1-3 positions."""
    candidates = []
    
    for list_name, actions in apl.lists.items():
        for i, action in enumerate(actions):
            if not _is_mutable_action(action):
                continue
            if _is_routing_action(action):
                continue
            
            score = action_ranking.get(action.action, 0)
            
            # Try promoting by 1, 2, 3 positions
            for delta in [1, 2, 3]:
                new_pos = i - delta
                if new_pos < 0:
                    continue
                # Don't promote past routing/variable actions
                if any(actions[j].is_variable or _is_routing_action(actions[j])
                       for j in range(new_pos, i)):
                    continue
                
                candidates.append((
                    list_name, i, new_pos, score,
                    f"M5: promote {list_name}[{i}] {action.action} to [{new_pos}] (-{delta})"
                ))
    
    candidates.sort(key=lambda x: -x[3])
    for list_name, from_idx, to_idx, _, desc in candidates[:max_candidates]:
        yield move_action(apl, list_name, from_idx, to_idx), desc


# ============================================================
# M6: Sub-list Routing Changes
# ============================================================

def generate_routing_changes(
    apl: APL,
    max_candidates: int = 10,
) -> Iterator[tuple[APL, str]]:
    """M6: Modify AoE routing thresholds."""
    for list_name, actions in apl.lists.items():
        for i, action in enumerate(actions):
            if not _is_routing_action(action):
                continue
            if not action.conditions:
                continue
            
            # Look for active_enemies>=N patterns
            for m in re.finditer(r'active_enemies>=(\d+)', action.conditions):
                threshold = int(m.group(1))
                for new_thresh in [threshold - 1, threshold + 1]:
                    if new_thresh < 2:
                        continue
                    new_apl = apl.copy()
                    act = new_apl.lists[list_name][i]
                    act.conditions = act.conditions.replace(
                        f"active_enemies>={threshold}",
                        f"active_enemies>={new_thresh}"
                    )
                    yield new_apl, f"M6: {list_name}[{i}] AoE threshold {threshold}->{new_thresh}"
            
            # Also try active_enemies<N
            for m in re.finditer(r'active_enemies<(\d+)', action.conditions):
                threshold = int(m.group(1))
                for new_thresh in [threshold - 1, threshold + 1]:
                    if new_thresh < 2:
                        continue
                    new_apl = apl.copy()
                    act = new_apl.lists[list_name][i]
                    act.conditions = act.conditions.replace(
                        f"active_enemies<{threshold}",
                        f"active_enemies<{new_thresh}"
                    )
                    yield new_apl, f"M6: {list_name}[{i}] ST threshold {threshold}->{new_thresh}"


# ============================================================
# Master Generator
# ============================================================

def generate_all_mutations(
    apl: APL,
    action_ranking: dict[str, float],
    max_total: int = 70,
) -> list[tuple[APL, str]]:
    """Generate all mutation candidates, prioritized.
    
    Returns list of (mutated_apl, description) tuples.
    """
    candidates = []
    
    # M1: Adjacent swaps (most conservative, likely to find small gains)
    for c in generate_adjacent_swaps(apl, action_ranking, max_candidates=15):
        candidates.append(c)
    
    # M5: Promotions (can find bigger gains by large position changes)
    for c in generate_promotions(apl, action_ranking, max_candidates=20):
        candidates.append(c)
    
    # M4: Threshold sweeps (fine-tuning)
    for c in generate_threshold_sweeps(apl, action_ranking, max_candidates=21):
        candidates.append(c)
    
    # M6: Routing changes (AoE breakpoints)
    for c in generate_routing_changes(apl, max_candidates=10):
        candidates.append(c)
    
    return candidates[:max_total]


if __name__ == "__main__":
    from .apl_parser import parse_apl
    
    sample = """
actions=auto_attack
actions+=/call_action_list,name=st,if=active_enemies<3
actions+=/call_action_list,name=aoe,if=active_enemies>=3
actions.st=rampage,if=rage>=80
actions.st+=/bloodthirst
actions.st+=/execute,if=target.health.pct<35
actions.st+=/raging_blow
"""
    apl = parse_apl(sample)
    ranking = {"rampage": 5000000, "bloodthirst": 3000000, "execute": 2000000, "raging_blow": 500000}
    
    mutations = generate_all_mutations(apl, ranking)
    print(f"Generated {len(mutations)} mutations:")
    for _, desc in mutations:
        print(f"  {desc}")
