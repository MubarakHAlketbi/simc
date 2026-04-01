# MID1_Death_Knight_Frost_Rider — Buffs & Procs

## Buffs
```
Trigger Count	Interval
	Dynamic Buffs
	Start
	Refresh
	Total
	Start
	Trigger
	Duration
	Uptime
	Benefit
	Overflow
	Expiry
	Alnscorned Essence	5.2	105.1	110.3	20.2s	2.4s	34.5s	59.66%	0.00%	0.0 (0.0)	4.6
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_alnscorned_essence
max_stacks:20
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:strength
amount:34.04
Trigger Details
interval_min/max:0.7s / 212.6s
trigger_min/max:0.7s / 98.9s
trigger_pct:99.99%
duration_min/max:0.0s / 204.6s
uptime_min/max:28.26% / 96.58%
Stack Uptimes
alnscorned_essence_1:3.58%
alnscorned_essence_2:3.78%
alnscorned_essence_3:3.97%
alnscorned_essence_4:4.17%
alnscorned_essence_5:4.39%
alnscorned_essence_6:4.62%
alnscorned_essence_7:4.87%
alnscorned_essence_8:5.14%
alnscorned_essence_9:6.04%
alnscorned_essence_10:6.78%
alnscorned_essence_11:5.99%
alnscorned_essence_12:4.24%
alnscorned_essence_13:1.35%
alnscorned_essence_14:0.38%
alnscorned_essence_15:0.28%
alnscorned_essence_16:0.09%
Spelldata
id:1266687
name:Alnscorned Essence
tooltip:{$=}pri increased by {$=}w1.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:20
duration:12.00
cooldown:0.00
default_chance:101.00%
	Alnsight	7.3	3.8	11.1	39.4s	24.9s	15.9s	38.62%	0.00%	3.8 (3.8)	6.9
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_alnsight
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:12.0s / 139.5s
trigger_min/max:0.0s / 109.0s
trigger_pct:100.00%
duration_min/max:0.0s / 92.2s
uptime_min/max:14.81% / 69.74%
Stack Uptimes
alnsight_1:38.62%
Spelldata
id:1266686
name:Alnsight
tooltip:Casting spells and abilities grants {$@=}spellname1266687.
description:{$@spelldesc1256896=Your damage and healing has a chance to grant you Alnsight for {$1266686d=12 seconds}. While active, casting spells and abilities manifests unstable Alnscorned and consumes their essence to grant you {$s1=19} {$=}pri for {$1266687d=12 seconds}. Multiple applications may overlap.}
max_stacks:0
duration:12.00
cooldown:0.00
default_chance:101.00%
	Anti-Magic Shell	6.8	0.0	6.8	43.9s	43.9s	6.9s	15.75%	0.00%	0.0 (0.0)	6.7
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_antimagic_shell
max_stacks:1
base duration:7.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Absorb Details
school:magic
high priority:no
Trigger Details
interval_min/max:40.0s / 80.2s
trigger_min/max:40.0s / 80.2s
trigger_pct:100.00%
duration_min/max:0.0s / 7.0s
uptime_min/max:13.08% / 18.00%
Stack Uptimes
antimagic_shell_1:15.75%
Spelldata
id:48707
name:Anti-Magic Shell
tooltip:Absorbing up to {$=}w1 magic damage.
Immune to harmful magic effects.
description:Surrounds you in an Anti-Magic Shell for {$d=7 seconds}, absorbing up to {$=}<shield> magic damage and preventing application of harmful magical effects.{$?s207188=false}[][ Damage absorbed generates Runic Power.]
max_stacks:0
duration:7.00
cooldown:40.00
default_chance:101.00%
	Anti-Magic Shell (_horsemen)	6.7	0.0	6.7	48.0s	48.0s	6.9s	15.48%	0.00%	63.7 (63.7)	6.6
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_antimagic_shell_horsemen
max_stacks:1
base duration:7.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:clip
tick_time behavior:hasted
period:1.00
Absorb Details
school:magic
high priority:no
Trigger Details
interval_min/max:45.0s / 94.6s
trigger_min/max:45.0s / 94.6s
trigger_pct:100.00%
duration_min/max:0.0s / 7.0s
uptime_min/max:11.16% / 17.55%
Stack Uptimes
antimagic_shell_horsemen_1:15.48%
Spelldata
id:444741
name:Anti-Magic Shell
tooltip:Absorbing up to {$=}w1 magic damage.
Immune to harmful magic effects.
description:Surrounds your target in an Anti-Magic Shell for {$d=7 seconds}, absorbing up to {$=}<shield> magic damage and preventing application of harmful magical effects.{$?s207188=false}[][ Damage absorbed generates Runic Power.]
max_stacks:0
duration:7.00
cooldown:40.00
default_chance:0.00%
	Apocalyptic Conquest	6.9	0.0	6.9	45.6s	45.3s	24.5s	56.42%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_apocalyptic_conquest
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.05
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:strength
amount:5.00%
Trigger Details
interval_min/max:10.0s / 107.2s
trigger_min/max:10.0s / 107.2s
trigger_pct:100.00%
duration_min/max:0.0s / 45.0s
uptime_min/max:38.27% / 76.89%
Stack Uptimes
apocalyptic_conquest_1:56.42%
Spelldata
id:444763
name:Apocalyptic Conquest
tooltip:Your Strength is increased by {$=}w1%.
description:While Nazgrim is active, gain Apocalyptic Conquest, increasing your Strength by {$s1=5}%.
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Arcanoweave Insight	5.9	5.2	11.1	49.6s	25.0s	26.8s	52.65%	0.00%	5.2 (5.2)	5.4
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_arcanoweave_insight
max_stacks:1
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:strength
amount:87.46
Trigger Details
interval_min/max:20.0s / 183.0s
trigger_min/max:0.0s / 110.0s
trigger_pct:100.00%
duration_min/max:0.0s / 134.3s
uptime_min/max:24.35% / 93.54%
Stack Uptimes
arcanoweave_insight_1:52.65%
Spelldata
id:1229746
name:Arcanoweave Insight
tooltip:{$=}pri increased by {$=}w1.
description:Increases your {$=}pri by $1229511s0.
max_stacks:0
duration:20.00
cooldown:0.00
default_chance:0.00%
	Blood Draw	3.0	0.0	3.0	120.0s	119.9s	7.9s	8.00%	0.00%	0.0 (0.0)	2.9
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_blood_draw
max_stacks:1
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:119.8s / 120.2s
trigger_min/max:119.8s / 120.2s
trigger_pct:100.00%
duration_min/max:0.0s / 8.0s
uptime_min/max:6.67% / 9.68%
Stack Uptimes
blood_draw_1:8.00%
Spelldata
id:454871
name:Blood Draw
tooltip:Damage taken reduced by {$=}w1% and Death Strike cost reduced by {$=}{{$s2=100}/-10}.
description:{$@spelldesc374598=When you fall below {$s1=30}% health you drain {$374606s1=0} health from nearby enemies, the damage you take is reduced by {$454871s1=10}% and your Death Strike cost is reduced by {$=}{{$454871s2=100}/-10} for {$454871d=8 seconds}.
Can only occur every {$374609d=120 seconds}.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:0.00%
	Bloodlust	1.0	0.0	1.0	0.0s	0.0s	40.0s	13.52%	0.00%	0.0 (0.0)	1.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_bloodlust
max_stacks:1
base duration:40.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:0.30
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 0.0s
trigger_min/max:0.0s / 0.0s
trigger_pct:100.00%
duration_min/max:40.0s / 40.0s
uptime_min/max:11.11% / 16.67%
Stack Uptimes
bloodlust_1:13.52%
Spelldata
id:2825
name:Bloodlust
tooltip:Haste increased by {$=}w1%.
description:Increases haste by {$s1=30}% for all party and raid members for {$d=40 seconds}.
Allies receiving this effect will become Sated and unable to benefit from Bloodlust or Time Warp again for {$57724d=600 seconds}.
max_stacks:0
duration:40.00
cooldown:300.00
default_chance:0.00%
	Bonegrinder (_crit)	15.4	44.5	60.0	20.1s	5.0s	8.5s	43.47%	0.00%	3.7 (3.7)	0.3
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_bonegrinder_crit
max_stacks:5
base duration:10.00
duration modifier:1.00
base cooldown:0.70
default_chance:101.00%
default_value:0.01
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:10.0s / 41.1s
trigger_min/max:0.8s / 31.6s
trigger_pct:100.00%
duration_min/max:0.0s / 29.7s
uptime_min/max:34.06% / 56.58%
Stack Uptimes
bonegrinder_crit_1:10.25%
bonegrinder_crit_2:11.73%
bonegrinder_crit_3:10.74%
bonegrinder_crit_4:10.76%
Spelldata
id:377101
name:Bonegrinder
tooltip:Critical Strike chance increased by {$s1=1}%.
description:{$@spelldesc377098=Consuming Killing Machine grants {$377101s1=1}% critical strike chance for {$377101d=10 seconds}, stacking up to {$=}{{$377101u=6}-1} times. At {$=}{{$377101u=6}-1} stacks your next Killing Machine consumes the stacks and grants you {$s1=10}% increased Frost damage for {$377103d=10 seconds}.}
max_stacks:6
duration:10.00
cooldown:0.00
default_chance:101.00%
	Bonegrinder (_frost)	14.7	0.0	14.7	20.8s	20.8s	9.9s	48.15%	49.73%	0.0 (0.0)	14.2
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_bonegrinder_frost
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.20
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:11.8s / 53.0s
trigger_min/max:11.8s / 53.0s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:38.74% / 56.12%
Stack Uptimes
bonegrinder_frost_1:48.15%
Spelldata
id:377103
name:Bonegrinder
tooltip:Frost damage increased by {$s1=0}%.
description:{$@spelldesc377098=Consuming Killing Machine grants {$377101s1=1}% critical strike chance for {$377101d=10 seconds}, stacking up to {$=}{{$377101u=6}-1} times. At {$=}{{$377101u=6}-1} stacks your next Killing Machine consumes the stacks and grants you {$s1=10}% increased Frost damage for {$377103d=10 seconds}.}
max_stacks:1
duration:10.00
cooldown:0.00
default_chance:101.00%
	Breath of Sindragosa	3.7	0.0	3.7	91.2s	91.2s	25.4s	31.50%	0.00%	92.6 (92.6)	3.5
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_breath_of_sindragosa
max_stacks:1
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:tick
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:90.0s / 101.2s
trigger_min/max:90.0s / 101.2s
trigger_pct:100.00%
duration_min/max:0.0s / 55.2s
uptime_min/max:23.31% / 40.73%
Stack Uptimes
breath_of_sindragosa_1:31.50%
Spelldata
id:1249658
name:Breath of Sindragosa
tooltip:Continuously dealing Frost damage every {$t1=1} sec to enemies in a cone in front of you.
description:Call upon Sindragosa's aid in battle for {$d=8 seconds}, continuously dealing {$=}{{$155166s2=0}*{$=}<CAP>/{$=}AP} Frost damage every {$t1=1} sec to enemies in a cone in front of you. Consuming Killing Machine or Rime increases the duration by {$=}{{$s3=800}/1000}.1 sec. Deals reduced damage to secondary targets.
|cFFFFFFFFGrants a charge of Empower Rune Weapon at the start and 2 Runes at the end.|r
max_stacks:0
duration:8.00
cooldown:90.00
default_chance:101.00%
	Charge!	3.7	0.0	3.7	91.2s	91.2s	14.7s	18.29%	0.00%	0.0 (0.0)	3.6
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_charge
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste_rating
amount:677.03
Trigger Details
interval_min/max:90.0s / 101.2s
trigger_min/max:90.0s / 101.2s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:16.19% / 20.94%
Stack Uptimes
charge_1:18.29%
Spelldata
id:1259633
name:Charge!
tooltip:Haste increased by {$=}w1.
description:Lead the charge to gain {$1251817s1=378} Haste for {$d=15 seconds}. All Vanguard of the Light volunteers within 40 yards also gain {$1251817s2=94} Speed for {$1262496d=6 seconds}.
max_stacks:0
duration:15.00
cooldown:90.00
default_chance:0.00%
	Chosen of Frostbrood (FWF)	3.7	0.0	3.7	91.2s	91.2s	10.9s	13.49%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_chosen_of_frostbrood_fwf
max_stacks:1
base duration:45.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:90.0s / 101.2s
trigger_min/max:90.0s / 101.2s
trigger_pct:100.00%
duration_min/max:0.1s / 11.7s
uptime_min/max:11.90% / 15.62%
Stack Uptimes
chosen_of_frostbrood_fwf_1:13.49%
Spelldata
id:1265639
name:Chosen of Frostbrood
tooltip:You may recall your Frostwyrm.
description:{$@spelldesc1265633=Frostwyrm's Fury extends the duration of an active Pillar of Frost by {$=}{{$s1=2000}/1000}.1 sec.
Enduring Strength grants an additional {$s2=4}% Strength.}
max_stacks:1
duration:45.00
cooldown:0.00
default_chance:101.00%
	Chosen of Frostbrood (Haste)	7.4	0.0	7.4	40.4s	40.4s	11.7s	28.92%	0.00%	0.0 (0.0)	7.1
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_chosen_of_frostbrood_haste
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.07
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:7.50%
Trigger Details
interval_min/max:2.0s / 89.0s
trigger_min/max:2.0s / 89.0s
trigger_pct:100.00%
duration_min/max:0.0s / 12.0s
uptime_min/max:25.91% / 32.40%
Stack Uptimes
chosen_of_frostbrood_haste_1:28.92%
Spelldata
id:1265630
name:Chosen of Frostbrood
tooltip:Haste increased by {$=}{{$=}w1}.1%.
description:{$@spelldesc1265632=Frostwyrm's Fury deals {$s1=100}% increased damage to the first enemy it hits and grants you {$1265630s1=15}% Haste for {$1265630d=12 seconds}.}
max_stacks:1
duration:12.00
cooldown:0.00
default_chance:101.00%
	Cryogenic Chamber	7.0	45.3	52.3	45.3s	5.6s	38.1s	88.55%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_cryogenic_chamber
max_stacks:20
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:5.6s / 72.6s
trigger_min/max:1.5s / 48.9s
trigger_pct:100.00%
duration_min/max:0.0s / 54.3s
uptime_min/max:76.79% / 95.46%
Stack Uptimes
cryogenic_chamber_1:13.89%
cryogenic_chamber_2:13.23%
cryogenic_chamber_3:11.66%
cryogenic_chamber_4:11.00%
cryogenic_chamber_5:10.68%
cryogenic_chamber_6:9.82%
cryogenic_chamber_7:8.09%
cryogenic_chamber_8:5.52%
cryogenic_chamber_9:2.90%
cryogenic_chamber_10:1.20%
cryogenic_chamber_11:0.42%
cryogenic_chamber_12:0.13%
cryogenic_chamber_13:0.02%
cryogenic_chamber_14:0.00%
cryogenic_chamber_15:0.00%
Spelldata
id:456370
name:Cryogenic Chamber
tooltip:Remorseless Winter has accumulated {$=}w1 damage.
description:{$@spelldesc456237=When Howling Blast consumes Rime, {$s1=15}% of the damage it deals is gathered into the next cast of Remorseless Winter, up to {$s2=20} times.}
max_stacks:20
duration:30.00
cooldown:0.00
default_chance:101.00%
	Death and Decay	10.1	1.1	11.2	30.2s	27.1s	11.2s	37.60%	0.00%	1.1 (1.1)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_death_and_decay
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:10.0s / 103.3s
trigger_min/max:10.0s / 85.7s
trigger_pct:100.00%
duration_min/max:0.0s / 42.8s
uptime_min/max:20.21% / 55.93%
Stack Uptimes
death_and_decay_1:37.60%
Spelldata
id:188290
name:Death and Decay
tooltip:{$?s206930=false}[Heart Strike will hit up to {$=}{{$m3=3}+2} targets.][Dealing Shadow damage to enemies inside Death and Decay.]
description:{$@spelldesc43265=Corrupts the targeted ground, causing {$=}{{$52212m1=0}*11} Shadow damage over {$d=10 seconds} to targets within the area.{$?s207311=false}&c1[
While you remain within the area, your Heart Strike will hit up to {$188290m3=0} additional targets.][]}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Empower Rune Weapon	14.6	0.0	14.6	20.3s	20.3s	1.1s	1.01%	0.00%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_empower_rune_weapon
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.8s / 97.6s
trigger_min/max:0.8s / 97.6s
trigger_pct:100.00%
duration_min/max:0.0s / 2.1s
uptime_min/max:0.00% / 3.57%
Stack Uptimes
empower_rune_weapon_1:1.01%
Spelldata
id:1230959
name:Empower Rune Weapon
tooltip:
description:{$@spelldesc47568=Drain the will of your enemy to empower your rune weapon, dealing {$s2=0} Shadowfrost damage and reduced damage to enemies nearby, gaining {$=}{{$1230959s1=400}/10} Runic Power, and grants you Killing Machine.}
max_stacks:1
duration:30.00
cooldown:0.00
default_chance:101.00%
	Empowered Strikes	36.4	0.1	36.5	8.3s	8.5s	0.4s	4.44%	31.98%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_empowered_strikes
max_stacks:20
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.8s / 30.6s
trigger_min/max:0.6s / 30.6s
trigger_pct:100.00%
duration_min/max:0.0s / 16.4s
uptime_min/max:0.57% / 11.67%
Stack Uptimes
empowered_strikes_1:4.43%
empowered_strikes_2:0.01%
Spelldata
id:1269300
name:Empowered Strikes
tooltip:Your next Obliterate deals {$=}w1% increased damage.
Your next Frostscythe deals {$=}w2% increased damage.
description:{$@spelldesc47568=Drain the will of your enemy to empower your rune weapon, dealing {$s2=0} Shadowfrost damage and reduced damage to enemies nearby, gaining {$=}{{$1230959s1=400}/10} Runic Power, and grants you Killing Machine.}
max_stacks:20
duration:30.00
cooldown:0.00
default_chance:101.00%
	Enduring Strength	6.8	0.0	6.8	44.9s	44.9s	20.3s	46.05%	0.00%	0.0 (0.0)	6.3
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_enduring_strength
max_stacks:1
base duration:6.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.16
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:39.0s / 61.6s
trigger_min/max:39.0s / 61.6s
trigger_pct:100.00%
duration_min/max:0.0s / 26.0s
uptime_min/max:40.07% / 51.29%
Stack Uptimes
enduring_strength_1:46.05%
Spelldata
id:377195
name:Enduring Strength
tooltip:Strength increased by {$=}w1%.
description:{$@spelldesc377190=When Pillar of Frost expires, your Strength is increased by {$377195s1=8}% for {$377195d=6 seconds}. This effect lasts {$=}{{$s2=2000}/1000} sec longer, up to {$=}{{$s4=20000}/1000} sec, for each Obliterate and Frostscythe critical strike during Pillar of Frost.}
max_stacks:0
duration:6.00
cooldown:0.00
default_chance:0.00%
	Enduring Strength (_builder)	7.0	47.4	54.5	45.5s	5.3s	14.0s	32.88%	99.77%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_enduring_strength_builder
max_stacks:20
base duration:20.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:42.0s / 56.7s
trigger_min/max:0.8s / 45.4s
trigger_pct:100.00%
duration_min/max:0.0s / 17.1s
uptime_min/max:29.41% / 36.13%
Stack Uptimes
enduring_strength_builder_1:4.16%
enduring_strength_builder_2:4.44%
enduring_strength_builder_3:4.67%
enduring_strength_builder_4:4.66%
enduring_strength_builder_5:3.72%
enduring_strength_builder_6:2.44%
enduring_strength_builder_7:2.65%
enduring_strength_builder_8:2.40%
enduring_strength_builder_9:1.98%
enduring_strength_builder_10:0.81%
enduring_strength_builder_11:0.59%
enduring_strength_builder_12:0.32%
enduring_strength_builder_13:0.04%
enduring_strength_builder_14:0.00%
Spelldata
id:377192
name:Enduring Strength
tooltip:When Pillar of Frost expires, you will gain {$377195s1=8}% Strength for {$=}<duration> sec.
description:{$@spelldesc377190=When Pillar of Frost expires, your Strength is increased by {$377195s1=8}% for {$377195d=6 seconds}. This effect lasts {$=}{{$s2=2000}/1000} sec longer, up to {$=}{{$s4=20000}/1000} sec, for each Obliterate and Frostscythe critical strike during Pillar of Frost.}
max_stacks:20
duration:20.00
cooldown:0.00
default_chance:100.00%
	Frost Shield	1.0	171.5	172.5	2.0s	1.7s	298.0s	99.33%	0.00%	171.5 (171.5)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_frost_shield
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Absorb Details
school:chaos
high priority:no
Trigger Details
interval_min/max:2.0s / 2.0s
trigger_min/max:0.0s / 3.2s
trigger_pct:100.00%
duration_min/max:238.0s / 358.0s
uptime_min/max:99.17% / 99.46%
Stack Uptimes
frost_shield_1:99.33%
Spelldata
id:207203
name:Frost Shield
tooltip:Absorbs {$=}w1 damage.
description:{$@spelldesc207200=Your auto attack damage grants you an absorb shield equal to {$s1=40}% of the damage dealt.}
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
	Frozen Dominion	7.1	0.0	7.1	45.6s	45.6s	14.7s	34.64%	0.00%	0.0 (0.0)	6.8
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_frozen_dominion
max_stacks:5
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:4.00
activated:true
reactable:false
reverse:false
refresh behavior:disabled
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:45.0s / 55.6s
trigger_min/max:45.0s / 55.6s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:32.09% / 37.17%
Stack Uptimes
frozen_dominion_1:34.64%
Spelldata
id:377253
name:Frozen Dominion
tooltip:Grants {$=}{{$s1=4}*$mas}% Mastery.
description:{$@spelldesc377226=Pillar of Frost now summons a Remorseless Winter that lasts {$=}{{$1233152d=12 seconds}-{$196770d=8 seconds}} sec longer.
Each enemy Remorseless Winter damages grants you {$=}{{$377253s1=4}*$mastery}% Mastery, up to {$=}{{$s2=4}*$mastery*{$377253u=5}}% for {$287338d=15 seconds}.}
max_stacks:5
duration:15.00
cooldown:0.00
default_chance:101.00%
	Icy Onslaught	38.7	12.5	51.2	7.7s	5.8s	4.4s	57.16%	74.31%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_icy_onslaught
max_stacks:4
base duration:30.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.7s / 32.2s
trigger_min/max:0.8s / 23.3s
trigger_pct:100.00%
duration_min/max:0.0s / 24.7s
uptime_min/max:46.19% / 67.60%
Stack Uptimes
icy_onslaught_1:43.24%
icy_onslaught_2:11.44%
icy_onslaught_3:2.23%
icy_onslaught_4:0.25%
Spelldata
id:1230273
name:Icy Onslaught
tooltip:Damage of Frost Strike and Glacial Advance increased by {$=}w1% and their cost by {$=}{{$=}w2/10} Runic Power.
description:{$@spelldesc1230272=Frost Strike and Glacial Advance now cause your next Frost Strike and Glacial Advance to deal {$1230273s1=15}% increased damage and cost {$=}{{$1230273s2=50}/10} more Runic Power.
This effect stacks until the next Runic Empowerment.}
max_stacks:4
duration:30.00
cooldown:0.00
default_chance:101.00%
	Icy Talons	1.0	177.3	178.3	157.1s	1.7s	295.5s	99.82%	100.00%	173.2 (173.2)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_icy_talons
max_stacks:5
base duration:10.00
duration modifier:1.00
base cooldown:0.50
default_chance:101.00%
default_value:0.06
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:44.1s / 279.0s
trigger_min/max:0.5s / 16.7s
trigger_pct:100.00%
duration_min/max:17.8s / 359.5s
uptime_min/max:97.16% / 99.86%
Stack Uptimes
icy_talons_1:0.64%
icy_talons_2:0.27%
icy_talons_3:0.42%
icy_talons_4:0.48%
icy_talons_5:98.01%
Spelldata
id:194879
name:Icy Talons
tooltip:Attack speed increased by {$=}w1%{$?a436687=false}[, and Runic Power spending abilities deal Shadowfrost damage.][.]
description:{$@spelldesc194878=Your Runic Power spending abilities increase your melee attack speed by {$s1=6}% for {$194879d=10 seconds}, stacking up to {$194879u=3} times.}
max_stacks:5
duration:10.00
cooldown:0.00
default_chance:101.00%
Trigger Spelldata
id:194878
name:Icy Talons
tooltip:
description:Your Runic Power spending abilities increase your melee attack speed by {$s1=6}% for {$194879d=10 seconds}, stacking up to {$194879u=3} times.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:101.00%
	Killing Machine	108.2	44.1	152.3	2.8s	2.0s	1.0s	35.78%	95.78%	7.5 (7.5)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_killing_machine
max_stacks:2
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:1000.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:0.0s / 23.7s
trigger_min/max:0.0s / 23.7s
trigger_pct:100.00%
duration_min/max:0.0s / 9.0s
uptime_min/max:24.49% / 47.59%
Stack Uptimes
killing_machine_1:26.95%
killing_machine_2:8.84%
Spelldata
id:51124
name:Killing Machine
tooltip:Your next Obliterate deals Frost damage, and is guaranteed to be a critical strike.
Your next Frostscythe is guaranteed to be a critical strike and it deals {$51128s2=4} times the normal damage.
description:Your auto attack has a chance to cause your next Obliterate {$?s207230=false}[or Frostscythe ][]to be a guaranteed critical strike.
max_stacks:2
duration:10.00
cooldown:0.00
default_chance:101.00%
	Killing Streak	2.3	105.5	107.8	93.6s	2.8s	130.0s	99.03%	0.00%	0.0 (0.0)	1.3
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_killing_streak
max_stacks:20
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.01
activated:false
reactable:false
reverse:false
refresh behavior:duration
stack behavior:asynchronous
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:haste
amount:1.50%
Trigger Details
interval_min/max:1.0s / 358.8s
trigger_min/max:0.7s / 24.5s
trigger_pct:99.99%
duration_min/max:0.0s / 359.9s
uptime_min/max:91.73% / 99.99%
Stack Uptimes
killing_streak_1:7.40%
killing_streak_2:19.14%
killing_streak_3:22.03%
killing_streak_4:18.42%
killing_streak_5:13.41%
killing_streak_6:8.86%
killing_streak_7:5.37%
killing_streak_8:2.81%
killing_streak_9:1.17%
killing_streak_10:0.35%
killing_streak_11:0.07%
killing_streak_12:0.01%
killing_streak_13:0.00%
killing_streak_14:0.00%
Spelldata
id:1230916
name:Killing Streak
tooltip:Haste increased by {$=}{{$=}W1}.1%.
description:{$@spelldesc1230153=Obliterate and Frostscythe consume all Killing Machines to deal {$s2=25}% increased critical strike damage and grant {$=}{{$1230916s1=15}/10}.1% Haste for {$1230916d=8 seconds} for each stack consumed.
Multiple applications may overlap.}
max_stacks:20
duration:8.00
cooldown:0.00
default_chance:101.00%
	Death Knight Frost 12.0 Class Set 4pc (mid1_4pc_buff)	7.1	0.0	7.1	45.6s	45.6s	3.7s	7.20%	7.56%	0.0 (0.0)	0.3
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_mid1_4pc_buff
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:45.0s / 55.6s
trigger_min/max:45.0s / 55.6s
trigger_pct:100.00%
duration_min/max:0.0s / 15.0s
uptime_min/max:1.07% / 20.97%
Stack Uptimes
mid1_4pc_buff_1:7.20%
Spelldata
id:1269322
name:Death Knight Frost 12.0 Class Set 4pc
tooltip:Your next Empower Rune Weapon incurs no cooldown.
description:{$@spelldesc1264802=Empower Rune Weapon recharges {$s1=20}% faster and Pillar of Frost grants {$s2=1} additional charge.}
max_stacks:1
duration:15.00
cooldown:0.00
default_chance:101.00%
	Mograine's Might	11.2	0.0	11.2	27.0s	27.1s	6.3s	23.45%	38.68%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_mograines_might
max_stacks:1
base duration:0.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:0.05
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:10.0s / 85.7s
trigger_min/max:10.0s / 85.7s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:11.14% / 36.84%
Stack Uptimes
mograines_might_1:23.45%
Spelldata
id:444505
name:Mograine's Might
tooltip:Your damage is increased by {$=}w1%{$?=}c2[ and your critical strike chance is increased by {$s4=5}%][].
description:{$@spelldesc444047=Your damage is increased by {$444505s1=5}% and you gain {$?=}c3[the benefits of your Death and Decay]?c2[{$444505s4=5}% critical strike chance][] while inside Mograine's Death and Decay.}
max_stacks:0
duration:-0.00
cooldown:0.00
default_chance:0.00%
	Pillar of Frost	7.1	0.0	7.1	45.6s	45.6s	14.9s	35.00%	39.19%	0.0 (0.0)	6.8
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_pillar_of_frost
max_stacks:1
base duration:12.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.30
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:strength
amount:30.00%
Trigger Details
interval_min/max:45.0s / 55.6s
trigger_min/max:45.0s / 55.6s
trigger_pct:100.00%
duration_min/max:0.0s / 18.0s
uptime_min/max:32.39% / 37.50%
Stack Uptimes
pillar_of_frost_1:35.00%
Spelldata
id:51271
name:Pillar of Frost
tooltip:Strength increased by {$=}w1%.{$?=}e5[
Increases Remorseless Winter's damage by {$=}w5%, its radius by {$=}w6%, but movement speed is reduced.][]
description:The power of frost increases your Strength by {$s1=30}% for {$d=12 seconds}.
max_stacks:0
duration:12.00
cooldown:45.00
default_chance:101.00%
	Potion of Recklessness (Mastery)	1.5	0.0	1.5	307.8s	307.8s	27.0s	13.17%	0.00%	0.0 (0.0)	1.1
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_potion_of_recklessness_Mastery
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:mastery_rating
amount:1725.00
Trigger Details
interval_min/max:300.0s / 326.1s
trigger_min/max:300.0s / 326.1s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.97% / 18.00%
Stack Uptimes
potion_of_recklessness_Mastery_1:13.17%
Spelldata
id:1236994
name:Potion of Recklessness
tooltip:Granting {$=}w1 {$?=}e1[Critical Strike]?e2[Haste]?e3[Versatility]?e4[Mastery][Highest secondary stat].
Reducing {$?=}e5[Critical Strike]?e6[Haste]?e7[Versatility]?e8[Mastery][lowest secondary stat] by {$=}w10.
description:Gain {$s2=935} of your highest secondary stat while losing {$s6=126} of your lowest secondary stat for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Potion of Recklessness (Vers Penalty)	1.5	0.0	1.5	307.8s	307.8s	27.0s	13.17%	0.00%	0.0 (0.0)	1.1
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_potion_of_recklessness_penalty_Vers
max_stacks:1
base duration:30.00
duration modifier:1.00
base cooldown:300.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:versatility_rating
amount:-232.00
Trigger Details
interval_min/max:300.0s / 326.1s
trigger_min/max:300.0s / 326.1s
trigger_pct:100.00%
duration_min/max:0.0s / 30.0s
uptime_min/max:9.97% / 18.00%
Stack Uptimes
potion_of_recklessness_penalty_Vers_1:13.17%
Spelldata
id:1236994
name:Potion of Recklessness
tooltip:Granting {$=}w1 {$?=}e1[Critical Strike]?e2[Haste]?e3[Versatility]?e4[Mastery][Highest secondary stat].
Reducing {$?=}e5[Critical Strike]?e6[Haste]?e7[Versatility]?e8[Mastery][lowest secondary stat] by {$=}w10.
description:Gain {$s2=935} of your highest secondary stat while losing {$s6=126} of your lowest secondary stat for {$d=30 seconds}.
max_stacks:0
duration:30.00
cooldown:300.00
default_chance:0.00%
	Remorseless Winter	7.1	0.0	7.1	45.6s	45.6s	13.8s	32.38%	0.00%	90.1 (90.1)	6.8
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_remorseless_winter
max_stacks:1
base duration:14.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:45.0s / 55.6s
trigger_min/max:45.0s / 55.6s
trigger_pct:100.00%
duration_min/max:0.0s / 14.0s
uptime_min/max:29.95% / 34.92%
Stack Uptimes
remorseless_winter_1:32.38%
Spelldata
id:1233152
name:Remorseless Winter
tooltip:Dealing {$196771s1=0} Frost damage to enemies within {$196771=}A1 yards each second.{$?s316916=true}[
Frostscythe damage increased by {$=}w4%.][]
description:Drain the warmth of life from all nearby enemies within {$196771=}A1 yards, dealing {$=}{9*{$196771s1=0}*{$=}<CAP>/{$=}AP} Frost damage over {$d=14 seconds} and reducing their movement speed by {$211793s1=20}%.
max_stacks:0
duration:14.00
cooldown:0.00
default_chance:0.00%
	Rime	52.6	0.0	52.7	5.6s	5.6s	2.0s	34.93%	99.89%	0.0 (0.0)	0.0
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_rime
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:60.00%
default_value:-0.00
activated:true
reactable:true
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:1.5s / 49.1s
trigger_min/max:0.8s / 49.1s
trigger_pct:60.14%
duration_min/max:0.0s / 8.4s
uptime_min/max:23.15% / 47.58%
Stack Uptimes
rime_1:34.93%
Spelldata
id:59052
name:Rime
tooltip:Your next Howling Blast will consume no Runes, generate no Runic Power, and deals {$s2=275}% additional damage.
description:Your next Howling Blast will consume no Runes, generate no Runic Power, and deal {$s2=275}% additional damage.
max_stacks:1
duration:15.00
cooldown:0.00
default_chance:100.00%
Trigger Spelldata
id:59057
name:Rime
tooltip:
description:Frost Strike and Glacial Advance have a {$s2=45}% chance to cause your next Howling Blast to consume no runes and deal {$59052s2=275}% additional damage.
max_stacks:0
duration:0.00
cooldown:0.00
default_chance:100.00%
	Rune Mastery	13.1	11.8	24.9	22.9s	11.8s	11.5s	50.16%	0.00%	11.8 (11.8)	12.6
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_rune_mastery
max_stacks:1
base duration:8.00
duration modifier:1.00
base cooldown:0.00
default_chance:15.00%
default_value:0.06
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Trigger Details
interval_min/max:8.0s / 184.6s
trigger_min/max:0.8s / 184.6s
trigger_pct:15.00%
duration_min/max:0.0s / 81.5s
uptime_min/max:17.25% / 75.83%
Stack Uptimes
rune_mastery_1:50.16%
Spelldata
id:374585
name:Rune Mastery
tooltip:Strength increased by {$=}w1%.
description:{$@spelldesc374574=Consuming a Rune has a chance to increase your Strength by {$s1=3}% for {$374585d=8 seconds}.}
max_stacks:0
duration:8.00
cooldown:0.00
default_chance:0.00%
	Unholy Strength	8.5	13.6	22.1	35.7s	13.2s	24.5s	69.56%	0.00%	13.6 (13.6)	7.8
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider
cooldown name:buff_unholy_strength
max_stacks:1
base duration:15.00
duration modifier:1.00
base cooldown:0.00
default_chance:101.00%
default_value:0.18
activated:true
reactable:false
reverse:false
refresh behavior:duration
stack behavior:default
tick behavior:none
tick_time behavior:unhasted
period:0.00
Stat Details
stat:strength
amount:18.00%
Trigger Details
interval_min/max:15.0s / 202.3s
trigger_min/max:0.0s / 57.1s
trigger_pct:100.00%
duration_min/max:0.0s / 206.6s
uptime_min/max:45.16% / 94.36%
Stack Uptimes
unholy_strength_1:69.56%
Spelldata
id:53365
name:Unholy Strength
tooltip:Strength increased by {$s1=15}%.
description:Affixes your rune weapon with a rune that has a chance to heal you for {$53365s2=4}% and increase total Strength by {$53365s1=15}% for {$53365d=15 seconds}.
max_stacks:1
duration:15.00
cooldown:0.00
default_chance:101.00%
	mograine - mograine: Death and Decay	11.2	0.0	11.2	27.0s	27.1s	9.8s	65.08%	0.00%	99.5 (99.5)	10.9
Buff Details
buff initial source:MID1_Death_Knight_Frost_Rider_mograine
cooldown name:buff_death_and_decay
max_stacks:1
base duration:10.00
duration modifier:1.00
base cooldown:0.00
default_chance:100.00%
default_value:-0.00
activated:true
reactable:false
reverse:false
refresh behavior:pandemic
stack behavior:default
tick behavior:clip
tick_time behavior:unhasted
period:1.00
Trigger Details
interval_min/max:10.0s / 85.7s
trigger_min/max:0.1s / 85.7s
trigger_pct:100.00%
duration_min/max:0.0s / 10.0s
uptime_min/max:57.14% / 73.80%
Stack Uptimes
death_and_decay_1:65.08%
Spelldata
id:444474
name:Death and Decay
tooltip:
description:Corrupts the targeted ground, causing {$=}{{$1251951m1=0}*11} Shadow damage over {$d=10 seconds} to targets within the area.{$?=}!c2[
While you remain within the area, your ][]{$?s223829=false}&!c2[Necrotic Strike and ][]{$?=}c1[Heart Strike will hit up to {$188290m3=0} additional targets.]?s207311&!c2[Clawing Shadows will hit up to {$=}{$55090s4-1} enemies near the target.]?!c2[Scourge Strike will hit up to {$=}{$55090s4-1} enemies near the target.][
While you remain within the area, your Obliterate will hit up to {$316916=}M2 additional {$=}Ltarget:targets;.]
max_stacks:0
duration:10.00
cooldown:0.00
default_chance:0.00%
```

