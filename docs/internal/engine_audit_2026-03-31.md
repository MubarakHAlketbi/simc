# Engine C++ Audit — 2026-03-31

Build: 12.0.1.66709 Live (post-upstream-merge)
Method: Verified all OUR C++ additions against wago.tools DBC and bundled sc_spell_data.inc

## BUGS FOUND

### BUG 1: Priest Shadow 2pc — WRONG EFFECT INDEXES (HIGH IMPACT)

File: `engine/class_modules/priest/sc_priest_shadow.cpp`
Spell: 1264854 (Priest Shadow 12.0 Class Set 2pc)

DBC effect order (bundled sc_spell_data.inc confirms):
```
effectN(1) = 1276461, index 0: Aura 107 (ADD_FLAT_MODIFIER), base=-500, MiscValue=14  → COST REDUCTION
effectN(2) = 1281990, index 1: Aura 108 (ADD_PCT_MODIFIER), base=10, MiscValue=0      → DAMAGE +10%
effectN(3) = 1281991, index 2: Aura 108 (ADD_PCT_MODIFIER), base=10, MiscValue=22     → PERIOD +10%
```

Our code (WRONG):
- Line 956: `m *= 1.0 + effectN(1).percent()` → reads -500/100 = **-5.0** → `m *= -4.0` (DESTROYS DAMAGE)
- Line 866: `base_costs += effectN(2).resource()` → reads damage modifier, not resource

Sim confirms: Shadow Word: Madness has **86 executes, 0 total damage**.

Fix needed:
- Line 956: change `effectN(1)` to `effectN(2)` for the +10% damage modifier
- Line 866: change `effectN(2)` to `effectN(1)` for the -500 cost reduction
- Consider implementing effectN(3) for +10% tick period

### BUG 2: Thalassian Phoenix Torque — WRONG EFFECT INDEXES (MEDIUM IMPACT)

File: `engine/player/unique_gear_midnight.cpp`
Spell: 1251815 (Thalassian Phoenix Torque)

DBC effect order (bundled sc_spell_data.inc confirms):
```
effectN(1) = 1256647, index 0: Aura 4 (DUMMY), coeff=0            → NOTHING
effectN(2) = 1256648, index 1: Effect 3, base=1                    → GEM MULTIPLIER
effectN(3) = 1260592, index 2: Aura 4, coeff=2.497, ScClass=-8    → DAMAGE VALUE
effectN(4) = 1260596, index 3: Aura 4, coeff=3.745, ScClass=-8    → HEAL VALUE
```

Our code (WRONG):
- Line 809: `effectN(1).average()` for damage → coeff=0 → **0 DAMAGE**
- Line 816: `effectN(2).average()` for heal → base=1, not a heal value

Fix needed:
- Line 809: change `effectN(1)` to `effectN(3)` for damage (coeff 2.497)
- Line 816: change `effectN(2)` to `effectN(4)` for heal (coeff 3.745)

### BUG 3: Duplicate Registration (LOW IMPACT)

File: `engine/player/unique_gear_midnight.cpp`
Spell: 1258275 registered twice as DISABLED_EFFECT (lines 4187 and 4192).
No functional impact but indicates copy-paste error.

## VERIFIED CORRECT

### Tier Sets (15 checked)
- DK Blood 2pc/4pc: MATCH
- DK Unholy 2pc/4pc: MATCH
- DH Havoc 2pc/4pc: MATCH (p()→dh() rename applied)
- DH Vengeance 2pc/4pc: MATCH
- Druid Guardian 2pc/4pc: MATCH
- Monk WW 2pc/4pc: MATCH
- Paladin Ret 4pc: MATCH
- Priest Shadow 4pc: MATCH
- Shaman Elemental 2pc/4pc: MATCH

### Trinkets (40+ sampled from unique_gear_midnight.cpp)
- Heart of the Wind, Kroluk's Warbanner, Vessel of Souls: MATCH
- Potion of Zealotry, Void Execution Mandate: MATCH
- Shadow of the Empyrean Requiem, Resonant Bellowstone: MATCH
- Ever-collapsing Void Fissure, Lightspire Core: MATCH
- Solarflare Prism, Undreamt God's Oozing Vestige: MATCH
- Crucible of Erratic Energies, Lost Idol of Hash'ey: MATCH
- Loa Worshiper's Band, Voidreaper's Libram: MATCH
- Crawling Plague, Mindpiercer's Sigil: MATCH
- Emberwing Feather, Locus-Walker's Ribbon: MATCH
- Gaze of the Alnseer, Glorious Crusader's Keepsake: MATCH
- Plume of Beloren, Magister's Alchemist Stone: MATCH
- Food coefficient spell (1219179): MATCH
- Umbric's Channeling Focus, Repurposed Volatile Manacell: MATCH
