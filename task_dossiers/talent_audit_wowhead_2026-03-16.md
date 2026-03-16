# Task Dossier: Full Talent Audit — Wowhead Midnight vs SimC

## Task Metadata

- **Issue/Row Reference:** Full project audit — all DPS/tank specs
- **Task Type:** Talent Audit / Verification
- **Target File(s):** All class modules + project_progress.md
- **Status:** Research Complete → Partial Implementation Needed
- **Wowhead Build Date:** 2026-03-16
- **Audit Method:** Firecrawl HTML extraction from talent calculator pages
  - URL format: https://www.wowhead.com/talent-calc/{class}/{spec}/{hero}
  - DOM selector: div[data-class-spec="{class}-{spec}"]
  - Spell links extracted via aria-label + href patterns within that div
- **Apex Talent Guide:** https://www.wowhead.com/guide/midnight/apex-talents-overview
  - Fetched 2026-03-16 via Firecrawl (44,452 chars)
  - Full guide saved locally: /tmp/apex_talents_full.md
- **Full diff report:** /tmp/talent_audit/diff_report.json
- **Raw HTML per spec:** /tmp/talent_audit/{class}_{spec}.html

---

## Audit Summary

Total Wowhead talents scanned: **2,792** across 33 specs
Total found in SimC:            **2,644**
Total missing:                  **148**
Coverage:                       **94.7%**

---

## Results by Spec

### Death Knight (sc_death_knight.cpp)

| Spec  | WH Talents | In SimC | Missing | Status |
|-------|-----------|---------|---------|--------|
| Blood  | 93 | 90 | 3 | OK |
| Frost  | 81 | 78 | 3 | OK |
| Unholy | 90 | 87 | 3 | OK |

All 3 specs share the same 3 missing talents from the DK class tree:

| Spell ID | Name           | Slug           | Notes |
|----------|----------------|----------------|-------|
| 1267028  | Blood Bond     | blood-bond     | New Midnight class talent |
| 1266819  | Death Notes    | death-notes    | New Midnight class talent |
| 1266818  | Death Defiance | death-defiance | New Midnight class talent |

**Action Required:** Verify if these affect DPS output. If they modify damage spells or generate resources, add `player_talent_t` entries. Otherwise mark as utility/N/A.

Source URLs (to verify):
- https://www.wowhead.com/beta/spell=1267028/blood-bond
- https://www.wowhead.com/beta/spell=1266819/death-notes
- https://www.wowhead.com/beta/spell=1266818/death-defiance

---

### Demon Hunter (sc_demon_hunter.cpp)

| Spec      | WH Talents | In SimC | Missing | Status |
|-----------|-----------|---------|---------|--------|
| Devourer  | 74 | 74 | 0 | COMPLETE |
| Havoc     | 84 | 84 | 0 | COMPLETE |
| Vengeance | 90 | 90 | 0 | COMPLETE |

**All DH specs fully covered. No action required.**

---

### Druid (sc_druid.cpp)

| Spec     | WH Talents | In SimC | Missing | Status |
|----------|-----------|---------|---------|--------|
| Balance  | 88 | 88 | 0 | COMPLETE |
| Feral    | 92 | 92 | 0 | COMPLETE |
| Guardian | 90 | 90 | 0 | COMPLETE |

**All Druid DPS/tank specs fully covered. No action required.**

---

### Evoker (sc_evoker.cpp)

| Spec          | WH Talents | In SimC | Missing | Status |
|---------------|-----------|---------|---------|--------|
| Devastation   | 96 | 92 | 4 | Minor gaps |
| Augmentation  | 97 | 91 | 6 | NEEDS WORK |

**Devastation (4 missing — shared with Aug):**

| Spell ID | Name                | Slug                 | DPS-relevant? |
|----------|---------------------|----------------------|---------------|
| 387787   | Regenerative Magic  | regenerative-magic   | No (defensive) |
| 387341   | Walloping Blow      | walloping-blow       | Yes — melee hit modifier |
| 1267206  | Strike from Above   | strike-from-above    | Yes — new Midnight dmg talent |
| 418101   | Potent Mana         | potent-mana          | Possible — mana regen buff |

