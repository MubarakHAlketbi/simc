# Reference Profile Comparison — simulationcraft.org vs Ours

Source: https://simulationcraft.org/reports/MID1_Raid.html  
Their build: 86712bd5dd (12.0.1.66709, hotfix 2026-03-31)  
Our build: midnight branch | Compared: 2026-04-01  
Method: All sims use OUR gear + OUR simc binary. Only talents/APL substituted.

## Quick Legend
- **dps_ours**: our profile on our engine
- **dps_ref_T**: our gear + their talent string
- **dps_ref_A**: our gear + their APL
- **dps_ref_TA**: our gear + their talents + their APL
- **reported**: DPS from simulationcraft.org (different engine/gear)
- **engine_div**: (dps_ours - reported) / reported — detects engine divergence

## Summary Table

| Spec | ours | ref_T | ref_A | ref_TA | reported | engine_div | winner |
|------|------|-------|-------|--------|----------|------------|--------|
| death_knight/blood_deathbringer | 52,924 | 53,464 (+1.02%) | 53,175 (+0.47%) | 53,388 (+0.88%) | 54,717 | -3.3% | **ref_T** |
| death_knight/blood_sanlayn | 46,578 | 46,344 (-0.50%) | 47,085 (+1.09%) | 46,868 (+0.62%) | 59,890 | -22.2% | **ref_A** |
| death_knight/frost | 110,844 | 111,021 (+0.16%) | 110,833 (-0.01%) | 110,937 (+0.08%) | 116,066 | -4.5% | **ref_T** |
| death_knight/frost_rider | 104,212 | 107,583 (+3.24%) | 104,209 (-0.00%) | 107,487 (+3.14%) | 112,231 | -7.1% | **ref_T** |
| death_knight/unholy_rider | 126,764 | 130,500 (+2.95%) | 126,455 (-0.24%) | 130,525 (+2.97%) | 130,435 | -2.8% | **ref_TA** |
| death_knight/unholy_sanlayn | 130,320 | 125,023 (-4.06%) | 130,552 (+0.18%) | 125,114 (-3.99%) | 124,990 | +4.3% | **ref_A** |
| demon_hunter/devourer_annihilator | 103,578 | 103,669 (+0.09%) | 108,272 (+4.53%) | 108,105 (+4.37%) | 108,625 | -4.6% | **ref_A** |
| demon_hunter/devourer_void-scarred | 98,986 | 107,348 (+8.45%) | 102,792 (+3.84%) | 109,954 (+11.08%) | 109,837 | -9.9% | **ref_TA** |
| demon_hunter/havoc_fel-scarred | 121,441 | 121,121 (-0.26%) | - (-) | - (-) | 114,804 | +5.8% | **ours** |
| demon_hunter/vengeance_aldrachi_reaver | 56,006 | 62,029 (+10.75%) | 56,076 (+0.13%) | 62,024 (+10.74%) | 62,207 | -10.0% | **ref_T** |
| demon_hunter/vengeance_annihilator | 56,646 | 68,519 (+20.96%) | 56,113 (-0.94%) | 68,599 (+21.10%) | 68,737 | -17.6% | **ref_TA** |
| druid/feral_wildstalker | 106,789 | 111,640 (+4.54%) | 106,992 (+0.19%) | 111,729 (+4.63%) | 120,320 | -11.2% | **ref_TA** |
| druid/guardian | 79,143 | 80,102 (+1.21%) | 79,239 (+0.12%) | 80,036 (+1.13%) | 88,270 | -10.3% | **ref_T** |
| evoker/devastation_fs | 107,378 | 103,496 (-3.62%) | 108,637 (+1.17%) | 103,511 (-3.60%) | 104,551 | +2.7% | **ref_A** |
| evoker/devastation_sc | 108,500 | 108,437 (-0.06%) | 108,789 (+0.27%) | 108,731 (+0.21%) | 109,070 | -0.5% | **ref_A** |
| hunter/beast_mastery | 97,614 | 108,813 (+11.47%) | 97,672 (+0.06%) | 108,894 (+11.56%) | 113,980 | -14.4% | **ref_TA** |
| hunter/marksmanship | 108,060 | 108,741 (+0.63%) | 108,032 (-0.03%) | 108,841 (+0.72%) | 108,733 | -0.6% | **ref_TA** |
| hunter/survival_pl_dw | 106,167 | 106,171 (+0.00%) | 106,172 (+0.01%) | 106,373 (+0.19%) | 110,339 | -3.8% | **ref_TA** |
| hunter/survival_sentinel_2h | 104,148 | 104,552 (+0.39%) | 104,062 (-0.08%) | 104,522 (+0.36%) | 108,605 | -4.1% | **ref_T** |
| mage/arcane_spellslinger | 100,891 | 101,653 (+0.76%) | 100,881 (-0.01%) | 101,592 (+0.70%) | 101,622 | -0.7% | **ref_T** |
| mage/arcane_sunfury | 101,196 | 92,290 (-8.80%) | 101,117 (-0.08%) | 92,213 (-8.88%) | 96,253 | +5.1% | **ours** |
| mage/fire_frostfire | 101,891 | 105,103 (+3.15%) | 101,777 (-0.11%) | 105,117 (+3.17%) | 105,174 | -3.1% | **ref_TA** |
| mage/fire_sunfury | 101,839 | 102,411 (+0.56%) | 101,825 (-0.01%) | 102,452 (+0.60%) | 102,438 | -0.6% | **ref_TA** |
| mage/frost_frostfire | 94,184 | 94,293 (+0.12%) | 94,176 (-0.01%) | 94,234 (+0.05%) | 95,610 | -1.5% | **ref_T** |
| mage/frost_spellslinger | 112,143 | 112,152 (+0.01%) | 112,250 (+0.10%) | 112,084 (-0.05%) | 113,638 | -1.3% | **ref_A** |
| monk/brewmaster | 62,399 | 56,542 (-9.39%) | 64,469 (+3.32%) | 72,125 (+15.59%) | 72,321 | -13.7% | **ref_TA** |
| monk/windwalker | 120,876 | 121,946 (+0.88%) | 120,902 (+0.02%) | 121,757 (+0.73%) | 114,446 | +5.6% | **ref_T** |
| monk/windwalker_conduit | 120,249 | 117,550 (-2.24%) | 120,233 (-0.01%) | 117,447 (-2.33%) | 109,083 | +10.2% | **ours** |
| paladin/protection | 59,946 | 63,095 (+5.25%) | 59,885 (-0.10%) | 63,084 (+5.23%) | 69,620 | -13.9% | **ref_T** |
| paladin/protection_lightsmith | 42,967 | 49,359 (+14.88%) | 42,972 (+0.01%) | 49,292 (+14.72%) | 55,406 | -22.4% | **ref_T** |
| paladin/retribution | 113,996 | 116,131 (+1.87%) | 115,412 (+1.24%) | 117,741 (+3.29%) | 112,984 | +0.9% | **ref_TA** |
| paladin/retribution_herald | 118,498 | 110,462 (-6.78%) | 118,351 (-0.12%) | 110,296 (-6.92%) | 104,924 | +12.9% | **ours** |
| priest/shadow_archon | 106,967 | 107,030 (+0.06%) | 106,675 (-0.27%) | 106,653 (-0.29%) | 107,607 | -0.6% | **ref_T** |
| priest/shadow_voidweaver | 104,780 | 103,440 (-1.28%) | 104,617 (-0.16%) | 103,006 (-1.69%) | 105,184 | -0.4% | **ours** |
| rogue/assassination | 102,747 | 101,634 (-1.08%) | 103,831 (+1.05%) | 103,340 (+0.58%) | 104,072 | -1.3% | **ref_A** |
| rogue/outlaw_fatebound | 102,593 | 104,070 (+1.44%) | 102,494 (-0.10%) | 104,109 (+1.48%) | 107,724 | -4.8% | **ref_TA** |
| rogue/outlaw_trickster | 98,419 | 98,339 (-0.08%) | 98,409 (-0.01%) | 98,349 (-0.07%) | 102,142 | -3.6% | **ours** |
| rogue/subtlety | 115,301 | 113,770 (-1.33%) | 117,548 (+1.95%) | 117,832 (+2.20%) | 109,256 | +5.5% | **ref_TA** |
| shaman/elemental_stormbringer | 126,294 | 125,870 (-0.34%) | 126,266 (-0.02%) | 125,863 (-0.34%) | 124,290 | +1.6% | **ours** |
| shaman/enhancement_stormbringer | 74,200 | 79,375 (+6.97%) | 81,061 (+9.25%) | 83,420 (+12.43%) | 91,989 | -19.3% | **ref_TA** |
| shaman/enhancement_totemic | 91,478 | 92,189 (+0.78%) | 91,586 (+0.12%) | 92,102 (+0.68%) | 101,146 | -9.6% | **ref_T** |
| warlock/affliction_hellcaller | 84,563 | - (-) | 99,130 (+17.23%) | - (-) | 99,300 | -14.8% | **ref_A** |
| warlock/affliction_soul_harvester | 94,536 | 92,088 (-2.59%) | 102,795 (+8.74%) | 102,827 (+8.77%) | 104,004 | -9.1% | **ref_TA** |
| warlock/demonology_soul_harvester | 91,072 | 99,130 (+8.85%) | 93,535 (+2.71%) | 100,042 (+9.85%) | 120,997 | -24.7% | **ref_TA** |
| warlock/destruction_diabolist | 100,611 | - (-) | 100,570 (-0.04%) | - (-) | 108,723 | -7.5% | **ours** |
| warlock/destruction_hellcaller | 94,553 | 101,494 (+7.34%) | 94,559 (+0.01%) | 101,505 (+7.35%) | 109,082 | -13.3% | **ref_TA** |
| warrior/protection | 75,570 | 74,866 (-0.93%) | 75,599 (+0.04%) | 74,792 (-1.03%) | 77,889 | -3.0% | **ref_A** |

