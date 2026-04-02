# SimulationCraft — Midnight Expansion (MID1) Progress

Last updated: 2026-04-02 — **v0.5.2 Full optimization pass complete**

**Game build: 12.0.1.66709 Live** — we target Live only, ignore 12.0.5.x PTR.

## Status

| Metric | Value |
|--------|-------|
| Release | **v0.4** (2026-03-31) |
| Profiles | 89/89 PASS (compile + 1-iter sim + talent validation) |
| Talent validation | 89/89 PASS (budget, prereqs, req_points gates) |
| Baselines | 126/126 (pre-v0.3 — need re-baseline after Layer 2+3 runs) |
| Tier sets | 33/33 initial audit done; 5 NEW bugs found 2026-04-01 via reference comparison |
| Engine audit | **v0.4.1** — 5 additional bugs found+fixed via reference profile comparison |
| Apex talents | 33/33 implemented (3 spell IDs each) |
| APL Layer 1 | **DONE** — 33/33 specs, blind mutation optimizer |
| APL Layer 2 | **IMPLEMENTED** — signal-guided optimizer (APS, buff waste, resource) |
| APL Layer 3 | **IMPLEMENTED** — LLM semantic advisor (missing consumers, synergies) |
| Optimization | 33/33 specs talent + APL Layer 1 done; Layer 2+3 ready to run |
| Tank HAC profiles | 6/6 tanks have HAC profiles |
| Tooling | 26 scripts, ~7,700 lines |
| Upstream sync | **SYNCED** — Build 66709, 24 upstream commits merged 2026-04-01 (38ee898 PTR skipped) |
| Build | gcc-14 clean, cmake -DSC_NO_NETWORKING=ON |

---

## What's Next

| # | Task | Type | Status |
|---|------|------|--------|
| ~~1~~ | ~~Upstream sync~~ — merged 359 commits, Build 66709 | Engine | **DONE** |
| ~~2~~ | ~~Re-baseline all specs~~ | Testing | **DONE** |
| ~~3~~ | ~~Engine correctness audit~~ — 6 bugs fixed | Testing | **DONE (v0.2)** |
| ~~7~~ | ~~Talent + APL Layer 1 optimization~~ — 33/33 specs | Optimization | **DONE (v0.3)** |
| ~~7b~~ | ~~APL Layer 2 implementation~~ — signal-guided optimizer | Optimization | **DONE (v0.4)** |
| ~~7c~~ | ~~APL Layer 3 implementation~~ — LLM advisor | Optimization | **DONE (v0.4)** |
|| ~~7d~~ | ~~Run Layer 2+3 on all 33 specs~~ — all complete, gains committed | Optimization | **DONE (v0.5)** |
|| ~~7e~~ | ~~Re-run talent optimizer~~ — 9 specs, gains committed | Optimization | **DONE (v0.5)** |
| ~~4~~ | ~~Re-extract Wowhead data~~ — rotation.md only (33 specs, build 66709) | Data | **DONE** |
| ~~5~~ | ~~Multi-target sweeps~~ — 56 specs × 4 targets = 224 sims, no anomalies | Testing | **DONE (v0.5)** |
| 6 | Proc rate validation — compare JSON execute counts vs RPPM/ICD | Testing | PENDING |
| 8 | Trinket combinatorics | Optimization | PENDING |
| 9 | Final docs + cleanup + contribute fixes back upstream | Maintenance | PENDING |

---

## v0.4 — Signal-Guided + LLM APL Optimizer (2026-03-31)

### What Was Built

Three-layer APL optimization pipeline — each layer builds on the previous:

**Layer 1 (DONE, v0.3)** — Blind mutation optimizer
- ~200 random candidates per spec (adjacent swap, threshold sweep, promote, route)
- Multi-stage funnel: 300 → 3k → 10k iterations
- Script: `scripts/apl_optimizer.py`

**Layer 2 (NEW, v0.4)** — Signal-guided optimizer
- Parses sim JSON2 output for per-ability APS, buff expire rates, resource flow
- 4 signal types:
  - **APS Inversion** — high-APS ability outranked by lower-APS (non-adjacent promotes)
  - **Buff Waste** — proc buff expires >40% of time; generates consumer promote + buff gate
  - **Resource Overcap** — resource wasted >8%; lowers spender threshold, adds emergency dump
  - **Interval Gap** — high-value ability cast less often than its CD allows
