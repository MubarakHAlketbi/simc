# MID1_Paladin_Retribution_Herald — Talents & Gear

## Talent Export String
```
CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQzy2MzsMMzAAAAAAwoMmhZGbDz2wMbzYMmZYGLsNMgZZ2mZmtGEAAwCgBAjZYGMjxsAMzMMmxgB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	104,924.2	104,924.2	78.1 / 0.074%	13,474.3 / 12.8%	104,221.1
	Resource
	Out
	In
	Waiting
	APM
	Active
	Holy Power	1.0	1.0	0.24%	60.9	100.0%
	Talent	CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQzy2MzsMMzAAAAAAwoMmhZGbDz2wMbzYMmZYGLsNMgZZ2mZmtGEAAwCgBAjZYGMjxsAMzMMmxgB
	Set Bonus
Luminant Verdict's Vestments (MID1)
Paladin Retribution 12.0 Class Set 2pc (2pc)
Paladin Retribution 12.0 Class Set 4pc (4pc)
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
	Up%
	MID1_Paladin_Retribution_Herald	104,924
	Blade of Justice
	3,347 (9,101)	3.2% (8.7%)	38.4	7.80s	40.4s / 13.5%	71,175	67,552	Direct	38.4	19,572	40,776	26,174	31.1%
Stats Details: Blade Of Justice
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	38.35	38.35	0.00	0.00	0.00	1.0536	0.0000	1,003,795.23	1,003,795.23	0.00%	67,552.28	67,552.28
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	68.86%	26.41	12	42	19,572.48	9,563	47,848	19,512.82	13,647	25,359	516,902	516,902	0.00%
	crit	31.14%	11.94	2	26	40,776.34	19,607	98,104	40,686.99	22,315	64,363	486,893	486,893	0.00%
Action Details: Blade Of Justice
id:184575
school:holy
range:20.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:12.000
cooldown hasted:true
category cooldown:true
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:on_hit
energize_resource:holy_power
energize_amount:2.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:184575
name:Blade of Justice
school:holy
tooltip:
description:{$?s403826=false}[Pierce enemies][Pierce an enemy] with a blade of light, dealing {$s1=0} Holy damage{$?s403826=false}[ to your target and {$404358s1=0} Holy damage to nearby enemies.][.]
|cFFFFFFFFGenerates {$s2=1} Holy Power.|r
Action Priority List
generators[I]:1.00
if_expr:talent.holy_flames&!dot.expurgation.ticking&time<5
generators[L]:16.25
if_expr:(buff.art_of_war.up|buff.righteous_cause.up)&(!talent.walk_into_light|!buff.avenging_wrath.up)
generators[O]:21.10
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Retribution Paladin	137027	#11	5.0%	Spec Spell
	Jurisdiction	402971	#4	10.0%	Talent
	Blades of Light	403664	#1	20.0%	Talent
	Hasted Cooldown	Retribution Paladin	1258011	#3	100.0%	Spec Spell
	Retribution Paladin	1258011	#5	100.0%	Spec Spell
	Hasted Gcd	Retribution Paladin	1258011	#4	100.0%	Spec Spell
	Max Range	Jurisdiction	402971	#1	8.0	Talent
	Periodic Damage	Retribution Paladin	137027	#12	5.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Art of War	406086	#1	150.0%	Spell Data	Callback
	Righteous Cause	402916	#1	150.0%	Spell Data	Callback
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
Light Within (_boj)
	5,754	5.5%	20.1	13.78s	0.0s	85,787	0	Direct	20.1	64,258	139,738	85,784	28.5%
Stats Details: Light Within Boj
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	20.12	20.12	0.00	0.00	0.00	0.0000	0.0000	1,725,789.87	1,725,789.87	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	71.48%	14.38	3	30	64,258.49	58,180	108,471	64,222.15	58,823	82,543	924,017	924,017	0.00%
	crit	28.52%	5.74	0	17	139,738.31	119,287	222,399	139,323.40	0	222,399	801,773	801,773	0.00%
Action Details: Light Within Boj
id:1261160
school:holy
range:20.0
travel_speed:0.0000
radius:20.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:8
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1261160
name:Light Within
school:holy
tooltip:
description:{$@spelldesc1261159={$?s402912=false}[Righteous Cause][Art of War] further empowers Blade of Justice to unleash a wave of Holy energy, dealing {$=}{{$1261160s1=0}*{$=}<mult>} Holy damage to its primary target and {$1261160s1=0} Holy damage to all other enemies in its path.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Retribution Paladin	137027	#11	5.0%	Spec Spell
	Periodic Damage	Retribution Paladin	137027	#12	5.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
	Blade of Justice (_walk_into_light)
	3,779 (8,020)	3.6% (7.6%)	39.0	7.39s	0.0s	61,646	0	Direct	39.0	19,370	39,906	29,048	47.1%
Stats Details: Blade Of Justice Walk Into Light
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	39.02	39.02	0.00	0.00	0.00	0.0000	0.0000	1,133,464.14	1,133,464.14	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	52.87%	20.63	8	37	19,369.73	11,475	47,848	19,360.71	13,288	29,157	399,637	399,637	0.00%
	crit	47.13%	18.39	6	32	39,906.42	23,528	98,104	39,891.58	25,155	60,703	733,828	733,828	0.00%
Action Details: Blade Of Justice Walk Into Light
id:184575
school:holy
range:20.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:0.000
cooldown hasted:true
category cooldown:true
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:on_hit
energize_resource:holy_power
energize_amount:2.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:184575
name:Blade of Justice
school:holy
tooltip:
description:{$?s403826=false}[Pierce enemies][Pierce an enemy] with a blade of light, dealing {$s1=0} Holy damage{$?s403826=false}[ to your target and {$404358s1=0} Holy damage to nearby enemies.][.]
|cFFFFFFFFGenerates {$s2=1} Holy Power.|r
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Retribution Paladin	137027	#11	5.0%	Spec Spell
	Jurisdiction	402971	#4	10.0%	Talent
	Blades of Light	403664	#1	20.0%	Talent
	Hasted Cooldown	Retribution Paladin	1258011	#3	100.0%	Spec Spell
	Retribution Paladin	1258011	#5	100.0%	Spec Spell
	Hasted Gcd	Retribution Paladin	1258011	#4	100.0%	Spec Spell
	Max Range	Jurisdiction	402971	#1	8.0	Talent
	Periodic Damage	Retribution Paladin	137027	#12	5.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Art of War	406086	#1	150.0%	Spell Data	Callback
	Righteous Cause	402916	#1	150.0%	Spell Data	Callback
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
Light Within (_boj_wil)
	4,241	4.0%	10.0	28.44s	0.0s	127,641	0	Direct	10.0	85,565	175,922	127,640	46.6%
Stats Details: Light Within Boj Wil
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	9.97	9.97	0.00	0.00	0.00	0.0000	0.0000	1,272,047.18	1,272,047.18	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	53.43%	5.33	0	16	85,564.97	58,180	116,442	85,159.27	0	113,702	455,625	455,625	0.00%
	crit	46.57%	4.64	0	12	175,922.49	119,287	238,743	174,674.48	0	238,743	816,422	816,422	0.00%
Action Details: Light Within Boj Wil
id:1261160
school:holy
range:20.0
travel_speed:0.0000
radius:20.0
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
reduced_aoe_targets:8
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:1261160
name:Light Within
school:holy
tooltip:
description:{$@spelldesc1261159={$?s402912=false}[Righteous Cause][Art of War] further empowers Blade of Justice to unleash a wave of Holy energy, dealing {$=}{{$1261160s1=0}*{$=}<mult>} Holy damage to its primary target and {$1261160s1=0} Holy damage to all other enemies in its path.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Retribution Paladin	137027	#11	5.0%	Spec Spell
	Periodic Damage	Retribution Paladin	137027	#12	5.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
	Consecration (blade_of_justice)
	0 (925)	0.0% (0.9%)	23.1	13.40s	0.0s	12,030	0
Stats Details: Consecrationblade Of Justice
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount
```
