# Paladin Audit Report — Protection & Retribution
Generated: 2026-03-24
Comparing: Wowhead extracted data vs SimC APL & class module code

---

## 1. RETRIBUTION PALADIN

### 1.1 Rotation Priority Comparison (Wowhead vs SimC APL)

**Wowhead Templar ST Priority:**
1. Avenging Wrath
2. Execution Sentence
3. Hammer of Light (after Wake of Ashes)
4. Hammer of Light (free proc with conditions)
5. Final Verdict at 5 HP
6. Wake of Ashes
7. Divine Toll
8. Blade of Justice with Art of War proc
9. Final Verdict (any HP)
10. Blade of Justice
11. Hammer of Wrath
12. Judgment

**SimC APL (apl_paladin.cpp) structure:**
- cooldowns: potion, trinkets, execution_sentence, avenging_wrath
- generators: finishers at 5HP > wake_of_ashes > divine_toll > blade_of_justice(proc) > finishers > hammer_of_wrath > blade_of_justice > hammer_of_wrath > judgment > templar_strike > templar_slash > crusader_strike
- finishers: hammer_of_light > divine_storm(AoE) > templars_verdict

**Differences Found:**

| # | Issue | Severity |
|---|-------|----------|
| R1 | **Hammer of Light conditions oversimplified**: Wowhead specifies complex Hammer of Light usage — use after Wake of Ashes, hold free proc for AW window, use if AW ending soon, skip if Undisputed Ruling already up but AW not coming for 5s, use if proc expiring. SimC APL just does `hammer_of_light` unconditionally in finishers list. | MEDIUM |
| R2 | **Execution Sentence timing**: Wowhead says cast ES then fit damage into window. SimC correctly gates ES on `cooldown.wake_of_ashes.remains<gcd` to align with Wake. MATCHES well. | OK |
| R3 | **Radiant Glory build (Templar RG)**: Wowhead has a separate priority for Templar RG where AW is not manually cast (it auto-triggers from Wake of Ashes). SimC APL handles this via `talent.radiant_glory` conditions on AW/ES/trinkets, which is correct. | OK |
| R4 | **Herald of the Sun priority**: Wowhead lists a distinct HotS priority — no Hammer of Light, includes Templar Strike/Templar Slash at bottom, prioritizes HoW with Art of War proc above BoJ with AoW. SimC APL has templar_strike/templar_slash at bottom of generators. However, the APL does NOT have a separate Herald of the Sun path — it uses one unified APL. The APL handles this via talent checks (e.g., `walk_into_light`) but does NOT specifically prioritize HoW>BoJ when both have AoW procs in HotS builds. | LOW |
| R5 | **Walk into Light interaction**: Wowhead HotS build prioritizes Hammer of Wrath with Art of War proc before Blade of Justice with AoW. SimC has `hammer_of_wrath,if=talent.walk_into_light` as a separate line AFTER `blade_of_justice,if=(buff.art_of_war.up|buff.righteous_cause.up)`. This means with Walk into Light, HoW is used after proc'd BoJ, which may differ from Wowhead priority. | LOW |
| R6 | **Crusader Strike as filler**: SimC APL includes `crusader_strike` as bottom-of-list filler. Wowhead guides don't mention it (Templar builds use Templar Strike/Slash instead, HotS has Templar Strike/Slash at bottom). This is correct behavior — Crusader Strike is the fallback when Templar abilities aren't talented. | OK |
| R7 | **Finishers list references templars_verdict not final_verdict**: SimC uses `templars_verdict` action name. This is correct — Final Verdict replaces Templar's Verdict when talented, and SimC handles the rename internally. | OK |
| R8 | **AoE threshold**: Wowhead says AoE on 3+ targets. SimC uses `active_enemies>=(3-talent.tempest_of_the_lightbringer)` which means 2+ with TotL talented. This is a SimC optimization beyond Wowhead's guide. | OK (SimC more precise) |

### 1.2 Tier Set Bonuses (Retribution)

**Wowhead Midnight S1 Tier:**
- 2pc: Expurgation deals 20% increased damage
- 4pc: Final Verdict applies Expurgation at 100% effectiveness, Divine Storm at 50%