## Procs & Uptimes
```
Proc
	Count
	Min
	Max
	Interval
	Min
	Max
	Killing Machine spent on Obliterate	144.3	104.0	190.0	2.8s	0.8s	24.5s
	Killing Machine wasted: Critical auto attacks	2.8	0.0	13.0	67.2s	1.2s	330.0s
	Killing Machine wasted: Empower Rune Weapon	0.9	0.0	6.0	95.6s	1.0s	338.2s
	Killing Machine wasted: Frost Strike	0.8	0.0	6.0	95.7s	0.8s	324.2s
	Killing Machine wasted: Howling Blades	2.7	0.0	14.0	71.4s	2.3s	326.3s
	Killing Machine wasted: Howling Blast	0.3	0.0	4.0	110.9s	1.9s	314.9s
	Killing Machine: Critical auto attacks	52.3	26.0	83.0	5.9s	1.2s	61.1s
	Killing Machine: Empower Rune Weapon	35.6	22.0	46.0	8.5s	0.7s	56.6s
	Killing Machine: Frost Strike	28.0	19.0	40.0	10.4s	0.8s	75.3s
	Killing Machine: Howling Blades	12.9	3.0	29.0	22.2s	1.7s	220.3s
	Killing Machine: Howling Blast	16.0	8.0	25.0	18.4s	1.5s	140.4s
	Razorice from Arctic Assault	107.7	75.0	136.0	2.8s	0.8s	24.5s
	Rune ready	195.9	147.0	249.0	1.8s	0.0s	15.1s
	Skyfury (Main Hand)	28.8	12.0	49.0	10.2s	1.2s	105.8s
```
