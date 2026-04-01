"""APL Parser/Serializer — parse .simc APL text into structured data and back."""

import re
from copy import deepcopy
from dataclasses import dataclass, field


@dataclass
class APLAction:
    """A single action in an APL sub-list."""
    list_name: str          # "default", "st", "aoe", "cooldowns", etc.
    action: str             # "rampage", "bloodthirst", "call_action_list", "variable"
    conditions: str         # raw if= expression, or ""
    args: dict = field(default_factory=dict)  # other key=value (target_if=, name=, op=, etc.)
    line_index: int = 0     # position within its sub-list (0-indexed)
    raw_line: str = ""      # original text

    @property
    def is_variable(self) -> bool:
        return self.action == "variable"

    @property
    def is_call(self) -> bool:
        return self.action == "call_action_list" or self.action == "run_action_list"

    def to_simc(self) -> str:
        """Serialize to .simc format action string (after the =/ or +=/)."""
        parts = [self.action]
        # For call_action_list/run_action_list, name= comes first
        if "name" in self.args:
            parts.append(f"name={self.args['name']}")
        # target_if before if
        if "target_if" in self.args:
            parts.append(f"target_if={self.args['target_if']}")
        if self.conditions:
            parts.append(f"if={self.conditions}")
        for k, v in self.args.items():
            if k not in ("if", "name", "target_if"):
                parts.append(f"{k}={v}")
        return ",".join(parts)

    def __repr__(self):
        cond = f",if={self.conditions}" if self.conditions else ""
        return f"APLAction({self.list_name}[{self.line_index}]: {self.action}{cond})"


@dataclass
class APL:
    """Complete APL — a collection of named action lists."""
    lists: dict[str, list[APLAction]] = field(default_factory=dict)

    def copy(self) -> "APL":
        """Deep copy for mutation."""
        return deepcopy(self)

    def get_list(self, name: str) -> list[APLAction]:
        return self.lists.get(name, [])

    @property
    def all_actions(self) -> list[APLAction]:
        """All actions across all lists, in list order."""
        result = []
        for actions in self.lists.values():
            result.extend(actions)
        return result

    @property
    def list_names(self) -> list[str]:
        return list(self.lists.keys())

    def get_talent_references(self) -> set[str]:
        """Extract all talent.X references from conditions."""
        refs = set()
        for action in self.all_actions:
            text = action.conditions
            for k, v in action.args.items():
                text += " " + v
            for m in re.finditer(r'talent\.(\w+)', text):
                refs.add(m.group(1))
        return refs

    def get_buff_references(self) -> set[str]:
        """Extract all buff.X references from conditions."""
        refs = set()
        for action in self.all_actions:
            text = action.conditions
            for k, v in action.args.items():
                text += " " + v
            for m in re.finditer(r'buff\.(\w+)', text):
                refs.add(m.group(1))
        return refs

    def to_simc(self) -> str:
        """Serialize entire APL to .simc override text."""
        lines = []
        for list_name, actions in self.lists.items():
            for i, action in enumerate(actions):
                prefix = f"actions.{list_name}" if list_name != "default" else "actions"
                op = "=" if i == 0 else "+="
                lines.append(f"{prefix}{op}/{action.to_simc()}")
        return "\n".join(lines)

    def to_override_lines(self) -> list[str]:
        """Return as list of override lines (for sim_runner overrides param)."""
        return self.to_simc().split("\n")


def parse_action_line(action_str: str) -> tuple[str, str, dict]:
    """Parse an action string like 'rampage,if=rage>=80,target_if=min:...'

    Returns: (action_name, if_condition, other_args_dict)
    """
    parts = action_str.split(",")
    action_name = parts[0].strip()
    conditions = ""
    args = {}

    for part in parts[1:]:
        part = part.strip()
        if "=" in part:
            key, _, value = part.partition("=")
            key = key.strip()
            value = value.strip()
            if key == "if":
                conditions = value
            else:
                args[key] = value
        # else: malformed, skip

    return action_name, conditions, args


def parse_apl(text: str) -> APL:
    """Parse .simc APL text into an APL object.

    Handles formats:
      actions=auto_attack
      actions+=/rampage,if=rage>=80
      actions.cooldowns=use_items
      actions.cooldowns+=/potion
      actions.precombat=snapshot_stats
    """
    apl = APL()
    list_counts = {}  # track line_index per list

    for raw_line in text.strip().split("\n"):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        # Match: actions[.listname][=|+=/]action_string
        m = re.match(r'^actions(?:\.(\w+))?\s*\+?=/?\s*(.+)$', line)
        if not m:
            continue

        list_name = m.group(1) or "default"
        action_str = m.group(2)

        action_name, conditions, args = parse_action_line(action_str)

        if list_name not in apl.lists:
            apl.lists[list_name] = []
            list_counts[list_name] = 0

        action = APLAction(
            list_name=list_name,
            action=action_name,
            conditions=conditions,
            args=args,
            line_index=list_counts[list_name],
            raw_line=raw_line,
        )
        apl.lists[list_name].append(action)
        list_counts[list_name] += 1

    return apl