**Augmentation (6 missing — 4 above + 2 more):**

| Spell ID | Name                | Slug                 | DPS-relevant? |
|----------|---------------------|----------------------|---------------|
| 1268881  | Improved Defy Fate  | improved-defy-fate   | Yes — enhances Defy Fate CD |
| 431715   | Nozdormu Adept      | nozdormu-adept       | Yes — Nozdormu passive synergy |

**Action Required:**
- Add `player_talent_t walloping_blow`, `strike_from_above`, `improved_defy_fate`, `nozdormu_adept` to Evoker
- Verify `potent_mana` affects combat output
- Verify `regenerative_magic` — likely utility only

Source URLs:
- https://www.wowhead.com/beta/spell=387341/walloping-blow
- https://www.wowhead.com/beta/spell=1267206/strike-from-above
- https://www.wowhead.com/beta/spell=1268881/improved-defy-fate
- https://www.wowhead.com/beta/spell=431715/nozdormu-adept

---

### Hunter (sc_hunter.cpp)

| Spec          | WH Talents | In SimC | Missing | Status |
|---------------|-----------|---------|---------|--------|
| Beast Mastery | 87 | 87 | 0 | COMPLETE |
| Marksmanship  | 82 | 82 | 0 | COMPLETE |
| Survival      | 82 | 82 | 0 | COMPLETE |

**All Hunter specs fully covered. No action required.**

---

### Mage (sc_mage.cpp)

| Spec   | WH Talents | In SimC | Missing | Status |
|--------|-----------|---------|---------|--------|
| Arcane | 79 | 79 | 0 | COMPLETE |
| Fire   | 83 | 83 | 0 | COMPLETE |
| Frost  | 78 | 78 | 0 | COMPLETE |

**All Mage specs fully covered. No action required.**

---

### Monk (monk/sc_monk.cpp + sc_monk.hpp)

| Spec        | WH Talents | In SimC | Missing | Status |
|-------------|-----------|---------|---------|--------|
| Brewmaster  | 78 | 76 | 2 | Minor |
| Windwalker  | 97 | 95 | 2 | Minor |

Both specs share the same 2 missing Monk class tree talents:

| Spell ID | Name               | Slug              | DPS-relevant? |
|----------|--------------------|-------------------|---------------|
| 1266719  | Silent Sanctuary   | silent-sanctuary  | Likely No — defensive/utility |
| 1266740  | Reinvigoration     | reinvigoration    | Possible — energy/resource regen |

**Action Required:** Fetch spell pages to determine if `reinvigoration` affects Energy regen enough to warrant modeling.

Source URLs:
- https://www.wowhead.com/beta/spell=1266719/silent-sanctuary
- https://www.wowhead.com/beta/spell=1266740/reinvigoration

---

### Paladin (paladin/)

| Spec        | WH Talents | In SimC | Missing | Status |
|-------------|-----------|---------|---------|--------|
| Protection  | 79 | 79 | 0 | COMPLETE |
| Retribution | 86 | 86 | 0 | COMPLETE |

**All Paladin DPS/tank specs fully covered. No action required.**

---

### Priest (priest/)

| Spec   | WH Talents | In SimC | Missing | Status |
|--------|-----------|---------|---------|--------|
| Shadow | 94 | 93 | 1 | OK |

| Spell ID | Name           | Slug          | DPS-relevant? |
|----------|----------------|---------------|---------------|
| 9484     | Shackle Horror | shackle-horror | No — CC utility |

**Action Required:** None. Shackle Horror is pure CC, not relevant to DPS simulation.

---

### Rogue (sc_rogue.cpp)

| Spec         | WH Talents | In SimC | Missing | Status |
|--------------|-----------|---------|---------|--------|
| Assassination | 82 | 82 | 0 | COMPLETE |
| Outlaw        | 82 | 82 | 0 | COMPLETE |
| Subtlety      | 83 | 82 | 1 | OK |