**SimC Implementation:**
- 4pc: IMPLEMENTED in sc_paladin_retribution.cpp
  - Divine Storm impact: `has_set_bonus(PALADIN_RETRIBUTION, MID1, B4)` → triggers expurgation at 50% (effectN(2))
  - Templar's Verdict/Final Verdict impact: triggers expurgation at 100% (effectN(1))
  - Empyrean Legacy interaction (TV procs DS) correctly handled with combined multiplier
  - Spell data stored: `spells.mid1_ret_4pc = sets->set(PALADIN_RETRIBUTION, MID1, B4)`
- 2pc: NOT explicitly found as a code check for `MID1, B2`. The 20% Expurgation damage increase is likely handled via automatic spell data parsing (the set bonus spell directly modifies Expurgation damage). This is the standard SimC pattern for simple damage% increases — they are parsed from DBC data automatically.

| # | Issue | Severity |
|---|-------|----------|
| T-R1 | 2pc bonus (20% Expurgation damage) — no explicit `MID1, B2` check found. If the DBC spell data has the damage modifier linked to Expurgation, it auto-applies. If not, this could be MISSING. Needs verification that the 2pc damage bonus is actually applying in simulation output. | NEEDS VERIFICATION |
| T-R2 | 4pc bonus fully implemented with correct effectiveness values. | OK |
| T-R3 | Wowhead says tier is "entirely passive and does not change rotation." SimC APL has no tier-specific conditions, which is correct. | OK |

### 1.3 Key Talent Effects (Retribution)

