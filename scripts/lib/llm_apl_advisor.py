"""LLM APL Advisor — Layer 3 semantic reasoning.

Builds a structured prompt from sim data + APL, calls an LLM, parses
structured CHANGE blocks back into APL mutations for DPS validation.

Only called when programmatic signals cannot generate a fix:
  - buff_waste with apl_reference_found=False (missing consumer)
  - resource_overcap > 15% that signal mutations didn't resolve
  - Layers 1+2 converge at 0 improvement

The LLM proposes changes; ALL are validated via DPS sim before acceptance.
"""

from __future__ import annotations

import os
import re
import json
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from .apl_parser import (
    APL, APLAction, parse_apl,
    insert_action, move_action, replace_condition,
    append_or_condition, make_action,
)
from .apl_signal_extractor import OptimizationSignal, signals_needing_llm

if TYPE_CHECKING:
    from .sim_runner import SimResult

# Mechanics context files live here (from wowhead extraction)
_WOWHEAD_DIR = Path(__file__).resolve().parents[2] / "wowhead"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class LLMChange:
    """A single proposed APL change from the LLM."""
    change_type: str        # promote | add_condition | modify_condition | add_action | swap
    target_line: str        # exact APL line to match (or "none")
    new_line: str           # replacement or new APL line
    reason: str
    confidence: str         # high | medium | low
    source: str = "llm"


# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------

def _load_wowhead_context(spec_name: str) -> str:
    """Load rotation.md from wowhead extraction for mechanic context."""
    # spec_name like "warlock_affliction" → wowhead/warlock/affliction/extracted/rotation.md
    parts = spec_name.split("_", 1)
    if len(parts) < 2:
        return ""
    cls, spec = parts[0], parts[1]
    path = _WOWHEAD_DIR / cls / spec / "extracted" / "rotation.md"
    if not path.exists():
        # Try alternate: dk_blood → death_knight/blood
        alt_map = {"dk": "death_knight", "dh": "demon_hunter"}
        cls_alt = alt_map.get(cls, cls)
        path = _WOWHEAD_DIR / cls_alt / spec / "extracted" / "rotation.md"
    if path.exists():
        content = path.read_text()
        # Trim to first 3000 chars to fit context
        return content[:3000]
    return "(Wowhead rotation data not available — use general class knowledge)"


def _format_ability_table(sim: SimResult, top_n: int = 20) -> str:
    """Format ability stats as a compact table for the prompt."""
    sorted_abs = sorted(sim.ability_stats, key=lambda x: -x.portion_aps)
    lines = ["  Ability                               DPS%    Casts  APS      Gap"]
    lines.append("  " + "-" * 70)
    for ab in sorted_abs[:top_n]:
        if ab.portion_aps == 0 and ab.executes == 0:
            continue
        lines.append(
            f"  {ab.name:40s}  {ab.portion_amount*100:4.1f}%  "
            f"x{ab.executes:5.1f}  {ab.portion_aps:7.0f}  {ab.interval:5.1f}s"
        )
    # Zero-APS but executed (CDs, summons)
    zero_aps = [ab for ab in sim.ability_stats if ab.portion_aps == 0 and ab.executes > 0]
    if zero_aps:
        lines.append("  [zero-APS executed actions: " +
                     ", ".join(f"{ab.name}(x{ab.executes:.0f})" for ab in zero_aps[:8]) + "]")
    return "\n".join(lines)


def _format_buff_table(sim: SimResult, signals: list[OptimizationSignal]) -> str:
    """Format buff waste signals as a compact table."""
    waste_buffs = [b for b in sim.buff_stats
                   if b.expire_rate > 0.30 and b.start_count >= 2]
    waste_buffs.sort(key=lambda x: -x.expire_rate)
    if not waste_buffs:
        return "  No significant buff waste detected."

    # Mark which ones need LLM
    needs_llm = {s.buff_name for s in signals if not s.apl_reference_found}

    lines = ["  Buff                                 Expire%  Uptime%  Starts  APL_Ref"]
    lines.append("  " + "-" * 70)
    for b in waste_buffs[:12]:
        ref = "NONE←LLM" if b.name in needs_llm else "FOUND"
        lines.append(
            f"  {b.name:40s}  {b.expire_rate*100:5.1f}%  "
            f"{b.uptime:6.1f}%  {b.start_count:5.1f}  {ref}"
        )
    return "\n".join(lines)