## Engine Divergence Analysis

Specs where our engine DPS differs from reported by more than ±5%:

| Spec | our_engine_DPS | reported_DPS | delta |
|------|---------------|-------------|-------|
| warlock/demonology_soul_harvester | 91,072 | 120,997 | -24.7% |
| paladin/protection_lightsmith | 42,967 | 55,406 | -22.4% |
| death_knight/blood_sanlayn | 46,578 | 59,890 | -22.2% |
| shaman/enhancement_stormbringer | 74,200 | 91,989 | -19.3% |
| demon_hunter/vengeance_annihilator | 56,646 | 68,737 | -17.6% |
| warlock/affliction_hellcaller | 84,563 | 99,300 | -14.8% |
| hunter/beast_mastery | 97,614 | 113,980 | -14.4% |
| paladin/protection | 59,946 | 69,620 | -13.9% |
| monk/brewmaster | 62,399 | 72,321 | -13.7% |
| warlock/destruction_hellcaller | 94,553 | 109,082 | -13.3% |
| paladin/retribution_herald | 118,498 | 104,924 | +12.9% |
| druid/feral_wildstalker | 106,789 | 120,320 | -11.2% |
| druid/guardian | 79,143 | 88,270 | -10.3% |
| monk/windwalker_conduit | 120,249 | 109,083 | +10.2% |
| demon_hunter/vengeance_aldrachi_reaver | 56,006 | 62,207 | -10.0% |
| demon_hunter/devourer_void-scarred | 98,986 | 109,837 | -9.9% |
| shaman/enhancement_totemic | 91,478 | 101,146 | -9.6% |
| warlock/affliction_soul_harvester | 94,536 | 104,004 | -9.1% |
| warlock/destruction_diabolist | 100,611 | 108,723 | -7.5% |
| death_knight/frost_rider | 104,212 | 112,231 | -7.1% |
| demon_hunter/havoc_fel-scarred | 121,441 | 114,804 | +5.8% |
| monk/windwalker | 120,876 | 114,446 | +5.6% |
| rogue/subtlety | 115,301 | 109,256 | +5.5% |
| mage/arcane_sunfury | 101,196 | 96,253 | +5.1% |

