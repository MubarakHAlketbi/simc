# Audit Fix Task List — Batched by Priority & File Locality
# Generated: 2026-03-24
# Source: audit_notes.md (42 issues from full 33-spec audit)
#
# Batching strategy:
#   - CRITICAL first, then HIGH, MEDIUM, LOW
#   - Group by same-file edits (minimize context switches)
#   - Parallelizable tasks in the same batch where possible
#   - Each batch targets ~2-4 hours of work
#   - Verification gates between batches

---

## Batch 1 — Missing Tier Sets [CRITICAL] (5 tasks)
All are the same pattern: read Wowhead tier.md, implement 2pc+4pc set bonus handlers.
Can be parallelized — each touches a different class module file.

| # | Issue | Spec | File | 2pc Effect | 4pc Effect |
|---|-------|------|------|------------|------------|
| 1.1 | #1 | DH Havoc | sc_demon_hunter.cpp | Blade Dance +15% damage | +6% haste in Metamorphosis |
| 1.2 | #3 | Evoker Augmentation | sc_evoker.cpp | Eruption +15% dmg, +0.3s EM extension | Empowers +20% dmg/CDR during EM |
| 1.3 | #4 | Priest Shadow | sc_priest.cpp / sc_priest_shadow.cpp | SW:M +10% dmg, -5 Insanity cost | Apparitions +40% dmg |
| 1.4 | #5 | Enhancement Shaman | sc_shaman.cpp | +15% Stormstrike/Lava Lash damage | +2% Mastery per Crash Lightning stack |
| 1.5 | #6 | Windwalker Monk | monk/sc_monk.cpp | VERIFY first — may be auto-parsed | VERIFY first — may be auto-parsed |

Verification gate: Build clean, run iterations=1 for each affected profile.

---

## Batch 2 — Guardian Druid APL Rewrite [CRITICAL] (1 large task)
Standalone — this is a full APL rewrite, not a patch.

| # | Issue | File | Work Required |
|---|-------|------|---------------|
| 2.1 | #2 | druid/guardian_apl.inc | FULL REWRITE. Read wowhead/druid/guardian/extracted/rotation.md. Implement: Ironfur, Frenzied Regen, Incarnation, Barkskin, HotW, Raze, Red Moon, rage management (Maul at ~80 rage), hero talent branching (Druid of the Claw / Elune's Chosen), fix double Convoke, remove "assisted_combat" stub. |

Verification gate: Guardian profile iterations=1 pass + 1000-iter baseline shows reasonable DPS.

---

## Batch 3 — Demon Hunter APL Fixes [HIGH] (3 tasks)
All in apl_demon_hunter.cpp — single file session.

| # | Issue | Spec | Fix |
|---|-------|------|-----|
| 3.1 | #7 | DH Devourer | Reorder: Cull above Void Ray inside Void Metamorphosis meta list |
| 3.2 | #8 | DH Devourer | Add Soul Smuggling logic: hold fragments before form transitions |
| 3.3 | #9 | DH Havoc | Move Inertia consumption to top priority after meta/CD checks |

Verification gate: DH profiles iterations=1 pass, spot-check DPS delta on Devourer + Havoc.

---

## Batch 4 — Death Knight APL Fixes [HIGH+MEDIUM] (5 tasks)
All in apl_death_knight.cpp — single file session.

| # | Issue | Spec | Fix |
|---|-------|------|-----|
| 4.1 | #11 | DK Unholy | Remove <=35% HP gate on Soul Reaper — cast on cooldown |
| 4.2 | #10 | DK Unholy | Change Death Coil to fire at >=80 RP threshold |
| 4.3 | #18 | DK Unholy | Move Putrefy from position 7 to position 4 in AoE list |
| 4.4 | #19 | DK Unholy | Add San'layn-specific priority adjustments |
| 4.5 | #12 | DK Frost | INVESTIGATE: Remorseless Winter in APL but not Wowhead — verify if SimC optimization or error |

Verification gate: DK profiles iterations=1 pass, 1000-iter Unholy baseline should improve.

---

## Batch 5 — Evoker APL Fixes [HIGH+MEDIUM] (3 tasks)
All in apl_evoker.cpp — single file session.

| # | Issue | Spec | Fix |
|---|-------|------|-----|
| 5.1 | #13 | Evoker Dev | Add Engulf to st_fs and aoe_fs Flameshaper action lists |
| 5.2 | #23 | Evoker Dev | Add Deep Breath on cooldown for Scalecommander ST (not just Strafing Run refresh) |
| 5.3 | #42 | Evoker | Fix typos: "Fameshaper" → "Flameshaper", "Scalemander" → "Scalecommander" |

Verification gate: Evoker profiles iterations=1 pass, Flameshaper DPS should jump significantly.

---

## Batch 6 — Monk APL Fixes [HIGH+MEDIUM] (3 tasks)
All in apl_monk.cpp — single file session.

| # | Issue | Spec | Fix |
|---|-------|------|-----|
| 6.1 | #14 | Brewmaster | Add Touch of Death as #1 priority (before other attacks) |
| 6.2 | #15 | Brewmaster | Move Blackout Kick higher; enforce BoK → Tiger Palm sequencing for Blackout Combo |
| 6.3 | #28 | Brewmaster | Add Spinning Crane Kick as AoE filler |

Verification gate: Monk profiles iterations=1 pass, Brewmaster DPS should increase.

---

## Batch 7 — Rogue + Mage APL Fixes [HIGH+MEDIUM] (3 tasks)
Two files, both small targeted changes.

