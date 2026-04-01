# MID1_Warlock_Destruction_Hellcaller — Talents & Gear

## Talent Export String
```
CsQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmZmlZjxMLGjFzAAgZmxMzsYBGYWMaMDgZL2YAAgxAjNAgZGYmxYAAAYmZmBAwMDD
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	109,082.5	109,082.5	65.7 / 0.060%	11,229.9 / 10.3%	49.4
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	2,019.8	2,011.3	0.00%	57.0	100.0%
	Talent	CsQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmZmlZjxMLGjFzAAgZmxMzsYBGYWMaMDgZL2YAAgxAjNAgZGYmxYAAAYmZmBAwMDD
	Set Bonus
Reign of the Abyssal Immolator (MID1)
Warlock Destruction 12.0 Class Set 2pc (2pc)
Warlock Destruction 12.0 Class Set 4pc (4pc)
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
	MID1_Warlock_Destruction_Hellcaller	109,082
	Blackened Soul
	6,915	6.3%	0.0	0.00s	0.0s	0	0	Direct	220.6	5,733	13,848	9,411	45.3%
Stats Details: Blackened Soul
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	220.59	0.00	0.00	0.00	0.0000	0.0000	2,076,030.14	2,076,030.14	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	54.68%	120.61	75	179	5,733.40	3,845	11,210	5,729.33	5,193	6,400	691,527	691,527	0.00%
	crit	45.32%	99.98	56	148	13,847.84	9,151	26,408	13,837.95	12,668	15,383	1,384,503	1,384,503	0.00%
Action Details: Blackened Soul
id:445736
school:shadowflame
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
base_crit:0.06
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.996334
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:0.988800
base_multiplier:1.000000
Spelldata
id:445736
name:Blackened Soul
school:shadowflame
tooltip:
description:{$@spelldesc440043=Spending Soul Shards on damaging spells will further corrupt enemies affected by your Wither, increasing its stack count by {$s1=1}.
Each time Wither gains a stack it has a chance to collapse, consuming a stack every {$445731t1=1} sec to deal {$445736s1=0} Shadowflame damage to its host until 1 stack remains.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Devastation	454735	#1	6.0%	Talent
	Crit Bonus	Ruin	387103	#1	30.0%	Talent
	Direct Damage	Destruction Warlock	137046	#17	-4.0%	Spec Spell
	Summoner's Embrace	453105	#1	3.0%	Talent
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Chaos Bolt
	31,019	28.4%	56.2	4.25s	76.9s / 25.6%	165,229	120,687	Direct	56.2	0	165,228	165,228	100.0%
Stats Details: Chaos Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	56.19	56.19	0.00	0.00	0.00	1.3691	0.0000	9,284,600.06	9,284,600.06	0.00%	120,687.37	120,687.37
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	56.19	43	69	165,227.59	100,011	292,406	165,340.65	153,180	182,780	9,284,600	9,284,600	0.00%
Action Details: Chaos Bolt
id:116858
school:chromatic
range:40.0
travel_speed:20.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:2.50
base_crit:0.06
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:soul_shard
base_cost:2
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:4.086180
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.896361
base_multiplier:1.000000
Spelldata
id:116858
name:Chaos Bolt
school:chromatic
tooltip:
description:Unleashes a devastating blast of chaos, dealing a critical strike for {$=}{2*{$s1=0}} Chaos damage. Damage is further increased by your critical strike chance.
Action Priority List
default[R]:56.19
if_expr:(talent.wither&(soul_shard>=4|buff.malevolence.up|pet.infernal.active|fight_remains<=15))|(talent.diabolic_ritual&variable.ritual_length>4)
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cast Time	Improved Chaos Bolt	456951	#2	-500.0	Talent
	Crit	Xalan's Cruelty	440040	#1	10.0%	Talent
	Xalan's Ferocity	440044	#4	10.0%	Talent
	Devastation	454735	#1	6.0%	Talent
	Crit Bonus	Ruin	387103	#1	30.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Chaotic Inferno	1244788	#1	5.0%	Talent
	Emberstorm	454744	#1	2.0%	Talent
	Xalan's Cruelty	440040	#3	5.0%	Talent
	Xalan's Ferocity	440044	#1	5.0%	Talent
	Improved Chaos Bolt	456951	#1	10.0%	Talent
	Through the Felvine	1266799	#4	35.0%	Talent
	Warlock Destruction 12.0 Class Set 2pc	1264873	#1	5.0%	Set Bonus
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Xalan's Cruelty	440040	#4	5.0%	Talent
	Xalan's Ferocity	440044	#2	5.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Percent Cast Time
	Backdraft	117828	#1	-30.0%	Spell Data	No-stacks
	Percent GCD
	Backdraft	117828	#2	-30.0%	Spell Data	No-stacks
	Damage on Debuff
	Immolate	157736	#2	6.0%
	Wither	445474	#2	6.0%
	Conflagrate
	11,990	11.0%	44.6	6.87s	42.9s / 14.3%	80,710	83,802	Direct	44.6	20,449	81,522	80,710	98.7%
Stats Details: Conflagrate
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	44.55	44.55	0.00	0.00	0.00	0.9631	0.0000	3,596,014.51	3,596,014.51	0.00%	83,801.69	83,801.69
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	1.33%	0.59	0	1	20,448.55	18,348	22,584	12,114.22	0	22,584	12,114	12,114	0.00%
	crit	98.67%	43.96	34	55	81,521.69	44,379	136,544	81,484.45	76,561	87,033	3,583,900	3,583,900	0.00%
Action Details: Conflagrate
id:17962
school:fire
range:40.0
travel_speed:0.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:10.960
cooldown hasted:true
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.06
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:2500
secondary_cost:0
energize_type:per_hit
energize_resource:soul_shard
energize_amount:0.7
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:3.593090
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.334787
base_multiplier:1.000000
Spelldata
id:17962
name:Conflagrate
school:fire
tooltip:
description:Triggers an explosion on the target, dealing {$s1=0} Fire damage.{$?s196406=true}[
Reduces the cast time of your next Incinerate or Chaos Bolt by {$117828s1=30}% for {$117828d=10 seconds}.][]
|cFFFFFFFFGenerates {$245330s1=5} Soul Shard Fragments.|r
Action Priority List
default[L]:44.56
if_expr:soul_shard<=4.2&buff.backdraft.stack<1
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Explosive Potential	388827	#1	-2000.0%	Talent
	Crit	Xalan's Ferocity	440044	#4	10.0%	Talent
	Devastation	454735	#1	6.0%	Talent
	Crit Bonus	Ruin	387103	#1	30.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Emberstorm	454744	#1	2.0%	Talent
	Roaring Blaze	1244310	#1	10.0%	Talent
	Xalan's Ferocity	440044	#1	5.0%	Talent
	Warlock Destruction 12.0 Class Set 4pc	1264874	#2	10.0%	Set Bonus
	Hasted Cooldown	Warlock	137042	#2	0.0%	Class Spell
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Xalan's Ferocity	440044	#2	5.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Critical Strike Chance
	Conflagration of Chaos	387109	#1	100.0%	Spell Data
	Embers of Nihilam
	0 (5,554)	0.0% (5.1%)	0.0	0.00s	0.0s	0	0
Stats Details: Embers Of Nihilam
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Embers Of Nihilam
id:1265770
school:shadowflame
range:0.0
travel_speed:0.0000
radius:-1.0
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
Spelldata
id:1265770
name:Embers of Nihilam
school:shadowflame
tooltip:
description:Casting Incinerate has a chance to evoke an echo of the Dark Titan's power.
{$@=}spellicon1265884 {$@=}spellname1265884
{$@spelldesc1265884=Hurl an ember torn from Nihilam at the target, dealing {$s1=0} Shadowflame damage and an additional {$s2=0} Shadowflame damage to all enemies within {$=}a2 yds.
Damage reduced beyond {$s3=8} targets.}
Echo of Sargeras
	570	0.5%	0.0	0.00s	0.0s	0	0	Direct	11.0	9,461	22,881	15,599	45.7%
Stats Details: Echo Of Sargeras
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	10.97	0.00	0.00	0.00	0.0000	0.0000	171,148.26	171,148.26	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	54.26%	5.95	0	14	9,461.08	7,388	15,469	9,439.00	0	13,637	56,332	56,332	0.00%
	crit	45.74%	5.02	0	12	22,880.58	17,872	37,005	22,768.65	0	32,169	114,816	114,816	0.00%
Action Details: Echo Of Sargeras
id:1265884
school:shadowflame
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
base_crit:0.06
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
```