def swap_actions(apl: APL, list_name: str, idx_a: int, idx_b: int) -> APL:
    """Create a new APL with two actions swapped within the same list."""
    new_apl = apl.copy()
    actions = new_apl.lists[list_name]
    actions[idx_a], actions[idx_b] = actions[idx_b], actions[idx_a]
    # Update line indices
    actions[idx_a].line_index = idx_a
    actions[idx_b].line_index = idx_b
    return new_apl


def move_action(apl: APL, list_name: str, from_idx: int, to_idx: int) -> APL:
    """Create a new APL with an action moved to a different position."""
    new_apl = apl.copy()
    actions = new_apl.lists[list_name]
    action = actions.pop(from_idx)
    actions.insert(to_idx, action)
    # Reindex
    for i, a in enumerate(actions):
        a.line_index = i
    return new_apl


def add_condition(apl: APL, list_name: str, idx: int, condition: str) -> APL:
    """Add an AND condition to an existing action."""
    new_apl = apl.copy()
    action = new_apl.lists[list_name][idx]
    if action.conditions:
        action.conditions = f"({action.conditions})&({condition})"
    else:
        action.conditions = condition
    return new_apl


def remove_condition_clause(apl: APL, list_name: str, idx: int,
                            clause_to_remove: str) -> APL:
    """Remove a specific clause from an action's condition."""
    new_apl = apl.copy()
    action = new_apl.lists[list_name][idx]
    if not action.conditions:
        return new_apl
    # Simple approach: remove the clause and surrounding & operators
    cond = action.conditions
    cond = cond.replace(f"&{clause_to_remove}", "")
    cond = cond.replace(f"{clause_to_remove}&", "")
    cond = cond.replace(clause_to_remove, "")
    action.conditions = cond.strip("&() ") if cond.strip("&() ") else ""
    return new_apl


def modify_threshold(apl: APL, list_name: str, idx: int,
                     old_value: str, new_value: str) -> APL:
    """Replace a numeric threshold in an action's condition."""
    new_apl = apl.copy()
    action = new_apl.lists[list_name][idx]
    action.conditions = action.conditions.replace(old_value, new_value)
    return new_apl


def insert_action(apl: APL, list_name: str, position: int, action: APLAction) -> APL:
    """Insert a new action at position in list_name, creating the list if needed."""
    new_apl = apl.copy()
    if list_name not in new_apl.lists:
        new_apl.lists[list_name] = []
    actions = new_apl.lists[list_name]
    action = deepcopy(action)
    action.list_name = list_name
    actions.insert(position, action)
    for i, a in enumerate(actions):
        a.line_index = i
    return new_apl


def replace_condition(apl: APL, list_name: str, idx: int, new_condition: str) -> APL:
    """Replace the entire if= condition of an action."""
    new_apl = apl.copy()
    new_apl.lists[list_name][idx].conditions = new_condition
    return new_apl


def append_or_condition(apl: APL, list_name: str, idx: int, extra: str) -> APL:
    """Append '|extra' to an action's condition."""
    new_apl = apl.copy()
    action = new_apl.lists[list_name][idx]
    if action.conditions:
        action.conditions = f"({action.conditions})|({extra})"
    else:
        action.conditions = extra
    return new_apl


def make_action(list_name: str, action_name: str, conditions: str = "",
                **kwargs) -> APLAction:
    """Convenience constructor for a new APLAction."""
    return APLAction(
        list_name=list_name,
        action=action_name,
        conditions=conditions,
        args={k: str(v) for k, v in kwargs.items()},
        line_index=0,
        raw_line="",
    )


if __name__ == "__main__":
    # Quick test with sample APL text
    sample = """
# Precombat
actions.precombat=snapshot_stats
actions.precombat+=/variable,name=trinket_sync,op=setif,value=1,value_else=0,condition=trinket.1.has_use_buff

# Default
actions=auto_attack
actions+=/charge,if=time<=0.5|movement.distance>5
actions+=/potion,if=buff.recklessness.up|target.time_to_die<25
actions+=/call_action_list,name=cooldowns
actions+=/call_action_list,name=st,if=active_enemies<3
actions+=/call_action_list,name=aoe,if=active_enemies>=3

# ST
actions.st=rampage,if=rage>=80
actions.st+=/bloodthirst
actions.st+=/execute,if=target.health.pct<35
actions.st+=/raging_blow

# AoE
actions.aoe=whirlwind
actions.aoe+=/rampage,if=rage>=80
actions.aoe+=/bladestorm
"""
    apl = parse_apl(sample)
    print(f"Lists: {apl.list_names}")
    print(f"Total actions: {len(apl.all_actions)}")
    print(f"Talent refs: {apl.get_talent_references()}")
    print(f"Buff refs: {apl.get_buff_references()}")
    print()
    print("Serialized:")
    print(apl.to_simc())
    print()

    # Test swap
    swapped = swap_actions(apl, "st", 0, 1)
    print("After swap st[0]<->st[1]:")
    for a in swapped.get_list("st"):
        print(f"  {a}")
