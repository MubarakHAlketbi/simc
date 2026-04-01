# MID1_Shaman_Enhancement_Totemic — Talents & Gear

## Talent Export String
```
CcQAAAAAAAAAAAAAAAAAAAAAAMzMjZmZmZmZmZmZmZGAAAAAAAAAYB2gZsox2AYmgNAsMjZMWWmBmZ2GLzMzMMWGzAAYAGzMxMDAMGA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	101,145.5	101,145.5	67.4 / 0.067%	11,649.3 / 11.5%	108.8
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	737.7	736.3	0.19%	58.9	100.0%
	Talent	CcQAAAAAAAAAAAAAAAAAAAAAAMzMjZmZmZmZmZmZmZGAAAAAAAAAYB2gZsox2AYmgNAsMjZMWWmBmZ2GLzMzMMWGzAAYAGzMxMDAMGA
	Set Bonus
Mantle of the Primal Core (MID1)
Shaman Enhancement 12.0 Class Set 2pc (2pc)
Shaman Enhancement 12.0 Class Set 4pc (4pc)
Charts
Abilities
	Damage Stats
	DPS
	DPS%
	Execute
	Interval
	Total Time
	DPE
	DPET
	Type
	Count
	Hit
	Crit
	Avg
	Crit%
	Avoid%
	Up%
	MID1_Shaman_Enhancement_Totemic	101,146
	Crash Lightning
	2,065 (12,703)	2.0% (12.6%)	38.1	7.87s	40.1s / 13.4%	99,954	95,062	Direct	38.1	13,762	27,509	16,259	18.2%	0.0%
Stats Details: Crash Lightning
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	38.11	38.11	0.00	0.00	0.00	1.0515	0.0000	619,641.18	619,641.18	0.00%	95,061.82	95,061.82
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	81.84%	31.19	16	49	13,761.68	10,731	23,175	13,756.57	12,456	15,203	429,224	429,224	0.00%
	crit	18.16%	6.92	0	19	27,509.35	21,461	45,544	27,444.18	0	38,346	190,417	190,417	0.00%
Action Details: Crash Lightning
id:187874
school:nature
range:5.0
travel_speed:0.0000
radius:8.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:15.000
cooldown hasted:true
category cooldown:true
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.04
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:6
harmful:true
Resources
resource:mana
base_cost:500
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:187874
name:Crash Lightning
school:nature
tooltip:
description:Electrocutes all enemies in front of you, dealing {$s1=0} Nature damage.
Enhances your weapons for {$187878d=12 seconds}, causing Stormstrike and Lava Lash to discharge {$195592s1=0} Nature damage split between up to {$195592=}i enemies in front of you. {$?s1252373=true}[Multiple applications may overlap.][]
Action Priority List
single_totemic[N]:38.11
if_expr:!buff.crash_lightning.up|talent.storm_unleashed.enabled
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Nature's Fury	381655	#1	4.0%	Talent
	Direct Damage	Enhancement Shaman	137041	#1	8.0%	Spec Spell
	Elemental Tempo	1250364	#1	10.0%	Talent
	Hasted Cooldown	Shaman	137038	#2	0.0%	Class Spell
	Enhancement Shaman	137041	#31	0.0%	Spec Spell
	Hasted Gcd	Shaman	137038	#3	100.0%	Class Spell
	Periodic Damage	Enhancement Shaman	137041	#2	8.0%	Spec Spell
	Elemental Tempo	1250364	#2	10.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Enhanced Elements	77223	#1	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#1	3.0%	Spell Data
	Crackling Surge	224127	#1	5.0%	Spell Data
	Elemental Weapons	408390	#1	0.0%	Spell Data	Conditional, Value-function
	Electrostatic Wager	1223332	#1	12.0%	Spell Data
	Periodic Damage
	Mastery: Enhanced Elements	77223	#5	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#2	3.0%	Spell Data
	Crackling Surge	224127	#2	5.0%	Spell Data
	Elemental Weapons	408390	#2	0.0%	Spell Data	Conditional, Value-function
Crash Lightning (_proc)
	8,889	8.8%	199.2	1.49s	0.0s	13,377	0	Direct	199.2	11,332	22,682	13,377	18.0%	0.0%
Stats Details: Crash Lightning Proc
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	199.23	199.23	0.00	0.00	0.00	0.0000	0.0000	2,665,135.36	2,665,135.36	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	81.98%	163.32	106	222	11,331.63	2,524	70,004	11,349.54	8,306	15,185	1,850,662	1,850,662	0.00%
	crit	18.02%	35.91	15	66	22,681.59	5,049	151,634	22,715.66	14,503	35,678	814,473	814,473	0.00%
Action Details: Crash Lightning Proc
id:195592
school:nature
range:5.0
travel_speed:0.0000
radius:8.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:0.000
cooldown hasted:true
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.04
target:Fluffy_Pillow
aoe:5
split_aoe_damage:true
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:195592
name:Crash Lightning
school:nature
tooltip:
description:{$@spelldesc187874=Electrocutes all enemies in front of you, dealing {$s1=0} Nature damage.
Enhances your weapons for {$187878d=12 seconds}, causing Stormstrike and Lava Lash to discharge {$195592s1=0} Nature damage split between up to {$195592=}i enemies in front of you. {$?s1252373=true}[Multiple applications may overlap.][]}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Nature's Fury	381655	#1	4.0%	Talent
	Direct Damage	Enhancement Shaman	137041	#1	8.0%	Spec Spell
	Elemental Tempo	1250364	#1	10.0%	Talent
	Hasted Cooldown	Shaman	137038	#2	0.0%	Class Spell
	Hasted Gcd	Shaman	137038	#3	100.0%	Class Spell
	Periodic Damage	Enhancement Shaman	137041	#2	8.0%	Spec Spell
	Elemental Tempo	1250364	#2	10.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Enhanced Elements	77223	#1	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#1	3.0%	Spell Data
	Crackling Surge	224127	#1	5.0%	Spell Data
	Elemental Weapons	408390	#1	0.0%	Spell Data	Conditional, Value-function
	Periodic Damage
	Mastery: Enhanced Elements	77223	#5	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#2	3.0%	Spell Data
	Crackling Surge	224127	#2	5.0%	Spell Data
	Elemental Weapons	408390	#2	0.0%	Spell Data	Conditional, Value-function
Crash Lightning (Unleashed)
	1,749	1.7%	64.5	4.59s	0.0s	8,139	0	Direct	64.5	6,903	13,803	8,139	17.9%	0.0%
Stats Details: Crash Lightning Unleashed
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	64.46	64.46	0.00	0.00	0.00	0.0000	0.0000	524,635.66	524,635.66	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	82.08%	52.91	29	83	6,902.85	5,433	11,577	6,900.18	6,327	7,601	365,205	365,205	0.00%
	crit	17.92%	11.55	1	26	13,802.99	10,866	23,001	13,799.02	11,337	18,044	159,431	159,431	0.00%
Action Details: Crash Lightning Unleashed
id:1252431
school:nature
range:100.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:0.000
cooldown hasted:true
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.04
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:1252431
name:Crash Lightning (Unleashed)
school:nature
tooltip:
description:{$@spelldesc1252373=Crash Lightning electrocutes the area struck, dealing {$s1=50}% of its damage {$s2=2} additional times over {$1252433d=2 seconds}, and its weapon enhancement effect now increases auto-attack speed by {$s3=15}%.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Nature's Fury	381655	#1	4.0%	Talent
	Direct Damage	Enhancement Shaman	137041	#1	8.0%	Spec Spell
	Elemental Tempo	1250364	#1	10.0%	Talent
	Hasted Cooldown	Shaman	137038	#2	0.0%	Class Spell
	Hasted Gcd	Shaman	137038	#3	100.0%	Class Spell
	Periodic Damage	Enhancement Shaman	137041	#2	8.0%	Spec Spell
	Elemental Tempo	1250364	#2	10.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Enhanced Elements	77223	#1	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#1	3.0%	Spell Data
	Crackling Surge	224127	#1	5.0%	Spell Data
	Elemental Weapons	408390	#1	0.0%	Spell Data	Conditional, Value-function
	Electrostatic Wager	1223332	#1	12.0%	Spell Data
	Periodic Damage
	Mastery: Enhanced Elements	77223	#5	2.00000	Spell Data	Mastery, Passive
	Amplification Core	456369	#2	3.0%	Spell Data
	Crackling Surge	224127	#2	5.0%	Spell Data
	Elemental Weapons	408390	#2	0.0%	Spell Data	Conditional, Value-function
	Doom Winds (_damage)
	3,054	3.0%	58.1	4.84s	0.0s	15,777	0	Direct	58.1	13,371	26,723	15,777	18.0%	0.0%
Stats Details: Doom Winds Damage
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	58.06	58.06	0.00	0.00	0.00	0.0000	0.0000	916,012.51	916,012.51	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	81.98%	47.60	27	63	13,371.28	8,948	19,908	13,361.71	12,076	14,681	636,487	636,487	0.00%
	crit	18.02%	10.46	1	23	26,723.38	17,896	39,833	26,706.46	19,718	32,756	279,525	279,525	0.00%
Action Details: Doom Winds Damage
id:469270
school:stormstrike
range:100.0
travel_speed:0.0000
radius:8.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.04
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:5
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:469270
name:Doom Winds
school:stormstrike
tooltip:
description:{$@spelldesc384352=Unleash a devastating storm around yourself, dealing {$469270s1=0} Stormstrike damage every {$466772s5=1} sec to nearby enemies for {$466772d=8 seconds}.
Increases your chance to activate Windfury Weapon by {$466772s1=100}%, and the damage of Windfury Weapon by {$466772s2=20}%.
}
```
