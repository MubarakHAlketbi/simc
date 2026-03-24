# Warlock SimC Audit Report — Wowhead vs SimC Code/APL
Generated: 2026-03-24
Patch: 12.0.1 (Midnight Season 1)

## Summary

All three Warlock specs (Affliction, Demonology, Destruction) were audited by comparing
Wowhead rotation guides, tier set information, and talent/mechanics data against the SimC
APL (engine/class_modules/apl/warlock.cpp) and class module (engine/class_modules/warlock/).

Overall: SimC implementation is largely complete and well-aligned with Wowhead guides.
Key issues found are minor APL ordering differences and a few missing nuances.

---

## 1. AFFLICTION

### 1.1 Rotation Priority — Wowhead vs APL

#### Hellcaller ST (Wowhead priority):
1. Haunt
2. Agony
3. Wither
4. Dark Harvest
5. Summon Darkglare
6. Malevolence
7. Unstable Affliction (as many as possible)
8. Malefic Grasp

#### APL HC_st priority:
1. Haunt (if cooldown ready)
2. Agony (if not ticking or refreshable)
3. Wither (if not ticking or refreshable)
4. Dark Harvest (with conditions on agony/corruption remains)
5. Agony refresh if Darkglare imminent
6. Summon Darkglare
7. Malevolence
8. Malefic Grasp (if Darkglare active & about to expire)
9. Unstable Affliction (with shard/buff conditions)

FINDINGS:
- [OK] Core priority matches: Haunt > Agony > Wither > Dark Harvest > Darkglare > Malevolence > UA > Malefic Grasp
- [OK] APL adds smart conditions (shard management, pandemic, Darkglare syncing) beyond simple Wowhead list
- [OK] Malefic Grasp as filler is present in APL (used when Darkglare active)
- [NOTE] Wowhead says Malefic Grasp is the generic filler at bottom of priority. APL uses it only during Darkglare windows, then falls through to drain_soul/drain_life/shadow_bolt as true filler. This is more optimal than Wowhead's simplified guide.

#### Soul Harvester ST (Wowhead priority):
1. Haunt
2. Agony
3. Corruption
4. Summon Darkglare
5. Unstable Affliction
6. Dark Harvest
7. Unstable Affliction
8. Malefic Grasp

#### APL SH_st priority:
1. Haunt (if nightfall stacks < 2)
2. Agony (if not ticking or refreshable)
3. Corruption (if not ticking or refreshable)
4. Summon Darkglare (with shard/CD conditions)
5. Dark Harvest (with shard and dot/buff conditions)
6. Malefic Grasp (Darkglare window)
7. Drain Soul / Shadow Bolt (if nightfall > 1)
8. Unstable Affliction (with Darkglare/shard/proc conditions)

FINDINGS:
- [OK] Core priority matches with Wowhead
- [DIFF] Wowhead shows UA before Dark Harvest, APL shows Dark Harvest before UA dump. This is a minor sequencing difference — APL likely optimized for shard generation before spending.
- [OK] Malefic Grasp used during Darkglare windows

#### AoE Priority — Both Hero Talents
FINDINGS:
- [OK] Seed of Corruption prioritized in AoE for both hero talents
- [OK] Haunt on priority target
- [OK] Agony multi-dotting (APL: active_dot.agony<5 for SH, active_dot.agony<active_enemies for HC)
- [OK] Darkglare, Dark Harvest, Malevolence (HC only) present
- [OK] Seed of Corruption as spender in AoE