def _format_resource_table(sim: SimResult) -> str:
    lines = ["  Resource        Spent       Overcap     Overcap%   End-Waste"]
    lines.append("  " + "-" * 65)
    for rs in sim.resource_stats:
        if rs.spent + rs.overcap < 100:
            continue
        lines.append(
            f"  {rs.resource:16s}  {rs.spent:10.0f}  {rs.overcap:10.0f}  "
            f"{rs.overcap_rate*100:7.1f}%  {rs.end_waste:10.0f}"
        )
    return "\n".join(lines)


def build_llm_prompt(
    spec_name: str,
    fight_style: str,
    sim: SimResult,
    apl_text: str,
    signals: list[OptimizationSignal],
    already_tested: list[str] | None = None,
) -> str:
    """Build the full structured prompt for the LLM."""

    wowhead_context = _load_wowhead_context(spec_name)
    ability_table = _format_ability_table(sim)
    buff_table = _format_buff_table(sim, signals)
    resource_table = _format_resource_table(sim)

    tested_str = ""
    if already_tested:
        tested_str = (
            "\nAUTOMATED MUTATIONS ALREADY TESTED (do not suggest these again):\n" +
            "\n".join(f"  - {t}" for t in already_tested[:20])
        )

    prompt = f"""You are analyzing a SimulationCraft APL (Action Priority List) for {spec_name.replace("_", " ").title()}.
Fight style: {fight_style}. Game build: 12.0.1.66709 (Midnight expansion, level 90).

Your task: identify SPECIFIC, ACTIONABLE APL changes that would increase DPS.
All suggestions must pass a DPS simulation test — you are proposing candidates, not applying changes.

═══════════════════════════════════════════════════════
SECTION A — ABILITY PERFORMANCE (sorted by DPS/second)
═══════════════════════════════════════════════════════
{ability_table}

═══════════════════════════════════════════════════════
SECTION B — BUFF WASTE SIGNALS
APL_Ref=NONE means this buff has NO consumer action in the current APL.
═══════════════════════════════════════════════════════
{buff_table}

═══════════════════════════════════════════════════════
SECTION C — RESOURCE FLOW
═══════════════════════════════════════════════════════
{resource_table}

═══════════════════════════════════════════════════════
SECTION D — SPEC MECHANICS CONTEXT (from Wowhead)
═══════════════════════════════════════════════════════
{wowhead_context}
{tested_str}

═══════════════════════════════════════════════════════
CURRENT APL (full text)
═══════════════════════════════════════════════════════
{apl_text}

═══════════════════════════════════════════════════════
ANALYSIS PROTOCOL — follow these steps IN ORDER
═══════════════════════════════════════════════════════

STEP 1 — BUFF WASTE (highest priority, especially APL_Ref=NONE)
For each buff with expire_rate > 40%:
  a) If APL_Ref=NONE: which APL action consumes this buff?
     Write the exact action name and the exact new APL line to add.
     If you don't know the consumer with high confidence, skip it.
  b) If APL_Ref=FOUND: is the consumer at the right priority? Does it use
     .react (server-confirmed) or .up (predicted)? Should it be .react?
  c) Write one specific CHANGE block per finding.

STEP 2 — APS ORDER VERIFICATION
For the top 8 abilities by DPS%:
  a) Find each in the APL.
  b) Is any high-DPS ability appearing AFTER a lower-DPS ability with no
     mechanical justification? (Mechanical justification = the lower ability
     sets up an amplifier buff that directly boosts the higher ability.)
  c) Write one specific CHANGE block per unjustified inversion.

STEP 3 — RESOURCE FLOW DIAGNOSIS
For any resource with overcap% > 15%:
  a) What is the primary spender in the APL for this resource?
  b) Is its threshold too conservative? What exact value would fix it?
  c) Is an emergency dump needed? Where in which sub-list?
  d) Write one specific CHANGE block per finding.

STEP 4 — MISSING SYNERGIES
Look at zero-APS executed actions (CDs, summons, pet summons):
  a) Are they fired BEFORE their amplified abilities, or after?
  b) If after, write a CHANGE to fix the ordering.
  c) Is any high-DPS ability missing a condition that gates it on its CD amplifier?

STEP 5 — OUTPUT FORMAT
For each change, write exactly:

CHANGE [N]:
  TYPE: [promote | add_condition | modify_condition | add_action | swap]
  TARGET_LINE: [exact current APL line — copy it verbatim — or "none" if adding new]
  NEW_LINE: [exact replacement or new APL line in SimC format]
  REASON: [one sentence citing the specific signal]
  CONFIDENCE: [high | medium | low]

STRICT RULES:
- Only output CHANGE blocks. No preamble, no narrative, no summary.
- Do NOT suggest changes to abilities with 0 portion_aps unless resource signal points there.
- Do NOT rewrite sub-list structure or rename sub-lists.
- Do NOT suggest changes already listed in AUTOMATED MUTATIONS ALREADY TESTED.
- Maximum 8 changes total.
- If you cannot ground a change in the signal data above, omit it.
- Use exact SimC APL syntax (actions.LISTNAME+=/ACTION,if=CONDITION).
"""
    return prompt


