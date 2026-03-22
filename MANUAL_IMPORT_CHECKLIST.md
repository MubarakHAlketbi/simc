# Manual Import Checklist

Items the automated pipeline cannot resolve — requires human review of Wowhead pages.
Generated: 2026-03-22

---

## 1. Missing Hero Talent Rotation Priorities (6 specs)

The extractor cannot find the second hero talent switch button on these Wowhead pages.
You need to visit each URL, manually click the missing hero talent, and copy the
rotation priority list into the corresponding `wowhead/{class}/{spec}/extracted/rotation.md`.

| # | Spec | URL | Has | Missing |
|---|------|-----|-----|---------|
| 1 | paladin/retribution | https://www.wowhead.com/guide/classes/paladin/retribution/rotation-cooldowns-pve-dps | Nothing (0 heroes found) | Herald of the Sun + Templar |
| 2 | death-knight/unholy | https://www.wowhead.com/guide/classes/death-knight/unholy/rotation-cooldowns-pve-dps | Rider of the Apocalypse | San'layn |
| 3 | druid/guardian | https://www.wowhead.com/guide/classes/druid/guardian/rotation-cooldowns-pve-tank | Druid of the Claw | Elune's Chosen |
| 4 | mage/arcane | https://www.wowhead.com/guide/classes/mage/arcane/rotation-cooldowns-pve-dps | Sunfury | Spellslinger |
| 5 | monk/brewmaster | https://www.wowhead.com/guide/classes/monk/brewmaster/rotation-cooldowns-pve-tank | Master of Harmony | Shado-Pan |
| 6 | monk/windwalker | https://www.wowhead.com/guide/classes/monk/windwalker/rotation-cooldowns-pve-dps | Conduit of the Celestials | Shado-Pan |

**What to check on each page:**
- Is there actually a hero talent switch button? (some guides may not differentiate)
- If yes, does it use a different UI pattern? (dropdown, radio button, toggle instead of button)
- If rotation is identical for both hero talents, note that — no import needed
- If different, copy the ST priority, AoE priority, and Opener for the missing hero talent

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

## 4. Phase 4 Missing HecticAddCleave Baselines (4 profiles)

These profiles have Patchwerk baselines but no HecticAddCleave. Need to be re-run
(this is automated — not manual — but noting for completeness):

| Profile | Patchwerk | HecticAddCleave |
|---------|-----------|-----------------|
| MID1_Death_Knight_Blood | Done | MISSING |
| MID1_Death_Knight_Blood_Deathbringer | Done | MISSING |
| MID1_Evoker_Devastation | Done | MISSING |
| MID1_Evoker_Devastation_FS | Done | MISSING |

---

## 5. HIGH Priority APL Gaps (11 specs)

The APL diff report flagged these specs as having significant gaps (3+ missing spells)
between the Wowhead rotation guide and the SimC APL. These need human review to determine
if the MISSING actions are real gaps or false positives (engine-managed, passive, etc.).

| # | Spec | Action |
|---|------|--------|
| 1 | death-knight/blood | Review `wowhead/APL_diff_report.md` section |
| 2 | death-knight/unholy | Review — note: only Rider of the Apocalypse rotation extracted |
| 3 | demon-hunter/devourer | Review — new spec, may have significant gaps |
| 4 | demon-hunter/havoc | Review |
| 5 | demon-hunter/vengeance | Review — tank spec, "Use X" format now parsed |
| 6 | druid/balance | Review — no valid talent hash, APL on defaults |
| 7 | druid/guardian | Review — tank, only Druid of the Claw extracted |
| 8 | hunter/survival | Review |
| 9 | rogue/subtlety | Review |
| 10 | shaman/elemental | Review |
| 11 | shaman/enhancement | Review |
| 12 | warrior/protection | Review — tank spec |

Full report: `wowhead/APL_diff_report.md`

---

## Priority Order

1. **Item 2** (talent strings) — 5 minutes, immediately unblocks Phase 4 DPS accuracy
2. **Item 1** (hero talent rotations) — 30-60 min, improves APL source data quality
3. **Item 3** (Weapon of Wind) — 15 min research, needs code implementation after
4. **Item 5** (APL gaps) — ongoing, review during Phase 4 optimization
5. **Item 4** (missing baselines) — automated, will be run when Phase 4 resumes