| Spell ID | Name                    | Slug                    | DPS-relevant? |
|----------|-------------------------|-------------------------|---------------|
| 382512   | Improved Find Weakness  | improved-find-weakness  | Yes — amplifies Find Weakness armor pen |

**Action Required:** Fetch spell page and verify if `improved_find_weakness` modifies armor ignore % beyond baseline. If yes, add to Subtlety talent tree. Likely a rank-2 passive of an existing node.

Source URL:
- https://www.wowhead.com/beta/spell=382512/improved-find-weakness

---

### Shaman (sc_shaman.cpp)

| Spec         | WH Talents | In SimC | Missing | Status |
|--------------|-----------|---------|---------|--------|
| Elemental    | 83 | 68 | 15 | NEEDS WORK |
| Enhancement  | 84 | 69 | 15 | NEEDS WORK |

**All 15 missing are identical — from the Shaman class tree, not spec trees:**

| Spell ID | Name                             | DPS-relevant? |
|----------|----------------------------------|---------------|
| 383010   | Elemental Orbit                  | YES — damage proc from Earth/Fire/Storm Elemental |
| 108271   | Astral Shift                     | No — defensive |
| 381689   | Brimming with Life               | No — max health |
| 462368   | Elemental Resistance             | No — magic resist |
| 51485    | Earthgrab Totem                  | No — root utility |
| 355630   | Windveil                         | No — dodge |
| 378211   | Refreshing Waters                | No — healing |
| 51886    | Cleanse Spirit                   | No — dispel |
| 192077   | Wind Rush Totem                  | No — raid movement |
| 1279819  | Primordial Bond                  | Possible — stat bonus |
| 51514    | Hex                              | No — CC |
| 108287   | Totemic Projection               | No — totem utility |
| 381650   | Elemental Warding                | No — damage reduction |
| 381930   | Mana Spring                      | Possible — mana regen |
| 204268   | Voodoo Mastery                   | No — Hex utility |

**Action Required:**
- Add `player_talent_t elemental_orbit` to Shaman class tree — this is a NEW Midnight talent with combat proc that IS DPS-relevant
- Add `player_talent_t primordial_bond` — verify if it grants a stat bonus in combat
- All other 13 are utility/defensive/healing and should be marked N/A for SimC

Source URLs:
- https://www.wowhead.com/beta/spell=383010/elemental-orbit   ← HIGH PRIORITY
- https://www.wowhead.com/beta/spell=1279819/primordial-bond

---

### Warlock (warlock/)

| Spec        | WH Talents | In SimC | Missing | Status |
|-------------|-----------|---------|---------|--------|
| Affliction  | 82 | 51 | 31 | NEEDS WORK |
| Demonology  | 84 | 53 | 31 | NEEDS WORK |
| Destruction | 80 | 49 | 31 | NEEDS WORK |

**All 31 missing are identical — entire Warlock CLASS tree is missing from SimC.**

Classified by DPS-relevance:

**DPS-Relevant (must add):**

| Spell ID | Name                         | Why it matters |
|----------|------------------------------|----------------|
| 1270701  | Gorefiend's Avarice          | New Midnight — resource/cooldown synergy |
| 1270690  | Pact of the Nathrezim        | New Midnight — damage pact mechanic |
| 1270255  | Oppressive Darkness          | New Midnight — stacking shadow dmg buff |
| 386689   | Pact of Gluttony             | Passive damage from soul shards |
| 385881   | Teachings of the Black Harvest | Passive — buffs multiple abilities |
| 389367   | Fel Synergy                  | Passive — secondary damage on pet attacks |
| 1265810  | Infernal Beneficiary         | Infernal/Doomguard damage bonus |
| 108416   | Dark Pact                    | Sacrifice shield — affects rotation |
| 108415   | Soul Link                    | Damage split — affects effective HP modeling |
| 1271689  | Empowered Drain Life         | Increases Drain Life damage coefficient |

**Utility (lower priority — model for completeness):**

