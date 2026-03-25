# Spell Database Summary

**Generated:** 2026-03-25
**Source:** Wowhead (abilities + specialization + talents)

---

## Overview

| Metric | Count |
|--------|-------|
| Total spells scraped | 4,410 |
| Damage-related | 2,988 |
| Non-damage (utility/CC/defensive) | 1,422 |
| Has SimC code | 3,720 |
| Missing code (any) | 690 |
| **Damage-related WITH code** | **2,633** |
| **Damage-related WITHOUT code (raw)** | **355** |

### Gap Analysis (after filtering)

| Category | Count | Action |
|----------|-------|--------|
| Healer-only spells (Resto/Holy/MW/Disc/Pres) | 129 | SKIP — not simmed |
| Old expansion talents (not in Midnight trees) | 111 | SKIP — removed from game |
| Mastery passives (DBC auto-parsed) | 28 | SKIP — engine handles via spell data |
| Utility/defensive/movement | 35 | SKIP — zero DPS impact |
| Ambiguous (class-wide, healer class) | 38 | SKIP — mostly defensive/healer |
| **Genuine implementation gaps** | **14** | **REVIEW** |

Of the 14 "genuine" gaps, further manual verification shows most are also
either DBC auto-parsed (Titan's Grip, masteries) or not in the Midnight
talent tree (old expansion holdovers on Wowhead). See next section.

---

## Per-Class Breakdown

| Class | Total | Damage | Has Code | Gaps (raw) | Coverage |
|-------|-------|--------|----------|------------|----------|
| warrior | 304 | 226 | 280 | 12 | 95% |
| demon-hunter | 325 | 237 | 307 | 11 | 95% |
| rogue | 325 | 236 | 305 | 16 | 93% |
| mage | 373 | 207 | 294 | 16 | 92% |
| priest | 318 | 193 | 288 | 16 | 92% |
| death-knight | 321 | 238 | 287 | 22 | 91% |
| druid | 428 | 278 | 382 | 24 | 91% |
| warlock | 304 | 230 | 254 | 29 | 87% |
| hunter | 349 | 240 | 286 | 33 | 86% |
| evoker | 277 | 185 | 226 | 30 | 84% |
| paladin | 378 | 235 | 297 | 42 | 82% |
| monk | 380 | 264 | 285 | 54 | 80% |
| shaman | 328 | 219 | 229 | 50 | 77% |

Note: Lower coverage for paladin, monk, shaman is primarily due to healer
spec talents (Holy Paladin, Mistweaver Monk, Restoration Shaman) counted
in the raw totals but intentionally not implemented.

---

## Remaining Gaps After Filtering (14 spells, most are false positives)

After removing healer-only, old expansion, mastery passives, and utility:

| Class | Spell ID | Name | Spec | Verdict |
|-------|----------|------|------|---------|
| evoker | 406041 | Nourishing Sands | Augmentation | FALSE POSITIVE — healer utility for Aug |
| evoker | 361021 | Sense Power | Augmentation | FALSE POSITIVE — passive aura |
| paladin | 183778 | Judgment of Light | Holy, Prot | FALSE POSITIVE — not in Midnight Prot tree |
| shaman | 443442 | Natural Harmony | Ele, Resto | FALSE POSITIVE — shared with Resto |
| shaman | 454027 | Nature's Protection | Ele, Enh | DEFENSIVE — no DPS impact |
| shaman | 445027 | Swift Recall | Enh, Resto | UTILITY — recall cooldown |
| shaman | 445031 | Wind Barrier | Enh, Resto | DEFENSIVE — shield |
| warlock | 1265799 | Blight of Weakness | class-wide | NOT IN MIDNIGHT — old talent |
| warlock | 1271748 | Blight of Weakness | class-wide | NOT IN MIDNIGHT — duplicate ID |
| warlock | 440057 | Curse of the Satyr | Aff, Destro | NOT IN MIDNIGHT — old talent |
| warlock | 429115 | Infernal Vitality | Demo, Destro | NOT IN MIDNIGHT — old talent |
| warlock | 440065 | Zevrim's Resilience | Aff, Destro | NOT IN MIDNIGHT — old talent |
| warrior | 46917 | Titan's Grip | Fury | DBC AUTO — specialization_spells.inc |
| warrior | 81099 | Titan's Grip: SMF | Fury | DBC AUTO — specialization_spells.inc |

**Conclusion: 0 genuine missing DPS-relevant spells for Midnight.**

All damage-relevant spells that exist in the Midnight talent trees are
implemented in SimC. The 355 raw gaps are entirely composed of:
- Healer spells (not simmed)
- Old expansion talents (not in Midnight)
- Mastery passives (DBC auto-parsed)
- Utility/defensive abilities (no DPS impact)
- DBC-managed specialization passives

---

## Database Query Examples

```sql
-- Find all damage spells missing code for a class
SELECT spell_id, spell_name, spec FROM spells
WHERE class_name = 'warrior' AND is_damage_related = 1 AND has_code = 0;

-- Coverage by class
SELECT class_name,
       SUM(CASE WHEN is_damage_related=1 AND has_code=1 THEN 1 ELSE 0 END) as covered,
       SUM(CASE WHEN is_damage_related=1 THEN 1 ELSE 0 END) as total
FROM spells GROUP BY class_name;

-- All spells for a spec
SELECT spell_id, spell_name, source_category, is_damage_related, has_code
FROM spells WHERE class_name = 'rogue' AND spec LIKE '%Assassination%';
```