| Talent | Status | Notes |
|--------|--------|-------|
| Execution Sentence | IMPLEMENTED | Cooldown with proper damage accumulation and alignment |
| Radiant Glory | IMPLEMENTED | Removes manual AW, auto-triggers from Wake |
| Hammer of Light | IMPLEMENTED | Both Wake-triggered (5HP) and free proc (Light's Deliverance) |
| Light's Deliverance | IMPLEMENTED | 50-stack mechanic triggers free HoL |
| Undisputed Ruling | IMPLEMENTED | Buff tracked in APL (Prot), referenced in Wowhead HoL advice but not in Ret APL conditions |
| Art of War | IMPLEMENTED | BoJ proc priority in generators |
| Final Verdict | IMPLEMENTED | Replaces TV internally |
| Expurgation | IMPLEMENTED | Triggered on BoJ, TV, DS (with tier) |
| Divine Toll | IMPLEMENTED | In generators list |
| Walk into Light | IMPLEMENTED | HoW priority condition in APL |
| Templar Strike/Slash | IMPLEMENTED | Bottom of generators as fillers |

---

## 2. PROTECTION PALADIN

### 2.1 Rotation Priority Comparison (Wowhead vs SimC APL)

**Wowhead Templar ST Priority:**
1. Avenging Wrath on cooldown
2. Judgment on cooldown
3. Shield of the Righteous at 3-5 HP or if free
4. Avenger's Shield on cooldown
5. Divine Toll at 0 HP
6. Blessed Hammer / Hammer of the Righteous on cooldown
7. Word of Glory below 50% health
8. Consecration as filler

**Wowhead Lightsmith ST Priority:**
1. Avenging Wrath on cooldown
2. Sacred Weapon if not inside AW
3. SotR at 3-5 HP or if free
4. Avenger's Shield on cooldown
5. Judgment on cooldown
6. Divine Toll at 0 HP
7. Holy Bulwark if any charges
8. Blessed Hammer / HotR on cooldown
9. Word of Glory below 50%
10. Consecration as filler

**SimC APL (apl_paladin.cpp) Protection:**
1. auto_attack
2. use_items
3. potion (during AW)
4. avenging_wrath (when divine_toll <=10s)
5. fireblood (during AW)
6. divine_toll (during AW or when AW CD <30s)
7. hammer_of_light (complex conditions: not during undisputed_ruling unless expiring, requires judgment debuff)
8. shield_of_the_righteous (complex conditions)
9. holy_armaments (sacred_weapon if <6s remaining)
10. hammer_of_wrath (if HoL ready and no judgment debuff)
11. judgment (if HoL ready and no judgment debuff)
12. avengers_shield (if vanguard buff or AW+apex)
13. holy_armaments (holy_bulwark if AW coming soon)
14. consecration (if divine_guidance stacks >=5)
15. hammer_of_wrath
16. judgment (if full recharge <=2 GCDs)
17. avengers_shield
18. hammer_of_the_righteous (if blessed_assurance)
19. blessed_hammer (if blessed_assurance)
20. judgment
21. holy_armaments (holy_bulwark if 2 charges)
22. consecration (if not up)
23. blessed_hammer
24. hammer_of_the_righteous
25. arcane_torrent
26. word_of_glory (if shining_light free)
27. consecration

**Differences Found:**

| # | Issue | Severity |
|---|-------|----------|
| P1 | **Judgment priority differs**: Wowhead Templar puts Judgment as #2 (right after AW). SimC APL has Judgment much lower — it appears at priority #11 (for HoL setup), #16 (if full recharge), and #20 (general). SimC is more nuanced but significantly deprioritizes Judgment vs Wowhead. | MEDIUM |
| P2 | **Hammer of Light in APL but not in Wowhead guide priority**: The Wowhead Templar priority does NOT mention Hammer of Light as a separate step (it's only in the opener: "Divine Toll + Hammer of Light"). SimC APL has detailed Hammer of Light conditions (lines 84, 87-88). The guide lumps it with Divine Toll. This is SimC being more precise. | LOW |
| P3 | **SotR conditions differ**: Wowhead says "3-5 HP or if free." SimC has complex conditions including checking hammer_of_light_ready buff, undisputed_ruling, hammer_of_light_free, and prev_gcd.1.divine_toll. SimC is much more sophisticated. | LOW (SimC better) |
| P4 | **Divine Toll alignment**: Wowhead says "0 Holy Power, use on cooldown." SimC gates it on `buff.avenging_wrath.up` or `cooldown.avenging_wrath.remains<30`. SimC properly aligns DT with AW window, which is the correct optimization. | LOW (SimC better) |
| P5 | **AW alignment**: Wowhead says "on cooldown." SimC conditions AW on `cooldown.divine_toll.remains<=10` to align with DT. This is a standard SimC optimization. | LOW (SimC better) |
| P6 | **Hammer of Wrath not in Wowhead priority**: Wowhead Prot guide doesn't mention Hammer of Wrath in the rotation priority at all. SimC has it at lines 87 and 92 (both during HoL setup and as regular filler). HoW is available during AW (Judgment converts to HoW), so SimC correctly includes it. | MEDIUM |
| P7 | **Blessed Assurance talent interaction**: SimC specifically prioritizes HotR/Blessed Hammer when blessed_assurance buff is up (lines 95-96). Wowhead doesn't mention this talent interaction. SimC is more precise. | LOW |
| P8 | **Vanguard buff for Avenger's Shield**: SimC prioritizes AS when Vanguard buff is up (line 89). Wowhead doesn't mention this. This is a talent-specific optimization. | LOW |
| P9 | **Divine Guidance + Consecration**: SimC casts Consecration when divine_guidance stacks >=5 (line 91). Wowhead doesn't mention this interaction. | LOW |
| P10 | **Word of Glory condition**: Wowhead says "below 50% health." SimC uses `buff.shining_light_free.up` (free WoG proc). SimC doesn't model health-based decisions (as expected for a DPS-focused sim). | EXPECTED |
| P11 | **AoE identical to ST**: Wowhead confirms AoE priority is same as ST for Prot. SimC has a single flat APL with no AoE/ST split. MATCHES. | OK |
| P12 | **Sacred Weapon/Holy Bulwark (Lightsmith)**: Wowhead Lightsmith puts Sacred Weapon as #2. SimC has holy_armaments for sacred_weapon at priority #9 (if <6s remaining) and holy_bulwark at #13 and #21. SimC is less aggressive about Sacred Weapon than Wowhead suggests. | LOW |
| P13 | **Precombat Consecration**: Wowhead opener says Consecration pre-pull. SimC precombat includes `consecration`. MATCHES. | OK |

### 2.2 Tier Set Bonuses (Protection)

**Wowhead Midnight S1 Tier:**
- 2pc: Shield of the Righteous deals 20% increased damage
- 4pc: After casting SotR, next Avenger's Shield deals 5% increased damage, stacks up to 5

**SimC Implementation:**
- 4pc: IMPLEMENTED — SotR triggers `buffs.light_blessed_shield` (spell 1272298) which is consumed by Avenger's Shield via `parse_effects(buffs.light_blessed_shield, CONSUME_BUFF)`
- 2pc: No explicit `MID1, B2` check found in Protection code. Like Ret 2pc, this is likely handled via automatic DBC spell data parsing for the flat 20% SotR damage increase.

| # | Issue | Severity |
|---|-------|----------|
| T-P1 | 2pc bonus (20% SotR damage) — no explicit code check. Likely auto-parsed from DBC data. Needs verification in sim output. | NEEDS VERIFICATION |
| T-P2 | 4pc bonus implemented: light_blessed_shield buff triggered on SotR, consumed by Avenger's Shield. Stack count and % values from spell data. | OK |
| T-P3 | Wowhead says tier is "completely passive, no rotation impact." SimC APL has no tier-specific conditions. MATCHES. | OK |

### 2.3 Key Talent Effects (Protection)

| Talent | Status | Notes |
|--------|--------|-------|
| Avenging Wrath | IMPLEMENTED | Aligned with Divine Toll in APL |
| Shield of the Righteous | IMPLEMENTED | Complex HP spending logic |
| Avenger's Shield | IMPLEMENTED | Vanguard + apex conditions |
| Divine Toll | IMPLEMENTED | AW alignment |
| Hammer of Light (Templar) | IMPLEMENTED | Detailed conditions including Undisputed Ruling |
| Sacred Weapon (Lightsmith) | IMPLEMENTED | holy_armaments with sacred_weapon conditions |
| Holy Bulwark (Lightsmith) | IMPLEMENTED | holy_armaments with charge management |
| Blessed Hammer | IMPLEMENTED | With blessed_assurance interaction |
| Consecration | IMPLEMENTED | Divine guidance interaction + uptime maintenance |
| Word of Glory | IMPLEMENTED | Shining Light free proc only (no health check) |
| Righteous Protector | IMPLEMENTED | Referenced in Divine Toll condition |
| Blessed Assurance | IMPLEMENTED | Prioritizes HotR/BH when buff is up |
| Vanguard | IMPLEMENTED | Avenger's Shield priority when buff up |

---

## 3. SUMMARY OF KEY FINDINGS

### Critical Issues (0)
None found. Both specs have functional APLs with all major abilities implemented.

### Medium Issues (3)
1. **R1**: Ret Hammer of Light usage is oversimplified in APL vs Wowhead's detailed conditions around AW windows, Undisputed Ruling, and proc expiry timing.
2. **P1**: Prot Judgment priority is significantly lower in SimC than Wowhead suggests (Wowhead: #2, SimC: #11/#16/#20). SimC's approach is likely more optimized but differs notably from the guide.
3. **P6**: Prot Hammer of Wrath is present in SimC but completely absent from Wowhead's rotation priority list.

### Low Issues (8)
- R4: No separate Herald of the Sun APL path (handled via talent checks)
- R5: Walk into Light HoW vs BoJ priority ordering
- P2/P3/P4/P5: SimC has more sophisticated conditions than Wowhead's simplified guide
- P7/P8/P9: SimC includes talent interactions (Blessed Assurance, Vanguard, Divine Guidance) not mentioned in Wowhead
- P12: Sacred Weapon priority lower in SimC than Wowhead suggests

### Verification Needed (2)
- **T-R1**: Ret 2pc (Expurgation +20% damage) — no explicit code, likely DBC auto-parsed
- **T-P1**: Prot 2pc (SotR +20% damage) — no explicit code, likely DBC auto-parsed

### Notes
- SimC APLs are generally MORE sophisticated than Wowhead guides, which is expected. Wowhead provides human-readable simplified priorities while SimC optimizes for simulation accuracy.
- Tier set 4pc bonuses are fully implemented for both specs.
- All core abilities and major talents are implemented in the class module.
- The Protection APL is notably more complex than the Wowhead guide suggests, with many talent-specific interactions that the guide omits for simplicity.
- The Retribution APL handles multiple hero talent builds (Templar, Templar RG, Herald of the Sun) through conditional talent checks rather than separate APL paths.