- ~20-40 targeted candidates per spec vs 200 random — 5-10x more efficient
- Key advantage: can ADD new APL constructs (buff gates, emergency dumps)
- Script: `scripts/signal_apl_optimizer.py`

**Layer 3 (NEW, v0.4)** — LLM semantic advisor
- Bridges the gap no formula can cross: "buff expires 96% of time but has no APL consumer"
- Programmatic system can't generate the fix without knowing *which action* consumes the buff
- LLM receives: ability APS table, buff waste signals, resource flow, full APL,
  Wowhead rotation mechanics context
- Strict 4-step protocol: buff waste → APS order → resource → missing synergies
- Outputs structured CHANGE blocks; ALL validated via DPS sim before acceptance
- Supports OpenAI API, Anthropic API, or Hermes internal model
- Script: `scripts/lib/llm_apl_advisor.py`

### New Files

| File | Lines | What |
|------|-------|------|
| `scripts/lib/sim_runner.py` | +120 | AbilityStats, BuffStats, ResourceStats added to SimResult |
| `scripts/lib/apl_parser.py` | +50 | insert_action, replace_condition, append_or_condition, make_action |
| `scripts/lib/apl_signal_extractor.py` | 340 | 4 signal types + combination + ranking |
| `scripts/lib/apl_signal_mutations.py` | 280 | S-M1 (non-adjacent promote), S-M2 (buff gate), S-M3 (resource dump), S-M4 (interval) |
| `scripts/lib/llm_apl_advisor.py` | 450 | Prompt builder, LLM caller, CHANGE parser, APL converter |
| `scripts/signal_apl_optimizer.py` | 320 | Layer 2+3 unified runner |

### Smoke Test Results (warlock_affliction)

Signal extraction found 10 signals on a single sim run:
- `unstable_affliction` APS inversion in 6 sub-lists (priority 0.84) — top spender appearing after DoTs
- 5 LLM-needed buff waste signals: `alnsight`, `arcanoweave_insight`, `arcanoweave_insight_ally`,
  `emberwing_heatwave`, `might_of_the_void` — trinket/gear proc buffs with no APL consumer
- 40 targeted mutations generated (vs 200 blind)

The 5 LLM-needed signals are exactly the kind Layer 1+2 cannot fix: the programmatic system
detects the expire rate but cannot determine which action to add to consume the buff — that
requires semantic knowledge of the trinket proc mechanics.

### Usage

```bash
# Single spec, both fight styles, Layer 2 only
python3 scripts/signal_apl_optimizer.py warlock_affliction

# Single spec, single style, with LLM
python3 scripts/signal_apl_optimizer.py warlock_affliction --fight-style HecticAddCleave --llm

# Signal-only (no blind mutations)
python3 scripts/signal_apl_optimizer.py warlock_affliction --no-blind

# All 33 specs with LLM (~4-8 hours)
python3 scripts/signal_apl_optimizer.py --all --llm
```

---

## v0.3 — Full Optimization Pass (2026-03-31)

All 33 specs optimized (Layer 1: talent local search + blind APL mutation).
Each spec produces two profiles: PW-optimized (`.simc`) and HAC-optimized (`_HAC.simc`).
Tank specs now include HAC profiles (tanks-skip-HAC restriction removed).

### Layer 1 Results

