# MID1_Warlock_Demonology_Soul_Harvester — Talents & Gear

## Talent Export String
```
CoQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmxsMAAAAAAAjtlBGwAmhtQGbGjx2sMzMjZAAzMzMzAMzMmxMDAAwYmZmZMDLDAD
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	120,996.9	120,996.9	103.1 / 0.085%	17,852.1 / 14.8%	24.3
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	1,912.4	1,901.7	0.00%	51.2	100.0%
	Talent	CoQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmxsMAAAAAAAjtlBGwAmhtQGbGjx2sMzMjZAAzMzMzAMzMmxMDAAwYmZmZMDLDAD
	Set Bonus
Reign of the Abyssal Immolator (MID1)
Warlock Demonology 12.0 Class Set 2pc (2pc)
Warlock Demonology 12.0 Class Set 4pc (4pc)
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
	MID1_Warlock_Demonology_Soul_Harvester	120,997
	Blighted Maw
	1,562	1.3%	0.0	0.00s	0.0s	0	0	Direct	88.9	5,274	0	5,274	0.0%
Stats Details: Blighted Maw
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	88.89	0.00	0.00	0.00	0.0000	0.0000	468,814.77	468,814.77	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	100.00%	88.89	45	127	5,274.07	2,322	12,026	5,268.94	4,122	6,326	468,815	468,815	0.00%
Action Details: Blighted Maw
id:1276960
school:shadowstorm
range:100.0
travel_speed:0.0000
radius:0.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
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
Direct Damage
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:2419.042766
base_dd_max:2419.042766
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:1276960
name:Blighted Maw
school:shadowstorm
tooltip:
description:{$@spelldesc1276956=The fangs of your Dreadstalkers are coated in corrosive bile, causing Dreadbite to deal additional damage equal to {$s1=50}% of damage dealt as Plague damage.}
	Demonbolt
	6,931	5.7%	92.6	3.20s	111.5s / 37.2%	22,463	18,658	Direct	92.4	15,877	37,568	22,526	30.7%
Stats Details: Demonbolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	92.62	92.36	0.00	0.00	0.00	1.2040	0.0000	2,080,435.17	2,080,435.17	0.00%	18,657.61	18,657.61
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	69.35%	64.05	36	91	15,877.05	12,433	28,987	15,874.17	14,570	17,370	1,016,904	1,016,904	0.00%
	crit	30.65%	28.31	9	50	37,568.12	29,408	68,320	37,560.60	32,203	44,763	1,063,532	1,063,532	0.00%
Action Details: Demonbolt
id:264178
school:shadowflame
range:40.0
travel_speed:35.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:4.50
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:5000
secondary_cost:0
energize_type:on_cast
energize_resource:soul_shard
energize_amount:2.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:3.967780
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.056000
base_multiplier:1.000000
Spelldata
id:264178
name:Demonbolt
school:shadowflame
tooltip:
description:Send the fiery soul of a fallen demon at the enemy, causing {$s1=0} Shadowflame damage.{$?=}c2[
|cFFFFFFFFGenerates 2 Soul Shards.|r][]
Action Priority List
soulharvest[R]:71.74
if_expr:soul_shard<4&buff.demonic_core.stack>=2&!talent.doom
soulharvest[S]:20.87
if_expr:soul_shard<4&buff.demonic_core.react
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Demonic Brutality	453908	#1	30.0%	Talent
	Direct Damage	Demonology Warlock	137044	#1	-4.0%	Spec Spell
	Spiteful Reconstitution	428394	#1	10.0%	Talent
	Periodic Damage	Demonology Warlock	137044	#2	-4.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Power Siphon	334581	#1	50.0%	Spell Data	No-stacks
	Percent Cast Time
	Demonic Core	264173	#1	-100.0%	Spell Data	No-stacks
	Demonic Soul
	7,609	6.3%	0.0	0.00s	0.0s	0	0	Direct	66.7	24,135	57,092	34,261	30.7%
Stats Details: Demonic Soul
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	66.69	0.00	0.00	0.00	0.0000	0.0000	2,284,870.87	2,284,870.87	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	69.27%	46.20	24	72	24,134.81	20,564	32,682	24,115.56	22,392	25,837	1,114,994	1,114,994	0.00%
	crit	30.73%	20.49	7	41	57,092.46	48,642	77,582	57,041.31	51,588	63,212	1,169,877	1,169,877	0.00%
Action Details: Demonic Soul
id:449801
school:shadow
range:100.0
travel_speed:0.0000
radius:10.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
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
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:3.532360
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:0.424320
base_multiplier:1.000000
Spelldata
id:449801
name:Demonic Soul
school:shadow
tooltip:
description:{$@spelldesc449614=A demonic entity now inhabits your soul, allowing you to detect if a Soul Shard has a Succulent Soul when it's generated.
Consuming a Succulent Soul unleashes your demonic soul, dealing {$449801s1=0} Shadow damage to all enemies within {$449801=}a1 yds of the target. Damage reduced beyond 8 targets.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Demonic Brutality	453908	#1	30.0%	Talent
	Direct Damage	Demonology Warlock	137044	#1	-4.0%	Spec Spell
	Demonology Warlock	137044	#7	-66.0%	Spec Spell
	Wicked Reaping	449631	#1	30.0%	Talent
	Periodic Damage	Demonology Warlock	137044	#2	-4.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Mastery: Master Demonologist	77219	#5	1.45000	Spell Data	Mastery, Passive
	Hand of Gul'dan
	0 (3,111)	0.0% (2.6%)	95.3	3.12s	112.3s / 37.4%	9,794	8,315
Stats Details: Hand Of Guldan
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	95.33	0.00	0.00	0.00	0.00	1.1778	0.0000	0.00	0.00	0.00%	8,315.43	8,315.43
Action Details: Hand Of Guldan
id:105174
school:shadowflame
range:40.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
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
resource:soul_shard
base_cost:3
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:105174
name:Hand of Gul'dan
school:shadowflame
tooltip:
description:Calls down a demonic meteor full of Wild Imps which burst forth to attack the target.
Deals up to {$=}{{$m1=3}*{$86040m1=0}} Shadowflame damage on impact to all enemies within {$86040=}A1 yds of the target{$?s196283=false}[, applies Doom to each target,][] and summons {$=}{{$m1=3}*{$104317m2=0}} Wild Imps.
Action Priority List
soulharvest[M]:55.71
if_expr:buff.dominion_of_argus.up
soulharvest[Q]:40.00
Hand of Gul'dan (_impact)
	3,111	2.6%	0.0	0.00s	0.0s	0	0	Direct	95.3	6,901	16,328	9,794	30.7%
Stats Details: Hand Of Guldan Impact
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	95.32	0.00	0.00	0.00	0.0000	0.0000	933,606.79	933,606.79	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	69.31%	66.07	38	90	6,900.60	5,911	9,253	6,896.54	6,460	7,306	455,913	455,913	0.00%
	crit	30.69%	29.26	11	51	16,327.77	13,981	21,809	16,317.30	14,834	18,112	477,694	477,694	0.00%
Action Details: Hand Of Guldan Impact
id:86040
school:shadowflame
range:40.0
travel_speed:0.0000
radius:8.0
trigger_gcd:0.0000
gcd_type:spell_cast_speed
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
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.501188
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.324800
base_multiplier:1.000000
Spelldata
id:86040
name:Hand of Gul'dan
school:shadowflame
tooltip:
description:{$@spelldesc105174=Calls down a demonic meteor full of Wild Imps which burst forth to attack the target.
Deals up to {$=}{{$m1=3}*{$86040m1=0}} Shadowflame damage on impact to all enemies within {$86040=}A1 yds of the target{$?s196283=false}[, applies Doom to each target,][] and summons {$=}{{$m1=3}*{$104317m2=0}} Wild Imps.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Demonic Brutality	453908	#1	30.0%	Talent
	Direct Damage	Demonology Warlock	137044	#1	-4.0%	Spec Spell
	Dominion of Argus	1276190	#2	20.0%	Talent
	Warlock Demonology 12.0 Class Set 2pc	1264871	#1	15.0%	Set Bonus
	Periodic Damage	Demonology Warlock	137044	#2	-4.0%	Spec Spell
	Shadow Bolt
	1,257	1.0%	28.5	9.77s	36.1s / 12.0%	13,189	10,411	Direct	29.4	9,009	21,296	12,792	30.8%
Stats Details: Shadow Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	28.50	29.39	0.00	0.00	0.00	1.2668	0.0000	375,920.99	375,920.99	0.00%	10,411.30	10,411.30
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	69.21%	20.34	4	41	9,008.92	7,736	12,112	9,008.27	7,969
```
