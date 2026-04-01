"""APL Signal Extractor — Layer 2 optimizer signal computation.

Computes four signal types from SimResult data:
  A. APS Priority Inversion  — high-APS ability outranked by lower-APS ability
  B. Proc Buff Waste         — proc buff expires without being consumed
  C. Resource Overcap        — resource wasted by hitting cap
  D. Interval Gap            — high-value ability cast less often than expected

Signals are combined when multiple types point to the same target action.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sim_runner import SimResult, AbilityStats, BuffStats, ResourceStats
    from .apl_parser import APL


# ---------------------------------------------------------------------------
# Resources that are primary DPS resources (overcap = bad)
# ---------------------------------------------------------------------------
_SPENDER_RESOURCES = {
    "rage", "energy", "focus", "runic_power", "fury",
    "holy_power", "combo_points", "soul_shards", "chi",
    "maelstrom", "insanity", "astral_power",
}

# Resources where overcap is often intentional (pools) — require end_waste too
_AMBIGUOUS_RESOURCES = {"maelstrom", "insanity", "astral_power", "mana"}

# APS floor: abilities below this contribute < 0.5% of DPS — ignore
_APS_FLOOR = 500.0

# Thresholds
_APS_INVERSION_THRESHOLD = 0.005   # 0.5% of total DPS gap to flag
_BUFF_WASTE_EXPIRE_RATE  = 0.40    # 40% expire rate to flag
_BUFF_WASTE_MIN_STARTS   = 2.0     # minimum activations per fight
_BUFF_WASTE_SIGNAL_FLOOR = 0.001   # 0.1% DPS value floor to care about
_RESOURCE_OVERCAP_THRESH = 0.08    # 8% overcap rate to flag
_INTERVAL_GAP_THRESH     = 0.003   # 0.3% DPS value to flag interval gaps


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class OptimizationSignal:
    """A single actionable signal pointing to a specific APL element."""

    type: str                   # "aps_inversion" | "buff_waste" | "resource_overcap" | "interval_gap"
    priority: float             # 0.0–1.0 (higher = more impactful)
    description: str            # human-readable explanation

    # Target identification
    target_action: str          # APL action name this signal points to
    target_list: str = ""       # APL sub-list name (if known)
    target_idx: int = -1        # position in sub-list (if known)

    # Signal-specific payload
    buff_name: str = ""         # for buff_waste signals
    resource_name: str = ""     # for resource_overcap signals
    blocker_action: str = ""    # for aps_inversion: the action above that should be below
    apl_reference_found: bool = True   # for buff_waste: False = no consumer in APL at all

    # Combined signal bookkeeping
    types: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.types:
            self.types = [self.type]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _total_dps(sim: SimResult) -> float:
    return sim.dps_mean if sim.dps_mean > 0 else 1.0


def _find_action_in_apl(apl: APL, action_name: str) -> list[tuple[str, int]]:
    """Return [(list_name, idx), ...] for every occurrence of action_name in APL."""
    results = []
    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            if act.action == action_name:
                results.append((list_name, i))
    return results


def _apl_position_score(apl: APL, action_name: str) -> float:
    """Lower score = appears earlier (higher priority) in APL.
    Returns large number if not found."""
    for list_name, actions in apl.lists.items():
        if list_name in ("precombat", "variables", "items", "ogcd"):
            continue
        for i, act in enumerate(actions):
            if act.action == action_name:
                return i + len(list_name) * 100  # crude positional score
    return 99999.0


def _buff_referenced_in_apl(apl: APL, buff_name: str) -> bool:
    """Check if buff.BUFF_NAME appears anywhere in APL conditions."""
    pattern = re.compile(r'\bbuff\.' + re.escape(buff_name) + r'\b')
    for act in apl.all_actions:
        text = act.conditions
        for v in act.args.values():
            text += " " + v
        if pattern.search(text):
            return True
    return False


def _consumer_actions_for_buff(apl: APL, buff_name: str) -> list[tuple[str, int]]:
    """Find actions that reference buff.BUFF_NAME in conditions."""
    pattern = re.compile(r'\bbuff\.' + re.escape(buff_name) + r'\b')
    results = []
    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            text = act.conditions
            for v in act.args.values():
                text += " " + v
            if pattern.search(text):
                results.append((list_name, i))
    return results


def _is_player_cd_action(apl: APL, buff_name: str) -> bool:
    """True if buff_name matches an APL action that the player directly activates."""
    for act in apl.all_actions:
        if act.action == buff_name and not act.is_call and not act.is_variable:
            return True
    return False


# ---------------------------------------------------------------------------
# Signal A: APS Priority Inversion
# ---------------------------------------------------------------------------

def aps_inversion_signals(sim: SimResult, apl: APL) -> list[OptimizationSignal]:
    """Detect abilities with high portion_aps that appear AFTER lower-APS abilities."""
    signals = []
    total = _total_dps(sim)

    # Build ability -> position map (using crude positional score)
    ab_by_name = {a.name: a for a in sim.ability_stats if a.portion_aps >= _APS_FLOOR}

    # For each pair (A, B) where A has higher APS but appears after B
    # Only check top-15 by APS to keep it tractable
    top_abs = sorted(ab_by_name.values(), key=lambda x: -x.portion_aps)[:15]
    for i, a_stat in enumerate(top_abs):
        pos_a = _apl_position_score(apl, a_stat.name)
        if pos_a >= 99999:
            continue  # not in APL at all — different signal

        for j, b_stat in enumerate(top_abs):
            if i == j:
                continue
            if b_stat.portion_aps >= a_stat.portion_aps:
                continue  # B is actually higher APS, not an inversion
            pos_b = _apl_position_score(apl, b_stat.name)
            if pos_b >= 99999:
                continue

            if pos_a > pos_b:  # A appears AFTER B despite higher APS
                gap = (a_stat.portion_aps - b_stat.portion_aps) / total
                if gap < _APS_INVERSION_THRESHOLD:
                    continue
                locs = _find_action_in_apl(apl, a_stat.name)
                if not locs:
                    continue
                list_name, idx = locs[0]
                signals.append(OptimizationSignal(
                    type="aps_inversion",
                    priority=min(gap * 10, 0.6),
                    description=(
                        f"{a_stat.name} (aps={a_stat.portion_aps:.0f}) appears after "
                        f"{b_stat.name} (aps={b_stat.portion_aps:.0f}); "
                        f"gap={gap*100:.2f}% of total DPS"
                    ),
                    target_action=a_stat.name,
                    target_list=list_name,
                    target_idx=idx,
                    blocker_action=b_stat.name,
                ))

    return signals


# ---------------------------------------------------------------------------
# Signal B: Proc Buff Waste
# ---------------------------------------------------------------------------

def buff_waste_signals(sim: SimResult, apl: APL) -> list[OptimizationSignal]:
    """Detect proc buffs that expire without being consumed."""
    signals = []
    total = _total_dps(sim)

    for b in sim.buff_stats:
        if b.start_count < _BUFF_WASTE_MIN_STARTS:
            continue
        if b.expire_rate < _BUFF_WASTE_EXPIRE_RATE:
            continue

        # Is it a player-activated CD? If so, expire is expected.
        if _is_player_cd_action(apl, b.name):
            continue

        # Also skip if start_count is very low (once-per-fight CDs)
        if b.is_player_cd:
            continue

        # Does the APL reference this buff anywhere?
        ref_found = _buff_referenced_in_apl(apl, b.name)
        consumers = _consumer_actions_for_buff(apl, b.name)

        # Estimate value: uptime * expire_rate * (rough dps fraction)
        # We don't know the buff's DPS value directly, but high expire on a
        # frequently-proccing buff with uptime implies meaningful DPS loss.
        value_proxy = b.expire_rate * (b.uptime / 100.0) * b.start_count / 10.0
        if value_proxy < _BUFF_WASTE_SIGNAL_FLOOR and ref_found:
            continue

        if consumers:
            list_name, idx = consumers[0]
            target_action = apl.lists[list_name][idx].action
        else:
            target_action = b.name  # no consumer found — LLM territory
            list_name = ""
            idx = -1

        signals.append(OptimizationSignal(
            type="buff_waste",
            priority=min(b.expire_rate * 0.8, 0.9),
            description=(
                f"Buff '{b.name}' expires {b.expire_rate:.0%} of the time "
                f"(uptime={b.uptime:.1f}%, starts={b.start_count:.1f}/fight). "
                f"APL reference: {'FOUND' if ref_found else 'NONE — needs LLM'}"
            ),
            target_action=target_action,
            target_list=list_name,
            target_idx=idx,
            buff_name=b.name,
            apl_reference_found=ref_found,
        ))

    return signals


# ---------------------------------------------------------------------------
# Signal C: Resource Overcap
# ---------------------------------------------------------------------------

def resource_overcap_signals(sim: SimResult, apl: APL) -> list[OptimizationSignal]:
    """Detect resources being wasted by overcapping."""
    signals = []
    total = _total_dps(sim)

    for rs in sim.resource_stats:
        rname = rs.resource
        if rname not in _SPENDER_RESOURCES:
            continue
        if rs.overcap_rate < _RESOURCE_OVERCAP_THRESH:
            continue
        # For ambiguous resources, also require significant end_waste
        if rname in _AMBIGUOUS_RESOURCES:
            # end_waste relative to spent — if < 2% of spent it's noise
            if rs.end_waste / (rs.spent + 1) < 0.02 and rs.overcap_rate < 0.20:
                continue

        # Find top spender for this resource in the APL —
        # highest-APS ability that the resource feeds
        # Heuristic: search ability names against APL actions
        top_spender = None
        best_aps = 0.0
        for ab in sorted(sim.ability_stats, key=lambda x: -x.portion_aps):
            locs = _find_action_in_apl(apl, ab.name)
            if locs and ab.portion_aps > best_aps:
                top_spender = ab
                best_aps = ab.portion_aps
                break  # first high-APS action that's in APL

        target_action = top_spender.name if top_spender else ""
        locs = _find_action_in_apl(apl, target_action) if target_action else []
        list_name, idx = locs[0] if locs else ("", -1)

        signals.append(OptimizationSignal(
            type="resource_overcap",
            priority=min(rs.overcap_rate, 0.7),
            description=(
                f"Resource '{rname}' overcap={rs.overcap_rate:.1%} "
                f"(spent={rs.spent:.0f}, wasted={rs.overcap:.0f}, "
                f"end={rs.end_waste:.0f}). "
                f"Top spender candidate: {target_action}"
            ),
            target_action=target_action,
            target_list=list_name,
            target_idx=idx,
            resource_name=rname,
        ))

    return signals


# ---------------------------------------------------------------------------
# Signal D: Interval Gap
# ---------------------------------------------------------------------------

def interval_gap_signals(sim: SimResult, apl: APL) -> list[OptimizationSignal]:
    """Detect high-value abilities being cast less often than their CD allows."""
    signals = []
    total = _total_dps(sim)

    # Focus on top-5 APS abilities with intervals that look suspicious
    top_abs = sorted(sim.ability_stats, key=lambda x: -x.portion_aps)[:8]
    for ab in top_abs:
        if ab.portion_aps < _APS_FLOOR:
            continue
        if ab.interval <= 0:
            continue

        # Flag if interval > 8s AND ability accounts for >1% DPS
        # (auto-attacks, DoTs, etc. naturally have long intervals — filter by executes)
        aps_frac = ab.portion_aps / total
        if ab.interval < 8.0:
            continue
        if aps_frac < 0.01:
            continue
        if ab.executes < 5:  # rarely cast — likely a CD, not a filler
            continue

        priority = min((ab.interval / 10.0) * aps_frac * 5.0, 0.3)
        if priority < _INTERVAL_GAP_THRESH:
            continue

        locs = _find_action_in_apl(apl, ab.name)
        if not locs:
            continue
        list_name, idx = locs[0]

        signals.append(OptimizationSignal(
            type="interval_gap",
            priority=priority,
            description=(
                f"{ab.name} has {ab.interval:.1f}s avg interval but "
                f"contributes {aps_frac*100:.1f}% DPS — "
                f"may be delayed by lower-priority actions"
            ),
            target_action=ab.name,
            target_list=list_name,
            target_idx=idx,
        ))

    return signals


# ---------------------------------------------------------------------------
# Signal Combination
# ---------------------------------------------------------------------------

def combine_signals(signals: list[OptimizationSignal]) -> list[OptimizationSignal]:
    """Merge signals pointing to the same target_action, boosting combined priority."""
    combined: dict[str, OptimizationSignal] = {}
    for sig in signals:
        key = sig.target_action
        if key in combined:
            existing = combined[key]
            # Boost priority with diminishing returns
            existing.priority = min(existing.priority + sig.priority * 0.4, 0.95)
            existing.types.append(sig.type)
            existing.description += f" | {sig.description}"
            # Inherit richer location if we don't have one
            if existing.target_list == "" and sig.target_list:
                existing.target_list = sig.target_list
                existing.target_idx = sig.target_idx
            # Inherit buff/resource names
            if not existing.buff_name and sig.buff_name:
                existing.buff_name = sig.buff_name
            if not existing.resource_name and sig.resource_name:
                existing.resource_name = sig.resource_name
        else:
            combined[key] = sig

    return sorted(combined.values(), key=lambda s: -s.priority)


# ---------------------------------------------------------------------------
# Master extractor
# ---------------------------------------------------------------------------

def extract_signals(sim: SimResult, apl: APL) -> list[OptimizationSignal]:
    """Run all signal extractors and return combined, ranked signal list."""
    raw = []
    raw += aps_inversion_signals(sim, apl)
    raw += buff_waste_signals(sim, apl)
    raw += resource_overcap_signals(sim, apl)
    raw += interval_gap_signals(sim, apl)
    return combine_signals(raw)


def signals_needing_llm(signals: list[OptimizationSignal]) -> list[OptimizationSignal]:
    """Return signals that require LLM semantic reasoning to fix."""
    return [s for s in signals if
            s.type == "buff_waste" and not s.apl_reference_found]


def format_signals_report(signals: list[OptimizationSignal]) -> str:
    """Human-readable signal report for debugging / LLM prompt."""
    if not signals:
        return "  No signals detected."
    lines = []
    for s in signals:
        types_str = "+".join(s.types)
        loc = f"{s.target_list}[{s.target_idx}]" if s.target_list else "unknown"
        lines.append(
            f"  [{types_str}] priority={s.priority:.2f}  "
            f"target={s.target_action} @ {loc}\n"
            f"    {s.description[:120]}"
        )
    return "\n".join(lines)
