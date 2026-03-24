# Demon Hunter Spec Audit: Wowhead vs SimC APL/Code
# Generated: 2026-03-24

==============================================================================
## 1. HAVOC DEMON HUNTER
==============================================================================

### Tier Set Bonuses (Midnight S1: "Devouring Reaver's Sheathe")
  Wowhead:
    2pc: Blade Dance damage increased by 15%
    4pc: Haste increased by additional 6% during Metamorphosis
  Wowhead notes: "No rotation changes"

  SimC Code:
    MISSING_MECHANIC: No DEMON_HUNTER_HAVOC MID1 set bonus references found in
    sc_demon_hunter.cpp at all. Zero hits for has_set_bonus(DEMON_HUNTER_HAVOC,
    MID1, B2) or B4. The Havoc 2pc and 4pc tier bonuses appear to be
    COMPLETELY UNIMPLEMENTED in the class module.
    - The 2pc (15% Blade Dance/Death Sweep damage) is not applied.
    - The 4pc (6% haste during Metamorphosis) is not applied.
    Since these are passive damage increases, this likely means SimC
    undervalues Havoc with 4pc equipped.

### Fel-Scarred ST Priority (Wowhead rotation.md lines 29-42)
  Wowhead Priority:
    1. If Inertia buff up, Cast Felblade or Fel Rush to proc
    2. Cast The Hunt
    3. Cast Death Sweep
    4. Cast Immolation Aura if capped on charges
    5. Cast Vengeful Retreat if Eye Beam is off cooldown
    6. Cast Eye Beam
    7. Cast Metamorphosis
    8. Cast Blade Dance
    9. Cast Annihilation
   10. Cast Chaos Strike
   11. Cast Immolation Aura
   12. Cast Felblade
   13. Cast Throw Glaive or Fel Rush (filler)

  APL (havoc, lines 160-264):
    - Step 1 (Inertia proc): Lines 213-214 handle Felblade/Fel Rush with
      inertia_ready checks. PRESENT but buried after cooldown calls. The APL
      puts Inertia consumption after the cooldown list call rather than at top.
      CONDITION_ISSUES: APL gates on inertia_consumer_soon which is more
      restrictive than Wowhead's simple "if Inertia buff is up".
    - Step 2 (The Hunt): Line 245 in cooldown list. PRESENT. Has extensive
      conditions about essence_break alignment, reavers_glaive, initiative.
      CONDITION_ISSUES: Wowhead says "on cooldown", APL has many gates.
    - Step 3 (Death Sweep): Line 247 in meta list. PRESENT.
    - Step 4 (Immolation Aura capped): Line 211 handles A Fire Inside charge
      capping. PRESENT.
    - Step 5 (Vengeful Retreat before Eye Beam): Line 215. PRESENT.
    - Step 6 (Eye Beam): Line 220 (outside meta), line 254 (in meta). PRESENT.
    - Step 7 (Metamorphosis): Line 235. PRESENT.
    - Step 8 (Blade Dance): Line 221. PRESENT.
    - Step 9 (Annihilation): Line 258 in meta list. PRESENT.
    - Step 10 (Chaos Strike): Line 228. PRESENT.
    - Step 11 (Immolation Aura): Lines 224-225, 229. PRESENT.
    - Step 12 (Felblade): Lines 223, 230, 259, 261. PRESENT.
    - Step 13 (Throw Glaive / Fel Rush filler): Lines 226-227, 231-232.
      PRESENT.

  WRONG_ORDER:
    - WH#1 Inertia proc is listed BEFORE The Hunt and all CDs, but in APL
      it comes AFTER cooldown sub-list call (line 208 calls cooldowns, then
      213-214 handle inertia). In practice this means APL may cast The Hunt
      before consuming an Inertia trigger, which contradicts Wowhead priority.
    - WH#5 Vengeful Retreat before Eye Beam: In APL (line 215), VR is
      positioned AFTER IA charge-cap and Immolation Aura entries (209-212).
      Wowhead places it directly before Eye Beam (#5 -> #6), APL inserts
      several IA conditions between them.

  MISSING:
    - "Consuming Fire" (mentioned in opener line 140): This is the Demonsurge
      version of Immolation Aura. The APL handles it via the demonsurge_available
      condition on immolation_aura (line 212, 252). PRESENT but implicit.
    - "Abyssal Gaze" (opener line 143): This is the Demonsurge Eye Beam. The
      APL references action.abyssal_gaze.demonsurge_available (line 212).
      PRESENT but implicit.

  CONDITION_ISSUES:
    - Essence Break: Wowhead rotation does NOT list Essence Break at all in
      the Fel-Scarred priority (lines 29-42). However, the APL has a full
      essence_break action in meta list (line 249) and checks essence_break
      debuff extensively. This suggests Essence Break may be talented in some
      APL builds but Wowhead's Fel-Scarred rotation explicitly omits it.
      The APL should gate essence_break on talent.essence_break (which it
      does implicitly since it's a talent-gated spell).

### Aldrachi Reaver ST Priority (Wowhead lines 326-337)
  Wowhead Priority:
    1. Cast The Hunt
    2. Cast Death Sweep
    3. Cast Vengeful Retreat
    4. Cast Eye Beam
    5. Cast Metamorphosis
    6. Cast Blade Dance
    7. Cast Reaver's Glaive
    8. Cast Annihilation
    9. Cast Chaos Strike
   10. Cast Immolation Aura
   11. Cast Felblade
   12. Cast Fel Rush (filler)
   Note: "Throw Glaive is NOT cast due to Screaming Brutality"

  APL Analysis:
    - Reaver's Glaive: Lines 204-205. PRESENT. Has complex targeting logic.
    - Steps 1-12 all mapped as in Fel-Scarred analysis above.

  WRONG_ORDER:
    - WH: Vengeful Retreat (#3) is before Eye Beam (#4). In APL, Vengeful
      Retreat (line 215-216) comes AFTER Eye Beam (line 220). This is a
      significant ordering difference for Aldrachi Reaver, where WH says
      VR is higher priority than Eye Beam unconditionally.

  CONDITION_ISSUES:
    - WH says "Throw Glaive is NOT cast due to Screaming Brutality". However
      APL line 226 casts throw_glaive with soulscar talent check but does NOT
      exclude it when screaming_brutality is talented. Line 232 also uses TG
      as filler without checking screaming_brutality.

  MISSING:
    - WH AoE note (line 375): "if Rending Strike and Glaive Flurry are up,
      you MUST use Chaos Strike to spend Rending Strike before Blade Dance".
      APL lines 199-203 handle this CS->BD ordering with rending_strike/
      glaive_flurry buff checks. PRESENT.

### Havoc Summary of Issues:
  MISSING_MECHANIC:
    [H-M1] Havoc 2pc tier (Blade Dance +15% dmg) NOT IMPLEMENTED in code
    [H-M2] Havoc 4pc tier (6% haste in Meta) NOT IMPLEMENTED in code

  WRONG_ORDER:
    [H-O1] Inertia consumption positioned after cooldowns in APL vs before
            everything in Wowhead
    [H-O2] Vengeful Retreat vs Eye Beam ordering differs for Aldrachi Reaver

  CONDITION_ISSUES:
    [H-C1] Throw Glaive not excluded when Screaming Brutality is talented
    [H-C2] Inertia consumption has more restrictive gates than Wowhead

==============================================================================
## 2. VENGEANCE DEMON HUNTER
==============================================================================

### Tier Set Bonuses (Midnight S1: "Devouring Reaver's Sheathe")
  Wowhead:
    2pc: Fracture damage increased by 35%
    4pc: Fracture has 30% chance for 180% AP Fire AoE (500ms ICD, reduced >5)
  Wowhead notes: "No rotation changes"

  SimC Code:
    - 4pc: IMPLEMENTED at lines 7886, 7946-7951. 30% proc chance, ICD,
      explosion_of_the_soul action (line 6670-6677). Correct.
    - 2pc: The 35% Fracture damage increase is likely handled via spell data
      passively (set bonus aura). SimC typically applies 2pc auras
      automatically. Appears correct.

### Annihilator ST Priority (Wowhead rotation.md lines 33-47)
  Wowhead Priority:
    1. Infernal Strike off-GCD if at/near 2 charges
    2. Metamorphosis if won't overcap duration & Spirit Bomb >10s CD
    3. Fracture if at/near 2 charges
    4. Spirit Bomb with 4+ Souls if Fiery Brand about to expire
    5. Fiery Brand if debuff not active
    6. Spirit Bomb with 6 Souls
    7. Immolation Aura
    8. Sigil of Flame
    9. Sigil of Spite if won't overcap Souls
   10. Soul Cleave with 1+ Souls
   11. Fel Devastation if 50+ Fury
   12. Soul Cleave at 0 Souls (fury dump)
   13. Fracture if won't cap Fury/Souls
   14. Felblade if won't cap Fury
   15. Throw Glaive (filler)

  APL (vengeance, lines 275-428):
    Main flow: default -> anni -> anni_voidfall -> anni_meta_entry ->
    anni_meta -> anni_cooldowns -> anni_fillers

    - Step 1 (Infernal Strike): Line 314. PRESENT.
    - Step 2 (Metamorphosis): Lines 370, 372-373. PRESENT.
      CONDITION_ISSUES: WH says "Spirit Bomb >10s remaining on CD". APL
      line 363 checks cooldown.spirit_bomb.remains<(2*gcd.max)|remains>20.
      Different threshold -- APL uses a burst_ready variable approach rather
      than simple >10s check.
    - Step 3 (Fracture near cap): Line 418 (anni_fillers), line 406
      (anni_meta). Also variable.fracture_cap_soon at line 311.
    - Step 4 (Spirit Bomb 4+ souls w/ Fiery Brand expiring): Not directly
      present. APL line 355 (ar_cooldowns) has spirit_bomb with fiery_demise
      and 3+ frags, but that's the AR path. In anni path, spirit_bomb is
      checked at lines 384, 390, 395, 405, 417 but none specifically gate
      on "Fiery Brand about to expire + 4 souls".
      MISSING: Fiery Brand expiration-triggered Spirit Bomb at reduced soul
      count is not in Annihilator APL path.
    - Step 5 (Fiery Brand): Lines 379, 401, 411. PRESENT with various
      conditions.
    - Step 6 (Spirit Bomb 6 Souls): Line 405 (anni_meta), 417 (anni_fillers)
      use variable.fragment_target (3-5 depending on Brand/Meta). PRESENT
      but threshold differs -- Wowhead says always 6 souls, APL uses 3-5.
      CONDITION_ISSUES: Fragment target is dynamic (3 in Brand, 4 in Meta,
      5 baseline) vs Wowhead's flat 6.
    - Step 7 (Immolation Aura): Lines 383, 402, 419, 423. PRESENT.
    - Step 8 (Sigil of Flame): Lines 421, 424. PRESENT.
    - Step 9 (Sigil of Spite): Lines 382, 404, 408, 413. PRESENT.
    - Step 10 (Soul Cleave 1+ Souls): Line 386 (voidfall), 399 (ur_fishing),
      425 (fillers). PRESENT.
    - Step 11 (Fel Devastation 50+ Fury): Lines 380, 407, 415. PRESENT.
      No explicit 50 fury check in APL -- relies on resource cost.
    - Step 12 (Soul Cleave fury dump): Line 425. PRESENT (fallback).
    - Step 13 (Fracture): Lines 386, 392, 398, 406, 418, 420, 426. PRESENT.
    - Step 14 (Felblade): Line 422. PRESENT.
    - Step 15 (Throw Glaive): Line 427. PRESENT.

  WRONG_ORDER:
    [V-O1] WH places Soul Cleave with 1+ Souls (#10) ABOVE Fel Devastation
           (#11). APL generally places Fel Devastation higher (in cooldowns
           and voidfall lists) than Soul Cleave. This is a minor priority
           inversion.
    [V-O2] WH places Sigil of Spite (#9) after Sigil of Flame (#8). In APL
           anni_cooldowns, Sigil of Spite comes before Immolation Aura and
           Sigil of Flame. The priority of SoS is elevated in the APL.

  MISSING:
    [V-M1] WH notes "Use Metamorphosis if Spirit Bomb >10s on CD". The APL
           uses a different burst coordination model (anni_meta_entry with
           Brand -> SpB -> Meta off-GCD). The simple "SB >10s" guard is
           absent.

### Aldrachi Reaver ST Priority (Wowhead lines 218-235)
  Additional AR-specific abilities:
    - Fracture with Rending Strike (#4 per WH): APL line 349-351 in
      ar_glaive_cycle. PRESENT.
    - Soul Cleave with Glaive Flurry (#8 per WH): APL line 350, 353.
      PRESENT.
    - Reaver's Glaive (#10 per WH): APL line 348. PRESENT.
    - Sigil of Spite to activate Art of the Glaive (#9): APL line 357.
      PRESENT but inside ar_cooldowns, not specifically gated on "no
      Reaver's Glaive available".

  CONDITION_ISSUES:
    [V-C1] WH says "Sigil of Spite to activate Art of the Glaive if you
           don't have a Reaver's Glaive". APL line 357 checks
           soul_fragments<=2+talent.soul_sigils but doesn't check for
           Reaver's Glaive availability.

### Vengeance Summary:
  MISSING_MECHANIC:
    (none -- tier is implemented)

  MISSING:
    [V-M1] Spirit Bomb at 4+ souls when Fiery Brand expiring (Annihilator)

  WRONG_ORDER:
    [V-O1] Soul Cleave vs Fel Devastation priority inversion
    [V-O2] Sigil of Spite elevated above Sigil of Flame in APL

  CONDITION_ISSUES:
    [V-C1] Meta entry uses burst_ready model vs WH's simple "SB >10s" check
    [V-C2] Spirit Bomb fragment threshold (3-5 dynamic) vs WH's flat 6
    [V-C3] Sigil of Spite Art of the Glaive check missing reaver's_glaive gate

==============================================================================
## 3. DEVOURER DEMON HUNTER (NEW SPEC)
==============================================================================

### Tier Set Bonuses (Midnight S1: "Devouring Reaver's Sheathe")
  Wowhead:
    2pc: Void Ray damage increased by 10%
    4pc: Collapsing Star damage +10% and generates 10 Fury

  SimC Code:
    - 4pc (Stars' Fury / fury gen): IMPLEMENTED at lines 6405-6408, 11085-
      11086. Collapsing Star energize action present.
    - 2pc (Void Ray +10%): Likely handled via spell data aura passively.
      No explicit code reference found but this is standard SimC behavior
      for simple damage% buffs from set bonuses.

### Void-Scarred ST Priority (Wowhead rotation.md lines 25-35)
  OUTSIDE VOID METAMORPHOSIS:
    1. Cast Voidblade if about to enter Void Metamorphosis
    2. Cast Reap on cooldown
    3. Cast Void Ray
    4. Cast Void Metamorphosis
    5. Cast Consume

  INSIDE VOID METAMORPHOSIS:
    1. Cast Cull on cooldown
    2. Cast Pierce the Veil
    3. Cast Void Ray
    4. Cast Devour

  APL (devourer, lines 76-149):
    OUTSIDE META:
    - Step 1 (Voidblade before meta): Line 109 checks
      void_metamorphosis_stack.at_max_stacks & devourers_bite & voidsurge.
      PRESENT but only for Devourer's Bite + Voidsurge builds. For non-melee
      ranged builds, Voidblade is absent from the non-meta section.
      CONDITION_ISSUES: WH says "if about to enter Void Metamorphosis". APL
      gates on at_max_stacks which is functionally similar but adds talent
      gates.
    - Step 2 (Reap on cooldown): Line 114 handles reap outside meta with
      charge cap prevention. Line 122 handles reap with moment_of_craving.
      PRESENT but with additional conditions (charge cap, not voidfall).
      CONDITION_ISSUES: WH says "on cooldown", APL gates on charge cap
      or moment_of_craving specifically.
    - Step 3 (Void Ray): Lines 107, 113. PRESENT.
    - Step 4 (Void Metamorphosis): Line 111. PRESENT.
    - Step 5 (Consume): Line 124. PRESENT.

    INSIDE META:
    - Step 1 (Cull on CD): Inside reaps list (lines 146-148: eradicate ->
      cull -> reap). Cull is present.
      WRONG_ORDER: WH says Cull is #1 inside meta. APL dispatches reaps via
      call_action_list with various conditions (lines 112, 117, 118, 122).
      Cull is not at top of the default list -- it's gated behind void_ray
      and collapsing_star calls.
    - Step 2 (Pierce the Veil): Line 108 and melee_combo line 142. PRESENT.
    - Step 3 (Void Ray): Lines 107, 113. PRESENT.
    - Step 4 (Devour): Line 123. PRESENT.

  MISSING:
    [D-M1] Collapsing Star is NOT in the Void-Scarred ST priority list
           per Wowhead ("Void-Scarred doesn't make use of Collapsing Star
           in Single Target" -- user comments confirm). APL line 116 and
           121 both include collapsing_star with should_use_star variable.
           The variable (line 136) gates on active_enemies>1 OR apex.1 OR
           dark_matter OR star_fragments&emptiness. This means in ST with
           certain talents, APL DOES cast Collapsing Star, which aligns
           with the "caster build" variant but differs from WH's base
           Void-Scarred ST priority.

### Void-Scarred AoE Priority (Wowhead lines 150-167)
  OUTSIDE META AoE additions:
    - Hungering Slash: Line 139 (melee_combo). PRESENT (AoE only gate).
    - Vengeful Retreat with Voidstep: Line 138 (melee_combo). PRESENT.
    - Eradicate: Line 146 (reaps). PRESENT.
    - Voidblade: Line 144 (melee_combo). PRESENT.

  INSIDE META AoE:
    - Eradicate: Wowhead #1. APL reaps list has eradicate first (line 146).
      PRESENT.
    - Collapsing Star: Wowhead #3. APL lines 116, 121. PRESENT.
    - Reaper's Toll: Wowhead #4. APL melee_combo line 140. PRESENT.
    - Pierce the Veil: Wowhead #6. APL melee_combo line 142. PRESENT.
    - Cull with 4+ fragments: Wowhead #7. In reaps sub-list, cull fires
      unconditionally (line 147). No 4+ fragment gate.
      CONDITION_ISSUES: WH says "Cull with 4+ Soul Fragments" in AoE meta.
      APL has no soul fragment check on Cull.

### Annihilator ST Priority (Wowhead lines 1160-1169)
  OUTSIDE META:
    1. Cast Void Ray
    2. Cast Reap when it will proc Voidfall
    3. Cast Void Metamorphosis
    4. Cast Consume

  INSIDE META:
    1. Cast Void Ray
    2. Cast Collapsing Star
    3. Cast Cull if it will proc Voidfall
    4. Cast Devour

  APL Analysis:
    - Void Ray: Lines 107, 113. PRESENT.
    - Reap for Voidfall: Line 118 handles voidfall_spending reap. PRESENT.
    - Void Metamorphosis: Line 111. PRESENT.
    - Consume: Line 124. PRESENT.
    - Collapsing Star: Lines 116, 121. PRESENT.
    - Cull for Voidfall: Line 118 (reaps with voidfall_spending). PRESENT.
    - Devour: Line 123. PRESENT.

  CONDITION_ISSUES:
    [D-C1] WH Annihilator says "Reap when it will proc Voidfall". APL line
           118 checks buff.voidfall_spending.react, which is the spending
           phase. This seems correct as spending = the meteors are happening.
    [D-C2] WH says Collapsing Star should aim for 5 per Meta (Annihilator),
           4 per Meta (Void-Scarred). No APL condition tracks casts-per-meta.

### Smuggling Mechanic (Wowhead detailed description)
  MISSING_MECHANIC:
    [D-M2] "Soul Smuggling" -- leaving Soul Fragments on ground before
           entering/leaving Void Metamorphosis. SimC's fragment system may
           handle this via pick_up_fragment mechanics, but the APL has no
           explicit "don't pick up fragments before meta" logic. Line 197
           has pick_up_fragment at fury<=40, which is a basic collection.
           The sophisticated smuggling optimization is NOT modeled.
    [D-M3] "Hungering Slash Smuggling" -- carrying Hungering Slash proc
           into Void Metamorphosis for Reaper's Toll upgrade. The APL
           melee_combo fires hungering_slash immediately in AoE (line 139).
           No smuggling delay logic present.
    [D-M4] "Eradicate/Moment of Craving Smuggling" -- carrying these buffs
           into Void Meta. Line 107 does attempt eradicate smuggling:
           "void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up"
           is cast before meta to smuggle eradicate in. This is partially
           implemented. Line 108 checks moment_of_craving for pierce_the_veil
           timing. Partial implementation.

### Devourer's Bite Optimization (Wowhead lines 977-982)
  Wowhead: "Hold Voidblade and The Hunt until right before Void Meta entry
            for maximum 12% damage per stack debuff window."
  APL: Lines 109-110 gate Voidblade/The Hunt on void_metamorphosis_stack.
       at_max_stacks, which triggers near meta entry. PRESENT.
  CONDITION_ISSUES:
    [D-C3] The APL only uses Devourer's Bite optimization for builds with
           both devourers_bite AND voidsurge. WH says it applies to both
           Void-Scarred and Annihilator melee builds.

### Devourer Summary:
  MISSING:
    [D-M1] Predators Wake (The Hunt upgrade) not directly in default APL
           priority -- only in melee_combo sub-list (line 143). Present.
    [D-M5] Soul Immolation: APL line 120 has soul_immolation only outside
           meta and AoE. Wowhead rotation doesn't mention Soul Immolation
           at all. This may be an APL-only addition. OTHER.

  MISSING_MECHANIC:
    [D-M2] Soul Smuggling mechanic not modeled in APL
    [D-M3] Hungering Slash smuggling not modeled
    [D-M4] Eradicate smuggling only partially modeled

  WRONG_ORDER:
    [D-O1] Inside Void Meta, WH Void-Scarred says Cull #1 > Pierce #2 >
           Void Ray #3 > Devour #4. APL default list puts Void Ray (113)
           before reaps/cull (112, 117) and melee_combo/pierce (119).
           Void Ray is effectively higher priority than Cull in the APL.
    [D-O2] WH Annihilator Inside Meta: Void Ray #1 > Collapsing Star #2.
           APL puts Void Ray at line 113 but Collapsing Star at lines 116/
           121 (before and after reaps). Effectively similar ordering.

  CONDITION_ISSUES:
    [D-C1] Reap Voidfall proc check uses buff.voidfall_spending (matches)
    [D-C2] No per-meta Collapsing Star count tracking
    [D-C3] Devourer's Bite only for voidsurge builds in APL
    [D-C4] Cull in AoE meta has no soul fragment count check (WH says 4+)

  OTHER:
    [D-X1] Soul Immolation present in APL but absent from Wowhead rotation
    [D-X2] APL uses complex should_use_star variable that may enable
           Collapsing Star in VS ST builds with certain talents (apex/
           dark_matter/emptiness+star_fragments), which partially contradicts
           the base WH VS ST rotation but aligns with "caster build" variant

==============================================================================
## CROSS-SPEC ISSUES
==============================================================================

  OTHER:
    [X-1] APL references "algethar_puzzle_box" trinket by name (havoc lines
          238-240) -- this is a Dragonflight trinket. May be outdated for
          Midnight season. Wowhead opener mentions it too, so this may be
          intentional placeholder.
    [X-2] Consumable data in APL appears correct:
          - Havoc: potion_of_recklessness, flask_of_the_shattered_sun,
            royal_roast, thalassian_phoenix_oil -- matches Wowhead.
          - Vengeance: lights_potential, flask_of_blood_knights -- different
            from Havoc as expected for tank.
          - Devourer: potion_of_recklessness, flask_of_the_magisters --
            makes sense for INT-based caster.

==============================================================================
## SEVERITY RANKING
==============================================================================

  CRITICAL (affects DPS accuracy):
    [H-M1] Havoc 2pc tier NOT IMPLEMENTED (Blade Dance +15% damage)
    [H-M2] Havoc 4pc tier NOT IMPLEMENTED (6% haste in Meta)

  HIGH (rotation correctness):
    [D-O1] Devourer Void-Scarred in-meta priority: Cull should be above
           Void Ray per Wowhead, APL has it reversed
    [D-M2] Soul Smuggling not modeled (significant DPS optimization)
    [H-O1] Havoc Inertia consumption positioned incorrectly

  MEDIUM (suboptimal but functional):
    [V-C2] Vengeance Spirit Bomb fragment threshold differs (3-5 vs 6)
    [V-M1] Spirit Bomb Brand-expiration trigger missing for Annihilator
    [H-C1] Throw Glaive not excluded with Screaming Brutality
    [D-C4] Cull AoE soul fragment check missing
    [D-C3] Devourer's Bite optimization limited to voidsurge builds

  LOW (minor optimization differences):
    [V-O1] Soul Cleave vs Fel Devastation ordering
    [V-O2] Sigil of Spite vs Sigil of Flame ordering
    [H-O2] Vengeful Retreat vs Eye Beam ordering for Aldrachi Reaver
    [D-M3] Hungering Slash smuggling not modeled
    [D-M4] Eradicate smuggling only partial