| Spell ID | Name                  | Notes |
|----------|-----------------------|-------|
| 333889   | Fel Domination        | Pet summon cooldown reduction |
| 108370   | Soul Leech            | Passive absorb |
| 111400   | Burning Rush          | Movement speed |
| 386113   | Fel Pact              | Healthstone cooldown |
| 219272   | Demon Skin            | Passive damage reduction |
| 386124   | Fel Armor             | Armor |
| 386110   | Fiendish Stride       | Burning Rush enhancement |
| 710      | Banish                | CC |
| 334275   | Curse of Exhaustion   | CC |
| 1714     | Curse of Tongues      | CC |
| 6789     | Mortal Coil           | Horror + heal |
| 268358   | Demonic Circle        | Teleport |
| 1265816  | Improved Mortal Coil  | Mortal Coil enhancement |
| 1265813  | Foul Mouth            | Curse enhancement |
| 1271699  | Empowered Healthstone | Healthstone buff |
| 389609   | Abyss Walker          | Demonic Circle buff |
| 1271694  | Fortified Soul        | HP buff |
| 111771   | Demonic Gateway       | Raid utility |
| 452902   | Swift Artifice        | Summoning speed |
| 1265801  | Frequent Traveler     | Gateway buff |
| 389590   | Demonic Resilience    | Damage reduction |

**Action Required:**
This is the largest gap in the entire codebase. The Warlock class tree is largely unregistered in SimC. All three specs share this deficit.
- Create dossier task: `warlock_class_tree_2026-03-16.md`
- Priority order: DPS-relevant talents first (10 listed above)
- Target file: `warlock/sc_warlock_init.cpp` and `warlock/sc_warlock.hpp`

Source URLs:
- https://www.wowhead.com/beta/spell=1270701/gorefiends-avarice
- https://www.wowhead.com/beta/spell=1270690/pact-of-the-nathrezim
- https://www.wowhead.com/beta/spell=1270255/oppressive-darkness
- https://www.wowhead.com/beta/spell=386689/pact-of-gluttony
- https://www.wowhead.com/beta/spell=385881/teachings-of-the-black-harvest

---

### Warrior (sc_warrior.cpp)

| Spec        | WH Talents | In SimC | Missing | Status |
|-------------|-----------|---------|---------|--------|
| Arms        | 67 | 67 | 0 | COMPLETE |
| Fury        | 83 | 83 | 0 | COMPLETE |
| Protection  | 82 | 82 | 0 | COMPLETE |

**All Warrior specs fully covered. No action required.**

---

## Apex Talent Audit (All Specs)

Source: https://www.wowhead.com/guide/midnight/apex-talents-overview
Retrieved: 2026-03-16

### System Overview
- 3-node path at bottom of each spec tree
- 4 total points: 1pt (node 1) + 2pt (node 2) + 1pt (node 3)
- Unlock: 20 pts in spec tree required; nodes unlock at levels 81, 84, 90

### All Apex Talent Spell IDs (from guide)

