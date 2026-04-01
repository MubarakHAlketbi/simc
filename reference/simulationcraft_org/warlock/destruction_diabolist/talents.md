# MID1_Warlock_Destruction_Diabolist — Talents & Gear

## Talent Export String
```
CsQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmZmlZjxMLGjFzAAgZmxMzsAGzYYhMw2wGNWYAAgxAjNAMzAYmxYAAAYmZmBAwMDD
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	108,722.6	108,722.6	64.4 / 0.059%	11,197.6 / 10.3%	52.5
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	1,728.8	1,721.8	0.00%	54.1	100.0%
	Talent	CsQAAAAAAAAAAAAAAAAAAAAAAwMzMzoZjhZmZmlZjxMLGjFzAAgZmxMzsAGzYYhMw2wGNWYAAgxAjNAMzAYmxYAAAYmZmBAwMDD
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
	MID1_Warlock_Destruction_Diabolist	108,723
	Chaos Bolt
	23,088	21.2%	58.3	4.13s	79.1s / 26.4%	118,627	87,479	Direct	58.3	0	118,626	118,626	100.0%
Stats Details: Chaos Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	58.30	58.30	0.00	0.00	0.00	1.3561	0.0000	6,915,684.00	6,915,684.00	0.00%	87,479.40	87,479.40
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	58.30	45	70	118,626.39	69,862	230,933	118,692.17	111,399	129,517	6,915,684	6,915,684	0.00%
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
base_dd_mult:1.325080
base_multiplier:1.000000
Spelldata
id:116858
name:Chaos Bolt
school:chromatic
tooltip:
description:Unleashes a devastating blast of chaos, dealing a critical strike for {$=}{2*{$s1=0}} Chaos damage. Damage is further increased by your critical strike chance.
Action Priority List
default[L]:30.70
if_expr:talent.diabolic_ritual&(demonic_art|(variable.ritual_length<action.chaos_bolt.execute_time))&target.health.pct>20
default[S]:27.60
if_expr:(talent.wither&(soul_shard>=4|buff.malevolence.up|pet.infernal.active|fight_remains<=15))|(talent.diabolic_ritual&variable.ritual_length>4)
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cast Time	Improved Chaos Bolt	456951	#2	-500.0	Talent
	Crit	Devastation	454735	#1	6.0%	Talent
	Crit Bonus	Ruin	387103	#1	30.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Chaotic Inferno	1244788	#1	5.0%	Talent
	Emberstorm	454744	#1	2.0%	Talent
	Flames of Xoroth	429657	#1	4.0%	Talent
	Improved Chaos Bolt	456951	#1	10.0%	Talent
	Warlock Destruction 12.0 Class Set 2pc	1264873	#1	5.0%	Set Bonus
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Flames of Xoroth	429657	#2	4.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Demonic Art: Overlord	428524	#1	20.0%	Spell Data
	Demonic Art: Mother of Chaos	432794	#1	20.0%	Spell Data
	Demonic Art: Pit Lord	432795	#1	20.0%	Spell Data
	Percent Cast Time
	Backdraft	117828	#1	-30.0%	Spell Data	No-stacks
	Demonic Art: Overlord	428524	#2	-50.0%	Spell Data
	Demonic Art: Mother of Chaos	432794	#2	-50.0%	Spell Data
	Demonic Art: Pit Lord	432795	#2	-50.0%	Spell Data
	Percent GCD
	Backdraft	117828	#2	-30.0%	Spell Data	No-stacks
	Damage on Debuff
	Immolate	157736	#2	6.0%
	Conflagrate
	11,562	10.6%	40.8	7.39s	42.2s / 14.1%	84,992	82,185	Direct	40.8	20,346	86,011	84,992	98.4%
Stats Details: Conflagrate
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	40.81	40.81	0.00	0.00	0.00	1.0342	0.0000	3,468,357.87	3,468,357.87	0.00%	82,184.68	82,184.68
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	1.55%	0.63	0	1	20,345.72	18,174	23,760	12,886.34	0	23,760	12,886	12,886	0.00%
	crit	98.45%	40.17	32	50	86,011.13	43,958	142,863	85,970.66	80,695	92,264	3,455,472	3,455,472	0.00%
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
base_dd_mult:1.322075
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
default[M]:40.81
if_expr:soul_shard<=4.2&buff.backdraft.stack<1
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Explosive Potential	388827	#1	-2000.0%	Talent
	Crit	Devastation	454735	#1	6.0%	Talent
	Crit Bonus	Ruin	387103	#1	30.0%	Talent
	Direct Damage	Summoner's Embrace	453105	#1	3.0%	Talent
	Emberstorm	454744	#1	2.0%	Talent
	Roaring Blaze	1244310	#1	10.0%	Talent
	Flames of Xoroth	429657	#1	4.0%	Talent
	Warlock Destruction 12.0 Class Set 4pc	1264874	#2	10.0%	Set Bonus
	Hasted Cooldown	Warlock	137042	#2	0.0%	Class Spell
	Periodic Damage	Summoner's Embrace	453105	#3	3.0%	Talent
	Flames of Xoroth	429657	#2	4.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Critical Strike Chance
	Conflagration of Chaos	387109	#1	100.0%	Spell Data
	Diabolic Oculi
	0 (5,455)	0.0% (5.0%)	0.0	0.00s	0.0s	0	0
Stats Details: Diabolic Oculi
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Diabolic Oculi
id:1268709
school:physical
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
id:1268709
name:Diabolic Oculi
school:physical
tooltip:
description:You summon a Diabolic Oculus, up to {$1269643u=3}, each time the duration of Diabolic Ritual is reduced by one of your spells.
Diabolic Oculi explode when consuming Demonic Art, dealing {$1269800s1=0} Fire damage to all enemies within {$1269800=}a1 yds of the target. Damage reduced beyond {$s1=8} targets.
Diabolic Gaze (_3)
	2,544	2.3%	63.0	4.67s	0.0s	12,121	0	Direct	62.6	8,525	17,832	12,203	39.5%
Stats Details: Diabolic Gaze 3
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	62.98	62.56	0.00	0.00	0.00	0.0000	0.0000	763,459.76	763,459.76	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	60.47%	37.83	16	69	8,524.66	7,199	12,384	8,516.08	7,774	9,456	322,510	322,510	0.00%
	crit	39.53%	24.73	8	48	17,832.04	15,055	25,900	17,813.88	16,230	20,331	440,949	440,949	0.00%
Action Details: Diabolic Gaze 3
id:1269885
school:chaos
range:40.0
travel_speed:30.0000
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:2.400000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:1269885
name:Diabolic Gaze
school:chaos
tooltip:
description:Fire a beam of destructive chaos magic at the target, dealing {$s1=0} Chaos damage.
Diabolic Gaze (_2)
	1,947	1.8%	60.6	4.80s	0.0s	9,646	0	Direct	60.5	5,899	14,262	9,667	45.1%
Stats Details: Diabolic Gaze 2
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	60.63	60.50	0.00	0.00	0.00	0.0000	0.0000	584,857.14	584,857.14	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	54.95%	33.24	11	60	5,898.76	4,943	8,583	5,896.51	5,466	6,522	196,101	196,101	0.00%
	crit	45.05%	27.26	6	53	14,262.30	11,956	20,759	14,259.76	13,191	15,756	388,756	388,756	0.00%
Action Details: Diabolic Gaze 2
id:1269886
school:chaos
range:40.0
travel_speed:30.0000
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
spell_power_mod.direct:1.600000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.030000
base_multiplier:1.000000
Spelldata
id:1269886
name:Diabolic Gaze
school:chaos
tooltip:
description:Fire a beam of destructive chaos magic at the target, dealing {$s1=0} Chaos damage.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Devastation
```
