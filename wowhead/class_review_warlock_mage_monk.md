# Class Code Audit Report — Warlock, Mage, Monk
Generated: 2026-03-17
Auditor: Hermes Agent

---

## Methodology

For each flagged item from the task brief:
1. Read full talent tables from wowhead/{class}/{spec}/info_base.md
2. Cross-referenced spell names with actual game spell data (sc_spell_data.inc)
3. Verified code name matches in sc_warlock_init.cpp, sc_mage.cpp, sc_monk.cpp
4. Checked for truncated names (info_base table pipe truncation)

---

## WARLOCK

### Verdict: All flagged items resolved correctly; one NOTE comment added.

#### Truncated/Shortened Names in info_base — All Correct in Code:

| info_base name | Actual spell name | Spell ID | Code identifier | Status |
|---|---|---|---|---|
| gorefiend | Gorefiend's Avarice | 1270701 | `gorefiends_avarice` | CORRECT (find_talent "Gorefiend's Avarice") |
| death | Death's Embrace | 234876 | `deaths_embrace` | CORRECT |
| alzzin | Alzzin's Iniquity | 1266803 | `alzzins_iniquity` | CORRECT (Hellcaller hero) |
| mark_of_peroth | Mark of Peroth'arn | 440045 | `mark_of_perotharn` | CORRECT (find_talent "Mark of Peroth'arn") |
| sacrolash | Sacrolash's Dark Strike | 386986 | `sacrolashs_dark_strike` | CORRECT |
| sataiel | Sataiel's Volition | 449637 | `sataiels_volition` | CORRECT (Soul Harvester hero) |
| xalan (x2) | Xalan's Ferocity / Xalan's Cruelty | 440044 / 440040 | `xalans_ferocity` / `xalans_cruelty` | CORRECT (two separate talents) |
| xavius | Xavius' Gambit | 416615 | `xavius_gambit` | CORRECT |
| imp_erator | Imp-erator | 416230 | `imperator` | CORRECT (find_talent "Imp-erator") |
| mind | Mind's Eyes | 1268716 | `minds_eyes` | CORRECT (Diabolist hero) |
| tyrant | Tyrant's Oblation | 1276746 | `tyrants_oblation` | CORRECT |
| alythess | Alythess's Ire | 1244941 | `alythesss_ire` | CORRECT (triple-s matches apostrophe) |

#### Multi-Rank Talents — Correct:
- shadow_of_nathreza (1261984) — code has `shadow_of_nathreza_1/2/3` (3-rank) — CORRECT
- dominion_of_argus (1276163) — code has `dominion_of_argus_1/2/3` (3-rank) — CORRECT
- embers_of_nihilam (1265770) — code has `embers_of_nihilam_1/2/3` (3-rank) — CORRECT

#### hand_of_guldan Verification:
- info_base shows ID 105174 for "Hand of Gul'dan" (this is the _cast_ proc spell)
- Code correctly registers the talent as "Hand of Gul'dan" (find by name, internal ID ~1250273)
  and `hand_of_guldan_cast = conditional_spell_lookup(..., 105174)` for the actual cast spell — CORRECT

#### Fuzzy Mismatch Resolutions:
- `improved_haunt` — Affliction spec talent (458034) — CORRECT for Affliction
- `improved_havoc` — Destruction spec talent (1244460) — CORRECT for Destruction (NOT swapped)
- `improved_shadow_bolt` (453080) — Affliction spec talent — CORRECT
- `improved_chaos_bolt` (456951) — Destruction spec talent — CORRECT
- `empowered_felstorm` (1279575) — Demonology spec talent — CORRECT
- `empowered_healthstone` (1271699) — Class talent — CORRECT
- `practiced_chaos` (1244284) — Destruction spec talent — CORRECT (Destruction has Chaos Bolt)
- `practiced_rituals` (1250375) — Demonology spec talent — CORRECT (Demonology uses rituals)
- `mark_of_perotharn` — correct form of "Mark of Peroth'arn" — CORRECT

#### Change Made:
**sc_warlock_init.cpp line ~104**: Added NOTE comment for Soul Link (ID 108415):
```cpp
// NOTE: not in info_base.md — Soul Link (ID 108415) is in info_base.md as a class talent but is NOT registered here.
// Soul Link is a passive utility/survivability talent (splits 10% damage to your demon pet); no direct DPS relevance per audit rules.
```

---

## MAGE

### Verdict: All flagged items already correctly implemented. No code changes needed.

#### Truncated/Shortened Names — All Correct in Code:

