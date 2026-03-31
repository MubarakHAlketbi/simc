# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-03-31 — **v0.2 Engine Correctness Audit**

**Game build: 12.0.1.66709 Live** — we target Live only, ignore 12.0.5.x PTR.

## Status

| Metric | Value |
|--------|-------|
| Release | **v0.2** (tagged 2026-03-31) |
| Profiles | 66/66 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 66/66 PASS (budget, prereqs, req_points gates) |
| Baselines | 120/120 FRESH (2026-03-31, Build 66709, target_error=0.1) — 3 new tank HAC need baselines |
| Tier sets | 33/33 behaviorally verified — all effectN reads checked against DBC |
| Engine audit | **COMPLETE** — 3132 effectN reads scanned, 6 bugs found+fixed |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL audit | 42/42 resolved |
| Talent builds | 29/33 profiles updated from Wowhead comparison |
| Tooling | 19 scripts, ~5,500 lines (optimization + validation + audit) |
| Upstream sync | **SYNCED** — Build 66709, merged 2026-03-31 |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

---

## What's Next

| # | Task | Type | Status |
|---|------|------|--------|
| ~~1~~ | ~~Upstream sync~~ — merged 359 commits, Build 66709 | Engine | **DONE** |
| ~~2~~ | ~~Re-baseline all specs~~ — 120/120 fresh on Build 66709 | Testing | **DONE** |
| ~~3~~ | ~~Engine correctness audit~~ — DBC verification, tier set behavioral checks, effectN OOB scan | Testing | **DONE (v0.2)** |
| **4** | **Re-extract Wowhead data** (build changed 66384→66709) | Data | PENDING |
| 5 | Multi-target sweeps (1,3,5,10 targets) for AoE scaling verification | Testing | PENDING |
| 6 | Proc rate validation — compare JSON execute counts vs RPPM/ICD tooltips | Testing | PENDING |
| 7 | Talent + APL optimization (per spec, both fight styles) | Optimization | PENDING |
| 8 | Trinket combinatorics | Optimization | PENDING |
| 9 | Final docs + cleanup + contribute fixes back upstream | Maintenance | PENDING |

---

## v0.2 Engine Correctness Audit (2026-03-31)

### Bugs Found and Fixed

| # | Class | Bug | Root Cause | DPS Impact | Commit |
|---|-------|-----|-----------|------------|--------|
| 1 | Priest Shadow | 2pc SW:Madness doing 0 damage | Swapped effectN indices (cost vs damage) | **+25.4%** | aad7db1 |
| 2 | Rogue Sub | 4pc Shadow Blades permanent (99.7% uptime) | `from_seconds(base_value())` on ms value (4000ms = 4000s) | **-19.6%** | 31e47b9 |
| 3 | Monk WW | 4pc CDR negated by manual adjust | Manual `cooldown->adjust(-5s)` cancelled auto-applied passive aura `(-5s)` | **+1.2%** | aad7db1 |
| 4 | Shaman Ele | Storm Elemental Elemental Unity TA bonus = 0 | effectN(5) OOB on 4-effect spell (should be effectN(4)) | ~0% (pet TA) | 155add0 |
| 5 | Trinket | Phoenix Torque wrong damage/heal indices | effectN index swap | Minor | aad7db1 |
| 6 | Shaman Enh | 2pc wrong semantic effect index | Read effectN(2) instead of effectN(1) (same value) | None | aad7db1 |

### Audit Scope

| Check | Scope | Result |
|-------|-------|--------|
| Spell ID existence (Level 1) | 568 Midnight IDs across 13 classes | 568/568 exist in DBC |
| Talent name match | 568 find_talent_spell lookups | 568/568 match DBC name |
| effectN OOB (Level 2) | 3132 reads across 38 source files | 32 candidates → 2 real bugs |
| from_seconds(base_value()) | 89 call sites | 1 bug (Rogue Sub 4pc, fixed) |
| Tier set behavioral | 33 specs × 2pc+4pc | All effectN values match tooltips |
| Tier set DPS delta | 33 specs (3000 iter each) | All 2.8%–20.1% (reasonable) |

### Tier Set Deltas (post-fix)