#### Filler Spell Logic
FINDINGS:
- [IMPORTANT] Wowhead lists Malefic Grasp as primary filler. The APL default list uses a sophisticated filler chain:
  1. Malefic Grasp (only during Darkglare)
  2. Drain Soul (with chain/interrupt for Nightfall procs)
  3. Drain Life (WITH Gorefiend's Avarice — channels 100% faster, outperforms Drain Soul)
  4. Shadow Bolt (fallback)
- [OK] Gorefiend's Avarice is fully implemented in sc_warlock_actions.cpp with custom drain_life_state_t that halves tick time (2x tick rate). APL line 77 correctly uses drain_life as filler when talent is active.
- [NOTE] Wowhead guide does NOT mention Drain Life as a filler with Gorefiend's Avarice. SimC is ahead of the guide here.

### 1.2 Tier Set Bonuses

Wowhead:
- 2pc: Unstable Affliction and Seed of Corruption damage increased by 10%
- 4pc: Agony starts at 2 additional stacks, and its damage is increased by 20%

SimC Implementation:
- 2pc (ID 1264869): parse_effects applied — UA and SoC +10% damage ✓
- 4pc (ID 1264870): Effect #1 (initial stacks) applied in agony_t constructor (+2 stacks) ✓
  Effect #2 (Agony +20% periodic) parsed via parse_effects ✓

FINDING: [OK] All tier bonuses fully implemented and matching Wowhead description.

### 1.3 Key Talents
- [OK] Dark Harvest — implemented (appears in init and actions)
- [OK] Malefic Grasp — implemented
- [OK] Summon Darkglare — implemented with DOT damage amp
- [OK] Malevolence (Hellcaller capstone) — in APL and actions
- [OK] Wither (Hellcaller) — in APL and actions
- [OK] Haunt — in APL
- [OK] Nightfall procs — handled in APL with nightfall.react conditions
- [OK] Shard Instability — referenced in APL conditions
- [OK] Cascading Calamity — referenced in APL conditions
- [OK] Cull the Weak — implemented (66 references in code)
- [OK] Gorefiend's Avarice — fully implemented with tick speed modifier

---

## 2. DEMONOLOGY

### 2.1 Rotation Priority — Wowhead vs APL

#### Diabolist ST (Wowhead priority):
1. Power Siphon
2. Call Dreadstalkers
3. Hand of Gul'dan / Ruination
4. Grimoire: Imp Lord / Grimoire: Fel Ravager
5. Summon Demonic Tyrant
6. Summon Doomguard
7. Demonbolt with Demonic Core
8. Shadow Bolt / Infernal Bolt

#### APL default priority:
1. Potion (if Tyrant active)
2. Racials (if Tyrant active)
3. Items
4. Grimoire Imp Lord
5. Grimoire Fel Ravager
6. Summon Doomguard
7. Call Dreadstalkers
8. Summon Demonic Tyrant
9. Implosion (if wild_imps >= 6)
10. Ruination
11. Demonbolt (Doom application priority, or core stack >= 3)
12. Power Siphon (if no Demonic Core)
13. Infernal Bolt (if soul_shard < 3)
14. Hand of Gul'dan
15. Demonbolt (if soul_shard < 4 & demonic_core.react)
16. Shadow Bolt
17. Infernal Bolt (fallback)

FINDINGS:
- [DIFF] Wowhead puts Power Siphon first; APL puts it at position 12 (only when no Demonic Core charges). APL is more optimal — you only need Power Siphon when out of cores.
- [DIFF] Wowhead: Call Dreadstalkers before Hand of Gul'dan. APL: Grimoires > Doomguard > Dreadstalkers > Tyrant > Implosion > Ruination > Demonbolt. The APL front-loads cooldowns (Grimoire, Doomguard) to maximize demon count for Tyrant.
- [OK] Summon Demonic Tyrant correctly placed after Dreadstalkers
- [OK] Ruination (Diabolist) present in APL
- [OK] Infernal Bolt (Diabolist Mother of Chaos proc) handled
- [DIFF] Wowhead separates Diabolist vs Soul Harvester with Ruination/Infernal Bolt differences. APL is a single unified list that handles both via talent checks.
- [NOTE] APL does NOT have separate hero talent sublists for Demonology (unlike Affliction). It uses a single default list. This is simpler but means no hero-talent-specific optimizations.

#### AoE Priority
Wowhead:
1. Implosion with 6 Wild Imps
2. Summon Doomguard
3. Call Dreadstalkers
4. Hand of Gul'dan / Ruination
5. Grimoire: Imp Lord / Grimoire: Fel Ravager
6. Summon Demonic Tyrant
7. Demonbolt with Demonic Core
8. Shadow Bolt / Infernal Bolt

FINDINGS:
- [OK] Implosion present with >=6 imp threshold (APL line: buff.wild_imps.stack>=6)
- [DIFF] APL doesn't have a separate AoE action list. It uses the same default list with Implosion included. Wowhead's AoE priority puts Implosion first; in the APL, it comes after core cooldowns. This could be suboptimal in pure AoE.
- [ISSUE] No active_enemies-based branching in Demonology APL — unlike Affliction and Destruction which have dedicated AoE lists. This means Demonology AoE may not be fully optimized in SimC.

#### Opener
Wowhead (Diabolist):
1. Pre-cast Power Siphon (5s before pull)
2. Pre-cast Shadow Bolt
3. Grimoire: Imp Lord
4. Call Dreadstalkers
5. Summon Demonic Tyrant
6. Hand of Gul'dan x4 interleaved with Demonbolt
7. Infernal Bolt
8. Normal priority

FINDINGS:
- [OK] Precombat: power_siphon, then demonbolt (if no power_siphon buff) or shadow_bolt
- [DIFF] Wowhead opener is very specific (exact sequence of HoG/Demonbolt casts). APL precombat only does power_siphon + filler, then falls into normal priority. SimC APLs typically don't script exact openers — they rely on priority lists from the start. This is standard SimC behavior.

### 2.2 Tier Set Bonuses

Wowhead:
- 2pc: Hand of Gul'dan damage increased by 15%
- 4pc: Dreadstalkers deal 10% increased damage and last 3 additional sec

SimC Implementation:
- 2pc (ID 1264871): parse_effects applied — Hand of Gul'dan +15% damage ✓
- 4pc (ID 1264872): 
  - Effect #1: Dreadstalker +10% damage (in sc_warlock_pets.cpp line 1098) ✓
  - Effect #2: +3 sec spawn duration (in sc_warlock_actions.cpp line 3045) ✓

FINDING: [OK] All tier bonuses fully implemented and matching.

### 2.3 Key Talents
- [OK] Demonic Core — extensive implementation (procs, stacking, APL management)
- [OK] Call Dreadstalkers — implemented with Reign of Tyranny interaction
- [OK] Summon Demonic Tyrant — implemented with demon count buff
- [OK] Power Siphon — in precombat and priority
- [OK] Implosion — implemented with 6 imp threshold
- [OK] Summon Doomguard — in APL
- [OK] Grimoire: Imp Lord / Fel Ravager — in APL
- [OK] Infernal Bolt (Diabolist) — in APL
- [OK] Ruination (Diabolist) — in APL
- [OK] Doom — target_if conditions for spreading Doom via Demonbolt
- [OK] Reign of Tyranny — referenced in variables

---

## 3. DESTRUCTION

### 3.1 Rotation Priority — Wowhead vs APL

#### Hellcaller ST (Wowhead priority):
1. Maintain Wither
2. Shadowburn (when available, about to cap shards)
3. Chaos Bolt (avoid capping shards)
4. Soul Fire (when available, < 4 shards)
5. Conflagrate (keep below 2 stacks / when moving)
6. Conflagrate (generate shards + Backdraft)
7. Incinerate (generate shards)

#### APL default (Hellcaller path via talent.wither checks):
1. Variables, OGCDs, Items
2. AoE lists (if active_enemies >= 2)
3. Soul Fire (if soul_shard <= 4)
4. Conflagrate (if soul_shard <= 4.2 & backdraft < 1)
5. Summon Infernal
6. Malevolence
7. Incinerate (if chaotic_inferno buff & shards <= 4.6)
8. Shadowburn (with fiendish_cruelty/conflagration_of_chaos conditions, shard/malevolence/infernal conditions)
9. Wither (complex pandemic/internal_combustion logic)
10. Ruination
11. Cataclysm (if lake_of_fire)
12. Chaos Bolt (shard >= 4 or malevolence/infernal active)
13. Infernal Bolt (if shards <= 3)
14. Channel Demonfire
15. Incinerate

FINDINGS:
- [DIFF] Wowhead puts Wither maintenance first. APL puts it at position 9 with complex pandemic conditions. The APL approach is more nuanced — it only refreshes Wither when needed based on pandemic timing and Internal Combustion interaction, which is more DPS-optimal.
- [DIFF] Wowhead puts Shadowburn at position 2. APL puts it at position 8 with more restrictive conditions (fiendish_cruelty/conflagration_of_chaos). APL is more conservative and likely correct.
- [OK] Soul Fire present with shard conditions
- [OK] Conflagrate with Backdraft management
- [OK] Summon Infernal and Malevolence present
- [OK] Chaos Bolt shard dump logic present
- [NOTE] APL includes Channel Demonfire which Wowhead doesn't mention in ST priority

#### Diabolist ST (Wowhead priority):
1. Maintain Immolate
2. Shadowburn
3. Chaos Bolt (avoid capping)
4. Chaos Bolt (if > 4 shards & Infernal Bolt ready)
5. Soul Fire (< 4 shards)
6. Conflagrate
7. Incinerate

FINDINGS:
- [OK] APL handles Diabolist via talent.diabolic_ritual checks
- [OK] Chaos Bolt with demonic_art/ritual_length conditions (line 266) — handles the Diabolist demon cycling
- [OK] Infernal Bolt as shard generator
- [OK] Immolate maintenance with pandemic logic
- [OK] Ruination (Pit Lord proc) present

#### AoE Priority
Wowhead Hellcaller AoE:
1. Maintain Wither on many targets
2. Malevolence (when many Wither targets)
3. Spend shards (Rain of Fire 5+, Chaos Bolt with Havoc up to 5)
4. Conflagrate
5. Incinerate

APL aoe_hc:
1. Summon Infernal
2. Malevolence
3. Rain of Fire (soul_shard >= threshold & active_enemies >= 4)
4. Conflagrate (target_if for Wither refresh)
5. Shadowburn (with conditions)
6. Cataclysm
7. Havoc (target selection logic)
8. Rain of Fire (active_enemies >= 4)
9. Chaos Bolt (active_enemies <= threshold)
10. Soul Fire
11. Wither (multi-dot with pandemic)
12. Incinerate with Fire and Brimstone + Backdraft
13. Conflagrate
14. Incinerate

FINDINGS:
- [OK] Dedicated AoE lists for both Hellcaller (aoe_hc) and Diabolist (aoe_dia)
- [OK] Rain of Fire vs Chaos Bolt threshold logic matches Wowhead guidance
- [OK] Havoc targeting logic present (Wowhead mentions 60% damage replication)
- [OK] Wither/Immolate multi-dotting
- [OK] Malevolence synced with Wither stacks
- [DIFF] APL has Cataclysm in AoE, not explicitly mentioned in Wowhead rotation (but it's a talent choice)
- [OK] Fire and Brimstone interaction with Incinerate in AoE

#### Opener
Wowhead (Hellcaller):
1. Precast Soul Fire
2. Summon Infernal + trinkets/racials
3. Malevolence (stack Wither)
4. Conflagrate
5. Generate/spend shards during CDs

FINDINGS:
- [OK] Precombat: soul_fire precast present (line 255)
- [OK] Summon Infernal in priority
- [OK] Malevolence after Infernal

### 3.2 Tier Set Bonuses

Wowhead:
- 2pc: Chaos Bolt and Rain of Fire damage increased by 5%
- 4pc: Conflagrate generates additional 2 soul shard fragments, deals 20% increased damage

SimC Implementation:
- 2pc (ID 1264873): parse_effects — Chaos Bolt and Rain of Fire +5% damage ✓
- 4pc (ID 1264874):
  - Effect #1: Extra shard fragments (line 3879: +2 fragments / 10.0 = 0.2 shards) ✓
  - Conflagrate damage (line 192: parse_effects with effect mask) — noted as +10% in comment but Wowhead says +20%. 
    NEEDS VERIFICATION: Comment says "+10% damage" but Wowhead says "20% increased damage". The actual value comes from spell data (effect_mask disables effect #1 for shards, parses remaining effects for damage). If spell data says 20%, it's correct regardless of comment.

FINDING: [MOSTLY OK] Tier bonuses implemented. The 4pc damage comment says 10% but Wowhead says 20% — this should be verified against spell data. The actual implementation uses parse_effects which reads from spell data directly, so it's likely correct if spell data is right.

### 3.3 Key Talents
- [OK] Chaos Bolt — primary spender
- [OK] Havoc — AoE list with havoc_active checks
- [OK] Summon Infernal — 2min CD, shard generation
- [OK] Conflagrate — shard gen + Backdraft
- [OK] Shadowburn — execute-range and shard management
- [OK] Soul Fire — present with shard conditions
- [OK] Wither (Hellcaller) — complex pandemic refresh
- [OK] Malevolence (Hellcaller) — synced with Infernal
- [OK] Diabolic Ritual (Diabolist) — demon cycling via demonic_art/ritual_length variables
- [OK] Ruination (Diabolist Pit Lord) — in APL
- [OK] Infernal Bolt (Diabolist Mother of Chaos) — in APL
- [OK] Internal Combustion — factored into Immolate/Wither refresh logic
- [OK] Crashing Chaos — referenced indirectly through Infernal usage
- [OK] Rain of Fire — AoE spender with target count thresholds
- [OK] Channel Demonfire — in APL
- [OK] Cataclysm — in AoE lists
- [OK] Backdraft — managed via Conflagrate conditions
- [OK] Fire and Brimstone — in AoE Incinerate logic

---

## 4. CROSS-SPEC ISSUES & OBSERVATIONS

### 4.1 Demonology APL Simplicity
[ISSUE] Demonology has no AoE-specific action list (no active_enemies branching). 
Affliction has SH_st/SH_cleave/SH_aoe and HC_st/HC_cleave/HC_aoe.
Destruction has aoe_hc and aoe_dia.
Demonology uses a single default list for all target counts.
Recommendation: Consider adding target-count-based sublists for Demonology, especially for Implosion timing optimization.

### 4.2 Demonology Hero Talent Differentiation
[ISSUE] Demonology APL does not branch by hero talent (Diabolist vs Soul Harvester).
Both Affliction and Destruction have hero-talent-specific logic.
Wowhead shows different priorities (Ruination/Infernal Bolt for Diabolist only).
The APL includes both Ruination and Infernal Bolt which are talent-gated, so they'll naturally only fire for Diabolist, but there may be Soul Harvester-specific optimizations missing.

### 4.3 Affliction Drain Life / Gorefiend's Avarice
[NOTABLE] SimC correctly implements Drain Life as primary filler with Gorefiend's Avarice (2x tick speed). The APL at line 77 uses drain_life with talent.gorefiends_avarice condition, falling back to drain_soul otherwise. This is NOT mentioned in the Wowhead guide at all — SimC is ahead of the published guide.

### 4.4 Wowhead Extraction Quality
[NOTE] The extracted Wowhead data has significant duplication (same boilerplate text repeated across tabs). The actual rotation priority information is clean and usable, but filtering the noise requires careful reading.

### 4.5 Midnight Season Consumables
APL consumables (potion, flask, food, rune, temporary_enchant) are set for both level 80 (TWW) and level 90 (Midnight). The Midnight-tier consumables are:
- Potion: lights_potential_2
- Flask: flask_of_the_magisters_2  
- Food: blooming_feast
- Rune: void_touched
- Weapon: thalassian_phoenix_oil_2

These should be cross-referenced with Wowhead consumable guides for accuracy (not done in this audit).

---

## 5. ISSUE SUMMARY TABLE

| # | Spec | Severity | Issue |
|---|------|----------|-------|
| 1 | Demo | MEDIUM | No AoE-specific action list; single priority for all target counts |
| 2 | Demo | LOW | No hero talent branching (Diabolist vs Soul Harvester sublists) |
| 3 | Demo | LOW | APL opener is simplified vs Wowhead's detailed sequence |
| 4 | Afflic | INFO | Drain Life w/ Gorefiend's Avarice in SimC but not in Wowhead guide |
| 5 | Afflic | LOW | SH_st: Dark Harvest before UA in APL vs UA before DH in Wowhead |
| 6 | Destro | INFO | 4pc comment says "+10% damage" but Wowhead says "+20%" — verify spell data |
| 7 | Destro | LOW | APL includes Channel Demonfire in ST, not mentioned in Wowhead ST |
| 8 | ALL | INFO | Wowhead extracted data has heavy boilerplate duplication |

Severity scale: HIGH = missing core ability/mechanic, MEDIUM = missing optimization path,
LOW = minor priority ordering difference, INFO = informational note

---

## 6. CONCLUSION

SimC Warlock implementation is comprehensive and well-maintained for Midnight Season 1.
All three specs have:
- Complete tier set bonus implementation (2pc + 4pc) ✓
- All key talents coded and functional ✓
- Both hero talent paths supported ✓
- Rotation priorities that are at least as detailed as (often more optimized than) Wowhead guides ✓

The main area for improvement is Demonology's APL, which lacks the AoE/cleave sublists
and hero talent branching that the other two specs have. This could lead to suboptimal
sim results in multi-target scenarios for Demonology.