## Talent Differences

Specs where reference talent string differs from ours:

| Spec | Our Talent String | Ref Talent String | DPS Impact |
|------|------------------|-------------------|------------|
| death_knight/blood_deathbringer | `CoPAAAAAAAAAAAAAAAAAAAAAAwYWGzMmxMjhZZmZ` | `CoPAAAAAAAAAAAAAAAAAAAAAAwYWGzMmZmZmhZbm` | +1.02% |
| death_knight/blood_sanlayn | `CoPAAAAAAAAAAAAAAAAAAAAAAwYWmZmxMmZmhZZm` | `CoPAAAAAAAAAAAAAAAAAAAAAAwYWGzMmZmZmhZbm` | -0.50% |
| death_knight/frost | `CsPAAAAAAAAAAAAAAAAAAAAAAMDwMzMzMDY2mZmZ` | `CsPAAAAAAAAAAAAAAAAAAAAAAMDwMjZMmZY2mZmZ` | +0.16% |
| death_knight/frost_rider | `CsPAAAAAAAAAAAAAAAAAAAAAAMDYmZMzMDDz2MzM` | `CsPAAAAAAAAAAAAAAAAAAAAAAMDwMjZMmZY2mZmZ` | +3.24% |
| death_knight/unholy_rider | `CwPAAAAAAAAAAAAAAAAAAAAAAAYmhZMzYGz2MmZa` | `CwPAAAAAAAAAAAAAAAAAAAAAAAwMjZMDDz2MzMTz` | +2.95% |
| death_knight/unholy_sanlayn | `CwPAAAAAAAAAAAAAAAAAAAAAAAwMjZMDDz2MzMTz` | `CwPAAAAAAAAAAAAAAAAAAAAAAAwMjZMDDz2MzMTz` | -4.06% |
| demon_hunter/devourer_annihilator | `CgcBAAAAAAAAAAAAAAAAAAAAAAA2mxMzMzwMGzMA` | `CgcBAAAAAAAAAAAAAAAAAAAAAAA2MmZmZmZmBzMA` | +0.09% |
| demon_hunter/devourer_void-scarred | `CgcBAAAAAAAAAAAAAAAAAAAAAAA2MmZmxMzMGzMA` | `CgcBAAAAAAAAAAAAAAAAAAAAAAA2MmZmZmZmBzMA` | +8.45% |
| demon_hunter/havoc_fel-scarred | `CEkAAAAAAAAAAAAAAAAAAAAAAYgZmZ2mxMzMmZmM` | `CEkAAAAAAAAAAAAAAAAAAAAAAYgZmZMjZmZmhJjZ` | -0.26% |
| demon_hunter/vengeance_aldrachi_reaver | `CUkAAAAAAAAAAAAAAAAAAAAAAAAYMzMjZmZkZmZY` | `CUkAAAAAAAAAAAAAAAAAAAAAAAAYMzMjhZkZmZGD` | +10.75% |
| demon_hunter/vengeance_annihilator | `CUkAAAAAAAAAAAAAAAAAAAAAAAAYMzMjZmZkZmZY` | `CUkAAAAAAAAAAAAAAAAAAAAAAAAYMzMjhZkZmZGD` | +20.96% |
| druid/feral_wildstalker | `CcGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjZwMzMjx` | `CcGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjZwMzMzM` | +4.54% |
| druid/guardian | `CgGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZm` | `CgGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZm` | +1.21% |
| evoker/devastation_fs | `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMD` | `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgZmZ` | -3.62% |
| evoker/devastation_sc | `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMD` | `CsbBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzMD` | -0.06% |
| hunter/beast_mastery | `C0PAAAAAAAAAAAAAAAAAAAAAAAMmxwCsBzwQDbAA` | `C0PAAAAAAAAAAAAAAAAAAAAAAAMmxwCsBzwQDbAA` | +11.47% |
| hunter/marksmanship | `C4PAAAAAAAAAAAAAAAAAAAAAAwCMwMGNWGAzgNAA` | `C4PAAAAAAAAAAAAAAAAAAAAAAwCMwMGNWGQmBbAA` | +0.63% |
| hunter/survival_pl_dw | `C8PAAAAAAAAAAAAAAAAAAAAAAMgxMG2ILwMM0gFj` | `C8PAAAAAAAAAAAAAAAAAAAAAAMgxMGWILwMM0gFj` | +0.00% |
| hunter/survival_sentinel_2h | `C8PAAAAAAAAAAAAAAAAAAAAAAMWgBmxoxyAYmgNz` | `C8PAAAAAAAAAAAAAAAAAAAAAAMWgBmxoxyAYmgNj` | +0.39% |
| mage/arcane_spellslinger | `C4DAAAAAAAAAAAAAAAAAAAAAAMzwYxMzsYZmZoZm` | `C4DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMzQzMz` | +0.76% |
| mage/arcane_sunfury | `C4DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMzQzMz` | `C4DAAAAAAAAAAAAAAAAAAAAAAYGmZZmZmFmZGamx` | -8.80% |
| mage/fire_frostfire | `C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZG` | `C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZG` | +3.15% |
| mage/fire_sunfury | `C8DAAAAAAAAAAAAAAAAAAAAAAYmFjFzMzCjhMzMD` | `C8DAAAAAAAAAAAAAAAAAAAAAAYGGLzMzswMDZmZG` | +0.56% |
| mage/frost_frostfire | `CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMmZmYmx` | `CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMmZmYmZ` | +0.12% |
| mage/frost_spellslinger | `CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMGzEzMz` | `CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMmZmYmZ` | +0.01% |
| monk/brewmaster | `CwQAAAAAAAAAAAAAAAAAAAAAAAAAAwMLbGDzw2MW` | `CwQAAAAAAAAAAAAAAAAAAAAAAAAAAgZbzYGzM2mx` | -9.39% |
| monk/windwalker | `C0QAAAAAAAAAAAAAAAAAAAAAAMzYMYMMLzMzyMAA` | `C0QAAAAAAAAAAAAAAAAAAAAAAMzYw2wwsMzMLzAA` | +0.88% |
| monk/windwalker_conduit | `C0QAAAAAAAAAAAAAAAAAAAAAAMzYw2wwsMzMbzAA` | `C0QAAAAAAAAAAAAAAAAAAAAAAMzYM2GGsMzMbzAA` | -2.24% |
| paladin/protection | `CIEAAAAAAAAAAAAAAAAAAAAAAsMzMYWGLjZMzMLb` | `CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLD` | +5.25% |
| paladin/protection_lightsmith | `CIEAAAAAAAAAAAAAAAAAAAAAAsNjBzyYZMjZmZZb` | `CIEAAAAAAAAAAAAAAAAAAAAAAsMzAzyMLmZMDLLD` | +14.88% |
| paladin/retribution | `CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAMa22mZmlx` | `CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQz22MzsMM` | +1.87% |
| paladin/retribution_herald | `CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQz22MzsMM` | `CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQzy2MzsMM` | -6.78% |
| priest/shadow_archon | `CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAA` | `CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAA` | +0.06% |
| priest/shadow_voidweaver | `CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAA` | `CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAA` | -1.28% |
| rogue/assassination | `CMQAAAAAAAAAAAAAAAAAAAAAAYmZmZzgBAAAAAmt` | `CMQAAAAAAAAAAAAAAAAAAAAAAYmZMbzgBAAAAAml` | -1.08% |
| rogue/outlaw_fatebound | `CQQAAAAAAAAAAAAAAAAAAAAAAAgx2MGzMzMzsNzM` | `CQQAAAAAAAAAAAAAAAAAAAAAAAgx2MGjZMzsNzMz` | +1.44% |
| rogue/outlaw_trickster | `CQQAAAAAAAAAAAAAAAAAAAAAAAgx2MGjZMzsNzMz` | `CQQAAAAAAAAAAAAAAAAAAAAAAAghHYMGzYmZbmZm` | -0.08% |
| rogue/subtlety | `CUQAAAAAAAAAAAAAAAAAAAAAAAgx2MAAAAAwsMGL` | `CUQAAAAAAAAAAAAAAAAAAAAAAAgx2MAAAAAwsMGL` | -1.33% |
| shaman/elemental_stormbringer | `CYQAAAAAAAAAAAAAAAAAAAAAAAAAAAzMbLzMmZmZ` | `CYQAAAAAAAAAAAAAAAAAAAAAAAAAAAzMbLzMzMzM` | -0.34% |
| shaman/enhancement_stormbringer | `CcQAAAAAAAAAAAAAAAAAAAAAAMzMzYmZmZmZmhZm` | `CcQAAAAAAAAAAAAAAAAAAAAAAMzMzwMzMzMzMzMz` | +6.97% |
| shaman/enhancement_totemic | `CcQAAAAAAAAAAAAAAAAAAAAAAMzMjZmZmZmZmZmZ` | `CcQAAAAAAAAAAAAAAAAAAAAAAMzMjZmZmZmZmZmZ` | +0.78% |
| warlock/affliction_soul_harvester | `CkQAAAAAAAAAAAAAAAAAAAAAAswMzY0swYZmZmZZ` | `CkQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZhhZmZmlB` | -2.59% |
| warlock/demonology_soul_harvester | `CoQAy0jxIDofkwJmoH7WhvESoZmZMzoZjhZmxsMA` | `CoQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmxsMA` | +8.85% |
| warlock/destruction_hellcaller | `CsQAAAAAAAAAAAAAAAAAAAAAAwMjZGNLmxiZGzys` | `CsQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmZmlZ` | +7.34% |
| warrior/protection | `CkEAAAAAAAAAAAAAAAAAAAAAA02AAAzMjZmZmZmZ` | `CkEAAAAAAAAAAAAAAAAAAAAAA02AAAzMDzMzMzMz` | -0.93% |

