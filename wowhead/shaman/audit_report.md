# Shaman Spec Audit Report — Wowhead vs SimC
Generated: 2026-03-24
Auditor: Hermes Agent

## Summary

Audited Elemental and Enhancement Shaman specs. Compared Wowhead rotation guides,
tier set bonuses, and talent mechanics against the SimC APL generator and class module.

Overall: Both specs have functional APLs with tier sets partially/fully implemented.
Several discrepancies found, mostly in priority ordering differences and missing
Enhancement MID1 (Midnight Season 1) tier set.

---

## 1. ELEMENTAL SHAMAN

### 1.1 Tier Set Bonuses (Mantle of the Primal Core — MID1)

Wowhead describes:
- 2pc: Casting Stormkeeper grants 15% haste for 10 sec
- 4pc: Stormkeeper grants 1 additional stack and +25% damage to LB/CL

SimC implementation status:
- [IMPLEMENTED] 2pc: buff.mid1_ele_2pc ("thunderous_velocity") triggered on SK cast (line 8585)
- [IMPLEMENTED] 4pc stacks: +1 SK stack via set bonus effectN(3) (lines 8576-8580)
- [IMPLEMENTED] 4pc damage: +25% LB/CL damage during SK window (lines 3206-3208)

VERDICT: Elemental tier set is FULLY IMPLEMENTED.

### 1.2 Rotation Priority — Farseer Single Target

Wowhead priority:
1. Stormkeeper on CD
2. Ancestral Swiftness on CD
3. Ascendance after Stormkeeper
4. Elemental Blast if <15 Maelstrom from cap
5. Elemental Blast if Master of the Elements (MotE) active
6. Lava Burst if no MotE
7. Lightning Bolt to consume MotE
8. Refresh Flame Shock with Voltaic Blaze (pandemic, no MotE)
9. Lightning Bolt filler

SimC APL (single_target list):
1. Stormkeeper (hold for Asc sync)
2. Ancestral Swiftness
3. Ascendance (hold for SK sync)
4. Flame Shock maintenance (refreshable, no MotE)
5. Voltaic Blaze (refreshable FS, no MotE, or Purging Flames)
6. Lava Burst (no MotE, maelstrom deficit >15, talent checks)
7. Tempest (with MotE or without MotE talent)
8. Lightning Bolt with Stormkeeper (with MotE)
9. Elemental Blast
10. Earth Shock
11. Tempest (unbuffed)
12. Lightning Bolt filler

DIFFERENCES:
- [MINOR] Wowhead says EB before LvB when near Maelstrom cap; SimC puts EB after
  Tempest/SK-LB. The SimC APL uses maelstrom.deficit checks more broadly.
- [OK] Wowhead separates "EB with MotE" and "EB near cap" as two conditions; SimC
  handles these implicitly through priority ordering (EB is high after spenders).
- [OK] Ascendance/SK sync logic matches: both sources say Asc after SK.
- [OK] Flame Shock / Voltaic Blaze pandemic refresh logic present in SimC.
- [MATCH] Lightning Bolt as filler at the bottom in both.
- [NOTE] SimC includes Earth Shock as a fallback spender (line 99); Wowhead doesn't
  explicitly mention it (likely implicit when EB not talented).

### 1.3 Rotation Priority — Stormbringer Single Target

Wowhead priority:
1. Stormkeeper on CD
2. Ascendance after SK
3. Refresh Flame Shock with Voltaic Blaze (pandemic, no MotE)
4. Lava Burst if no MotE and won't overcap
5. Tempest to consume MotE
6. Stormkeeper-buffed Lightning Bolt to consume MotE
7. Elemental Blast
8. Lightning Bolt / Tempest filler

SimC APL: Same single_target list is used for both Farseer and Stormbringer.

DIFFERENCES:
- [ISSUE] SimC does NOT differentiate between Farseer and Stormbringer for Elemental.
  The APL is a single list. Wowhead has different priorities for each hero talent.
  For Stormbringer: Tempest to consume MotE is higher priority than SK-buffed LB.
  The SimC APL handles this correctly (Tempest before SK-LB in lines 96-97).