| info_base name | Actual spell name | Spell ID | Code identifier | Status |
|---|---|---|---|---|
| archmage | Archmage's Wrath | 444968 | `archmages_wrath` | CORRECT (Spellslinger hero) |
| consortium | Consortium's Bauble | 461260 | `consortiums_bauble` | CORRECT |
| memory_of_al | Memory of Al'ar | 449619 | `memory_of_alar` | CORRECT (Sunfury hero) |
| touch_of_the_archmage | Touch of the Archmage | 1257942 | `touch_of_the_archmage_1/2/3` | CORRECT (3-rank, found by ID) |
| winter (arcane, 382424) | Winter's Protection | 382424 | `winters_protection` | CORRECT (class talent) |
| winter (frost, 417489) | Winter's Blessing | 417489 | `winters_blessing` | CORRECT (frost spec talent) |
| fire | Fire's Ire | 450831 | `fires_ire` | CORRECT (fire spec talent) |
| fired_up | Fired Up | 1257343 | `fired_up_1/2/3` | CORRECT (3-rank, found by ID) |
| hand_of_frost | Hand of Frost | 1262935 | `hand_of_frost_1/2/3` | CORRECT (3-rank, found by ID) |

Note: The info_base truncates "Archmage's Wrath" to "Archmage", "Winter's Protection" to "Winter",
"Fire's Ire" to "Fire", etc. due to table column width limits. All are correctly implemented.

---

## MONK

### Verdict: All flagged items already correctly implemented. No code changes needed.

#### Truncated/Shortened Names — All Correct in Code:

| info_base name | Actual spell name | Spell ID | Code identifier | Status |
|---|---|---|---|---|
| bring_me_another | Bring Me Another | 1265129 | `bring_me_another_1/2/3` | CORRECT (3-rank) |
| gai_plin | Gai Plin's Imperial Brew | 383700 | `gai_plins_imperial_brew` | CORRECT |
| niuzao | Niuzao's Resolve | 1241097 | `niuzaos_resolve` | CORRECT |
| spirit (450595) | Spirit's Essence | 450595 | `spirits_essence` | CORRECT (class talent) |
| stormstout | Stormstout's Last Keg | 383707 | `stormstouts_last_keg` | CORRECT |
| tiger (116841) | Tiger's Lust | 116841 | `tigers_lust` | CORRECT (class talent) |
| veteran (450987) | Veteran's Eye | 450987 | `veterans_eye` | CORRECT (Shado-Pan hero) |
| wind (450514) | Wind's Reach | 450514 | `winds_reach` | CORRECT (class talent) |
| yu (414131) | Yu'lon's Grace | 414131 | `yulons_grace` | CORRECT (class talent) |
| yu (1262667) | Yu'lon's Avatar | 1262667 | `yulons_avatar` | CORRECT (CotC hero) |
| brawler (451485) | Brawler's Intensity | 451485 | `brawlers_intensity` | CORRECT (windwalker) |
| chi_ji (443566) | Chi-Ji's Swiftness | 443566 | `chijis_swiftness` | CORRECT (CotC hero) |
| dance_of_chi_ji (325201) | Dance of Chi-Ji | 325201 | `dance_of_chiji` | CORRECT (windwalker) |
| tigereye_brew (1261703) | Tigereye Brew | 1261703 | `tigereye_brew_1/2/3` | CORRECT (3-rank) |
| xuen (392993) | Xuen's Battlegear | 392993 | `xuens_battlegear` | CORRECT (windwalker) |

---

## Summary of Changes

### Files Modified:
1. `engine/class_modules/warlock/sc_warlock_init.cpp`
   - Added NOTE comment about Soul Link (ID 108415) not being registered (utility-only talent)

### Files Not Modified (all verified correct):
- `engine/class_modules/warlock/sc_warlock.hpp`
- `engine/class_modules/warlock/sc_warlock.cpp`
- `engine/class_modules/warlock/sc_warlock_actions.cpp`
- `engine/class_modules/sc_mage.cpp`
- `engine/class_modules/monk/sc_monk.cpp`
- `engine/class_modules/monk/sc_monk.hpp`

### Key Finding:
The vast majority of "missing" items in the audit report were due to info_base.md table column truncation.
The pipe character in spell names (like apostrophes in "Gorefiend's Avarice") caused the table to 
display truncated forms. All actual SimC code identifiers correctly match the full spell names.

### DPS-Relevant Missing Implementations: NONE FOUND
All DPS-relevant talents from info_base.md are implemented in the SimC code.

---
*Audit completed: 2026-03-17 by Hermes Agent*
