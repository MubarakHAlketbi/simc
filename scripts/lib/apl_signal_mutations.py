"""APL Signal Mutation Generators — Layer 2 targeted mutation generation.

Translates OptimizationSignal objects into concrete APL mutations (APL, description)
tuples that share the same interface as the blind mutation generators in apl_mutations.py.

Signal → Mutation mapping:
  aps_inversion   → non-adjacent promote (target above blocker)
  buff_waste      → promote consumer, add buff.react gate, upgrade .up→.react
  resource_overcap → lower spender threshold, add emergency dump
  interval_gap    → promote target by larger delta
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from .apl_parser import (
    APL, APLAction,
    move_action, insert_action, replace_condition,
    append_or_condition, make_action, add_condition, modify_threshold,
)
from .apl_signal_extractor import OptimizationSignal

if TYPE_CHECKING:
    pass


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_first(apl: APL, action_name: str,
                skip_lists: tuple[str, ...] = ("precombat", "variables")) -> tuple[str, int] | None:
    """Return (list_name, idx) of first occurrence of action_name, skipping utility lists."""
    for list_name, actions in apl.lists.items():
        if list_name in skip_lists:
            continue
        for i, act in enumerate(actions):
            if act.action == action_name:
                return list_name, i
    return None


def _find_all(apl: APL, action_name: str,
              skip_lists: tuple[str, ...] = ("precombat", "variables")) -> list[tuple[str, int]]:
    results = []
    for list_name, actions in apl.lists.items():
        if list_name in skip_lists:
            continue
        for i, act in enumerate(actions):
            if act.action == action_name:
                results.append((list_name, i))
    return results


def _find_blocker_position(apl: APL, list_name: str,
                           target_idx: int, blocker_name: str) -> int | None:
    """Find the position of blocker_name in list_name that is before target_idx."""
    actions = apl.lists.get(list_name, [])
    for i, act in enumerate(actions):
        if i >= target_idx:
            break
        if act.action == blocker_name:
            return i
    return None


def _extract_resource_thresholds(condition: str, resource: str) -> list[tuple[str, float]]:
    """Extract 'resource>=X' or 'resource>X' patterns, return [(full_match, value)]."""
    results = []
    for m in re.finditer(rf'\b{re.escape(resource)}\s*[>]=?\s*(\d+(?:\.\d+)?)', condition):
        try:
            results.append((m.group(0), float(m.group(1))))
        except ValueError:
            pass
    return results


# ---------------------------------------------------------------------------
# S-M1: Non-Adjacent Promote (APS Inversion)
# ---------------------------------------------------------------------------

def mutations_aps_inversion(signal: OptimizationSignal, apl: APL) -> list[tuple[APL, str]]:
    """Move target_action directly above blocker_action in the same list."""
    results = []
    if not signal.target_action or not signal.blocker_action:
        return results

    # Find target and blocker in every sub-list they share
    for list_name, actions in apl.lists.items():
        target_positions = [i for i, a in enumerate(actions) if a.action == signal.target_action]
        blocker_positions = [i for i, a in enumerate(actions) if a.action == signal.blocker_action]
        for tidx in target_positions:
            for bidx in blocker_positions:
                if tidx > bidx:  # target is after blocker — that's the inversion
                    new_apl = move_action(apl, list_name, tidx, bidx)
                    results.append((new_apl,
                        f"S-M1: promote {signal.target_action} above {signal.blocker_action} "
                        f"in {list_name} (APS inversion, gap={signal.priority:.2f})"))
    return results


# ---------------------------------------------------------------------------
# S-M2: Buff Consumer Promote + Gate
# ---------------------------------------------------------------------------

def mutations_buff_waste(signal: OptimizationSignal, apl: APL) -> list[tuple[APL, str]]:
    """
    For buff_waste signals with a known consumer in the APL:
      1. Promote consumer higher in its sub-list
      2. Upgrade buff.X.up → buff.X.react on consumer condition
      3. Add buff.X.react as OR clause if consumer lacks the gate entirely
    """
    results = []
    if not signal.buff_name:
        return results
    if not signal.apl_reference_found:
        return results  # LLM territory

    buff = signal.buff_name

    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            # Check if this action references our buff
            cond_text = act.conditions
            for v in act.args.values():
                cond_text += " " + v
            if f"buff.{buff}" not in cond_text:
                continue

            # Mutation 1: promote consumer up 1-3 positions
            for delta in [1, 2, 3]:
                new_pos = i - delta
                if new_pos < 0:
                    break
                # Don't jump over variable/routing actions
                if any(actions[j].is_variable or actions[j].is_call
                       for j in range(new_pos, i)):
                    break
                new_apl = move_action(apl, list_name, i, new_pos)
                results.append((new_apl,
                    f"S-M2a: promote {act.action} (buff.{buff} consumer) "
                    f"by {delta} in {list_name} (expire_rate={signal.priority:.0%})"))

            # Mutation 2: upgrade buff.X.up → buff.X.react
            if f"buff.{buff}.up" in act.conditions:
                new_cond = act.conditions.replace(f"buff.{buff}.up", f"buff.{buff}.react")
                new_apl = replace_condition(apl, list_name, i, new_cond)
                results.append((new_apl,
                    f"S-M2b: upgrade buff.{buff}.up→.react on {act.action} in {list_name}"))

            # Mutation 3: add buff.react as OR condition if only checking .up
            if f"buff.{buff}.react" not in act.conditions and f"buff.{buff}.up" in act.conditions:
                pass  # already handled by mutation 2

            # Mutation 4: if consumer has no buff gate at all but was found via args
            # (e.g., early_chain_if=buff.X.react) — add explicit if= gate
            if f"buff.{buff}" in cond_text and f"buff.{buff}" not in act.conditions:
                new_apl = append_or_condition(apl, list_name, i, f"buff.{buff}.react")
                results.append((new_apl,
                    f"S-M2c: add buff.{buff}.react OR gate to {act.action} in {list_name}"))

    return results


# ---------------------------------------------------------------------------
# S-M3: Resource Overcap Fix
# ---------------------------------------------------------------------------

def mutations_resource_overcap(signal: OptimizationSignal, apl: APL) -> list[tuple[APL, str]]:
    """
    For resource_overcap signals:
      1. Lower the resource threshold on the top spender
      2. Add an emergency dump if overcap is severe (>20%)
    """
    results = []
    if not signal.resource_name or not signal.target_action:
        return results

    resource = signal.resource_name
    overcap_rate = signal.priority  # repurposed as severity

    # Find all occurrences of target_action and reduce its resource threshold
    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            if act.action != signal.target_action:
                continue
            thresholds = _extract_resource_thresholds(act.conditions, resource)
            for full_match, val in thresholds:
                # Try reducing by 10%, 20%, 30%
                for pct in [10, 20, 30]:
                    new_val = val * (1 - pct / 100)
                    new_val_str = str(int(round(new_val))) if val == int(val) else f"{new_val:.1f}"
                    old_val_str = str(int(val)) if val == int(val) else str(val)
                    if new_val_str == old_val_str:
                        continue
                    new_apl = modify_threshold(apl, list_name, i, old_val_str, new_val_str)
                    results.append((new_apl,
                        f"S-M3a: lower {resource} threshold {old_val_str}→{new_val_str} "
                        f"on {act.action} in {list_name} (overcap={overcap_rate:.1%})"))

    # Add emergency dump if overcap is severe
    if overcap_rate > 0.20:
        # Find the last real action in every DPS sub-list, append an emergency dump
        for list_name, actions in apl.lists.items():
            if list_name in ("precombat", "variables", "items", "ogcd", "end_of_fight"):
                continue
            if not actions:
                continue
            # Check if an emergency dump already exists
            has_dump = any(
                resource in act.conditions and
                any(kw in act.conditions for kw in [">=90", ">=0.9", "max_stack"])
                for act in actions
            )
            if has_dump:
                continue
            # Add emergency dump at end of list
            dump_action = make_action(
                list_name, signal.target_action,
                conditions=f"{resource}>=90"
            )
            new_apl = insert_action(apl, list_name, len(actions), dump_action)
            results.append((new_apl,
                f"S-M3b: add emergency {resource} dump ({signal.target_action},{resource}>=90) "
                f"to end of {list_name}"))
            break  # only add to one list to avoid explosion

    return results


# ---------------------------------------------------------------------------
# S-M4: Interval Gap — large promote
# ---------------------------------------------------------------------------

def mutations_interval_gap(signal: OptimizationSignal, apl: APL) -> list[tuple[APL, str]]:
    """Promote a delayed high-value ability by up to 5 positions."""
    results = []
    if not signal.target_action:
        return results

    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            if act.action != signal.target_action:
                continue
            for delta in [2, 3, 4, 5]:
                new_pos = i - delta
                if new_pos < 0:
                    new_pos = 0
                if new_pos == i:
                    continue
                # Don't jump over routing/variable
                if any(actions[j].is_variable or actions[j].is_call
                       for j in range(new_pos, i)):
                    break
                new_apl = move_action(apl, list_name, i, new_pos)
                results.append((new_apl,
                    f"S-M4: promote {act.action} by {delta} in {list_name} "
                    f"(interval gap={signal.description[:50]})"))
            break

    return results


# ---------------------------------------------------------------------------
# Master generator
# ---------------------------------------------------------------------------

def generate_signal_mutations(
    signals: list[OptimizationSignal],
    apl: APL,
    max_total: int = 40,
) -> list[tuple[APL, str]]:
    """Generate all signal-targeted mutations, ranked by signal priority."""
    candidates: list[tuple[APL, str, float]] = []  # (apl, desc, priority)

    for sig in signals:
        muts: list[tuple[APL, str]] = []

        if "aps_inversion" in sig.types:
            muts += mutations_aps_inversion(sig, apl)
        if "buff_waste" in sig.types:
            muts += mutations_buff_waste(sig, apl)
        if "resource_overcap" in sig.types:
            muts += mutations_resource_overcap(sig, apl)
        if "interval_gap" in sig.types:
            muts += mutations_interval_gap(sig, apl)

        for m_apl, m_desc in muts:
            candidates.append((m_apl, m_desc, sig.priority))

    # Sort by signal priority descending, deduplicate by description
    candidates.sort(key=lambda x: -x[2])
    seen = set()
    result = []
    for m_apl, m_desc, _ in candidates:
        if m_desc not in seen:
            seen.add(m_desc)
            result.append((m_apl, m_desc))
        if len(result) >= max_total:
            break

    return result