# ---------------------------------------------------------------------------
# LLM caller
# ---------------------------------------------------------------------------

def call_llm(prompt: str) -> str:
    """Call the LLM API and return the response text.

    Uses the hermes-agent internal API if available, otherwise falls back
    to a direct OpenAI/Anthropic call via environment variables.
    """
    # Try Hermes internal model first (fastest, cheapest)
    try:
        import subprocess
        result = subprocess.run(
            ["python3", "-c",
             f"""
import sys, os
sys.path.insert(0, os.path.expanduser('~/.hermes'))
try:
    from hermes_tools import llm_call
    print(llm_call({repr(prompt)}, model='claude-opus-4-6'))
except Exception as e:
    print(f'ERROR: {{e}}')
"""],
            capture_output=True, text=True, timeout=120
        )
        out = result.stdout.strip()
        if out and not out.startswith("ERROR:"):
            return out
    except Exception:
        pass

    # Fallback: OpenAI API
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if api_key:
        try:
            import urllib.request
            payload = json.dumps({
                "model": "gpt-4o",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 2000,
                "temperature": 0.1,
            }).encode()
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=payload,
                headers={"Content-Type": "application/json",
                         "Authorization": f"Bearer {api_key}"},
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"LLM_ERROR: {e}"

    # Fallback: Anthropic API
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key:
        try:
            import urllib.request
            payload = json.dumps({
                "model": "claude-opus-4-6",
                "max_tokens": 2000,
                "messages": [{"role": "user", "content": prompt}],
            }).encode()
            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={"Content-Type": "application/json",
                         "x-api-key": api_key,
                         "anthropic-version": "2023-06-01"},
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                return data["content"][0]["text"]
        except Exception as e:
            return f"LLM_ERROR: {e}"

    return "LLM_ERROR: no API key configured (set OPENAI_API_KEY or ANTHROPIC_API_KEY)"


# ---------------------------------------------------------------------------
# Response parser
# ---------------------------------------------------------------------------

def parse_llm_response(response: str) -> list[LLMChange]:
    """Parse CHANGE [N] blocks from LLM response."""
    changes = []

    # Split on CHANGE [N]: markers
    blocks = re.split(r'CHANGE\s*\[?\d+\]?\s*:', response)
    for block in blocks[1:]:  # skip preamble
        change = _parse_change_block(block.strip())
        if change:
            changes.append(change)

    return changes