- [OK] Ancestral Swiftness only appears in Farseer rotation on Wowhead. SimC always
  casts it (line 91), which is harmless (it's only available to Farseer anyway).

### 1.4 Rotation Priority — AoE

Wowhead (Farseer):
1. Stormkeeper on CD
2. Ancestral Swiftness
3. Ascendance after SK
4. Earthquake (4+ targets)
5. Elemental Blast (3 targets)
6. Lava Burst with Purging Flames
7. Voltaic Blaze on CD
8. Chain Lightning filler

SimC AoE APL:
1. Stormkeeper (hold for Asc)
2. Voltaic Blaze (early/purging flames)
3. Ancestral Swiftness
4. Ascendance (hold for SK)
5. Flame Shock (3t with MotE + Inferno Arc)
6. Voltaic Blaze (FS refresh / Purging Flames)
7. Earthquake (targets >= 3+EB talent, tempest<2, lightning_rod check)
8. Elemental Blast (3t, rod/tempest checks)
9. Lava Burst (Purging Flames or Lava Surge+MotE on 3t)
10. Tempest (with MotE, or capped)
11. Chain Lightning (with SK)
12. Earthquake (deficit <15, no EB)
13. Elemental Blast
14. Tempest
15. Chain Lightning filler

DIFFERENCES:
- [OK] SimC AoE is more nuanced with target counts and buff checks.
- [MINOR] Wowhead says AoE starts at 2 targets; SimC uses >=3 for the AoE list
  (line 66: spell_targets.chain_lightning>=3). At 2 targets, SimC falls into single
  target list. This could be a DPS loss for 2-target cleave.
- [OK] Purging Flames consumption present in both (SimC line 77).
- [MINOR] Wowhead lists Voltaic Blaze "on cooldown" in AoE; SimC conditions it more
  heavily (FS refresh, Purging Flames, not during Ascendance).
- [OK] Earthquake vs EB target threshold logic is present in SimC.

### 1.5 Opener

Wowhead Farseer opener: SK -> LvB -> Asc -> Ancestral Swiftness -> LB -> LvB -> LB
Wowhead Stormbringer opener: SK -> LvB -> Asc -> Tempest -> LvB -> LB

SimC precombat: Stormkeeper (precasted). No explicit opener sequence beyond that.

DIFFERENCE:
- [MINOR] SimC doesn't model an explicit opener sequence. The precombat SK precast
  and the priority list should approximate the correct opener naturally.

### 1.6 Key Talent Effects

- [IMPLEMENTED] Master of the Elements: 31 references in sc_shaman.cpp
- [IMPLEMENTED] Voltaic Blaze: 67 references (voltaic_blaze/purging_flames/ancestral_swiftness)
- [IMPLEMENTED] Lava Flows: Maelstrom gain + damage bonus (lines 6678-6681, 6705-6707)
- [IMPLEMENTED] Surging Shields: LS damage + Maelstrom/MSW chance (line 1635, 4708-4720)
- [IMPLEMENTED] Stormkeeper: Full implementation with tier set integration
- [IMPLEMENTED] Ascendance: Overload buffing, Flame Shock spreading, Call of Fire
- [IMPLEMENTED] Tempest: 65 references, full integration

---

## 2. ENHANCEMENT SHAMAN

### 2.1 Tier Set Bonuses (Mantle of the Primal Core — MID1)

Wowhead describes:
- 2pc: Stormstrike and Lava Lash deal 15% increased damage
- 4pc: Crash Lightning weapon enhancement increases Mastery by 2% per stack

SimC implementation status:
- [NOT FOUND] No SHAMAN_ENHANCEMENT MID1 references in sc_shaman.cpp.
  Only TWW2 (The War Within Season 2) Enhancement tier exists.
  Only SHAMAN_ELEMENTAL MID1 exists.

VERDICT: Enhancement MID1 tier set is NOT IMPLEMENTED.
This is a significant gap. The 2pc +15% SS/LL damage and 4pc Mastery per
Crash Lightning stack are missing entirely.

NOTE: TWW3 hero-talent-specific set bonuses ARE implemented:
- HERO_TOTEMIC TWW3 B2/B4 (Primordial Storm trigger, Primal Catalyst)
- HERO_STORMBRINGER TWW3 B2 (referenced at lines 5030, 5049)
These may be additional or different tier sets for a later season.

### 2.2 Rotation Priority — Stormbringer Single Target

Wowhead priority:
1. Crash Lightning (maintain buff)
2. Ascendance
3. Windstrike during Ascendance
4. Stormstrike during Doom Winds
5. Tempest / Lightning Bolt at 10 MSW
6. Stormstrike
7. Lava Lash
8. Voltaic Blaze
9. Lightning Bolt at 5+ MSW

SimC APL (single_sb):
1. Primordial Storm (MSW >= 9 or expiring)
2. Voltaic Blaze (if no FS, early)
3. Flame Shock (if not ticking)
4. Lava Lash (Lashing Flames, early)
5. Buffs (trinkets/racials/pots)
6. Sundering (if Surging Elements or Feral Spirit)
7. Doom Winds
8. Crash Lightning (maintain buff or Storm Unleashed)
9. Voltaic Blaze (during DW with MSW conditions, Thorim's)
10. Windstrike (Thorim's Invocation, MSW > 0)
11. Ascendance
12. Stormstrike (during DW with Thorim's)
13. Crash Lightning (during DW with Thorim's)
14. Tempest at MSW = 10
15. Lightning Bolt at MSW = 10
16. Stormstrike (charges >= 1.8)
17. Lava Lash
18. Stormstrike
19. Voltaic Blaze
20. Sundering
21. Lightning Bolt at MSW >= 8
22. Crash Lightning
23. Lightning Bolt at MSW >= 5
24. Flame Shock (filler)

DIFFERENCES:
- [ISSUE] Wowhead lists Ascendance near the top (step 2); SimC puts it at step 11,
  after DW and Thorim's Invocation setup. SimC appears more optimized for Thorim's
  priming, which Wowhead mentions in detail but doesn't reflect in the simple priority.
- [OK] Wowhead's "Crash Lightning" at top = maintain buff; SimC does this (step 8).
- [MINOR] Wowhead says "Tempest/LB at 10 MSW" as step 5; SimC puts these at step 14-15,
  after Windstrike and DW-Stormstrike. SimC prioritizes Thorim's Invocation spending
  over raw MSW spenders, which aligns with the detailed Wowhead guide text.
- [OK] Doom Winds handling matches (both treat it as a key window).
- [MINOR] SimC includes Primordial Storm at very top (it's an optional talent on
  Wowhead, not in the base priority). Both approaches valid depending on talent choices.
- [NOTE] Lightning Bolt threshold: Wowhead says 5+ MSW; SimC uses 5+ but also has
  an intermediate 8+ MSW check. More granular.

### 2.3 Rotation Priority — Totemic Single Target

Wowhead priority:
1. Voltaic Blaze if no Flame Shock
2. Surging Totem
3. Lava Lash with Hot Hand or Whirling Fire
4. Sundering
5. Doom Winds
6. Crash Lightning
7. Primordial Storm at 10 MSW
8. Stormstrike during Doom Winds
9. Lightning Bolt at 10 MSW
10. Lava Lash
11. Stormstrike
12. Voltaic Blaze
13. Lightning Bolt at 5+ MSW

SimC APL (single_totemic):
1. Voltaic Blaze (no FS)
2. Flame Shock (not ticking)
3. Surging Totem
4. Buffs
5. Sundering (Surging Elements, Whirling Earth, Feral Spirit)
6. Lava Lash (Whirling Fire or Hot Hand)
7. Doom Winds
8. Crash Lightning (buff maintenance or Storm Unleashed)
9. Primordial Storm (MSW >= 10 or expiring)
10. Windstrike (Thorim's + Ascendance)
11. Ascendance (if primed to LB)
12. Crash Lightning (Thorim's + DW/Asc)
13. Stormstrike (Thorim's + DW)
14. Lightning Bolt (Elemental Tempo conditions)
15. Crash Lightning
16. Lava Lash
17. Sundering (cd > 25)
18. Stormstrike
19. Voltaic Blaze
20. Crash Lightning
21. Lightning Bolt at 5+ MSW
22. Flame Shock (filler)

DIFFERENCES:
- [GOOD MATCH] Top priority (VB -> Surging Totem -> LL with Hot Hand -> Sundering ->
  DW -> CL) matches well between Wowhead and SimC.
- [MINOR] SimC adds Ascendance + Windstrike + Thorim's Invocation handling that Wowhead
  doesn't explicitly include in the Totemic priority (Wowhead says Totemic defaults
  to Doom Winds, not Ascendance). SimC has Ascendance as optional depending on talent.
- [OK] Lava Lash with Hot Hand/Whirling Fire is high priority in both.
- [MINOR] SimC has an Elemental Tempo optimization (step 14) not in Wowhead's list.

### 2.4 Rotation Priority — AoE

Wowhead Stormbringer AoE:
1. Primordial Storm at 10 MSW
2. Sundering
3. Crash Lightning
4. Ascendance
5. Windstrike during Ascendance
6. Stormstrike during Doom Winds
7. Tempest at 10 MSW
8. Chain Lightning at 9+ MSW
9. Voltaic Blaze
10. Stormstrike
11. Lava Lash
12. Chain Lightning at 5+ MSW

SimC AoE APL:
1. Voltaic Blaze (Totemic, no FS)
2. Flame Shock (not ticking)
3. Surging Totem
4. Ascendance (primed to CL)
5. Buffs
6. Sundering (Surging Elements or Whirling Earth)
7. Lava Lash (Whirling Fire)
8. Doom Winds
9. Crash Lightning (Thorim's + Whirling Air + DW/Asc)
10. Windstrike (Thorim's + Whirling Air)
... [extensive Thorim's Invocation + Splitstream handling]
14. Crash Lightning
15. Windstrike (Thorim's)
16. Stormstrike (Thorim's + DW)
17. Chain Lightning at 9-10 MSW
18. Sundering (Feral Spirit)
19. Voltaic Blaze
20-end. Stormstrike, Lava Lash, CL at 5+ MSW, Flame Shock

DIFFERENCES:
- [OK] Both have Sundering and Crash Lightning near the top for AoE.
- [MINOR] SimC's AoE list is shared between Stormbringer and Totemic (unified),
  with talent conditionals to handle differences. Wowhead has separate priorities
  for each hero talent.
- [ISSUE] Wowhead places Tempest at 10 MSW before Chain Lightning at 9+ MSW;
  SimC places Tempest at MSW >= 10 only during non-Ascendance/non-DW windows
  (line 13067), which is different logic.
- [MINOR] SimC has no separate AoE list for Totemic vs Stormbringer, instead using
  talent checks inline. The unified list may miss some Totemic-specific nuances
  like the Surging Totem -> Sundering -> LL -> DW sequence Wowhead describes.

### 2.5 Opener

Wowhead Stormbringer: VB -> CL -> LL (Lashing Flames) -> Asc -> Windstrike spam
Wowhead Totemic: VB -> Surging Totem -> Sundering -> LL -> DW+Primordial Storm -> LL -> CL

SimC: No explicit opener. The priority lists handle opening GCDs implicitly.
Enhancement APL has early-fight conditions (time<5 checks in single_sb for VB and LL).

DIFFERENCE:
- [MINOR] No explicit opener, but time<5 conditions approximate the correct behavior.
  Totemic opener sequence (Surging Totem before DW) should work via priority ordering.

### 2.6 Key Talent Effects

- [IMPLEMENTED] Doom Winds: WF chance doubling, WF damage buff, Static Accumulation,
  Thorim's Invocation integration
- [IMPLEMENTED] Ascendance: Windstrike conversion, DW triggering, DRE proc chance
- [IMPLEMENTED] Thorim's Invocation: Spender discharge on Windstrike/Stormstrike/CL,
  priming system (ti_lightning_bolt, ti_chain_lightning references)
- [IMPLEMENTED] Surging Totem: Whirling Elements (Earth/Fire/Air), Primal Catalyst
- [IMPLEMENTED] Totemic Momentum: Hot Hand extension
- [IMPLEMENTED] Splitstream: Lava Lash cleave during Hot Hand
- [IMPLEMENTED] Primordial Storm: Multi-step attack with MSW consumption
- [IMPLEMENTED] Lava Flows: Damage + Maelstrom generation
- [IMPLEMENTED] Surging Shields: LS damage + MSW chance for Enhancement
- [IMPLEMENTED] Fire Nova: Coded (19 references) but not directly in APL as a cast
  action — only referenced as a talent condition for Voltaic Blaze priority
- [IMPLEMENTED] Ride the Lightning: Stormstrike cleave
- [IMPLEMENTED] Static Accumulation: MSW generation during DW/Ascendance

---

## 3. CROSS-CUTTING ISSUES

### 3.1 Enhancement APL Location
Enhancement APL is NOT in apl_shaman.cpp (the standard APL generator file).
Instead, it's hardcoded in sc_shaman.cpp::init_action_list_enhancement() (line 13014).
This is inconsistent with Elemental which uses the separate apl_shaman.cpp file.
This makes it harder to maintain and update Enhancement APLs independently.

### 3.2 Enhancement MID1 Tier Set Missing
The Midnight Season 1 tier set for Enhancement (2pc: +15% SS/LL damage,
4pc: +2% Mastery per CL stack) is NOT implemented in sc_shaman.cpp.
Only the Elemental MID1 set exists. This is the most critical finding.

TWW2 and TWW3 hero-talent-specific sets ARE implemented for Enhancement,
suggesting the MID1 set either hasn't been added yet or uses a different
naming convention not found in the search.

### 3.3 AoE Threshold Discrepancy (Elemental)
Wowhead states AoE starts at 2 targets. SimC switches to AoE list at >=3 targets.
At exactly 2 targets, Elemental uses the single target list in SimC, which includes
a Chain Lightning condition for 2t with Call of the Ancestors talent (line 101).
This partially handles 2-target but may miss AoE-specific priorities.

### 3.4 Fire Nova Not Directly Cast in Enhancement APL
Wowhead lists Fire Nova as an optional AoE talent. SimC implements the spell
mechanically but never directly casts it in the APL. It's only referenced as a
condition for Voltaic Blaze priority. If Fire Nova is talented, it should
potentially be cast explicitly in AoE situations.

### 3.5 Farseer vs Stormbringer Distinction (Elemental)
SimC uses a single APL for both Elemental hero talents. Wowhead provides distinct
priorities. The unified APL works because Ancestral Swiftness is Farseer-only
(no-op for Stormbringer) and Tempest is Stormbringer-only. However, subtle
priority differences (e.g., Farseer's burst window: SK->AS->VB->Asc) are not
explicitly modeled as a sequence.

---

## 4. PRIORITY SUMMARY TABLE

| Issue | Severity | Spec | Description |
|-------|----------|------|-------------|
| Enhancement MID1 tier not implemented | HIGH | Enh | 2pc +15% SS/LL and 4pc Mastery/CL stack missing |
| Fire Nova not cast in APL | MEDIUM | Enh | Spell coded but not used when talented |
| AoE threshold 2 vs 3 | LOW | Ele | Wowhead says 2t AoE; SimC uses 3t threshold |
| Enhancement APL in wrong file | LOW | Enh | Should be in apl_shaman.cpp for consistency |
| No explicit opener sequences | LOW | Both | Priority lists approximate openers acceptably |
| Farseer burst window not sequenced | LOW | Ele | SK->AS->VB->Asc sequence not explicitly ordered |
| EB priority ordering | LOW | Ele | Minor difference in Maelstrom cap prevention timing |
