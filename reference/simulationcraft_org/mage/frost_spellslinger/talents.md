# MID1_Mage_Frost_Spellslinger — Talents & Gear

## Talent Export String
```
CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMmZmYmZmZMjZWMzMzMjZAAAgZmZWWmZaDAAAAAAsBw2yYmZGMLzDYMDLAAAMzCwMhBMDGA
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	113,638.2	113,638.2	72.2 / 0.064%	12,467.7 / 11.0%	40.7
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	2,719.5	2,711.6	0.00%	48.0	100.0%
	Talent	CAEAAAAAAAAAAAAAAAAAAAAAAYGGLzMzsMmZmYmZmZMjZWMzMzMjZAAAgZmZWWmZaDAAAAAAsBw2yYmZGMLzDYMDLAAAMzCwMhBMDGA
	Set Bonus
Voidbreaker's Accordance (MID1)
Mage Frost 12.0 Class Set 2pc (2pc)
Mage Frost 12.0 Class Set 4pc (4pc)
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
	MID1_Mage_Frost_Spellslinger	113,638
	Flurry
	0 (9,511)	0.0% (8.4%)	36.4	8.13s	42.9s / 14.3%	78,395	66,593
Stats Details: Flurry
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	36.42	0.00	0.00	0.00	0.00	1.1773	0.0000	0.00	0.00	0.00%	66,592.99	66,592.99
Action Details: Flurry
id:44614
school:frost
range:40.0
travel_speed:50.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:30.000
cooldown hasted:true
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:2500
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Spelldata
id:44614
name:Flurry
school:frost
tooltip:
description:Unleash a flurry of ice, striking the target {$s1=3} times for a total of {$=}{{$228354s1=0}*{$s1=3}} Frost damage.
|CFFffffffApplies {$=}{{$1246769s2=1}*{$s1=3}} {$=}lstack:stacks; of Freezing.|R
Action Priority List
ss_st[K]:25.64
if_expr:buff.brain_freeze.react&buff.thermal_void.down
ss_st[R]:10.78
if_expr:cooldown_react
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Hasted Cooldown	Frost Mage	137020	#5	0.0%	Spec Spell
Flurry (_bolt)
	8,858	7.8%	145.7	2.00s	0.0s	18,253	0	Direct	145.7	12,331	28,906	18,254	35.7%
Stats Details: Flurry Bolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	145.67	145.67	0.00	0.00	0.00	0.0000	0.0000	2,658,974.90	2,658,974.90	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	64.27%	93.62	52	143	12,331.17	7,961	21,803	12,325.65	11,241	13,428	1,154,495	1,154,495	0.00%
	crit	35.73%	52.05	25	87	28,906.48	18,497	49,745	28,904.50	24,834	32,727	1,504,480	1,504,480	0.00%
Action Details: Flurry Bolt
id:228354
school:frost
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
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:1.285200
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.386000
base_multiplier:1.000000
Spelldata
id:228354
name:Flurry
school:frost
tooltip:
description:{$@spelldesc44614=Unleash a flurry of ice, striking the target {$s1=3} times for a total of {$=}{{$228354s1=0}*{$s1=3}} Frost damage.
|CFFffffffApplies {$=}{{$1246769s2=1}*{$s1=3}} {$=}lstack:stacks; of Freezing.|R}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Piercing Cold	378919	#1	20.0%	Talent
	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Frost Mage	137020	#1	5.0%	Spec Spell
	Glacial Attunement	1247759	#1	20.0%	Talent
	Mage Frost 12.0 Class Set 2pc	1264836	#1	10.0%	Set Bonus
	Periodic Damage	Frost Mage	137020	#2	5.0%	Spec Spell
	Mage Frost 12.0 Class Set 2pc	1264836	#2	10.0%	Set Bonus
Glacial Assault
	653	0.6%	17.5	15.86s	0.0s	11,172	0	Direct	17.5	8,014	16,948	11,172	35.3%
Stats Details: Glacial Assault
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	17.54	17.54	0.00	0.00	0.00	0.0000	0.0000	195,999.84	195,999.84	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	64.65%	11.34	1	28	8,014.39	7,039	12,215	8,012.87	7,163	9,274	90,907	90,907	0.00%
	crit	35.35%	6.20	0	17	16,948.10	14,802	25,629	16,906.38	0	23,100	105,093	105,093	0.00%
Action Details: Glacial Assault
id:379029
school:frost
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
spell_power_mod.direct:1.500000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.050000
base_multiplier:1.000000
Spelldata
id:379029
name:Glacial Assault
school:frost
tooltip:
description:{$@spelldesc378947=Flurry has a {$s1=12}% chance each hit to call down an icy comet, crashing into your target and nearby enemies for {$379029s1=0} Frost damage.
|CFFffffffApplies {$s2=1} {$=}lstack:stacks; of Freezing.|R}
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Frost Mage	137020	#1	5.0%	Spec Spell
	Periodic Damage	Frost Mage	137020	#2	5.0%	Spec Spell
	Frost Splinter
	16,346	14.4%	1,380.5	0.23s	0.0s	3,549	0	Direct	1,374.4	2,514	5,306	3,565	37.6%
Stats Details: Frost Splinter
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	1,380.51	1,374.44	0.00	0.00	0.00	0.0000	0.0000	4,899,275.71	4,899,275.71	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	62.36%	857.09	631	1,111	2,513.69	2,126	4,022	2,513.52	2,345	2,733	2,154,471	2,154,471	0.00%
	crit	37.64%	517.35	369	717	5,305.50	4,470	8,458	5,306.59	4,966	5,720	2,744,805	2,744,805	0.00%
Action Details: Frost Splinter
id:443722
school:frost
range:100.0
travel_speed:45.0000
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
spell_power_mod.direct:0.453000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.050000
base_multiplier:1.000000
Spelldata
id:443722
name:Frost Splinter
school:frost
tooltip:
description:Conjure raw Frost magic into a sharp projectile that deals {$s1=0} Frost damage.
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Charm of Aegwynn	1244105	#1	5.0%	Talent
	Direct Damage	Frost Mage	137020	#1	5.0%	Spec Spell
	Periodic Damage	Frost Mage	137020	#2	5.0%	Spec Spell
Controlled Instincts
	0	0.0%	1,374.4	0.22s	0.0s
Stats Details: Controlled Instincts
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	1,374.44	0.00	0.00	0.00	0.00	0.0000	0.0000	0.00	0.00	0.00%	0.00	0.00
Action Details: Controlled Instincts
id:444487
school:frost
range:100.0
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
aoe:5
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
may_crit:false
attack_power_mod.direct:0.000000
spell_power_mod.direct:0.000000
base_dd_min:1312.729737
base_dd_max:1312.729737
base_dd_mult:1.000000
base_multiplier:1.000000
Spelldata
id:444487
name:Controlled Instincts
school:frost
tooltip:
description:{$@spelldesc444483={$?=}c1[{$s1=40}%][{$s4=60}%] of the direct damage dealt by {$?=}c1[an Arcane Splinter][a Frost Splinter] is also dealt to nearby enemies. Damage reduced beyond {$s5=5} targets.}
	Frostbolt
	2,734	2.4%	29.7	8.86s	40.9s / 13.6%	27,668	20,085	Direct	29.7	17,605	40,882	27,668	43.2%
Stats Details: Frostbolt
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	29.69	29.69	0.00	0.00	0.00	1.3776	0.0000	821,603.81	821,603.81	0.00%	20,084.68	20,084.68
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	56.77%	16.86	6	32	17,604.54	15,796	27,307	17,604.95	16,288	19,866	296,749	296,749	0.00%
	crit	43.23%	12.84	2	26	40,882.25	36,700	63,652	40,885.26	37,266	46,501	524,855	524,855	0.00%
Action Details: Frostbolt
id:116
school:frost
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
base_execute_time:1.75
base_crit:0.00
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:mana
base_cost:5000
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:2.448000
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.443750
base_multiplier:1.000000
Spelldata
id:116
name:Frostbolt
school:frost
tooltip:
description:Launches a bolt of frost at the enemy, causing {$228597s1=0} Frost damage and slowing movement speed by {$205708s1=50}% for {$205708d=8 seconds}.{$?a1246769=true}[
|CFFffffffApplies {$1246769s1=1} {$=}lstack:stacks; of Freezing.|R][]
Action Priority List
ss_st[S]:29.69
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit Bonus	Piercing Cold
```
