# MID1_Paladin_Retribution — Talents & Gear

## Talent Export String
```
CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQz22MzsMMzAAAAAAwoMmhZGbDz2wMbzYMmZYGbsNMAAkZm2mZ2mBAsBYAwYGmBzYMbYZGMMmxgB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	112,983.7	112,983.7	90.0 / 0.080%	15,419.1 / 13.6%	89,400.3
	Resource
	Out
	In
	Waiting
	APM
	Active
	Holy Power	1.3	1.3	4.75%	58.6	100.0%
	Talent	CYEAAAAAAAAAAAAAAAAAAAAAAAAAAAAQz22MzsMMzAAAAAAwoMmhZGbDz2wMbzYMmZYGbsNMAAkZm2mZ2mBAsBYAwYGmBzYMbYZGMMmxgB
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
	MID1_Paladin_Retribution	112,984
	Blade of Justice
	5,469 (15,624)	4.8% (13.8%)	52.0	5.80s	52.2s / 17.4%	90,050	89,808	Direct	52.0	21,405	47,947	31,521	38.1%
Stats Details: Blade Of Justice
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	52.04	52.04	0.00	0.00	0.00	1.0027	0.0000	1,640,287.44	1,640,287.44	0.00%	89,808.36	89,808.36
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	61.88%	32.20	17	50	21,404.68	9,686	48,123	21,347.25	14,083	27,777	689,300	689,300	0.00%
	crit	38.12%	19.83	5	37	47,946.76	19,859	98,666	47,876.26	29,667	68,843	950,988	950,988	0.00%
Action Details: Blade Of Justice
id:184575
school:holy
range:20.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:10.000
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
generators[J]:1.00
if_expr:talent.holy_flames&!dot.expurgation.ticking&time<5
generators[N]:28.99
if_expr:(buff.art_of_war.up|buff.righteous_cause.up)&(!talent.walk_into_light|!buff.avenging_wrath.up)
generators[P]:22.05
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Light of Justice	404436	#1	-2000.0%	Talent
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
	10,155	9.0%	29.1	10.02s	0.0s	104,728	0	Direct	29.1	71,158	157,773	104,725	38.8%
Stats Details: Light Within Boj
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	29.08	29.08	0.00	0.00	0.00	0.0000	0.0000	3,045,553.32	3,045,553.32	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	61.24%	17.81	5	37	71,157.82	58,927	117,110	71,127.53	60,532	86,429	1,267,333	1,267,333	0.00%
	crit	38.76%	11.27	2	26	157,772.94	120,819	240,111	157,781.08	124,264	204,630	1,778,220	1,778,220	0.00%
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
	Consecration (blade_of_justice)
	0 (967)	0.0% (0.9%)	22.2	13.93s	0.0s	13,088	0
Stats Details: Consecrationblade Of Justice
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	22.16	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Consecrationblade Of Justice
id:26573
school:holy
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:false
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:26573
name:Consecration
school:holy
tooltip:Damage every {$t1=1} sec.
description:Consecrates the land beneath you, causing {$?s405289=true}[{$=}{{$=}<dmg>*1.05} Radiant][{$=}{{$=}<dmg>*1.05} Holy] damage over {$d=12 seconds} to enemies who enter the area{$?s204054=true}[ and reducing their movement speed by {$204054s2=50}%.][.] Limit {$s2=1}.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Retribution Paladin	1258011	#11	11000.0	Spec Spell
	Direct Damage	Retribution Paladin	137027	#15	-6.0%	Spec Spell
Consecration (_tick_blade_of_justice)
	967	0.9%	0.0	0.00s	0.0s	0	0	Periodic	417.6	460	1,069	694	38.5%	0.0%
Stats Details: Consecration Tick Blade Of Justice
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	417.59	0.00	0.0000	0.0000	290,000.44	290,000.44	0.00%	0.00	0.00
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	61.45%	256.62	177	345	459.67	275	925	459.62	397	514	117,964	117,964	0.00%
	crit	38.55%	160.96	106	230	1,068.76	565	1,896	1,068.82	898	1,202	172,037	172,037	0.00%
Action Details: Consecration Tick Blade Of Justice
id:81297
school:holy
range:50000.0
travel_speed:0.0000
radius:9.2
trigger_gcd:0.0000
gcd_type:attack_haste
min_gcd:0.0000
cooldown:11.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:81297
name:Consecration
school:holy
tooltip:
description:Deals {$s1=0} Holy damage every {$26573t1=1} sec to enemies within {$=}A1 yards.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	Retribution Paladin	1258011	#11	11000.0	Spec Spell
	Direct Damage	Retribution Paladin	137027	#11	5.0%	Spec Spell
	Retribution Paladin	137027	#15	-6.0%	Spec Spell
	Burning Crusade	403026	#2	10.0%	Talent
	Max Radius	Consecrated Ground	204054	#5	15.0%	Talent
	Periodic Damage	Retribution Paladin	137027	#12	5.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Avenging Wrath	31884	#1	20.0%	Spell Data	No-stacks
	Sentinel	389539	#1	20.0%	Spell Data	No-stacks
	Periodic Damage
	Avenging Wrath	31884	#2	20.0%	Spell Data	No-stacks
	Sentinel	389539	#2	20.0%	Spell Data	No-stacks
	Damage on Debuff
	Sanctify	382538	#1	20.0%
	Divine Storm
	755	0.7%	5.4	60.84s	0.0s	41,977	0	Direct	5.4	27,160	55,664	41,977	52.0%
Stats Details: Divine Storm
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.38	5.38	0.00	0.00	0.00	0.0000	0.0000	226,006.11	226,006.11	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	48.02%	2.59	0	6	27,159.70	18,149	36,069	26,241.80	0	36,069	70,220	70,220	0.00%
	crit	51.98%	2.80	0	6	55,664.29	37,211	73,952	54,443.82	0	73,952	155,786	155,786	0.00%
Action Details: Divine Storm
id:53385
school:holy
range:0.0
travel_speed:0.0000
radius:8.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
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
reduced_aoe_targets:5
harmful:true
Resources
resource:holy_power
base_cost:3
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
```
