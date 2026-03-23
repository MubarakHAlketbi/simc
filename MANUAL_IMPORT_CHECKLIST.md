# Manual Import Checklist

Items requiring human review. Updated: 2026-03-22 (post visual audit of all 33 specs)

---

## 1. Missing Hero Talent Rotation Priorities — FULLY RESOLVED

**ALL 6 RESOLVED** — three separate extractor bugs fixed through visual inspection of
every Wowhead rotation page:

| # | Spec | Root Cause | Fix |
|---|------|-----------|-----|
| 1 | paladin/retribution | Build-variant buttons ("Templar ES" not "Templar") | Prefix matching |
| 2 | mage/arcane | Build-variant buttons ("Spellslinger" prefix) | Prefix matching |
| 3 | death-knight/unholy | Apostrophe stripped ("Sanlayn" not "San'layn") | Name normalization |
| 4 | druid/guardian | Apostrophe stripped ("Elunes Chosen" not "Elune's Chosen") | Name normalization |
| 5 | monk/brewmaster | Hyphen to space ("Shado Pan" not "Shado-Pan") | Name normalization |
| 6 | monk/windwalker | Hyphen to space ("Shado Pan" not "Shado-Pan") | Name normalization |

**Additional finding:** visual audit of all 33 specs found 5 specs with 3 build variants
(previously collapsed into 2 by prefix grouping). Now all captured:

| Spec | Build Variants |
|------|---------------|
| mage/arcane | Spellslinger (Orb) + Spellslinger Missile Build + Sunfury |
| paladin/retribution | Templar ES + Templar RG + Herald of the Sun |
| warlock/destruction | Hellcaller + Diabolist + Diabolist Demons |
| warrior/arms | Slayer + Colossus + Colossus Smash |
| shaman/elemental | Farseer + Stormbringer + Farseer AoE |

**Final validation: 33/33 specs have 2+ hero builds, real differentiated content, zero errors.**

---

## 2. Missing Talent Strings (2 profiles using defaults)

These profiles have `talents=` commented out and are running on game defaults.
The extracted talent codes exist — just need to pick the right build.

| # | Profile | Issue | Extracted Talent Codes |
|---|---------|-------|----------------------|
| 1 | MID1_Druid_Balance.simc | `# talents=` commented out — running defaults (causes ~3k DPS in Phase 4) | `wowhead/druid/balance/extracted/talents.md` has 5 builds under Elune's Chosen + Keeper of the Grove. Pick Build 1 for the base profile. |
| 2 | MID1_Evoker_Augmentation.simc | `# talents=` commented out — running defaults (~8k DPS) | `wowhead/evoker/augmentation/extracted/talents.md` has 4 builds under Scalecommander. Pick Build 1 for the base profile. Note: Chronowarden hero talent was not extracted (only Scalecommander visible). |

**Suggested talent codes:**
```
# Druid Balance (Elune's Chosen Build 1):
talents=CYGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWoMbNjxMDMmlZmZmBYYWmZbYGzYjlZMzMjZ2wAgBYZbshpZmlRAAAA2MzMzMYzYYMDgZGAYA

# Evoker Augmentation (Scalecommander Build 1):
talents=CEcBAAAAAAAAAAAAAAAAAAAAAMmxMbzMzMWGYmlZMGmZDAAAAAGAAMzMwgxUjZmZAAAAwMmZGzMbjZGYmNDMmxCLwAzwQjYBzMmZAgB
```

**Before applying:** verify these codes correspond to common raid builds on Wowhead.

---

## 3. Monk Windwalker — Weapon of Wind (ID 1272678) Implementation

The talent is registered in code but has NO effect implementation:
- `sc_monk.hpp:950` — `player_talent_t weapon_of_wind;` declared
- `sc_monk.cpp:5526` — `talent.windwalker.weapon_of_wind = _ST("Weapon of Wind");` registered
- No parse_effects, no buff, no action, no damage modifier anywhere in the codebase

**What's needed from Wowhead:**
- URL: https://www.wowhead.com/spell=1272678
- What does Weapon of Wind do? (e.g. +10% damage during Zenith, as previously noted)
- What spell effect type is it? (flat damage multiplier? buff? proc?)
- What effectN values does it have?

---

## 4. Apex Talents — All Specs Use Max Rank (Rank 4)

**RESOLVED:** Full apex talent data extracted from Wowhead and saved to
`wowhead/apex_talents_wowhead.md`. All 33 DPS/tank specs + 5 healer specs documented
with R1/R2-3/R4 descriptions.

**Key facts:**
- All specs should use max rank (Rank 4 = all 3 nodes talented, 4 points total)
- Rank 4 unlocks at Level 90 (level cap)
- Each apex talent has 3 sequential nodes: R1 (level 81), R2-3 (level 84, 2-point), R4 (level 90)
- Demonology Warlock apex (Spell #1264137) has INCOMPLETE data on Wowhead — R1/R2 descriptions missing

**Notable Wowhead tooltip issues (verify against live spell data):**
- Blood DK "Dance of Midnight" R4: shows 0% damage increase and 0% DR — placeholder
- Feral "Unseen Predator" R2-3: shows 0% damage increase — placeholder
- Survival Hunter R1: shows "Aimed Shot always critically strikes" — copy error from Marksmanship
- Demonology Warlock: talent name not displayed, only Spell #1264137 reference

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

The APL diff report flagged these specs with 3+ missing spells between Wowhead guide
and SimC APL. Need human review to separate real gaps from false positives.
Note: items 2 and 7 now have full hero talent data (previously incomplete).

| # | Spec | Notes |
|---|------|-------|
| 1 | death-knight/blood | Review `wowhead/APL_diff_report.md` section |
| 2 | death-knight/unholy | Both heroes now extracted (was only Rider) |
| 3 | demon-hunter/devourer | New spec, may have significant gaps |
| 4 | demon-hunter/havoc | Review |
| 5 | demon-hunter/vengeance | Tank spec, "Use X" format now parsed |
| 6 | druid/balance | No valid talent hash, APL on defaults |
| 7 | druid/guardian | Both heroes now extracted (was only Druid of the Claw) |
| 8 | hunter/survival | Review |
| 9 | rogue/subtlety | Review |
| 10 | shaman/elemental | Now has 3 builds including Farseer AoE variant |
| 11 | shaman/enhancement | Review |
| 12 | warrior/protection | Tank spec |

Full report: `wowhead/APL_diff_report.md`

---

## Priority Order

1. **Item 2** (talent strings) — 5 minutes, immediately unblocks Phase 4 DPS accuracy
2. **Item 3** (Weapon of Wind) — 15 min research, needs code implementation after
3. **Item 6** (APL gaps) — ongoing, review during Phase 4 optimization
4. **Item 5** (missing baselines) — automated, run when Phase 4 resumes
