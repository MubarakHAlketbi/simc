#!/usr/bin/env python3
"""
Midnight SimC Talent Audit — v4
Rewrites missing_from_code.md and missing_from_info_base.md from scratch.

Cross-reference: wowhead/*/info_base.md Talent Tree tables  vs  SimC CPP registrations.

SimC registration signals (handles ALL classes/patterns):
  1. find_talent_spell( tree, "Name" )          — direct name call
  2. find_talent_spell( tree, NUMERIC_ID )       — direct ID call
  3. CT("Name") / ST("Name") / HT("Name")       — lambda shorthand (Druid, Evoker, Priest)
  4. _CT("Name") / _ST("Name") / _HT("Name")    — lambda shorthand (Monk, Shaman)
  5. { talent.X, "Name" }                       — Shaman initializer-list pattern

A Wowhead talent row is "COVERED" if its spell ID OR its normalised name matches
at least one SimC registration signal.

Outputs:
  missing_from_code.md      — Wowhead rows with no ID match AND no name match in SimC
  missing_from_info_base.md — SimC name/ID registrations with no match in any Wowhead table
"""

import re
from pathlib import Path
from datetime import date

REPO    = Path(__file__).parent.parent
WOWHEAD = REPO / "wowhead"
ENGINE  = REPO / "engine" / "class_modules"
TODAY   = date.today().isoformat()


