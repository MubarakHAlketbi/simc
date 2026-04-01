# MID1_Shaman_Elemental_Stormbringer — Talents & Gear

## Talent Export String
```
CYQAAAAAAAAAAAAAAAAAAAAAAAAAAAzMbLzMzMzMLbbDMmZAAAAAbmZbzMzwmhFmtZmGamNAYWmZmxYbxEmZ2GLzMzMGWmlZsYmhZWAAGAzMzMGGG
```

## Gear
```
DPS
	DPS(e)
	DPS Error
	DPS Range
	DPR
	124,290.3	124,290.3	144.8 / 0.116%	25,031.2 / 20.1%	479.9
	Resource
	Out
	In
	Waiting
	APM
	Active
	Mana	230.3	230.0	0.00%	50.6	100.0%
	Talent	CYQAAAAAAAAAAAAAAAAAAAAAAAAAAAzMbLzMzMzMLbbDMmZAAAAAbmZbzMzwmhFmtZmGamNAYWmZmxYbxEmZ2GLzMzMGWmlZsYmhZWAAGAzMzMGGG
	Set Bonus
Root Warden's Regalia (MID_RWR)
Root Warden's Regalia (2pc)
Mantle of the Primal Core (MID1)
Shaman Elemental 12.0 Class Set 2pc (2pc)
Shaman Elemental 12.0 Class Set 4pc (4pc)
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
	MID1_Shaman_Elemental_Stormbringer	124,290
	Ascendance
	0 (1,194)	0.0% (1.0%)	3.0	120.67s	2.8s / 0.9%	118,245	125,390
Stats Details: Ascendance
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	2.99	0.00	0.00	0.00	0.00	0.9431	0.0000	0.00	0.00	0.00%	125,389.99	125,389.99
Action Details: Ascendance
id:1219480
school:fire
range:0.0
travel_speed:0.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:120.000
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
id:1219480
name:Ascendance
school:fire
tooltip:Transformed into a powerful Fire Ascendant, empowering your Mastery: Elemental Overload.{$?=}{$=}w3>0[
Haste increased by {$=}w3%.][]
description:Transform into a Flame Ascendant for {$d=15 seconds}, instantly casting a Flame Shock and a {$s1=0}0% effectiveness Lava Burst at up to {$s7=6} nearby enemies.
While ascended, Elemental Overload damage is increased by {$s8=75}% and spells affected by your Mastery: Elemental Overload cause {$s9=1} additional Elemental {$=}LOverload:Overloads;.
Action Priority List
single_target[D]:2.99
if_expr:cooldown.stormkeeper.remains>15|fight_remains<20
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Cooldown	First Ascendant	462440	#1	-60000.0	Talent
Lava Burst (_asc)
	448 (1,194)	0.4% (1.0%)	3.0	120.67s	0.0s	118,245	0	Direct	3.0	0	44,360	44,360	100.0%
Stats Details: Lava Burst Asc
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	2.99	2.99	0.00	0.00	0.00	0.0000	0.0000	132,565.93	132,565.93	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	2.99	2	3	44,359.92	35,631	50,655	44,363.71	40,458	48,852	132,566	132,566	0.00%
Action Details: Lava Burst Asc
id:51505
school:fire
range:40.0
travel_speed:50.0000
radius:-1.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:true
charges:2
base_recharge_multiplier:1.000
base_execute_time:0.00
base_crit:0.10
target:Fluffy_Pillow
aoe:-1
split_aoe_damage:false
harmful:true
Resources
resource:mana
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:maelstrom
energize_amount:8.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:1.389960
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.478046
base_multiplier:1.000000
Spelldata
id:51505
name:Lava Burst
school:fire
tooltip:
description:Hurls molten lava at the target, dealing {$285452s1=0} Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock and its damage is increased by your critical strike chance.{$?a343725=true}[
|cFFFFFFFFGenerates {$343725s3=8} Maelstrom.|r][]
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charges	Echo of the Elements	333919	#1	1.0%	Talent
	Crit	Feedback Loop	1270062	#1	10.0%	Talent
	Crit Bonus	Elemental Fury	60188	#1	125.0%	Talent
	Direct Damage	Elemental Shaman	137040	#1	-14.0%	Spec Spell
	Elemental Shaman	137040	#21	62.0%	Spec Spell
	Fire and Ice	382886	#1	3.0%	Talent
	Elemental Resonance	1258895	#1	3.0%	Talent
	Periodic Damage	Elemental Shaman	137040	#2	-14.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Amplification Core	456369	#1	3.0%	Spell Data
	Elemental Weapons	408390	#1	0.0%	Spell Data	Conditional, Value-function
	Mastery: Elemental Overload	168534	#3	0.68400	Spell Data	Mastery, Passive
	Periodic Damage
	Amplification Core	456369	#2	3.0%	Spell Data
	Elemental Weapons	408390	#2	0.0%	Spell Data	Conditional, Value-function
	Mastery: Elemental Overload	168534	#4	0.68400	Spell Data	Mastery, Passive
Lava Burst Overload (_asc)
	747	0.6%	7.0	120.59s	0.0s	31,689	0	Direct	7.0	0	31,745	31,745	100.0%
Stats Details: Lava Burst Overload Asc
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	6.98	6.97	0.00	0.00	0.00	0.0000	0.0000	221,284.61	221,284.61	0.00%	0.00	0.00
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	crit	100.00%	6.97	2	12	31,744.79	25,540	36,308	31,740.19	28,033	34,971	221,285	221,285	0.00%
Action Details: Lava Burst Overload Asc
id:285466
school:fire
range:100.0
travel_speed:50.0000
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
base_crit:0.10
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:none
base_cost:0
secondary_cost:0
energize_type:none
energize_resource:maelstrom
energize_amount:3.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:1.389960
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:1.434996
base_multiplier:0.421875
Spelldata
id:285466
name:Lava Burst Overload
school:fire
tooltip:
description:Hurls molten lava at the target, dealing {$?a382032=true}[{$=}{{$s1=0}*({$382032s1=25}+{$168534s2=25})/100}][{$=}{{$s1=0}*{$168534s2=25}/100}] Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock.
Generates {$343725s4=3} Maelstrom.|r
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Crit	Feedback Loop	1270062	#1	10.0%	Talent
	Crit Bonus	Elemental Fury	60188	#1	125.0%	Talent
	Direct Damage	Elemental Shaman	137040	#1	-14.0%	Spec Spell
	Elemental Shaman	137040	#21	62.0%	Spec Spell
	Elemental Resonance	1258895	#1	3.0%	Talent
	Periodic Damage	Elemental Shaman	137040	#2	-14.0%	Spec Spell
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Amplification Core	456369	#1	3.0%	Spell Data
	Mastery: Elemental Overload	168534	#3	0.68400	Spell Data	Mastery, Passive
	Periodic Damage
	Amplification Core	456369	#2	3.0%	Spell Data
	Mastery: Elemental Overload	168534	#4	0.68400	Spell Data	Mastery, Passive
	Elemental Blast
	13,018 (17,953)	10.5% (14.5%)	30.7	9.64s	44.1s / 14.7%	175,057	121,844	Direct	30.7	55,565	200,761	127,337	49.4%
Stats Details: Elemental Blast
	Type	Executes	Direct Results	Ticks	Tick Results	Refreshes	Execute Time per Execution	Tick Time per Tick	Actual Amount	Raw Amount	Mitigated	Amount per Total Time	Amount per Total Execute Time
	damage	30.72	30.65	0.00	0.00	0.00	1.4367	0.0000	3,903,049.05	3,903,049.05	0.00%	121,843.82	121,843.82
	Direct Results	Count	Simulation	Iteration Average	Amount
	Percent	Mean	Min	Max	Mean	Min	Max	Mean	Min	Max	Actual	Raw	Mitigated
	hit	50.57%	15.50	4	28	55,565.01	43,925	96,501	55,555.39	48,281	65,462	861,353	861,353	0.00%
	crit	49.43%	15.15	4	28	200,760.82	158,477	346,132	200,775.85	176,763	236,735	3,041,696	3,041,696	0.00%
Action Details: Elemental Blast
id:117014
school:elemental
range:40.0
travel_speed:40.0000
radius:0.0
trigger_gcd:1.5000
gcd_type:spell_cast_speed
min_gcd:0.7500
cooldown:0.000
cooldown hasted:false
category cooldown:false
charges:1
base_recharge_multiplier:1.000
base_execute_time:2.00
base_crit:0.19
target:Fluffy_Pillow
aoe:0
harmful:true
Resources
resource:maelstrom
base_cost:90
secondary_cost:0
energize_type:none
energize_resource:none
energize_amount:0.0
Direct Damage
may_crit:true
attack_power_mod.direct:0.000000
spell_power_mod.direct:2.012500
base_dd_min:0.000000
base_dd_max:0.000000
base_dd_mult:4.768504
base_multiplier:1.000000
Spelldata
id:117014
name:Elemental Blast
school:elemental
tooltip:
description:Harnesses the raw power of the elements, dealing {$s1=0} Elemental damage and increasing your Critical Strike or Haste by {$118522s1=3}% or Mastery by {$=}{{$173184s1=3}*{$168534=}bc1}% for {$118522d=10 seconds}.
Action Priority List
single_target[I]:30.86
target_if_expr:debuff.lightning_rod.remains
Affected By (Passive)
	Type	Spell	ID	Value	Source
	Charge Cooldown	Elemental Shaman	137040	#6	-100.0%	Spec Spell
	Crit	Stormcaller	454021	#1	5.0%	Talent
	Nature's Fury	381655	#1	4.0%	Talent
	Feedback Loop	1270062	#1	10.0%	Talent
	Crit Bonus	Stormcaller	454021	#2	5.0%	Talent
	Elemental Fury	60188	#1	125.0%	Talent
	Direct Damage	Elemental Shaman	137040	#1	-14.0%	Spec Spell
	Elemental Shaman	137040	#18	388.0%	Spec Spell
	Swelling Maelstrom	381707	#2	5.0%	Talent
	Fire and Ice	382886	#1	3.0%	Talent
	Elemental Resonance	1258895	#1	3.0%	Talent
	Natural Gift	1264691	#1	2.0%	Talent
	Periodic Damage	Elemental Shaman	137040	#2	-14.0%	Spec Spell
	Natural Gift	1264691	#2	2.0%	Talent
Affected By (Dynamic)
	Type	Spell	ID	Value	Source	Notes
	Direct Damage
	Amplification Core	456369	#1	3.0%	Spell Data
	Crackling Surge	224127	#1	5.0%	Spell Data
	Molten Weapon	224125	#1	5.0%	Spell Data
	Elemental Weapons	408390	#1	0.0%	Spell Data	Conditional, Value-function
	Mastery: Elemental Overload	168534	#3	0.68400	Spell Data	Mastery, Passive
	Periodic Damage
	Amplification Core	456369	#2	3.0%	Spell Data
	Crackling Surge	224127	#2	5.0%	Spell Data
	Molten Weapon	224125	#2	5.0%	Spell Data
	Elemental Weapons	408390	#2	0.0%	Spell Data	Conditional, Value-function
	Mastery: Elemental Overload	168534	#4	0.68400	Spell Data	Mastery, Passive
Elemental Blast Overload
	4,935	4.0%	41.4	10.64s	0.0s	35,591	0	Direct	41.4	15,399	56,016	35,666
```