| Spec               | Apex Name             | Spell ID | Node 1 | Node 2 (2pt) | Node 3 |
|--------------------|-----------------------|----------|--------|--------------|--------|
| Blood DK           | Dance of Midnight     | 1264506  | Parry->Heart Strike free | Proc Dancing Rune Weapon 6s | +dmg/−dmg taken per DRW |
| Frost DK           | Chosen of Frostbrood  | 1265632  | FWF +100% 1st hit, +15% haste 12s | FWF extends PoF 2s; +4% Str | All Frost +10%; FWF +100%; recall at 50% |
| Unholy DK          | Forbidden Knowledge   | 1242158  | Army→Necrotic Coil(1242174) + Graveyard(383269) 15s | Putrefy→Ghoul+3% Mastery 12s | Magus+8% per Necro/Grave; Dread Plague 20% rouse |
| Devourer DH        | Midnight              | 1242486  | Collapsing Star always crits | +3% Cosmic dmg; CS crit+50% of crit% | Void Meta→5 Soul Frags+instant CS |
| Havoc DH           | Eternal Hunt          | 1270898  | The Hunt→Eye Beam+100% wider | Hunt −15s CD, +15% dmg, DoT+2 enemies | Blade Dance+20%; channel Eye Beam→refresh BD CD |
| Vengeance DH       | Untethered Rage       | 1270444  | SC/SB proc Untethered Rage→free 10s Meta | SC/SB +1 fragment, +5% dmg each | Non-proc→Seething Anger (+1% Agi per stack, 12s) |
| Balance Druid      | Ascendant Eclipses    | 1261564  | Eclipse→instant Wrath/SF; first 3 Starsurge/Starfall+20% | Crits during Eclipse→languish 12% over 6s | Eclipse→Solar Bolt(1261573)/Lunar Bolt(1263137) always crit |
| Feral Druid        | Unseen Predator       | 1263657  | Ferocious Bite 15%/pt→Unseen Slash(1263827)+Swipe(1263902) | Unseen Attacks→+dmg% 5s stackable | Tiger's Fury→Unseen Attack next 2 combo gen; Rip+30% |
| Guardian Druid     | Wild Guardian         | 1269614  | Post-Berserk→Wild Guardian(1269616): echo next 2 Ironfur/Maul/FR at 50% | +3% Mastery; Maul always empowered +20% Nature 12s | Wild Guardian→2 Dream Guide charges; echoes at 150%, 2x over 8s |
| Devastation Evoker | Rising Fury           | 1271687  | Dragonrage→+4% haste per 6s, stack 5 | On end: Risen Fury 4s/stack; haste+dmg+Essence Burst/4s | At 5 stacks: all dmg +8% |
| Augmentation Evoker| Duplicate             | 1259173  | Breath of Eons→future-you 20s; casts Eruption/Fire Breath/Upheaval | Extend Ebon Might→Duplicate+50% of extension | While active: Ebon Might+100% stats; Upheaval/Eruption+25% |
| BM Hunter          | Nature's Ally         | 1273043  | Bestial Wrath→Animal Companion 15s | Pet dmg+5%; BW strikes 2 extra targets | Barbed+Cobra+15%; all 3 increase next Kill Command+30% |
| MM Hunter          | Take Aim              | 1273132  | Rapid Fire+25%; each shot−0.5s Aimed Shot CD | Aimed Shot crit+25% of crit%; other ranged+3% | Aimed Shot always crits |
| Survival Hunter    | Raptor Swipe          | 1259003  | [Note: guide says Aimed Shot crits — likely typo, see comments] | Raptor Strike/WB/Swipe+10%; Swipe primary+25% | Raptor Strike→100% Raptor Swipe; Swipe with Tip→Strike as One 300% |
| Arcane Mage        | Touch of the Archmage | 1257942  | Touch of the Magi+15% dmg taken | Arcane Charges+15% Blast/Pulse/Barrage; Missiles+10% | TotM explosion→pulsing rune 75% over 6s, +50% on initial target |
| Fire Mage          | Fired Up              | 1257343  | Hot Streak 20%→Fired Up stack +4% Fire 12s | Combustion→higher Fired Up chance; Fired Up→+1s Combustion | Fired Up→−2.5s Fire Blast CD; all Fire+3% |
| Frost Mage         | Hand of Frost         | 1262769  | Shatter 10%→Hand of Frost (500% SP Frost+1 Freezing) | Each Freezing Shattered+1% Hand proc; Hand dmg→+1% spell dmg 8s | Ray of Frost→4 Hands; +1 RoF charge; RoF+25% |
| Brewmaster Monk    | Bring Me Another      | 1265129  | Brew 20%→Empty Barrel→Keg Smash ricochet 300% AP, 4x 80% | Barrel→reset Keg Smash CD, 0 energy; Phys+10% | Fortifying Brew/Celestial→tap keg, Refreshing Drink(1265145) for self+2 allies |
| Windwalker Monk    | Tigereye Brew         | 1261703  | In combat→+2% crit/8s during next Zenith, stack 20 | Crit dmg+5% | Crit chance→15% chance to increase Fists of Fury dmg per hit |
| Prot Paladin       | Glory of the Vanguard | 1267203  | Judgment→Vanguard: Avenger's Shield echoing bolt line 300% AP | Judgment+10%; Vanguard→+1 Holy Power | Post-Vanguard Shield of the Righteous+50%, light refract 4 targets 200% AP; during AW: AS always Vanguard |
| Ret Paladin        | Light Within          | 1261113  | Righteous Cause/Art of War→Blade of Justice+150% | AW→Final Verdict/Templar's Verdict+Divine Storm+10% | BoJ wave of Holy energy: 442.557%*2 AP primary, 442.557% all in path |
| Shadow Priest      | Void Apparitions      | 1264096  | Idol activation→Shadowy Apparitions | Apparitions 15/30% chance→Void Apparitions+Void Bolt(1264177) 150% SP | Tentacle Slam→100% Idol activation |
| Discipline Priest  | Master the Darkness   | 1253590  | Penance 50%→Power Word: Shield→Void Shield(1253593) 3 allies 15s | Shadow dmg+Atonement+3% | Void Shield reflects 25% dmg→Atonement healing |
| Assassination Rogue| Implacable            | 1265385  | Envenom+10%; on expiry+20% energy regen 5s; +15% per Envenom used during bonus (max 80%) | Nature+Bleed+10% | Post-Kingsbane: 5 rapid strikes 1s (260% AP Phys+180% AP Nature), each applies poisons, generates CP |
| Outlaw Rogue       | Gravedigger           | 1265861  | Between the Eyes 45%→2 stacks bonus dmg | Dispatch 5+ CP→Scoundrel Strike 160% AP | Dispatch 12%/CP→hidden bullet; at 6→free BtE, 0 energy, +6 CP, reset CD |
| Subtlety Rogue     | Ancient Arts          | 1268932  | Shadow Techniques combo gen 15%/stack→Shadow Clone repeats attack 50% as Shadow | Shadow+5%; Clones 50% chance to trigger ST | Finishing move with 5+ ST stacks→expend for CP up to max |
| Elemental Shaman   | Feedback Loop         | 1270061  | Elemental Overload+35% | Spell crit+5%; Elemental Fury+25% crit dmg | Overloads 25% chance to cause additional Overload (no chain) |
| Enhancement Shaman | Storm Unleashed       | 1262713  | Maelstrom spent 2%→next Crash Lightning ignores CD; CL weapon enhance can overlap | Maelstrom spending+8%; Weapon Imbuements+10% | CL electrocutes 50% dmg 2x over 2s; CL weapon enhance→+15% auto-attack speed |
| Restoration Shaman | Stormstream Totem     | 1267016  | Riptide 6%→Healing Stream→Stormstream Totem (healer spec — N/A) | — | — |
| Affliction Warlock | Shadow of Nathreza    | 1261984  | Haunt→demonic soul (36.181%SP * 18 Shadow over duration to host+3 nearby w/Corruption) | Haunt initial+50%; +2% dmg to host | Haunt dmg chance→release soul→Wrath of Nathreza(1262028) meteor 10yd |
| Demonology Warlock | (Spell 1264137)       | 1264137  | [Guide data incomplete — Soulkeeper mechanic] | Soulkeeper collects Demonic Cores, increasing chance to proc Willbreaker(1264367) | Willbreaker: 100% SP Chaos / 0.5s over 8.5s, 10yd |
| Destruction Warlock| Embers of Nihilam     | 1265770  | Incinerate chance→Echo of Sargeras(1265884): 150% SP Shadowflame+130% SP 10yd AoE | +4% crit+4% haste 6s on proc | Chaos Bolt/Shadowburn/Rain of Fire→50/50/60% EoS; targets Immolate if no target |
| Arms Warrior       | Master of Warfare     | 1269391  | Overpower→Heroic Strike(1269383): 600% AP Phys+Master of Warfare stack (3% armor pen 30s, stackable) | Per stack: Mortal Strike/Cleave/Overpower+2.5%, crit dmg+2.5% | Heroic Strike→−2s Colossus Smash CD |
| Fury Warrior       | Rampaging Berserker   | 1269308  | Rampage+10%; Rampage→Berserk (+3% Str 8s, stackable) | Rampage−15 Rage, +5% dmg during Recklessness | Recklessness→+3 Berserk stacks, Recklessness duration+50% |
| Prot Warrior       | Phalanx               | 1269311  | Thunder Clap→next Shield Slam: wave 198% AP Phys to front, −5% dmg taken 8s | Thunder Clap+Phalanx+10% | During Shield Block: Shield Slam+10% dmg, +20% crit chance |