## APL Differences

| Spec | APL diff summary | DPS impact (ref_A vs ours) |
|------|-----------------|---------------------------|
| death_knight/blood_deathbringer | ours=57 ref=54 shared=52 only_ours=5 only_ref=2 | +0.47% |
| death_knight/blood_sanlayn | ours=55 ref=54 shared=42 only_ours=13 only_ref=12 | +1.09% |
| death_knight/frost | ours=86 ref=83 shared=83 only_ours=3 only_ref=0 | -0.01% |
| death_knight/frost_rider | ours=86 ref=83 shared=83 only_ours=3 only_ref=0 | -0.00% |
| death_knight/unholy_rider | ours=59 ref=59 shared=44 only_ours=15 only_ref=15 | -0.24% |
| death_knight/unholy_sanlayn | ours=60 ref=59 shared=58 only_ours=2 only_ref=1 | +0.18% |
| demon_hunter/devourer_annihilator | ours=59 ref=61 shared=31 only_ours=28 only_ref=30 | +4.53% |
| demon_hunter/devourer_void-scarred | ours=59 ref=61 shared=44 only_ours=15 only_ref=17 | +3.84% |
| demon_hunter/havoc_fel-scarred | ours=94 ref=99 shared=94 only_ours=0 only_ref=5 | N/A |
| demon_hunter/vengeance_aldrachi_reaver | ours=121 ref=121 shared=121 only_ours=0 only_ref=0 | +0.13% |
| demon_hunter/vengeance_annihilator | ours=121 ref=121 shared=96 only_ours=25 only_ref=25 | -0.94% |
| druid/feral_wildstalker | ours=70 ref=110 shared=36 only_ours=34 only_ref=74 | +0.19% |
| druid/guardian | ours=0 ref=49 shared=0 only_ours=0 only_ref=49 | +0.12% |
| evoker/devastation_fs | ours=105 ref=93 shared=66 only_ours=39 only_ref=27 | +1.17% |
| evoker/devastation_sc | ours=105 ref=93 shared=66 only_ours=39 only_ref=27 | +0.27% |
| hunter/beast_mastery | ours=59 ref=59 shared=59 only_ours=0 only_ref=0 | +0.06% |
| hunter/marksmanship | ours=64 ref=64 shared=64 only_ours=0 only_ref=0 | -0.03% |
| hunter/survival_pl_dw | ours=63 ref=63 shared=63 only_ours=0 only_ref=0 | +0.01% |
| hunter/survival_sentinel_2h | ours=63 ref=63 shared=63 only_ours=0 only_ref=0 | -0.08% |
| mage/arcane_spellslinger | ours=73 ref=74 shared=73 only_ours=0 only_ref=1 | -0.01% |
| mage/arcane_sunfury | ours=73 ref=74 shared=73 only_ours=0 only_ref=1 | -0.08% |
| mage/fire_frostfire | ours=90 ref=90 shared=90 only_ours=0 only_ref=0 | -0.11% |
| mage/fire_sunfury | ours=90 ref=90 shared=90 only_ours=0 only_ref=0 | -0.01% |
| mage/frost_frostfire | ours=86 ref=86 shared=86 only_ours=0 only_ref=0 | -0.01% |
| mage/frost_spellslinger | ours=86 ref=86 shared=86 only_ours=0 only_ref=0 | +0.10% |
| monk/brewmaster | ours=42 ref=47 shared=33 only_ours=9 only_ref=14 | +3.32% |
| monk/windwalker | ours=133 ref=133 shared=132 only_ours=1 only_ref=1 | +0.02% |
| monk/windwalker_conduit | ours=133 ref=133 shared=132 only_ours=1 only_ref=1 | -0.01% |
| paladin/protection | ours=34 ref=34 shared=34 only_ours=0 only_ref=0 | -0.10% |
| paladin/protection_lightsmith | ours=34 ref=34 shared=34 only_ours=0 only_ref=0 | +0.01% |
| paladin/retribution | ours=37 ref=41 shared=25 only_ours=12 only_ref=16 | +1.24% |
| paladin/retribution_herald | ours=41 ref=41 shared=41 only_ours=0 only_ref=0 | -0.12% |
| priest/shadow_archon | ours=57 ref=59 shared=54 only_ours=3 only_ref=5 | -0.27% |
| priest/shadow_voidweaver | ours=57 ref=59 shared=54 only_ours=3 only_ref=5 | -0.16% |
| rogue/assassination | ours=47 ref=45 shared=32 only_ours=15 only_ref=13 | +1.05% |
| rogue/outlaw_fatebound | ours=50 ref=49 shared=48 only_ours=2 only_ref=1 | -0.10% |
| rogue/outlaw_trickster | ours=50 ref=49 shared=48 only_ours=2 only_ref=1 | -0.01% |
| rogue/subtlety | ours=46 ref=48 shared=36 only_ours=10 only_ref=12 | +1.95% |
| shaman/elemental_stormbringer | ours=63 ref=61 shared=61 only_ours=2 only_ref=0 | -0.02% |
| shaman/enhancement_stormbringer | ours=108 ref=106 shared=105 only_ours=3 only_ref=1 | +9.25% |
| shaman/enhancement_totemic | ours=108 ref=106 shared=105 only_ours=3 only_ref=1 | +0.12% |
| warlock/affliction_hellcaller | ours=94 ref=93 shared=93 only_ours=1 only_ref=0 | +17.23% |
| warlock/affliction_soul_harvester | ours=95 ref=93 shared=72 only_ours=23 only_ref=21 | +8.74% |
| warlock/demonology_soul_harvester | ours=47 ref=61 shared=10 only_ours=37 only_ref=51 | +2.71% |
| warlock/destruction_diabolist | ours=79 ref=78 shared=78 only_ours=1 only_ref=0 | -0.04% |
| warlock/destruction_hellcaller | ours=79 ref=78 shared=78 only_ours=1 only_ref=0 | +0.01% |
| warrior/protection | ours=62 ref=62 shared=56 only_ours=6 only_ref=6 | +0.04% |