def slug(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[''`\u2019]", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ─── 1. Extract SimC registrations ──────────────────────────────────────────

CPP_FILES = sorted(ENGINE.rglob("*.cpp"))

# name registrations:  slug → [(file, line, raw)]
simc_names: dict[str, list[tuple[str, int, str]]] = {}
# id registrations:    spell_id_str → [(file, line)]
simc_ids:   dict[str, list[tuple[str, int]]]      = {}

# Pattern 1+2: find_talent_spell( ..., "Name" or NUMERICID )
RE_DIRECT_NAME = re.compile(r'find_talent_spell\s*\([^,]+,\s*"([^"]+)"')
RE_DIRECT_ID   = re.compile(r'find_talent_spell\s*\([^,]+,\s*(\d{4,})')

# Pattern 3+4: CT/ST/HT/_CT/_ST/_HT ( optional_ptr_arg "Name" )
RE_LAMBDA_NAME = re.compile(r'\b_?[CSH]T\s*\(\s*(?:[^,"]+,\s*)?"([^"]{3,})"')

# Pattern 5: Shaman/Monk initializer { talent.X, "Name" }
RE_INIT_NAME   = re.compile(r'\{\s*[a-z_\.]+\s*,\s*"([^"]{3,})"')

for cpp in CPP_FILES:
    rel   = str(cpp.relative_to(ENGINE))
    lines = cpp.read_text(errors="replace").splitlines()
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("//"):
            continue
        # name lookups
        for pat in (RE_DIRECT_NAME, RE_LAMBDA_NAME, RE_INIT_NAME):
            for m in pat.finditer(line):
                raw = m.group(1)
                if len(raw) < 3:
                    continue
                # filter out obvious non-talent strings
                if raw.startswith("buff") or raw.startswith("action") or raw.startswith("pet"):
                    continue
                s = slug(raw)
                if s:
                    simc_names.setdefault(s, []).append((rel, i, raw))
        # id lookups
        for m in RE_DIRECT_ID.finditer(line):
            sid = m.group(1)
            simc_ids.setdefault(sid, []).append((rel, i))

print(f"SimC: {sum(len(v) for v in simc_names.values())} name registrations, "
      f"{len(simc_names)} unique slugs")
print(f"      {sum(len(v) for v in simc_ids.values())} ID registrations, "
      f"{len(simc_ids)} unique IDs")


# ─── 2. Extract Wowhead talent tables ────────────────────────────────────────

RE_ROW = re.compile(r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|')

wowhead_by_spec: dict[tuple[str, str], list[dict]] = {}

for ib in sorted(WOWHEAD.rglob("info_base.md")):
    parts = ib.relative_to(WOWHEAD).parts
    if len(parts) < 3:
        continue
    cls, spec = parts[0], parts[1]
    in_tbl = False
    rows   = []
    for line in ib.read_text(errors="replace").splitlines():
        if re.match(r"^##\s+Talent Tree", line):
            in_tbl = True
            continue
        if in_tbl and re.match(r"^##\s+(?!Talent)", line):
            break
        if in_tbl:
            m = RE_ROW.match(line)
            if m:
                name = m.group(2).strip()
                # strip markdown link suffix e.g. "[link](url)"
                name = re.sub(r'\[link\]\([^)]+\)', '', name).strip()
                rows.append({
                    "id":   m.group(1),
                    "name": name,
                    "rank": m.group(3),
                    "slug": slug(name),
                })
    if rows:
        wowhead_by_spec[(cls, spec)] = rows

total_wh = sum(len(v) for v in wowhead_by_spec.values())
print(f"Wowhead: {total_wh} talent rows across {len(wowhead_by_spec)} specs")


# ─── 3. Coverage check ───────────────────────────────────────────────────────

def covered(row: dict) -> bool:
    """Return True if this Wowhead row has a SimC registration (by ID or name)."""
    if row["id"] in simc_ids:
        return True
    s = row["slug"]
    if s in simc_names:
        return True
    # partial slug match — handles truncated names like "Thorim" matching "Thorim's Invocation"
    if len(s) >= 5:
        for k in simc_names:
            if k.startswith(s) or s.startswith(k[:max(5, len(k)-3)]):
                return True
    return False


# ─── 4. missing_from_code.md ─────────────────────────────────────────────────

lines_mfc  = []
total_miss = 0

spec_summary = []
for (cls, spec), rows in sorted(wowhead_by_spec.items()):
    miss = [r for r in rows if not covered(r)]
    spec_summary.append((cls, spec, len(miss), len(rows)))
    total_miss += len(miss)

lines_mfc += [
    "# Talents in info_base.md NOT Found in SimC Code",
    "",
    f"Generated: {TODAY}",
    "Detection: find_talent_spell(ID/\"Name\") + lambda CT/ST/HT + initializer-list patterns.",
    "A Wowhead row is MISSING only when neither its spell ID nor its name matches any SimC",
    "talent registration. Partial-prefix slug matching handles truncated info_base names.",
    "",
    f"**Total missing: {total_miss}** across "
    f"{sum(1 for _,_,n,_ in spec_summary if n > 0)} specs",
    "",
]

zero = [(c, s) for c, s, n, _ in spec_summary if n == 0]
if zero:
    lines_mfc.append("**Fully covered (0 missing):** " +
                     ", ".join(f"{c.replace('-',' ').title()}/{s.replace('-',' ').title()}"
                               for c, s in zero))
    lines_mfc.append("")

lines_mfc += ["---", ""]

for (cls, spec), rows in sorted(wowhead_by_spec.items()):
    miss = [r for r in rows if not covered(r)]
    if not miss:
        continue
    dcls  = cls.replace("-", " ").title()
    dspec = spec.replace("-", " ").title()
    lines_mfc.append(f"## {dcls} / {dspec} ({len(miss)} / {len(rows)} missing)")
    lines_mfc += ["", "| Spell ID | Name | Max Rank | Wowhead |",
                  "|----------|------|----------|---------|"]
    for r in miss:
        lines_mfc.append(f"| {r['id']} | {r['name']} | {r['rank']} | "
                         f"[link](https://www.wowhead.com/spell={r['id']}) |")
    lines_mfc.append("")

(WOWHEAD / "missing_from_code.md").write_text("\n".join(lines_mfc))
print(f"\nWrote missing_from_code.md  ({total_miss} missing)")


# ─── 5. missing_from_info_base.md ────────────────────────────────────────────

all_wh_ids   = {r["id"]   for rows in wowhead_by_spec.values() for r in rows}
all_wh_slugs = {r["slug"] for rows in wowhead_by_spec.values() for r in rows}

def file_to_class(fkey: str) -> str:
    f = fkey.lower()
    if "warrior"      in f: return "Warrior"
    if "shaman"       in f: return "Shaman"
    if "sc_mage"      in f or "/mage" in f: return "Mage"
    if "rogue"        in f: return "Rogue"
    if "druid"        in f: return "Druid"
    if "hunter"       in f: return "Hunter"
    if "death_knight" in f: return "Death Knight"
    if "demon_hunter" in f: return "Demon Hunter"
    if "evoker"       in f: return "Evoker"
    if "warlock"      in f: return "Warlock"
    if "monk"         in f: return "Monk"
    if "paladin"      in f: return "Paladin"
    if "priest"       in f: return "Priest"
    return fkey

class_names: dict[str, set[tuple[str, str]]] = {}  # class → {(name, file)}
class_ids:   dict[str, set[tuple[str, str]]] = {}  # class → {(id, file)}

for s, locs in simc_names.items():
    if s not in all_wh_slugs:
        # also check partial match
        partial = any(s.startswith(ws[:max(5,len(ws)-3)]) or ws.startswith(s)
                      for ws in all_wh_slugs if len(ws) >= 5)
        if partial:
            continue
        for fkey, lineno, raw in locs:
            cls = file_to_class(fkey)
            class_names.setdefault(cls, set()).add((raw, fkey))

for sid, locs in simc_ids.items():
    if sid not in all_wh_ids:
        for fkey, lineno in locs:
            cls = file_to_class(fkey)
            class_ids.setdefault(cls, set()).add((sid, fkey))

total_names = sum(len(v) for v in class_names.values())
total_ids   = sum(len(v) for v in class_ids.values())

lines_mfib = [
    "# Talent Names / IDs in SimC Code NOT Found in info_base.md",
    "",
    f"Generated: {TODAY}",
    "Detection: find_talent_spell(ID/\"Name\") + lambda + initializer-list patterns.",
    "An entry is flagged when it has no match (by ID or name) in any Wowhead talent table.",
    "",
    "Common causes:",
    "  - Utility/CC/defensive abilities not listed in DPS-focused info_base.md",
    "  - Old-expansion talents removed in Midnight (stale SimC code)",
    "  - Internal proc/helper spells that aren't real talent tree nodes",
    "  - Renamed talents where SimC still uses the old string",
    "  - Shared class baseline abilities registered for buff-tracking purposes",
    "",
    "Action: Verify on Wowhead. Stale → update SimC. Utility → leave with // N/A.",
    "",
    f"**Names not in Wowhead: {total_names}**  |  **IDs not in Wowhead: {total_ids}**",
    "",
    "---",
    "",
]

all_classes = sorted(set(list(class_names) + list(class_ids)))
for cls in all_classes:
    names = sorted(class_names.get(cls, set()))
    ids   = sorted(class_ids.get(cls, set()))
    total = len(names) + len(ids)
    lines_mfib.append(f"## {cls} ({total} entries)")
    lines_mfib.append("")
    if names:
        lines_mfib += ["**By Name:**", "", "| Talent Name | File |", "|-------------|------|"]
        for raw, fkey in names:
            lines_mfib.append(f"| `{raw}` | {fkey} |")
        lines_mfib.append("")
    if ids:
        lines_mfib += ["**By ID (ID-only registration, no name in Wowhead):**",
                       "", "| Spell ID | File |", "|----------|------|"]
        for sid, fkey in ids:
            lines_mfib.append(f"| {sid} | {fkey} |")
        lines_mfib.append("")

(WOWHEAD / "missing_from_info_base.md").write_text("\n".join(lines_mfib))
print(f"Wrote missing_from_info_base.md  ({total_names} names + {total_ids} IDs not in docs)")

print("\nDone.")