def _parse_change_block(block: str) -> LLMChange | None:
    """Parse a single CHANGE block."""
    def extract(field: str) -> str:
        m = re.search(rf'{field}\s*:\s*(.+?)(?=\n\s*[A-Z_]+\s*:|$)', block, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ""

    change_type = extract("TYPE").lower().split()[0] if extract("TYPE") else ""
    target_line = extract("TARGET_LINE")
    new_line = extract("NEW_LINE")
    reason = extract("REASON")
    confidence = extract("CONFIDENCE").lower().split()[0] if extract("CONFIDENCE") else "low"

    # Validate
    valid_types = {"promote", "add_condition", "modify_condition", "add_action", "swap"}
    if change_type not in valid_types:
        return None
    if not new_line or new_line.lower() in ("none", ""):
        return None
    if confidence not in ("high", "medium", "low"):
        confidence = "low"

    return LLMChange(
        change_type=change_type,
        target_line=target_line if target_line.lower() != "none" else "",
        new_line=new_line,
        reason=reason,
        confidence=confidence,
    )


# ---------------------------------------------------------------------------
# Change → APL mutation
# ---------------------------------------------------------------------------

def apply_llm_change(change: LLMChange, apl: APL, apl_text: str) -> tuple[APL, str] | None:
    """Convert an LLMChange into an (APL, description) mutation tuple.

    Returns None if the change cannot be applied (target not found, etc.).
    """
    desc = f"LLM-{change.change_type}[{change.confidence}]: {change.reason[:80]}"

    # --- add_action: parse new_line as a new APL action ---
    if change.change_type == "add_action":
        try:
            new_apl_text = apl_text + "\n" + change.new_line
            new_apl = parse_apl(new_apl_text)
            return new_apl, desc
        except Exception:
            return None

    # --- All other types require finding target_line ---
    if not change.target_line:
        # No target — try parsing as add_action anyway
        if change.new_line.startswith("actions"):
            try:
                new_apl_text = apl_text + "\n" + change.new_line
                return parse_apl(new_apl_text), desc
            except Exception:
                pass
        return None

    # Find target_line in APL text (fuzzy: strip whitespace)
    target_stripped = change.target_line.strip()
    found_list = None
    found_idx = None
    for list_name, actions in apl.lists.items():
        for i, act in enumerate(actions):
            if act.raw_line.strip() == target_stripped:
                found_list, found_idx = list_name, i
                break
        if found_list:
            break

    if found_list is None:
        # Try matching by action+conditions content
        # Parse target_line to extract action name
        m = re.match(r'actions(?:\.\w+)?\+?=/?(\w+)', target_stripped)
        if m:
            action_name = m.group(1)
            for list_name, actions in apl.lists.items():
                for i, act in enumerate(actions):
                    if act.action == action_name:
                        found_list, found_idx = list_name, i
                        break
                if found_list:
                    break

    if found_list is None:
        return None

    # --- promote: move action up ---
    if change.change_type == "promote":
        new_pos = max(0, found_idx - 1)
        if new_pos == found_idx:
            return None
        new_apl = move_action(apl, found_list, found_idx, new_pos)
        return new_apl, desc

    # --- swap: swap with adjacent ---
    if change.change_type == "swap":
        swap_pos = found_idx - 1 if found_idx > 0 else found_idx + 1
        actions = apl.lists[found_list]
        if swap_pos < 0 or swap_pos >= len(actions):
            return None
        from .apl_parser import swap_actions
        new_apl = swap_actions(apl, found_list, found_idx, swap_pos)
        return new_apl, desc

    # --- modify_condition / add_condition: replace with new_line's condition ---
    if change.change_type in ("modify_condition", "add_condition"):
        # Extract if= from new_line
        cond_m = re.search(r',if=(.+?)(?:,\w+=|$)', change.new_line)
        if cond_m:
            new_cond = cond_m.group(1)
            new_apl = replace_condition(apl, found_list, found_idx, new_cond)
            return new_apl, desc
        return None

    return None


# ---------------------------------------------------------------------------
# Master entry point
# ---------------------------------------------------------------------------

def get_llm_mutations(
    spec_name: str,
    fight_style: str,
    sim: SimResult,
    apl_text: str,
    signals: list[OptimizationSignal],
    already_tested: list[str] | None = None,
    min_confidence: str = "medium",
) -> list[tuple[APL, str]]:
    """Full Layer 3 pipeline: build prompt → call LLM → parse → convert to mutations.

    Returns list of (APL, description) tuples ready for multi-stage eval.
    Only returns 'high' and 'medium' confidence changes by default.
    """
    conf_levels = {"high": 2, "medium": 1, "low": 0}
    min_conf_val = conf_levels.get(min_confidence, 1)

    prompt = build_llm_prompt(spec_name, fight_style, sim, apl_text, signals, already_tested)
    response = call_llm(prompt)

    if response.startswith("LLM_ERROR"):
        print(f"  [LLM] Error: {response}")
        return []

    changes = parse_llm_response(response)
    print(f"  [LLM] Parsed {len(changes)} CHANGE blocks from response")

    apl = parse_apl(apl_text)
    mutations = []
    for change in changes:
        if conf_levels.get(change.confidence, 0) < min_conf_val:
            continue
        mut = apply_llm_change(change, apl, apl_text)
        if mut:
            mutations.append(mut)
            print(f"    [{change.confidence}] {change.change_type}: {change.reason[:70]}")
        else:
            print(f"    [SKIP] Could not apply: {change.target_line[:50]}")

    return mutations
