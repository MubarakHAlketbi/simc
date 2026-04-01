# MID1_Hunter_Beast_Mastery — Talents & Gear

## Talent Export String
```
C0PAAAAAAAAAAAAAAAAAAAAAAAMmxwCsBzwQDbAAYG2GzsMzwMmZYYmxYmxMzYGzwMzYGzghmBAAAAAMDAAAzMzMAzshwwsA2MA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	113,979.6	113,979.6	60.8 / 0.053%	10,573.3 / 9.3%	2,432.0
	Resource
	Out
	In
	Waiting
	APM
	Active
	Focus	19.9	19.7	1.30%	51.1	100.0%
	Talent	C0PAAAAAAAAAAAAAAAAAAAAAAAMmxwCsBzwQDbAAYG2GzsMzwMmZYYmxYmxMzYGzwMzYGzghmBAAAAAMDAAAzMzMAzshwwsA2MA
	Set Bonus
Root Warden's Regalia (MID_RWR)
Root Warden's Regalia (2pc)
Primal Sentry's Camouflage (MID1)
Hunter Beast Mastery 12.0 Class Set 2pc (2pc)
Hunter Beast Mastery 12.0 Class Set 4pc (4pc)
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
	MID1_Hunter_Beast_Mastery	113,980
	Auto Shot
	1,459	1.3%	126.8	2.37s	0.0s	3,451	1,482	Direct	126.6	2,703	5,544	3,458	26.6%
Stats Details: Auto Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	126.83	126.57	0.00	0.00	0.00	2.3282	0.0000	437,698.65	625,283.79	30.00%	1,482.25	1,482.25
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	73.42%	92.92	62	128	2,703.20	2,081	4,272	2,702.17	2,569	2,815	251,184	358,835	30.00%
	crit	26.58%	33.65	14	60	5,543.55	4,267	8,758	5,542.07	4,949	6,257	186,514	266,449	30.00%
Action Details: Auto Shot
id:75
school:physical
range:40.0
travel_speed:60.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:3.00
base_crit:0.00
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
weapon_multiplier:1.000000
Spelldata
id:75
name:Auto Shot
school:physical
tooltip:Firing at the target.
description:Automatically shoots the target until cancelled.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Precision Strikes	1267003	#1	25.0%	Talent
	Lethal Barbs	1264781	#2	25.0%	Talent
	Barbed Shot
	26,318	23.1%	53.9	5.70s	63.0s / 21.0%	146,394	125,259	Periodic	251.6	22,672	46,467	31,367	36.5%	99.6%
Stats Details: Barbed Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	53.91	0.00	251.59	251.59	52.82	1.1687	1.1871	7,891,673.79	7,891,673.79	0.00%	21,820.40	125,258.70
	Tick Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Total	Mitigated
	hit	63.46%	159.66	109	221	22,671.71	8,850	70,881	22,675.16	20,764	26,745	3,619,719	3,619,719	0.00%
	crit	36.54%	91.94	46	138	46,466.51	18,116	145,533	46,480.50	40,599	58,883	4,271,955	4,271,955	0.00%
Action Details: Barbed Shot
id:217200
school:physical
range:40.0
travel_speed:80.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:18.000
cooldown hasted:true
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.10
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
Damage Over Time
tick_may_crit:true
tick_zero:true
tick_on_application:true
rolling_periodic:true
attack_power_mod.tick:0.779000
spell_power_mod.tick:0.000000
base_td:0.000000
base_td_mult:1.633204
base_multiplier:1.000000
dot_duration:14.00
base_tick_time:2.00
hasted_ticks:false
dot_behavior:unknown
Spelldata
id:217200
name:Barbed Shot
school:physical
tooltip:Suffering {$=}w1 damage every {$t1=2} sec.
description:Fire a shot that tears through your enemy, causing them to bleed for {$=}{{$s1=0}*{$s2=5}} damage over {$d=14 seconds}. If Barbed Shot is reapplied, any remaining damage will be added to the new Barbed Shot.
|cFFFFFFFFGenerates {$=}{{$246152s1=5}*{$246152d=8 seconds}/{$246152t1=2}} Focus over {$246152d=8 seconds}.|r
Action Priority List
st[C]:3.90
if_expr:cooldown.bestial_wrath.remains<gcd
target_if_expr:dot.barbed_shot.remains|max_prio_damage
st[F]:50.01
target_if_expr:dot.barbed_shot.remains|max_prio_damage
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Thrill of the Hunt	1265051	#1	10.0%	Talent
	Direct Damage	Beast Mastery Hunter	137015	#1	-3.0%	Spec Spell
	War Orders	393933	#2	10.0%	Talent
	Nature's Ally	1273126	#1	15.0%	Talent
	Duration	Savagery	424557	#2	2000.0	Talent
	Hasted Cooldown	Hunter	137014	#9	0.0%	Class Spell
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
	Periodic Damage	Beast Mastery Hunter	137015	#2	-3.0%	Spec Spell
	Better Together	472357	#4	10.0%	Talent
	No Mercy	472660	#1	10.0%	Talent
	War Orders	393933	#1	10.0%	Talent
	Jagged Wounds	1265044	#1	10.0%	Talent
	Nature's Ally	1273126	#3	15.0%	Talent
	Boar Charge
	2,384 (5,250)	2.1% (4.6%)	0.0	0.00s	0.0s	0	0	Direct	8.3	67,882	138,898	86,558	26.3%
Stats Details: Boar Charge
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	8.28	0.00	0.00	0.00	0.0000	0.0000	716,357.79	1,023,368.27	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	73.70%	6.10	1	10	67,882.29	46,305	114,219	67,817.48	47,425	93,373	414,052	591,503	30.00%
	crit	26.30%	2.18	0	7	138,898.26	94,939	228,873	126,911.27	0	228,873	302,306	431,865	27.41%
Action Details: Boar Charge
id:471936
school:physical
range:100.0
travel_speed:50.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
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
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:471936
name:Boar Charge
school:physical
tooltip:
description:{$@spelldesc471876=While in combat, every {$471877d=30 seconds} your next Kill Command summons the aid of a Beast.
{$@=}spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by {$=}{{$471881s1=1}*{$s3=10}}% for {$471881d=12 seconds}.
{$@=}spellicon471936 Boar
A Boar charges through your target {$s2=1} {$=}Ltime:times;, dealing {$471936s1=0} physical damage to the primary target and {$471938s1=0} damage to up to {$471938s2=5} nearby enemies.
{$@=}spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing {$471999=}o1 damage over {$471999d=10 seconds} to up to {$471999s2=8} nearby enemies.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Beast Mastery Hunter	137015	#1	-3.0%	Spec Spell
	Periodic Damage	Beast Mastery Hunter	137015	#2	-3.0%	Spec Spell
Boar Charge (_cleave)
	2,866	2.5%	0.0	0.00s	0.0s	0	0	Direct	8.3	81,452	166,720	104,065	26.5%
Stats Details: Boar Charge Cleave
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	8.28	0.00	0.00	0.00	0.0000	0.0000	861,222.76	1,230,318.22	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	73.48%	6.08	1	10	81,451.77	55,566	137,063	81,395.10	56,624	111,541	495,346	707,637	30.00%
	crit	26.52%	2.19	0	7	166,720.44	113,927	281,021	152,768.39	0	274,648	365,877	522,682	27.50%
Action Details: Boar Charge Cleave
id:471938
school:physical
range:100.0
travel_speed:50.0000
radius:8.0
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
reduced_aoe_targets:5
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:471938
name:Boar Charge
school:physical
tooltip:
description:{$@spelldesc471876=While in combat, every {$471877d=30 seconds} your next Kill Command summons the aid of a Beast.
{$@=}spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by {$=}{{$471881s1=1}*{$s3=10}}% for {$471881d=12 seconds}.
{$@=}spellicon471936 Boar
A Boar charges through your target {$s2=1} {$=}Ltime:times;, dealing {$471936s1=0} physical damage to the primary target and {$471938s1=0} damage to up to {$471938s2=5} nearby enemies.
{$@=}spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing {$471999=}o1 damage over {$471999d=10 seconds} to up to {$471999s2=8} nearby enemies.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Beast Mastery Hunter	137015	#1	-3.0%	Spec Spell
	Periodic Damage	Beast Mastery Hunter	137015	#2	-3.0%	Spec Spell
	Cobra Shot
	9,742	8.5%	91.4	3.22s	108.5s / 36.2%	31,998	26,932	Direct	91.1	16,984	43,710	32,090	56.5%
Stats Details: Cobra Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	91.35	91.09	0.00	0.00	0.00	1.1881	0.0000	2,923,095.29	4,175,850.41	30.00%	26,932.28	26,932.28
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	43.48%	39.60	18	62	16,983.93	11,141	71,108	16,976.22	13,356	22,037	672,577	960,824	30.00%
	crit	56.52%	51.49	28	80	43,709.75	28,675	183,415	43,708.39	35,922	52,840	2,250,518	3,215,026	30.00%
Action Details: Cobra Shot
id:193455
school:physical
range:40.0
travel_speed:45.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.30
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:focus
base_cost:35
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:193455
name:Cobra Shot
school:physical
tooltip:
description:A quick shot causing {$=}{{$s2=0}*{$=}<mult>} Physical damage.
Reduces the cooldown of Kill Command by {$s3=1} sec.
Action Priority List
st[G]:91.35
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Thrill of the Hunt	1265051	#2	30.0%	Talent
	Crit Bonus	Serpentine Strikes	468701	#1	50.0%	Talent
	Direct Damage	Beast Mastery Hunter	137015	#1	-3.0%	Spec Spell
	Nature's Ally	1273126	#1
```
