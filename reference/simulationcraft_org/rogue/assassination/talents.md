# MID1_Rogue_Assassination — Talents & Gear

## Talent Export String
```
CMQAAAAAAAAAAAAAAAAAAAAAAYmZMbzgBAAAAAmlBbzAAAAAAabbmZmZmZMmZmZ2mZZmZGMmZmZMzYYAMwCMjRjZBklBsZAwMzgB
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	104,072.1	104,072.1	86.0 / 0.083%	15,125.8 / 14.5%	3,297.7
	Resource
	Out
	In
	Waiting
	APM
	Active
	Energy	31.6	31.1	7.56%	53.9	100.0%
	Talent	CMQAAAAAAAAAAAAAAAAAAAAAAYmZMbzgBAAAAAmlBbzAAAAAAabbmZmZmZMmZmZ2mZZmZGMmZmZMzYYAMwCMjRjZBklBsZAwMzgB
	Set Bonus
Motley of the Grim Jest (MID1)
Rogue Assassination 12.0 Class Set 2pc (2pc)
Rogue Assassination 12.0 Class Set 4pc (4pc)
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
	MID1_Rogue_Assassination	104,072
	Ambush
	2,829	2.7%	30.8	9.34s	30.9s / 10.3%	27,613	27,490	Direct	30.8	17,313	39,317	27,614	46.8%	0.0%
Stats Details: Ambush
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	30.79	30.79	0.00	0.00	0.00	1.0045	0.0000	850,310.15	1,214,728.79	30.00%	27,489.66	27,489.66
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	53.19%	16.38	2	33	17,313.43	10,415	34,966	17,292.14	13,889	23,837	283,568	405,097	30.00%
	crit	46.81%	14.41	3	32	39,317.45	24,076	78,585	39,250.73	31,427	50,740	566,743	809,632	30.00%
Action Details: Ambush
id:8676
school:physical
range:5.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.0000
gcd_type:none
min_gcd:1.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.05
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:energy
base_cost:50
secondary_cost:0
energize_type:on_hit
energize_resource:combo_points
energize_amount:2.0
Weapon
normalized:false
weapon_power_mod:0.166667
weapon_multiplier:0.000000
Spelldata
id:8676
name:Ambush
school:physical
tooltip:
description:Ambush the target, causing {$s1=0} Physical damage.{$?s383281=false}[
Has a {$=}{{$279876s1=30}*{$383281s1=80}/100}% chance to grant Opportunity.][]
|cFFFFFFFFAwards {$s2=2} combo {$=}lpoint:points;.|r
Action Priority List
generate[K]:30.79
if_expr:spell_targets.fan_of_knives<=1+talent.blindside
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Deadly Precision	381542	#1	5.0%	Talent
	Crit Bonus	Lethality	382238	#2	20.0%	Talent
	Direct Damage	Assassination Rogue	137037	#1	35.0%	Spec Spell
	Assassination Rogue	137037	#8	8.0%	Spec Spell
	Assassination Rogue	137037	#10	-4.0%	Spec Spell
	Periodic Damage	Assassination Rogue	137037	#2	35.0%	Spec Spell
	Assassination Rogue	137037	#11	-4.0%	Spec Spell
	Amplifying Poison
	6,855	6.6%	0.0	0.00s	0.0s	0	0	Direct	672.1	2,043	4,205	3,055	46.8%	0.0%
Stats Details: Amplifying Poison
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	672.06	0.00	0.00	0.00	0.0000	0.0000	2,053,214.92	2,053,214.92	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	53.19%	357.50	236	472	2,043.04	824	7,264	2,043.05	1,671	2,524	730,386	730,386	0.00%
	crit	46.81%	314.56	208	422	4,205.42	1,696	14,806	4,205.04	3,447	5,157	1,322,829	1,322,829	0.00%
Action Details: Amplifying Poison
id:383414
school:nature
range:100.0
travel_speed:0.0000
radius:0.0
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
id:383414
name:Amplifying Poison
school:nature
tooltip:Envenom consumes stacks to amplify its damage.
description:{$@spelldesc381664=Coats your weapons with a Lethal Poison that lasts for {$d=3600 seconds}. Each strike has a {$h=30}% chance to poison the enemy, dealing {$383414s1=0} Nature damage and applying Amplifying Poison for {$383414d=12 seconds}. Envenom can consume {$s2=10} stacks of Amplifying Poison to deal {$s1=35}% increased damage. Max {$383414u=20} stacks.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Assassination Rogue	137037	#1	35.0%	Spec Spell
	Assassination Rogue	137037	#10	-4.0%	Spec Spell
	Virulent Poisons	381543	#1	10.0%	Talent
	Fatal Concoction	392384	#1	40.0%	Talent
	Implacable	1265386	#2	20.0%	Talent
	Periodic Damage	Assassination Rogue	137037	#2	35.0%	Spec Spell
	Assassination Rogue	137037	#11	-4.0%	Spec Spell
	Implacable	1265386	#3	20.0%	Talent
	Auto Attack
	0 (11,737)	0.0% (11.3%)	2.9	121.52s	0.0s	1,212,251	0
Stats Details: Auto Attack
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	2.90	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Auto Attack
id:0
school:none
range:-1.0
travel_speed:0.0000
radius:-1.0
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
Auto Attack (Main Hand)
	7,845	7.5%	472.7	0.74s	0.0s	4,978	6,775	Direct	472.7	3,889	8,008	4,978	41.9%	16.4%
Stats Details: Auto Attack Mh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	472.65	472.65	0.00	0.00	0.00	0.7348	0.0000	2,352,781.56	3,361,116.51	30.00%	6,774.63	6,774.63
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	41.74%	197.26	122	271	3,889.19	2,897	8,136	3,887.97	3,505	4,465	767,191	1,095,987	30.00%
	crit	41.89%	197.99	130	272	8,008.33	5,966	16,756	8,005.26	7,339	9,210	1,585,591	2,265,130	30.00%
	miss	16.37%	77.39	42	119	0.00	0	0	0.00	0	0	0	0	0.00%
Action Details: Auto Attack Mh
id:0
school:physical
range:5.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.80
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
Auto Attack (Off Hand)
	3,892	3.7%	471.8	0.74s	0.0s	2,474	3,366	Direct	471.8	1,933	3,979	2,474	41.9%	16.4%
Stats Details: Auto Attack Oh
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	471.83	471.83	0.00	0.00	0.00	0.7348	0.0000	1,167,077.87	1,667,254.10	30.00%	3,366.49	3,366.49
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	41.71%	196.82	127	274	1,932.66	1,439	4,004	1,932.09	1,734	2,250	380,388	543,412	30.00%
	crit	41.90%	197.69	129	278	3,979.39	2,963	8,326	3,978.11	3,645	4,514	786,690	1,123,842	30.00%
	miss	16.39%	77.31	43	117	0.00	0	0	0.00	0	0	0	0	0.00%
Action Details: Auto Attack Oh
id:1
school:physical
range:5.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.80
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
	Deadly Poison (_driver)
	0 (9,209)	0.0% (8.8%)	0.0	0.00s	0.0s	0	0
Stats Details: Deadly Poison Driver
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Deadly Poison Driver
id:2823
school:physical
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:0.0000
gcd_type:none
min_gcd:0.0000
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:1.50
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
id:2823
name:Deadly Poison
school:physical
tooltip:Each strike has a chance of causing the target to suffer Nature damage every {$2818t1=2} sec for {$2818d=12 seconds}. Subsequent poison applications deal instant Nature damage.
description:Coats your weapons with a Lethal Poison that lasts for {$d=3600 seconds}. Each strike has a {$h=35}% chance to poison the enemy for {$=}{{$2818m1=0}*{$2818d=12 seconds}/{$2818t1=2}} Nature damage over {$2818d=12 seconds}. Subsequent poison applications will instantly deal {$113780s1=0} Nature damage.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Virulent Poisons	381543	#1	10.0%	Talent
	Fatal Concoction	392384	#1	40.0%	Talent
	Implacable	1265386	#2	20.0%	Talent
	Periodic Damage	Virulent Poisons	381543	#2	10.0%	Talent
	Fatal Concoction	392384	#2	40.0%	Talent
	Implacable	1265386	#3	20.0%	Talent
	Proc Chance	Improved Poisons	381624	#1	5.0%	Talent
Deadly Poison (_instant)
	6,846	6.6%	0.0	0.00s	0.0s	0	0	Direct	670.5	2,044	4,210	3,058	46.8%	0.0%
Stats Details: Deadly Poison Instant
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	670.50	0.00	0.00	0.00	0.0000	0.0000	2,050,066.05	2,050,066.05	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	53.21%	356.76	237	473	2,044.26	855	7,215	2,044.18	1,681	2,583	729,302	729,302	0.00%
```