| # | Issue | Spec | File | Fix |
|---|-------|------|------|-----|
| 7.1 | #16 | Rogue Sub | apl_rogue.cpp | Split Shadow Dance CP threshold: Deathstalker enters low CP, Trickster enters 6+ CP |
| 7.2 | #35 | Rogue Sub | apl_rogue.cpp | Change Shadowstrike AoE threshold from <=2 to <=3 targets |
| 7.3 | #17 | Frost Mage | apl/mage.cpp | Add FoF 2-stack priority, fix Glacial Spike vs FoF ordering, remove Comet Storm from Spellslinger |

Verification gate: Rogue Sub + Frost Mage iterations=1 pass.

---

## Batch 8 — Medium APL Condition Fixes [MEDIUM] (10 tasks)
Spread across multiple files — group by class where possible.

| # | Issue | Spec | File | Fix |
|---|-------|------|------|-----|
| 8.1 | #20 | DH Vengeance | apl_demon_hunter.cpp | Change Spirit Bomb fragment threshold to flat 6 |
| 8.2 | #21 | Druid Balance | druid/balance_apl.inc | Add AP<40 condition to Convoke |
| 8.3 | #22 | Druid Balance | druid/balance_apl.inc | Change Eclipse entry threshold from 60 AP to 90% |
| 8.4 | #24 | Hunter BM | apl_hunter.cpp | Add Killer Cobra interaction to Pack Leader ST list |
| 8.5 | #25 | Hunter BM | apl_hunter.cpp | Change Barbed Shot pre-BW window from 1.5s to 3s |
| 8.6 | #26 | Mage Fire | apl/mage.cpp | Change Sunfury Flamestrike threshold from 3 to 4 targets |
| 8.7 | #29 | Paladin Ret | apl_paladin.cpp | Add AW/Undisputed Ruling/proc expiry conditions to Hammer of Light |
| 8.8 | #30 | Priest Shadow | apl_priest.cpp | Add absorb shield detection for Voidweaver SW:D |
| 8.9 | #31 | Shaman Ele | apl_shaman.cpp | Change AoE threshold from >=3 to >=2 targets |
| 8.10 | #32+#33 | Warlock Demo | apl/warlock.cpp | Add AoE action lists + Diabolist vs Soul Harvester hero talent branching |

Verification gate: All affected profiles iterations=1 pass.

---

## Batch 9 — Tier Set Verification [MEDIUM] (1 task, multi-spec)
Verify whether "missing" tier bonuses are actually auto-parsed from DBC spell data.

| # | Issue | Specs | Method |
|---|-------|-------|--------|
| 9.1 | #27 | Mage (Arc 4pc, Fire 2pc, Frost 2pc), Paladin Ret 2pc, DH Vengeance, DH Devourer, Druid Guardian | For each: run sim with tier equipped, check sim log for set bonus buff uptime. If zero → implement explicitly. If present → document as DBC auto-parsed. |

Verification gate: Document results. Implement any truly missing bonuses.

---

## Batch 10 — Low Priority Cleanup [LOW] (5 tasks)
Non-urgent. Do after all above batches.

| # | Issue | Spec | Fix |
|---|-------|------|-----|
| 10.1 | #34 | Warlock Destro | Verify 4pc damage value: code comment says 10%, Wowhead says 20%, check spell data |
| 10.2 | #36 | DK Blood | Review extra Death Strike fillers — may be intentional for survivability |
| 10.3 | #37 | DK Frost | Document ERW condition complexity as intentional SimC optimization |
| 10.4 | #38 | Druid Feral | Remove outdated Algethar Puzzle Box trinket reference |
| 10.5 | #40 | Paladin Prot | Review Judgment priority — document if intentional SimC optimization |

---

## Execution Order Summary

| Batch | Priority | Tasks | Est. Effort | Parallelizable |
|-------|----------|-------|-------------|----------------|
| 1 | CRITICAL | 5 tier sets | 3-4 hrs | Yes (5 different files) |
| 2 | CRITICAL | Guardian APL rewrite | 2-3 hrs | No (single large task) |
| 3 | HIGH | DH APL fixes | 1-2 hrs | No (single file) |
| 4 | HIGH+MED | DK APL fixes | 1-2 hrs | No (single file) |
| 5 | HIGH+MED | Evoker APL fixes | 1 hr | No (single file) |
| 6 | HIGH+MED | Monk APL fixes | 1 hr | No (single file) |
| 7 | HIGH+MED | Rogue + Mage APL | 1-2 hrs | Partially (2 files) |
| 8 | MEDIUM | Multi-spec condition fixes | 2-3 hrs | Yes (10 different files) |
| 9 | MEDIUM | Tier set verification | 1-2 hrs | Yes (parallel sims) |
| 10 | LOW | Cleanup | 1 hr | Yes |
| **TOTAL** | | **42 issues** | **~15-20 hrs** | |

### Recommended Parallel Lanes:
- Lane A: Batch 1 (tier sets) → Batch 9 (tier verification)
- Lane B: Batch 2 (Guardian APL) → Batch 3 (DH APL) → Batch 4 (DK APL) → Batch 5 (Evoker APL) → Batch 6 (Monk APL) → Batch 7 (Rogue+Mage APL)
- Lane C: Batch 8 (medium condition fixes) → Batch 10 (low cleanup)

After all batches: full rebuild, 56-profile smoke test, re-run Phase 4 baselines.