---

## Implementation Priority Queue

Based on the audit, these are ordered by impact:

### Priority 1 — DPS-Critical (implement immediately)

1. **Warlock class tree — DPS passives** (affects all 3 specs)
   - Gorefiend's Avarice (1270701), Pact of Nathrezim (1270690), Oppressive Darkness (1270255)
   - Pact of Gluttony (386689), Teachings of Black Harvest (385881)
   - Target: `warlock/sc_warlock_init.cpp`, `warlock/sc_warlock.hpp`

2. **Shaman — Elemental Orbit** (affects Elemental + Enhancement)
   - New Midnight talent — elemental proc during Elemental usage
   - Target: `sc_shaman.cpp`

3. **Evoker — Strike from Above + Nozdormu Adept + Improved Defy Fate** (Aug/Devast)
   - Target: `sc_evoker.cpp`

4. **Subtlety Rogue — Improved Find Weakness** (382512)
   - Likely armor pen modifier on Find Weakness
   - Target: `sc_rogue.cpp`

### Priority 2 — Verify before implementing

5. **DK — Blood Bond / Death Notes / Death Defiance** (all 3 specs)
   - May be utility. Fetch spell pages to confirm.

6. **Monk — Reinvigoration** (1266740)
   - May affect Energy regen rate in rotation.