| Spec | PW DPS | HAC DPS | Talent | APL Gains |
|------|-------:|--------:|--------|-----------|
| warrior_arms | 82,060 | 202,711 | -/Y | HAC +1.97% |
| warrior_fury | 92,619 | 217,892 | Y/Y | PW +0.59% |
| warrior_protection | 75,532 | 136,209 | Y/Y | — |
| paladin_protection | 59,962 | 113,834 | Y/Y | — |
| paladin_retribution | 114,026 | 178,327 | Y/Y | — |
| hunter_bm | 97,673 | 204,410 | Y/Y | — |
| hunter_mm | 108,100 | 182,240 | Y/Y | — |
| hunter_survival | 104,176 | 185,493 | Y/Y | HAC +0.56% |
| rogue_assassination | 102,775 | 187,520 | Y/Y | HAC +1.39% |
| rogue_outlaw | 102,657 | 214,926 | Y/Y | HAC +0.39% |
| rogue_subtlety | 115,329 | 225,134 | Y/Y | — |
| priest_shadow | 104,818 | 154,134 | Y/Y | HAC +1.64% |
| dk_blood | 46,588 | 97,667 | -/Y | HAC +1.12% |
| dk_frost | 110,960 | 188,079 | -/Y | — |
| dk_unholy | 126,982 | 272,428 | -/Y | — |
| shaman_elemental | 126,334 | 240,113 | Y/Y | — |
| shaman_enhancement | 91,512 | 174,899 | Y/Y | HAC +1.63% |
| mage_arcane | 100,952 | 217,673 | Y/Y | — |
| mage_fire | 101,877 | 209,626 | Y/Y | — |
| mage_frost | 112,278 | 206,929 | Y/Y | — |
| warlock_affliction | 94,414 | 155,809 | Y/Y | HAC +3.63% |
| warlock_demonology | 97,205 | 525,527 | Y/Y | — |
| warlock_destruction | 94,548 | 162,645 | Y/Y | HAC +3.50% |
| monk_brewmaster | 61,918 | 119,969 | Y/Y | PW +0.72% |
| monk_windwalker | 120,841 | 211,599 | Y/Y | HAC +0.02% |
| druid_balance | 76,039 | 117,750 | Y/Y | — |
| druid_feral | 106,929 | 199,563 | Y/Y | HAC +1.20% |
| druid_guardian | 79,222 | 139,526 | Y/Y | — |
| dh_havoc | 121,588 | 206,497 | -/Y | — |
| dh_vengeance | 56,115 | 94,589 | Y/Y | PW +0.95%, HAC +0.33% |
| dh_devourer | 103,645 | 179,714 | -/Y | HAC +0.09% |
| evoker_devastation | 108,492 | 176,264 | Y/Y | HAC +6.32% |
| evoker_augmentation | 68,519 | 114,737 | Y/Y | PW +0.29% |

Talent: Y = new optimal build found, - = existing already optimal.
12/33 specs had APL improvements. Notable: evoker_devastation HAC +6.32%,
warlock_affliction HAC +3.63%, warlock_destruction HAC +3.50%.

---

## v0.2 — Engine Correctness Audit (2026-03-31)

### Bugs Found and Fixed

| # | Class | Bug | Root Cause | DPS Impact |
|---|-------|-----|-----------|------------|
| 1 | Priest Shadow | 2pc SW:Madness 0 damage | Swapped effectN indices | **+25.4%** |
| 2 | Rogue Sub | 4pc permanent Shadow Blades | from_seconds on ms value | **-19.6%** |
| 3 | Monk WW | 4pc CDR negated | Manual adjust cancelled auto-apply | **+1.2%** |
| 4 | Shaman Ele | Storm Ele Unity TA = 0 | effectN(5) OOB (should be 4) | ~0% |
| 5 | Trinket | Phoenix Torque wrong indices | effectN index swap | Minor |
| 6 | Shaman Enh | 2pc wrong effectN | Read effectN(2) not effectN(1) | None |

---

## Completed Work

### v0.4 — Signal-Guided + LLM APL Optimizer (2026-03-31)
- Layer 2: signal extraction (APS inversion, buff waste, resource overcap, interval gap)
- Layer 3: LLM semantic advisor (missing buff consumers, mechanic synergies)
- 6 new files, ~1,700 lines; integrated with existing multi-stage eval pipeline
- Smoke tested: 10 signals detected on warlock_affliction, 40 mutations generated

### v0.3 — Full Optimization Pass (2026-03-31)
- 33/33 specs optimized: talent local search + APL Layer 1
- 89/89 profiles pass validation (66 + 23 new HAC profiles)
- Tank specs all have HAC profiles (tanks-skip-HAC removed)
- optimize_all_specs.py orchestration script

