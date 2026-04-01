# MID1_Hunter_Marksmanship — Talents & Gear

## Talent Export String
```
C4PAAAAAAAAAAAAAAAAAAAAAAwCMwMGNWGQmBbAAAAAAAAAzYGzwMmZGzgx0MmZmZ222MzMDzMYmZbwsMYGAAwMzMAwMjNmFDwGG
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	108,732.8	108,732.8	95.6 / 0.088%	16,177.9 / 14.9%	10,009.7
	Resource
	Out
	In
	Waiting
	APM
	Active
	Focus	10.8	10.6	0.00%	47.0	100.0%
	Talent	C4PAAAAAAAAAAAAAAAAAAAAAAwCMwMGNWGQmBbAAAAAAAAAzYGzwMmZGzgx0MmZmZ222MzMDzMYmZbwsMYGAAwMzMAwMjNmFDwGG
	Set Bonus
Root Warden's Regalia (MID_RWR)
Root Warden's Regalia (2pc)
Primal Sentry's Camouflage (MID1)
Hunter Marksmanship 12.0 Class Set 2pc (2pc)
Hunter Marksmanship 12.0 Class Set 4pc (4pc)
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
	MID1_Hunter_Marksmanship	108,733
	Aimed Shot
	43,509 (47,926)	40.0% (44.1%)	68.4	4.34s	123.6s / 41.2%	209,809	116,084	Direct	69.3	0	187,961	187,961	100.0%
Stats Details: Aimed Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	68.41	69.32	0.00	0.00	0.00	1.8074	0.0000	13,029,926.21	18,614,180.30	30.00%	116,084.11	116,084.11
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	69.32	52	86	187,960.81	77,450	487,242	188,083.53	169,244	210,946	13,029,926	18,614,180	30.00%
Action Details: Aimed Shot
id:19434
school:physical
range:40.0
travel_speed:100.0000
radius:8.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:15.000
cooldown hasted:true
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:2.50
base_crit:1.00
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
id:19434
name:Aimed Shot
school:physical
tooltip:
description:A powerful aimed shot that {$?a1273128=true}[critically strikes, dealing {$=}{{$s1=0}*2} Physical damage][deals {$s1=0} Physical damage].
Action Priority List
sentst[I]:68.90
if_expr:cooldown.volley.remains>2|buff.trueshot.up|!talent.volley
target_if_expr:debuff.sentinels_mark.up|max_prio_damage
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Take Aim	1273128	#1	100.0%	Talent
	Crit Bonus	Lethality	1259922	#1	10.0%	Talent
	Direct Damage	Specialized Arsenal	459542	#1	10.0%	Talent
	Hasted Cooldown	Marksmanship Hunter	137016	#6	100.0%	Spec Spell
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
	Periodic Damage	Specialized Arsenal	459542	#2	10.0%	Talent
Aimed Shot (_double_tap)
	4,416	4.1%	0.0	0.00s	0.0s	0	0	Direct	7.4	0	177,998	177,998	100.0%
Stats Details: Aimed Shot Double Tap
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	7.43	0.00	0.00	0.00	0.0000	0.0000	1,322,248.54	1,888,926.48	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	7.43	3	10	177,998.31	62,284	376,447	178,987.13	129,292	263,878	1,322,249	1,888,926	30.00%
Action Details: Aimed Shot Double Tap
id:19434
school:physical
range:40.0
travel_speed:100.0000
radius:8.0
trigger_gcd:1.5000
gcd_type:attack_haste
min_gcd:0.7500
cooldown:15.000
cooldown hasted:true
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:2.50
base_crit:1.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:focus
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:19434
name:Aimed Shot
school:physical
tooltip:
description:A powerful aimed shot that {$?a1273128=true}[critically strikes, dealing {$=}{{$s1=0}*2} Physical damage][deals {$s1=0} Physical damage].
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Take Aim	1273128	#1	100.0%	Talent
	Crit Bonus	Lethality	1259922	#1	10.0%	Talent
	Direct Damage	Specialized Arsenal	459542	#1	10.0%	Talent
	Hasted Cooldown	Marksmanship Hunter	137016	#6	100.0%	Spec Spell
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
	Periodic Damage	Specialized Arsenal	459542	#2	10.0%	Talent
	Arcane Shot
	22,163	20.4%	90.1	3.33s	68.0s / 22.7%	73,745	97,740	Direct	89.9	34,140	103,646	73,878	57.2%
Stats Details: Arcane Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	90.09	89.93	0.00	0.00	0.00	0.7545	0.0000	6,643,609.71	6,643,609.71	0.00%	97,740.39	97,740.39
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	42.83%	38.51	20	65	34,140.44	20,649	57,898	34,143.48	30,208	38,033	1,314,920	1,314,920	0.00%
	crit	57.17%	51.41	30	73	103,646.26	50,561	200,729	103,701.68	89,671	118,293	5,328,690	5,328,690	0.00%
Action Details: Arcane Shot
id:185358
school:arcane
range:40.0
travel_speed:70.0000
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
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:focus
base_cost:40
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:185358
name:Arcane Shot
school:arcane
tooltip:
description:A quick shot that causes $sw2 Arcane damage.{$?s260393=false}[
Arcane Shot has a {$260393h=30}% chance to reduce the cooldown of Rapid Fire by {$=}{{$260393m1=50}/10}.1 sec.][]
Action Priority List
sentst[G]:90.09
if_expr:buff.precise_shots.up
target_if_expr:debuff.sentinels_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Lethality	1259922	#1	10.0%	Talent
	Direct Damage	Take Aim	1273129	#2	6.0%	Talent
	Hasted Gcd	Hunter	137014	#3	0.0%	Class Spell
	Periodic Damage	Take Aim	1273129	#3	6.0%	Talent
	Auto Shot
	1,535	1.4%	76.4	3.95s	0.0s	6,025	1,739	Direct	76.2	3,114	8,391	6,038	55.4%
Stats Details: Auto Shot
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	76.40	76.24	0.00	0.00	0.00	3.4655	0.0000	460,331.94	657,617.05	30.00%	1,738.64	1,738.64
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	44.59%	34.00	17	53	3,113.99	2,935	4,092	3,113.83	2,971	3,329	105,869	151,241	30.00%
	crit	55.41%	42.24	20	64	8,390.94	7,089	13,131	8,391.62	7,633	9,032	354,463	506,376	30.00%
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
base_execute_time:5.00
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
	Crit Bonus	Lethality	1259922	#1	10.0%	Talent
	Direct Damage	Precision Strikes	1267003	#1	25.0%	Talent
	Precise Shots	260240	#2	100.0%	Talent
	Let Fly!
	1,427	1.3%	0.0	0.00s	0.0s	0	0	Direct	37.4	5,462	16,098	11,444	56.2%
Stats Details: Let Fly
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	37.40	0.00	0.00	0.00	0.0000	0.0000	428,025.82	611,465.45	30.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	43.76%	16.37	4	33	5,462.07	5,012	8,554	5,461.70	5,062	6,475	89,397	127,709	30.00%
	crit	56.24%	21.04	8	41	16,097.72	12,272	29,649	16,099.57	13,574	19,849	338,629	483,756	30.00%
Action Details: Let Fly
id:1271682
school:physical
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
id:1271682
name:Let Fly!
school:physical
tooltip:
description:{$@spelldesc1264829=Spending Precise Shots has a small chance to release a volley of arrows at your target, dealing {$1271682s1=0} damage to nearby enemies.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Lethality	1259922	#1	10.0%	Talent
	Direct Damage	Take Aim	1273129	#2	6.0%	Talent
	Periodic Damage	Take Aim	1273129	#3	6.0%	Talent
	Lunar Storm
	8,898	8.2%	0.0	0.00s	0.0s	0	0	Direct	166.1	7,172	21,689	16,045	61.1%
Stats Details: Lunar Storm
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	166.11	0.00	0.00	0.00	0.0000	0.0000	2,665,228.88	2,665,228.88	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	38.88%	64.58	30	115	7,171.98	6,578	9,176	7,177.59	6,796	7,672	463,201	463,201	0.00%
	crit	61.12%	101.53	54	152	21,688.82	16,076	31,828	21,704.79	19,594	24,407	2,202,028	2,202,028	0.00%
Action Details: Lunar Storm
id:1253733
```
