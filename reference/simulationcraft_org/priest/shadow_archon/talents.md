# MID1_Priest_Shadow_Archon — Talents & Gear

## Talent Export String
```
CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAAAgxYxMGLzMY2mZGzw2MzYmZGbIzYxMNAzAMzmZ0sZAIjxCAmBYMzMjZbMz2yAMDGA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	107,607.1	107,607.1	57.8 / 0.054%	9,887.2 / 9.2%	117.1
	APS
	APS Error
	APS Range
	APR
	195.6	0.8 / 0.406%	104.9 / 53.6%	0.0
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	856.9	851.4	0.00%	52.9	100.0%
	Talent	CIQAAAAAAAAAAAAAAAAAAAAAAMMjZGAAAAAAAAAAAgxYxMGLzMY2mZGzw2MzYmZGbIzYxMNAzAMzmZ0sZAIjxCAmBYMzMjZbMz2yAMDGA
	Set Bonus
Arcanoweave Trappings (MID_AT)
Arcanoweave Trappings (2pc)
Blind Oath's Burden (MID1)
Priest Shadow 12.0 Class Set 2pc (2pc)
Priest Shadow 12.0 Class Set 4pc (4pc)
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
	MID1_Priest_Shadow_Archon	107,607
	Halo
	0 (3,003)	0.0% (2.8%)	5.3	61.47s	5.4s / 1.8%	168,496	165,903
Stats Details: Halo
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	5.35	0.00	0.00	0.00	0.00	1.0156	0.0000	0.00	0.00	0.00%	165,903.32	165,903.32
Action Details: Halo
id:120644
school:shadow
range:46.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:60.000
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
resource:mana
base_cost:10000
secondary_cost:0
energize_type:on_hit
energize_resource:insanity
energize_amount:5.0
Spelldata
id:120644
name:Halo
school:shadow
tooltip:
description:Creates a ring of Shadow energy around you that quickly expands to a {$s2=40} yd radius, healing allies for {$120692s1=0} and dealing {$=}<shadowhalodamage> Shadow damage to enemies. Healing reduced beyond {$s1=6} targets.{$?s137033=true}[
|cFFFFFFFFGenerates {$=}{{$m5=500}/100} Insanity.|r][]
Action Priority List
cds[F]:5.36
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Max Range	Phantom Reach	459559	#1	15.0%	Talent
Halo (_damage_shadow)
	1,966 (3,003)	1.8% (2.8%)	20.9	14.07s	0.0s	43,130	0	Direct	20.8	24,856	49,783	28,309	13.9%
Stats Details: Halo Damage Shadow
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	20.89	20.84	0.00	0.00	0.00	0.0000	0.0000	589,991.50	589,991.50	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	86.14%	17.95	9	24	24,856.24	15,782	38,595	24,838.82	21,656	27,937	446,245	446,245	0.00%
	crit	13.86%	2.89	0	10	49,782.51	31,564	76,463	47,394.92	0	75,735	143,747	143,747	0.00%
Action Details: Halo Damage Shadow
id:390964
school:shadow
range:46.0
travel_speed:57.5000
radius:115.0
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
spell_power_mod.direct:1.442000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:2.511774
base_multiplier:1.000000
Spelldata
id:390964
name:Halo
school:shadow
tooltip:
description:{$@spelldesc120517=Creates a ring of Holy energy around you that quickly expands to a {$s2=40} yd radius, healing allies for {$120692s1=0} and dealing {$=}<holyhalodamage> Holy damage to enemies.
Healing reduced beyond {$s1=6} targets.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Shadow Priest	137033	#1	-14.0%	Spec Spell
	Shadow Priest	137033	#19	178.0%	Spec Spell
	Focused Power	1249230	#1	3.0%	Talent
	Twin Disciplines	1251077	#1	2.0%	Talent
	Max Range	Phantom Reach	459559	#1	15.0%	Talent
	Periodic Damage	Shadow Priest	137033	#2	-14.0%	Spec Spell
	Focused Power	1249230	#2	3.0%	Talent
	Twin Disciplines	1251077	#2	2.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Twist of Fate	390978	#1	10.0%	Spell Data
	Voidform	194249	#1	30.0%	Spell Data	No-stacks
	Shadowform	232698	#1	10.0%	Spell Data
	Periodic Damage
	Twist of Fate	390978	#2	10.0%	Spell Data
	Voidform	194249	#2	30.0%	Spell Data	No-stacks
	Shadowform	232698	#3	10.0%	Spell Data
	Damage on Debuff
	Resonant Energy	453850	#1	2.0%
Halo (_damage_shadow_return)
	1,037	1.0%	10.4	27.70s	0.0s	29,929	0	Direct	10.4	26,304	52,790	30,038	14.1%
Stats Details: Halo Damage Shadow Return
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	10.39	10.35	0.00	0.00	0.00	0.0000	0.0000	311,029.43	311,029.43	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	85.90%	8.90	1	20	26,304.46	16,098	38,440	26,278.60	19,019	33,158	233,977	233,977	0.00%
	crit	14.10%	1.46	0	8	52,789.68	32,195	76,167	41,200.16	0	76,167	77,052	77,052	0.00%
Action Details: Halo Damage Shadow Return
id:390964
school:shadow
range:0.0
travel_speed:57.5000
radius:115.0
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
spell_power_mod.direct:1.442000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:2.511774
base_multiplier:1.000000
Spelldata
id:390964
name:Halo
school:shadow
tooltip:
description:{$@spelldesc120517=Creates a ring of Holy energy around you that quickly expands to a {$s2=40} yd radius, healing allies for {$120692s1=0} and dealing {$=}<holyhalodamage> Holy damage to enemies.
Healing reduced beyond {$s1=6} targets.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Shadow Priest	137033	#1	-14.0%	Spec Spell
	Shadow Priest	137033	#19	178.0%	Spec Spell
	Focused Power	1249230	#1	3.0%	Talent
	Twin Disciplines	1251077	#1	2.0%	Talent
	Max Range	Phantom Reach	459559	#1	15.0%	Talent
	Periodic Damage	Shadow Priest	137033	#2	-14.0%	Spec Spell
	Focused Power	1249230	#2	3.0%	Talent
	Twin Disciplines	1251077	#2	2.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Twist of Fate	390978	#1	10.0%	Spell Data
	Voidform	194249	#1	30.0%	Spell Data	No-stacks
	Shadowform	232698	#1	10.0%	Spell Data
	Periodic Damage
	Twist of Fate	390978	#2	10.0%	Spell Data
	Voidform	194249	#2	30.0%	Spell Data	No-stacks
	Shadowform	232698	#3	10.0%	Spell Data
	Damage on Debuff
	Resonant Energy	453850	#1	2.0%
	Horrific Vision
	1,004	0.9%	25.5	12.22s	0.0s	11,804	0	Direct	25.5	10,344	20,685	11,804	14.1%
Stats Details: Horrific Vision
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	25.51	25.51	0.00	0.00	0.00	0.0000	0.0000	301,154.21	301,154.21	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	85.88%	21.91	12	31	10,344.32	7,165	17,723	10,337.32	9,204	11,630	226,660	226,660	0.00%
	crit	14.12%	3.60	0	12	20,684.73	14,330	35,257	20,197.28	0	34,057	74,494	74,494	0.00%
Action Details: Horrific Vision
id:1243105
school:shadow
range:115.0
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:1.820000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:0.903516
base_multiplier:1.000000
Spelldata
id:1243105
name:Horrific Vision
school:shadow
tooltip:
description:{$@spelldesc373280=You create Horrific Visions when casting harmful spells on enemies.
At {$s1=50} stacks of Horrific Visions, your target sees a nightmare, dealing {$1243105s1=0} Shadow damage and granting you {$=}{{$1243113=}o1/100} Insanity over {$1243113s2=3} sec.
At {$s2=100} stacks, your target witnesses a vision of N'Zoth, dealing {$1243106s1=0} Shadow damage and granting you {$=}{{$1243114=}o1/100} Insanity over {$1243114s2=3} sec.}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Direct Damage	Shadow Priest	137033	#1	-14.0%	Spec Spell
	Focused Power	1249230	#1	3.0%	Talent
	Twin Disciplines	1251077	#1	2.0%	Talent
	Max Range	Phantom Reach	459559	#1	15.0%	Talent
	Periodic Damage	Shadow Priest	137033	#2	-14.0%	Spec Spell
	Focused Power	1249230	#2	3.0%	Talent
	Twin Disciplines	1251077	#2	2.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Twist of Fate	390978	#1	10.0%	Spell Data
	Voidform	194249	#1	30.0%	Spell Data	No-stacks
	Shadowform	232698	#1	10.0%	Spell Data
	Periodic Damage
	Twist of Fate	390978	#2	10.0%	Spell Data
	Voidform	194249	#2	30.0%	Spell Data	No-stacks
	Shadowform	232698	#3	10.0%	Spell Data
	Damage on Debuff
	Resonant Energy	453850	#1	2.0%
	Idol of C'Thun
	0 (2,029)	0.0% (1.9%)	0.0	0.00s	0.0s	0	0
Stats Details: Idol Of Cthun
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	0.00	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Idol Of Cthun
```