7. **Shaman — Primordial Bond** (1279819)
   - Verify if stat grant is combat-relevant.

8. **Evoker — Walloping Blow / Potent Mana**
   - Verify DPS impact.

### Priority 3 — Utility only (mark N/A in SimC)

- Shadow Priest: Shackle Horror (9484) — pure CC
- Shaman class tree: 13 of 15 missing talents — defensive/CC/healing
- Warlock class tree: 21 of 31 missing talents — defensive/utility
- Monk: Silent Sanctuary (1266719) — defensive

---

## Apex Talent Implementation Status

All 33 DPS/tank specs have apex talent code already present in SimC (verified by grep).
The Apex Talents guide was fully extracted and all spell IDs confirmed (54 total spell refs).

Demonology Warlock note: guide data for apex talent node 1 and node 2 descriptions are incomplete/placeholder. Spell 1264137 has no name in the guide. Willbreaker (1264367) is the proc spell.

---

## Verification Checklist

- [x] Wowhead talent calculator extracted for all 33 DPS/tank specs
- [x] Apex Talents guide fully extracted (54 spell refs)
- [x] SimC code searched for all 2,792 Wowhead talent references
- [x] Missing talents classified by DPS-relevance
- [ ] Spell pages fetched for Priority 1 items
- [ ] Priority 1 talents implemented in SimC
- [ ] Priority 2 talents verified and triaged
- [ ] project_progress.md updated with Apex Talent section

---

## Files Referenced

- Raw audit data: `/tmp/talent_audit/diff_report.json`
- Per-spec HTML: `/tmp/talent_audit/{class}_{spec}.html`
- Apex guide: `/tmp/apex_talents_full.md`
- Batch data: `/tmp/talent_audit/batch_{0,1,2}.json`

---

## Post-Implementation

**Commit Message (draft):** `[Midnight] Talent audit dossier — Wowhead vs SimC, 94.7% coverage`
**Date:** 2026-03-16

---

*Dossier version: 1.0 - 2026-03-16*