## Key Findings & Lessons

*(Auto-generated — fill in manual analysis after reviewing the table above)*

### Talent Lessons

Reference talents beat ours (>0.5% gain) — investigate these builds:
- demon_hunter/vengeance_annihilator: ref_T is +20.96% vs ours
- paladin/protection_lightsmith: ref_T is +14.88% vs ours
- hunter/beast_mastery: ref_T is +11.47% vs ours
- demon_hunter/vengeance_aldrachi_reaver: ref_T is +10.75% vs ours
- warlock/demonology_soul_harvester: ref_T is +8.85% vs ours
- demon_hunter/devourer_void-scarred: ref_T is +8.45% vs ours
- warlock/destruction_hellcaller: ref_T is +7.34% vs ours
- shaman/enhancement_stormbringer: ref_T is +6.97% vs ours
- paladin/protection: ref_T is +5.25% vs ours
- druid/feral_wildstalker: ref_T is +4.54% vs ours
- death_knight/frost_rider: ref_T is +3.24% vs ours
- mage/fire_frostfire: ref_T is +3.15% vs ours
- death_knight/unholy_rider: ref_T is +2.95% vs ours
- paladin/retribution: ref_T is +1.87% vs ours
- rogue/outlaw_fatebound: ref_T is +1.44% vs ours
- druid/guardian: ref_T is +1.21% vs ours
- death_knight/blood_deathbringer: ref_T is +1.02% vs ours
- monk/windwalker: ref_T is +0.88% vs ours
- shaman/enhancement_totemic: ref_T is +0.78% vs ours
- mage/arcane_spellslinger: ref_T is +0.76% vs ours
- hunter/marksmanship: ref_T is +0.63% vs ours
- mage/fire_sunfury: ref_T is +0.56% vs ours

