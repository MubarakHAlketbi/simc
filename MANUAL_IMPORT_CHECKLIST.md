# Manual Import Checklist

Items requiring human review. Updated: 2026-03-22 (post imported_data.md application)

---

## 1. Missing Hero Talent Rotation Priorities — FULLY RESOLVED

All 6 original issues fixed via extractor bugs. Visual audit of all 33 specs confirmed
2+ hero builds each with real differentiated content. 5 specs with 3 build variants
now captured (mage/arcane, paladin/ret, warlock/destro, warrior/arms, shaman/ele).

---

## 2. Missing Talent Strings — RESOLVED

| # | Profile | Status |
|---|---------|--------|
| 1 | MID1_Druid_Balance.simc | APPLIED — Keeper of the Grove Build 1 |
| 2 | MID1_Druid_Balance_Elune.simc | APPLIED — Elune's Chosen build |
| 3 | MID1_Evoker_Augmentation.simc | APPLIED — Chronowarden Build 1 |
| 4 | MID1_Evoker_Augmentation_Chronowarden.simc | APPLIED — Chronowarden Build 1 |

All 4 profiles pass 1-iter smoke test. Source: imported_data.md (user-verified Wowhead codes).

---

## 3. Monk Windwalker — Weapon of Wind (ID 1272678) — RESOLVED

**Implemented** via parse_effects in sc_monk.cpp.

Spell data from Wowhead:
- +10% damage during Zenith (passive aura modifying Zenith effectN #2 and #4)
- Affects: Zenith, Weapons of Order

Implementation: `parse_effects( p()->buff.zenith, p()->talent.windwalker.weapon_of_wind );`
The DBC data has Weapon of Wind (1272678) as a flat modifier to Zenith's damage effects.
parse_effects resolves this automatically when passed as an argument.

Build: clean. Smoke test: MID1_Monk_Windwalker.simc passes.

---

## 4. Apex Talents — RESOLVED

Full data in `wowhead/apex_talents_wowhead.md`. Updated with imported corrections:

| Correction | Before | After |
|-----------|--------|-------|
| Blood DK Dance of Midnight R4 | "0% damage / 0% DR" (placeholder) | Swapped R2-3 and R4 — capstone is "When you consume a Rune, chance to call DRW for 6 sec" |
| Feral Unseen Predator R2-3 | "0% damage increase" (placeholder) | 8% at Rank 2, 15% at Rank 3 (from trait data) |
| Demo Warlock apex name | "(Spell #1264137)" | Dominion of Argus — R1: 1276163, R2-3: 1276190, R4: 1276222 |

---

## 5. Phase 4 Missing HecticAddCleave Baselines (4 profiles)

Automated — not manual. These need sim runs:

| Profile | Patchwerk | HecticAddCleave |
|---------|-----------|-----------------|
| MID1_Death_Knight_Blood | Done | MISSING |
| MID1_Death_Knight_Blood_Deathbringer | Done | MISSING |
| MID1_Evoker_Devastation | Done | MISSING |
| MID1_Evoker_Devastation_FS | Done | MISSING |

---

## 6. HIGH Priority APL Gaps (11 specs)

APL diff flagged 11 specs with 3+ missing spells. Need review during Phase 4 optimization.
Full report: `wowhead/APL_diff_report.md`

| # | Spec | Notes |
|---|------|-------|
| 1 | death-knight/blood | |
| 2 | death-knight/unholy | Both heroes now extracted |
| 3 | demon-hunter/devourer | New spec |
| 4 | demon-hunter/havoc | |
| 5 | demon-hunter/vengeance | Tank, "Use X" format now parsed |
| 6 | druid/balance | Talent hash now applied — DPS should improve |
| 7 | druid/guardian | Both heroes now extracted |
| 8 | hunter/survival | |
| 9 | rogue/subtlety | |
| 10 | shaman/elemental | 3 builds including Farseer AoE |
| 11 | shaman/enhancement | |
| 12 | warrior/protection | Tank |

---

## Remaining Items (priority order)

1. **Item 5** (missing baselines) — automated, run when Phase 4 resumes
2. **Item 6** (APL gaps) — review during Phase 4 optimization loop
