#!/usr/bin/env python3
"""Validate all MID1 profiles against talent tree constraints."""
import glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.lib.talent_validator import TreeConstraints, validate_build, count_points
from scripts.lib.tree_codec_bridge import decode_profile_talents
from scripts.lib.talent_tree import SPEC_MAP

profiles = sorted(glob.glob("profiles/MID1/MID1_*.simc"))
pass_count = 0
fail_count = 0
skip_count = 0

for p in profiles:
    basename = os.path.basename(p)
    with open(p) as f:
        content = f.read()

    spec_line = None
    talent_str = None
    for line in content.split("\n"):
        if line.startswith("spec="):
            spec_line = line.strip().split("=", 1)[1]
        if line.startswith("talents="):
            talent_str = line.strip().split("=", 1)[1]

    if not spec_line or not talent_str:
        print(f"  SKIP  {basename} (missing spec/talents)")
        skip_count += 1
        continue

    # Map spec
    SPEC_ALIASES = {
        "beast_mastery": "hunter_bm",
        "marksmanship": "hunter_mm",
    }
    # Extract class from filename: MID1_{Class}_{Spec}[_{Variant}].simc
    file_parts = basename.replace("MID1_", "").replace(".simc", "").split("_")
    file_class = file_parts[0].lower() if file_parts else ""
    # Map file class names to SPEC_MAP prefixes
    CLASS_PREFIX_MAP = {
        "death": "dk", "demon": "dh", "hunter": "hunter", "warrior": "warrior",
        "mage": "mage", "warlock": "warlock", "priest": "priest", "rogue": "rogue",
        "shaman": "shaman", "monk": "monk", "druid": "druid", "paladin": "paladin",
        "evoker": "evoker",
    }
    class_prefix = CLASS_PREFIX_MAP.get(file_class, file_class)

    found = SPEC_ALIASES.get(spec_line.lower())
    if not found:
        # Match using both class (from filename) and spec
        for s in SPEC_MAP:
            parts = s.split("_")
            if spec_line.lower() == parts[-1] and s.startswith(class_prefix):
                found = s
                break
    if not found:
        for s in SPEC_MAP:
            parts = s.split("_")
            if spec_line.lower() == parts[-1]:
                found = s
                break
    if not found:
        for s in SPEC_MAP:
            if spec_line.lower() in s:
                found = s
                break
    if not found:
        print(f"  SKIP  {basename} (cant map spec={spec_line})")
        skip_count += 1
        continue

    try:
        tc = TreeConstraints.build(found)
        selections = decode_profile_talents(talent_str, found)
        result = validate_build(selections, tc)
        cp, sp, hp = count_points(selections, tc)

        if result.valid:
            print(f"  PASS  {basename:55s} class={cp:2d}/34 spec={sp:2d}/34 hero={hp:2d}")
            pass_count += 1
        else:
            print(f"  FAIL  {basename}")
            for err in result.errors[:5]:
                print(f"        {err}")
            fail_count += 1
    except Exception as e:
        print(f"  ERR   {basename}: {e}")
        fail_count += 1

print(f"\n{pass_count} passed, {fail_count} failed, {skip_count} skipped")