Our talents beat reference (>0.5% lead) — our optimizer working:
- monk/brewmaster: our talents lead by 9.39%
- mage/arcane_sunfury: our talents lead by 8.80%
- paladin/retribution_herald: our talents lead by 6.78%
- death_knight/unholy_sanlayn: our talents lead by 4.06%
- evoker/devastation_fs: our talents lead by 3.62%
- warlock/affliction_soul_harvester: our talents lead by 2.59%
- monk/windwalker_conduit: our talents lead by 2.24%
- rogue/subtlety: our talents lead by 1.33%
- priest/shadow_voidweaver: our talents lead by 1.28%
- rogue/assassination: our talents lead by 1.08%
- warrior/protection: our talents lead by 0.93%
- death_knight/blood_sanlayn: our talents lead by 0.50%

### APL Lessons

Reference APL beats ours (>0.5%) — consider adopting or investigating:
- warlock/affliction_hellcaller: ref_A is +17.23% vs ours
- shaman/enhancement_stormbringer: ref_A is +9.25% vs ours
- warlock/affliction_soul_harvester: ref_A is +8.74% vs ours
- demon_hunter/devourer_annihilator: ref_A is +4.53% vs ours
- demon_hunter/devourer_void-scarred: ref_A is +3.84% vs ours
- monk/brewmaster: ref_A is +3.32% vs ours
- warlock/demonology_soul_harvester: ref_A is +2.71% vs ours
- rogue/subtlety: ref_A is +1.95% vs ours
- paladin/retribution: ref_A is +1.24% vs ours
- evoker/devastation_fs: ref_A is +1.17% vs ours
- death_knight/blood_sanlayn: ref_A is +1.09% vs ours
- rogue/assassination: ref_A is +1.05% vs ours

Our APL beats reference (>0.5%) — our optimization paying off:
- demon_hunter/vengeance_annihilator: our APL leads by 0.94%

### Engine Divergence Lessons
*(Fill in after reviewing engine_div column — large divergences indicate bugs or missing features)*

---
*Generated by scripts/compare_reference_profiles.py on 2026-04-01 20:04*