| Spec | Delta | Spec | Delta | Spec | Delta |
|------|-------|------|-------|------|-------|
| BM Hunter | +5.2% | Assa Rogue | +8.9% | Blood DK | +5.2% |
| MM Hunter | +2.8% | Outlaw Rogue | +8.6% | Frost DK | +6.2% |
| SV Hunter | +3.6% | Sub Rogue | +19.5% | Unholy DK | +3.8% |
| Arcane Mage | +3.5% | Arms Warrior | +8.3% | Shadow Priest | +16.0% |
| Fire Mage | +6.3% | Fury Warrior | +4.8% | Ele Shaman | +11.3% |
| Frost Mage | +3.7% | Ret Paladin | +13.2% | Enh Shaman | +10.1% |
| Affli Lock | +3.0% | WW Monk | +3.2% | Havoc DH | +12.1% |
| Demo Lock | +4.7% | Balance Druid | +11.7% | Dev Evoker | +6.0% |
| Destro Lock | +6.9% | Feral Druid | +6.2% | Aug Evoker | +20.1% |

---

## Completed Work

### v0.2 — Engine Correctness Audit (2026-03-31)
- Full DBC behavioral audit across all 13 class modules
- 6 bugs found and fixed (3 with significant DPS impact)
- Audit tooling: verify_spell_ids.py, deep_audit.py, audit_class_spells.py
- Upstream merge: 359 commits, 44 conflict resolution
- 120/120 fresh baselines on Build 66709

### v0.1 — Optimization System (2026-03-30)
- Talent validator with real DB2 edges (6,409 TraitEdge.csv)
- APL optimizer with 4 mutation operators + multi-stage filtering
- Talent hill-climbing local search
- req_points gate bug fix (purchased-only counting)

### Data Extraction & Auditing (Phases 1-4)
- Wowhead extraction (33 specs × 5 pages)
- 3-way upstream APL comparison (198 sims, 10k iter)
- Profile updates (gear, consumables, talents)
- Wowhead build comparison (262 builds, 29/33 improved)

---

## Known Issues

### Open

- **Darkmoon Deck sigil stacking** — Issue #81, blocked on beta/live data.
  See `docs/internal/darkmoon_investigation.md`.
- **Priest Shadowfiend effectN(4)** — OOB on 3-effect spell. Returns 0 for
  Holy/Disc mana regen. Low impact (healer sim only, not DPS).
- **Wowhead data stale** — extracted on Build 66384, current is 66709.
- **Multi-target scaling unverified** — need 1/3/5/10 target sweeps.
- **Proc rates unverified** — need JSON execute count vs RPPM/ICD comparison.

### Resolved (v0.2)

- Rogue Sub 4pc permanent Shadow Blades — fixed (from_seconds on ms)
- Shaman Storm Elemental effectN(5) OOB — fixed (effectN(4))
- Priest Shadow 2pc swapped indices — fixed
- Monk WW 4pc CDR double-negation — fixed
- Phoenix Torque wrong indices — fixed
- Shaman Enh 2pc wrong semantic index — fixed

### Resolved (v0.1 and earlier)

- req_points gate validator bug — fixed 2026-03-30
- Hero tree spec filtering — fixed 2026-03-29
- 4 broken talent strings — fixed 2026-03-29
- DK Blood HAC crash — fixed (player_t::interrupt race condition)
- Guardian Druid APL — full rewrite, 3k → 10.6k DPS (2026-03-27)
- 5 missing tier sets — fixed 2026-03-24
- 8 APL desync issues — fixed 2026-03-25

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — mission, workflow, domain knowledge, pitfalls |
| `FORK_VS_UPSTREAM_REVIEW.md` | Fork vs upstream divergence analysis + post-mortem |
| `APL_optimization.md` | APL syntax reference, rules, common mistakes |
| `optimization_action_plan.md` | Optimization design — talent local search + APL mutation |
| `OPTIMIZATION_HOWTO.md` | Step-by-step manual guide — exact commands to optimize any spec |
| `project_structure.md` | Codebase navigation — maps task types to source files |
| `docs/internal/engine_audit_2026-03-31.md` | Detailed DBC audit findings log |
| `docs/internal/behavioral_audit_2026-03-31.md` | Tier set tooltip vs code comparison |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket stacking investigation (Issue #81) |
| `docs/archive/` | Historical audit data, APL diff reports |