### v0.2 — Engine Correctness Audit (2026-03-31)
- Full DBC behavioral audit across all 13 class modules
- 6 bugs found and fixed (3 significant DPS impact)
- Upstream merge: 359 commits, 44 conflict resolution

### v0.1 — Optimization System (2026-03-30)
- Talent validator with real DB2 edges (6,409 TraitEdge.csv)
- APL optimizer with 4 mutation operators + multi-stage filtering
- Talent hill-climbing local search; req_points gate bug fix

---

## Known Issues

### Open

- **Darkmoon Deck sigil stacking** — Issue #81, blocked on live data.
  See `docs/internal/darkmoon_investigation.md`.
- **Priest Shadowfiend effectN(4)** — OOB on 3-effect spell. Healer sim only, low impact.
- **Multi-target scaling unverified** — need 1/3/5/10 target sweeps.
- **Proc rates unverified** — need JSON execute count vs RPPM/ICD comparison.
- **Baselines stale** — 126 baselines predate v0.3 talent/APL changes.
- **Layer 2+3 not yet run on all specs** — first run completed on warlock_affliction (2026-04-01).
  PW: LLM produced 2 high-confidence CHANGE blocks, neither survived Stage 2. HAC: LLM call
  intermittently fails (openrouter/free rate-limited on second call). No improvements found —
  warlock_affliction APL is at signal optimum. Layer 1 gains (+3.63% HAC) came from talent
  optimization, not APL structure. Ready to run --all once LLM reliability is confirmed.
- **Wowhead rotation validator false positives** — 6 specs produce "MISSING HERO TALENTS"
  warnings that are false positives. Cause: build-variant button names ('Templar RG',
  'Farseer AoE') used as content keys don't match HERO_TALENTS slug list. Content is
  complete. Affected: monk/brewmaster, monk/windwalker, dk/unholy, druid/guardian,
  paladin/retribution, mage/arcane. Safe to ignore.
- **DANGER: update_talents_from_extracted.py must NOT be run post-v0.3.** It overwrites
  `talents=` lines with Wowhead's Build 1 — which our optimizer already beats for 27/33
  specs. This script was for project initialization only. Running it now = silent regression.

### Resolved (v0.4)
- APL Layer 2+3 implemented and smoke tested

### Resolved (v0.3)
- tanks-skip-HAC convention removed — all 6 tank specs have HAC profiles

### Resolved (v0.2)
- Rogue Sub 4pc permanent Shadow Blades — fixed
- Shaman Storm Elemental effectN(5) OOB — fixed
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

---

## Reference Files

| File | What |
|------|------|
| `AGENTS.md` | Agent guide — mission, workflow, domain knowledge, pitfalls |
| `APL_optimization.md` | APL syntax reference + 3-layer optimization pipeline |
| `optimization_action_plan.md` | Optimization architecture + success criteria |
| `OPTIMIZATION_HOWTO.md` | Step-by-step manual guide |
| `project_structure.md` | Codebase navigation |
| `docs/internal/signal_guided_apl_design.md` | Layer 2 signal system design |
| `docs/internal/llm_apl_advisor_design.md` | Layer 3 LLM advisor design |
| `docs/internal/behavioral_audit_checklist.md` | **USE FOR ALL C++ WORK** — 5-step per-modifier protocol (bounds, accessor, semantic, double-apply, tier delta) |
| `docs/internal/bug_postmortem_2026-04-01.md` | Why 5 bugs passed prior audits + which checklist step catches each |
| `docs/internal/engine_audit_2026-03-31.md` | DBC audit findings (v0.2) |
| `docs/internal/behavioral_audit_2026-03-31.md` | Tier set behavioral audit (v0.2, some entries superseded by 2026-04-01 fixes) |
| `docs/internal/darkmoon_investigation.md` | Darkmoon trinket investigation (Issue #81) |
| `docs/analysis/reference_comparison_findings.md` | Reference profile comparison findings — bugs, talent failures, NYI gaps |
| `FORK_VS_UPSTREAM_REVIEW.md` | Fork vs upstream post-mortem |
| `docs/archive/` | Historical audit data, APL diff reports |
