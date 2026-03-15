# Task Dossier Template

**Purpose:** Single source of truth for a specific implementation task. Never edit code until this dossier is complete and verified.

---

## Task Metadata

- **Issue/Row Reference:** (e.g., "Row 45: Druid Balance - General Changes")
- **Task Type:** (Class Ability / Trinket / Set Bonus / Talent / APL / Consumable)
- **Target File(s):** (Based on project_structure.md mapping)
- **Status:** Pending → Research → Implementation → Testing → Complete
- **Wowhead Build Date:** YYYY-MM-DD

---

## Ground Truth Data

### 1. Spell/Ability Details (if applicable)

**Spell Name:** 
**Spell ID:** 
**Wowhead Spell URL:**
**Retrieved:** YYYY-MM-DD

**Tooltip Description:**
```
Paste full tooltip from Wowhead
```

**Mechanics:**
- Damage formula: 
- Coefficient: 
- Cast time: 
- Cooldown: 
- Resources: 
- Scaling: 
- Notes on interaction with other abilities/talents:

**Extracted from Spell Page:**
- Any additional effects (proc, debuff, buff)
- Scaling tokens or dummy spells referenced:
  - Token Spell ID: 
  - Token URL: 
  - Token mechanics:

---

### 2. Item/Trinket Details (if applicable)

**Item Name:**
**Item ID:**
**Wowhead Item URL:**
**Retrieved:** YYYY-MM-DD

**Item Level Variants:** (if multiple ilvls exist)
- Base numbers may be item-level dependent

**Item Effect Spell ID:**
**Item Effect Spell URL:**
**Retrieved:** YYYY-MM-DD

**Effect Description:**
```
Paste effect tooltip
```

**Proc Details:**
- Proc chance: 
- Cooldown: 
- Trigger conditions: 
- Scaling formula: 
- Associated buff/debuff: 

**Additional Spell(s):** (if effect references other spells)

---

### 3. Talent Details (if applicable)

**Talent Node ID/Spell ID:**
**Talent Name:**
**Wowhead URL:**
**Retrieved:** YYYY-MM-DD

**Talent Tree & Row:**
**Requirements:**
**Effect on Selection:**
- Spell granted: 
- Passive modifier: 
- Interaction with other talents:

---

### 4. Set Bonus Details (if applicable)

**Set Name:**
**Set ID:**
**Wowhead URL:**
**Retrieved:** YYYY-MM-DD

**2-Piece Bonus:**
- Spell ID: 
- Effect: 
- Conditions: 

**4-Piece Bonus:**
- Spell ID: 
- Effect: 
- Conditions: 

**Notes on Stacking/Interaction:**

---

### 5. Profile Requirements (for testing)

**Profile to Use:** (path to .simc file in profiles/MID1/)
**Talent Configuration:** (specific talents to select)
**Gear Setup:** (mention if specific trinkets/items needed)
**Target Information:** (boss, iterations, desired results)

**Expected Outcome:** (rough DPS/HPS range, specific mechanics to verify)

---

## Implementation Notes

**Important Interactions:** (with other spells, talents, or buffs)
**Edge Cases:** (special conditions that might break)
**Previous Attempts/Issues:** (if reworking existing code)
**Related GitHub Issues:** 

---

## Verification Checklist

- [ ] All Wowhead data cross-referenced and URLs documented
- [ ] Formulas/coefficients extracted correctly (with calculations if needed)
- [ ] Target file(s) identified using project_structure.md
- [ ] Test profile exists or will be created
- [ ] No conflicting implementations in other files
- [ ] Build system implications noted (new files? header updates?)

---

## Code Changes Plan

**Before writing any code, complete the sections above.** Then:

1. **Locate** target file via project_structure.md
2. **Identify** existing similar patterns to follow
3. **Draft** implementation logic in this dossier first
4. **Review** against Wowhead mechanics
5. **Write** code following the drafted plan
6. **Test** with specified profile
7. **Update** project_progress.md

---

## Post-Implementation

**Commit Message:** (draft)
**Files Modified:**
**project_progress.md Rows Updated:**
**Date Completed:** YYYY-MM-DD

---

*Template version: 1.0 - March 15, 2026*
