#!/usr/bin/python3
import os
import argparse
import shutil
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pathlib import Path

# Parse command line arguments, fail if none provided
parser = argparse.ArgumentParser(description='Convert arma 2 to arma 3')
parser.add_argument('--input', type=str, help='input directory, the one containing the \'default\' and \'stealth\' folders')
parser.add_argument('--output', type=str, help='output directory')
args = parser.parse_args()
if args.input and args.output:
	A2_DIR = args.input
	A3_DIR = args.output + "RadioProtocolENG/"
	A3_BASE = args.output
else:
    parser.error('Invalid options provided.')

# mappings, sounds not applicable for arma3 are commented out
'''
'DIRS_' 				directories created in createdirs()
'DEFAULT_'				sound files with source in the default folder of input or it's subfolder
'''
# DIRS_
DIRS_Combat = {"010_Vehicles","015_Targeting","020_Names","025_Numbers","030_Teams","035_NumbersGrid","040_MoveDistanceAbsolute1","070_MoveDirectionRelative1","100_Commands","110_Com_Announce","130_Com_Reply","200_CombatShouts","DirectionCompass1","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1",}
DIRS_CombatContact = {"010_Vehicles"}
DIRS_CombatEngage = {"010_Vehicles","020_Names","025_Numbers","030_Teams","035_NumbersGrid","DirectionCompass1","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1",}
DIRS_Normal = {"005_Weapons","010_Vehicles","015_Targeting","020_Names","025_Numbers","030_Teams","035_NumbersGrid","040_MoveDistanceAbsolute1","070_MoveDirectionRelative1","080_MoveAlphabet","090_MoveLocations","100_Commands","110_Com_Announce","120_Com_Ask","130_Com_Reply","140_Com_Status","150_Reporting","220_Support","230_GenericRadioMessages","DirectionCompass1","DirectionCompass2","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1"}
DIRS_NormalContact = {"010_Vehicles"}
DIRS_NormalEngage = {"010_Vehicles","020_Names","025_Numbers","030_Teams","035_NumbersGrid","DirectionCompass1","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1"}
DIRS_NormalTarget = {"010_Vehicles","020_Names","025_Numbers","030_Teams","035_NumbersGrid","DirectionCompass1","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1"}
DIRS_NormalWatch = {"020_Names","025_Numbers","030_Teams","DirectionCompass1"}
DIRS_Stealth = {"010_Vehicles","015_Targeting","020_Names","025_Numbers","030_Teams","035_NumbersGrid","040_MoveDistanceAbsolute1","070_MoveDirectionRelative1","080_MoveAlphabet","090_MoveLocations","100_Commands","110_Com_Announce","120_Com_Ask","130_Com_Reply","140_Com_Status","150_Reporting","200_CombatShouts","220_Support","DirectionCompass1","DirectionCompass2","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1"}
DIRS_StealthEngage = {"010_Vehicles","020_Names","025_Numbers","030_Teams","035_NumbersGrid","DirectionCompass1","DirectionRelative1","DirectionRelative2","DirectionRelative3","DistanceAbsolute1"}
DIRS_StealthWatch = {"020_Names","025_Numbers","030_Teams","DirectionCompass1"}

#Files without destination are commented out
DEFAULT_000_Unused = {
#"And":,ja 
#"AttackThat":,tuhotkaa tuo
#"BailOutE":,ulos äkkiä!COMBAT
#"BeAdvised":,huomio
#"Are":,ootta
#"AtEase":,raauhassa
#"BlueOnBlueE":,omia!
#"BoardThat":,matkustajaksi ajoneuvoon
#"CantShoot":,en pysty ampumaan!
#"ClearedToEngage":,valmiina ampumaan
#"Close":,lähellä
#"ContactE":,vihollista! 
#"DoYouReadQ":,oletteko kuulolla?
#"EnemyFireE":,vihollistulta!
#"Follow":,seuratkaa
#"GoTo":, menkää kohteeseen
#"GoToThat":,menkääs kohteeseen
#"Grid":,karttaruutu
#"GetSupportAt":,huolla ittes kohteessa, aiemmin sinnepäin TODO?
#"GetBackE":,tulkaa takasin muotohon!
#"ImAtGrid":,olen karttaruudussa
#"IsHistory":,on tuhottu
#"Is":,ON!
#"ListenUp":,olkaas kuulolla
#"Loader":,lataajaksi
#"Move":,menkää kohteeseen
#"MoveTo":,menkää kohteeseen
#"MoveToThat":,menkää kohteesehen
#"ObserveThat":,tähystäkää kohdetta
#"OscarMike":,sain
#"PlaceAMine":,aseta miina
#"Position":,sijainti
#"RearmAt":,aseistaudu kohteessa, TODO
#"RefuelAt":,tankkaa kohteessa
#"RepairThat":,korjaa tuo 
#"ReturnTheFlag":,Palauttakaa lippu
#"StandUp":,ylös
#"StatusRedE":,tämä räjähtää kohta!
#"StayCrouched":,polvelle
#"SuppressiveFireE":100:antakees tuli-isku!
#"TakeTheFlag":,ota lippu
#"TakingFireE":,kuulaa tulee!
#"Target":,maali
#"TargetThat":,ota jyvälle tuo
#"ThisIs":,täällä
#"WeLost":,ei helvetti
}
DEFAULT_015_Targeting = {
"015_Targeting/Attack_1":"AttackE",
"015_Targeting/Attack_2":"AttackE",
"015_Targeting/CancelTarget_1":"CancelTarget",
"015_Targeting/CancelTarget_2":"CancelTarget",
"015_Targeting/Engage_1":"EngageE",
"015_Targeting/Engage_2":"EngageThat",
"015_Targeting/Fire_2":"FireE",
"015_Targeting/Fire_1":"Fire",
"015_Targeting/NoTarget_1":"NoTarget",
"015_Targeting/NoTarget_2":"NoTarget",
}

NUMBERS_MOVE_035_NumbersGrid = {
"grid_move_to_eight_1":"eight",
"grid_move_to_eight_2":"eight",
"grid_move_to_five_1":"five",
"grid_move_to_five_2":"five",
"grid_move_to_four_1":"four",
"grid_move_to_four_2":"four",
"grid_move_to_nine_1":"nine",
"grid_move_to_nine_2":"nine",
"grid_move_to_one_1":"one",
"grid_move_to_one_2":"one",
"grid_move_to_seven_1":"seven",
"grid_move_to_seven_2":"seven",
"grid_move_to_six_1":"six",
"grid_move_to_six_2":"six",
"grid_move_to_three_1":"three",
"grid_move_to_three_2":"three",
"grid_move_to_two_1":"two",
"grid_move_to_two_2":"two",
"grid_move_to_zero_1":"zero",
"grid_move_to_zero_2":"zero",
}
NUMBERS_FIRST_035_NumbersGrid = {
"grid_eight_1":"eight",
"grid_five_1":"five",
"grid_four_1":"four",
"grid_nine_1":"nine",
"grid_one_1":"one",
"grid_seven_1":"seven",
"grid_six_1":"six",
"grid_three_1":"three",
"grid_two_1":"two",
"grid_zero_1":"zero",
}
NUMBERS_FIRST_035_NumbersGrid_2 = {
"grid_eight_2":"eight",
"grid_five_2":"five",
"grid_four_2":"four",
"grid_nine_2":"nine",
"grid_one_2":"one",
"grid_seven_2":"seven",
"grid_six_2":"six",
"grid_three_2":"three",
"grid_two_2":"two",
"grid_zero_2":"zero",
}
NUMBERS_LIST_035_NumbersGrid = {
"grid_eight_2_1":"eight",
"grid_eight_2_2":"eight",
"grid_eight_3_1":"eight",
"grid_eight_3_2":"eight",
"grid_five_2_1":"five",
"grid_five_2_2":"five",
"grid_five_3_1":"five",
"grid_five_3_2":"five",
"grid_four_2_1":"four",
"grid_four_2_2":"four",
"grid_four_3_1":"four",
"grid_four_3_2":"four",
"grid_nine_2_1":"nine",
"grid_nine_2_2":"nine",
"grid_nine_3_1":"nine",
"grid_nine_3_2":"nine",
"grid_one_2_1":"one",
"grid_one_2_2":"one",
"grid_one_3_1":"one",
"grid_one_3_2":"one",
"grid_seven_2_1":"seven",
"grid_seven_2_2":"seven",
"grid_seven_3_1":"seven",
"grid_seven_3_2":"seven",
"grid_six_2_1":"six",
"grid_six_2_2":"six",
"grid_six_3_1":"six",
"grid_six_3_2":"six",
"grid_three_2_1":"three",
"grid_three_2_2":"three",
"grid_three_3_1":"three",
"grid_three_3_2":"three",
"grid_two_2_1":"two",
"grid_two_2_2":"two",
"grid_two_3_1":"two",
"grid_two_3_2":"two",
"grid_zero_2_1":"zero",
"grid_zero_2_2":"zero",
"grid_zero_3_1":"zero",
"grid_zero_3_2":"zero",
}

DEFAULT_100_Commands = {
"100_Commands/Advance":"Advance",
"100_Commands/AssembleThatWeapon":"AssembleThat",
"100_Commands/CancelManualFire_1":"CancelManualFire",
"100_Commands/CancelManualFire_2":"CancelManualFire",
"100_Commands/CancelManualFire_3":"CancelManualFire",
"100_Commands/CeaseFire_1":"CeaseFireE",
"100_Commands/CeaseFire_2":"CeaseFireE",
"100_Commands/CheckYourFire":"CheckYourFireE",
"100_Commands/Danger":"DangerE",
"100_Commands/DeactivateCharge":"DeactivateCharge",
"100_Commands/DetonateCharge":"DetonateCharge",
"100_Commands/DisarmThatMine":"DisarmThatMine",
"100_Commands/DisassembleThatWeapon":"DisassembleThat",
"100_Commands/Dismount_2":"Disembark",
"100_Commands/Disengage":"Disengage",
"100_Commands/Dismount_1":"Dismount",
"100_Commands/GetInThatVehicleDriver":"Driver",
"100_Commands/Eject_1":"EjectE",
"100_Commands/Eject_2":"EjectE",
"100_Commands/EngageAtWill":"EngageAtWill",
"100_Commands/GetInThatVehicleCommander":"Commander",
"100_Commands/CopyMyStance":"CopyMyStance",
"100_Commands/FallBack":"FallBackE",
"100_Commands/VehFast_1":"Fast",
"100_Commands/VehFast_2":"Fast",
"100_Commands/VehFast_3":"Fast",
"100_Commands/FireAtWill":"FireAtWill",
"100_Commands/FlankLeft":"FlankLeft",
"100_Commands/FlankRight":"FlankRight",
"100_Commands/FlashlightsOff":"FlashlightsOff",
"100_Commands/FlashlightsOn":"FlashlightsOn",
"100_Commands/FormOnMe":"FormOnMeE",
"100_Commands/VehForward_1":"Forward",
"100_Commands/VehForward_2":"Forward",
"100_Commands/FreeToEngage":"FreeToEngage",
"100_Commands/GoProne_1":"GetDownE",
"100_Commands/GetInThatVehicle":"GetInThat",
"100_Commands/GetSupport":"GetSupportAt",
"100_Commands/GoProne":"GoProne",
"100_Commands/GetInThatVehicleGunner":"Gunner",
"100_Commands/Halt":"Halt",
"100_Commands/HealThatSoldier":"HealThat",
"100_Commands/GoProne_2":"HitTheDirt",
"100_Commands/HoldFire":"HoldFire",
"100_Commands/PointersOff.ogg":"LasersOff",
"100_Commands/PointersOn.ogg":"LasersOn",
"100_Commands/VehLeft_1":"Left",
"100_Commands/VehLeft_2":"Left",
"100_Commands/VehLeft_3":"Left",
"100_Commands/LightThatFire":"LightThatFire",
"100_Commands/ManualFire_1":"ManualFire",
"100_Commands/ManualFire_2":"ManualFire",
"100_Commands/ManualFire_3":"ManualFire",
"100_Commands/ObserveThatPosition":"ObserveThatPosition",
"100_Commands/SuppressiveFire":"OpenUpE",
"100_Commands/GetInThatVehiclePilot":"Pilot",
"100_Commands/PutOutThatFire":"PutOutThatFire",
"100_Commands/Rearm":"RearmAt",
"100_Commands/Regroup":"RegroupE",
"100_Commands/RequestingSupport":"RequestingSupportTo",
"100_Commands/ReturnToFormation":"ReturnToFormationE",
"100_Commands/VehBackward_1":"Reverse",
"100_Commands/VehRight_1":"Right",
"100_Commands/VehRight_2":"Right",
"100_Commands/VehRight_3":"Right",
"100_Commands/ScanHorizon":"ScanHorizon",
"100_Commands/SetCharge":"SetACharge",
"100_Commands/SetTheTimer":"SetTheTimer",
"100_Commands/VehSlow_1":"Slow",
"100_Commands/VehSlow_2":"Slow",
"100_Commands/StayAlert":"StayAlert",
"100_Commands/StayBack":"StayBack",
"100_Commands/CommStealth":"Stealth",
"100_Commands/Stop":"StopE",
"100_Commands/VehStop_1":"StopE",
"100_Commands/VehStop_2":"StopE",
"100_Commands/VehStop_3":"StopE",
"100_Commands/TakeCoverE":"TakeCoverE",
"100_Commands/WeaponsFree":"WeaponsFree",
}
DEFAULT_110_Com_Announce = {
"110_Com_Announce/AreaClear":"AreaClear",
"110_Com_Announce/Clear":"Clear",
"110_Com_Announce/EyesOnTarget":"EyesOnTarget",
"110_Com_Announce/HeIsDown":"HesDownE",
"110_Com_Announce/HostileDown":"HostileDownE",
"110_Com_Announce/IAmTheNewActual":"ImTheNewActual",
"110_Com_Announce/HeIsDown":"IveGotHimE",
"110_Com_Announce/Ready":"Ready",
"110_Com_Announce/ReadyToFire":"ReadyToFire",
"110_Com_Announce/ScratchOne":"ScratchOneE",
"110_Com_Announce/StandingBy":"StandingBy",
"110_Com_Announce/TakingCommand":"TakingCommand",
"110_Com_Announce/TargetAcquired":"TargetAcquired",
"110_Com_Announce/TargetEliminated":"TargetEliminated",
"110_Com_Announce/TargetInSight":"TargetInSight",
"110_Com_Announce/Waiting":"Waiting",
}
DEFAULT_120_Com_Ask = {
"120_Com_Ask/RepeatLastOver":"RepeatLast",
"120_Com_Ask/ReportPosition":"ReportPositionE",
"120_Com_Ask/ReportIn":"ReportStatus",
"120_Com_Ask/SayAgainOver":"SayAgain",
"120_Com_Ask/WhatIsYourLocationQ":"WhereAreYouQ",
}
DEFAULT_130_Com_Reply = {
"130_Com_Reply/Attacking":"AttackingE",
"130_Com_Reply/CannotFire":"CannotFire",
"130_Com_Reply/Confirmation1_1":"Copy",
"130_Com_Reply/Confirmation1_2":"SolidCopy",
"130_Com_Reply/Confirmation1_3":"Understood",
#"130_Com_Reply/Confirmation1_4":"Copy",
#"130_Com_Reply/Confirmation1_5":"Copy",
#"130_Com_Reply/Confirmation1_6":"Copy",
#"130_Com_Reply/Confirmation1_7":"Copy",
#"130_Com_Reply/Confirmation1_8":"Copy",
#"130_Com_Reply/Confirmation1_9":"Copy",
#"130_Com_Reply/Confirmation1_10":"Copy",
"130_Com_Reply/Engaging":"EngagingE",
"130_Com_Reply/EngagingTarget":"EngagingTargetE",
"130_Com_Reply/Negative_1":"Negative",
#"130_Com_Reply/Negative_2":"Negative",
#"130_Com_Reply/Negative_3":"Negative",
"130_Com_Reply/NoCanDo_1":"NoCanDo",
#"130_Com_Reply/NoCanDo_2":"NoCanDo",
"130_Com_Reply/OnTheWay_1":"OnTheWay",
#"130_Com_Reply/OnTheWay_2":"OnTheWay",
#"130_Com_Reply/OnTheWay_3":"OnTheWay",
"130_Com_Reply/Confirmation2_1":"Roger",
#"130_Com_Reply/Confirmation2_2":"Roger",
#"130_Com_Reply/Confirmation2_3":"Roger",
#"130_Com_Reply/Confirmation2_4":"Roger",
#"130_Com_Reply/Confirmation2_5":"Roger",
#"130_Com_Reply/Confirmation2_6":"Roger",
#"130_Com_Reply/Confirmation2_7":"Roger",
#"130_Com_Reply/Confirmation2_8":"Roger",
#"130_Com_Reply/Confirmation2_9":"Roger",
#"130_Com_Reply/Confirmation2_10":"Roger",
}
DEFAULT_140_Com_Status = {
"140_Com_Status/FuelLow_1":"BingoFuel",
"140_Com_Status/FuelLow_2":"BingoFuel",
"140_Com_Status/CriticalDamage_1":"CriticalDamageE",
"140_Com_Status/CriticalDamage_2":"CriticalDamageE",
"140_Com_Status/HealthInjured":"Injured",
"140_Com_Status/HeIsDeadE":"IsDead",
"140_Com_Status/HeIsHitE":"IsDownE",
"140_Com_Status/HealthMedic":"MedicE",
"140_Com_Status/HealthNeedMedicNow":"MedicE",
"140_Com_Status/HealthINeedHelpNow":"NeedHelpE",
"140_Com_Status/AmmoCritical_1":"NoMoreAmmoE",
"140_Com_Status/AmmoCritical_2":"OutOfAmmoE",
"140_Com_Status/AmmoCritical_3":"NoMoreAmmoE",
"140_Com_Status/AmmoLow":"RunningOutOfAmmo",
"140_Com_Status/FuelCritical_1":"OutOfFuelE",
"140_Com_Status/FuelCritical_2":"RunningOutOfFuel",
"140_Com_Status/HealthINeedSomeHelpHere":"SomebodyHelpMeE",
"140_Com_Status/HealthIAmWounded":"WoundedE",
}
DEFAULT_150_Reporting = {
"150_Reporting/EnemyDetected_1":"HostilesE",
"150_Reporting/EnemyDetected_2":"combat/CS_HostilesE",
#"150_Reporting/EnemyDetected_3":"HostilesE",
#"150_Reporting/EnemyDetected_4":"HostilesE",
#"150_Reporting/EnemyDetected_5":"HostilesE",
#"150_Reporting/EnemyDetected_6":"HostilesE",
#"150_Reporting/EnemyDetected_7":"HostilesE",
#"150_Reporting/EnemyDetected_8":"HostilesE",
#"150_Reporting/EnemyDetected_9":"HostilesE",
#"150_Reporting/EnemyDetected_10":"HostilesE",
"150_Reporting/BombDetected_1":"weapons/Bombs",
"150_Reporting/MineDetected_1":"weapons/Mine",
"150_Reporting/ExplosiveDetected_1":"weapons/Charge",
}

DEFAULT_ALPHABET = {"alpha","bravo","charlie","delta","echo","fotxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","whiskey","xray","yankee","zulu",}

CLOCKFACING_DirectionRelative1 = {
"DirectionRelative1/back_1":"at6",
"DirectionRelative1/back_2":"at6",
"DirectionRelative1/front_1":"at12",
"DirectionRelative1/front_2":"at12",
"DirectionRelative1/left_1":"at9",
"DirectionRelative1/left_2":"at9",
"DirectionRelative1/right_1":"at3",
"DirectionRelative1/right_2":"at3",
}
CLOCKFACING_DirectionRelative2 = {
"DirectionRelative2/at10":"at10",
"DirectionRelative2/at11":"at11",
"DirectionRelative2/at12":"at12",
"DirectionRelative2/at1":"at1",
"DirectionRelative2/at2":"at2",
"DirectionRelative2/at3":"at3",
"DirectionRelative2/at4":"at4",
"DirectionRelative2/at5":"at5",
"DirectionRelative2/at6":"at6",
"DirectionRelative2/at7":"at7",
"DirectionRelative2/at8":"at8",
"DirectionRelative2/at9":"at9",
}
CLOCKFACING_DirectionRelative3 = {
"DirectionRelative3/reportBack_1":"at6",
"DirectionRelative3/reportBack_2":"at6",
"DirectionRelative3/reportBack_3":"at6",
"DirectionRelative3/reportBack_4":"at6",
"DirectionRelative3/reportFront_1":"at12",
"DirectionRelative3/reportFront_2":"at12",
"DirectionRelative3/reportFront_3":"at12",
"DirectionRelative3/reportFront_4":"at12",
"DirectionRelative3/reportLeft_1":"at9",
"DirectionRelative3/reportLeft_2":"at9",
"DirectionRelative3/reportLeft_3":"at9",
"DirectionRelative3/reportLeft_4":"at9",
"DirectionRelative3/reportRight_1":"at3",
"DirectionRelative3/reportRight_2":"at3",
"DirectionRelative3/reportRight_3":"at3",
"DirectionRelative3/reportRight_4":"at3",
}

DEFAULT_200_CombatShouts = {
"200_CombatShouts/ContactE":"combat/CS_ContactE",
"200_CombatShouts/CoveringE_1":"combat/CS_CoveringFireE",
"200_CombatShouts/CoveringE_2":"combat/CS_CoveringGoE",
"200_CombatShouts/CoveringE_3":"combat/CS_GoILLCoverE",
"200_CombatShouts/CoveringE_4":"combat/CS_GoImCoveringE",
"200_CombatShouts/CoverMeE":"combat/CS_CoverMeE",
"200_CombatShouts/ReloadingE_1":"combat/CS_ReloadingE",
"200_CombatShouts/ReloadingE_2":"combat/CS_ChangingMagsE",
"200_CombatShouts/ReloadingE_3":"combat/CS_CoverMeWhileIReloadE",
"200_CombatShouts/ReloadingE_4":"combat/CS_IgottaReloadE",
"200_CombatShouts/SuppressingE_1":"combat/CS_SuppresiveFireE",
"200_CombatShouts/ThrowingGrenadeE_1":"combat/CS_FireInTheHoleE",
"200_CombatShouts/ThrowingSmokeE_1":"weapons/Smoke",
"200_CombatShouts/UnderFireE_1":"UnderFireE",
"200_CombatShouts/UnderFireE_2":"TakingFireE",
"200_CombatShouts/WitnessKilledE_1":"HesDownE",
#"200_CombatShouts/":"combat/CS_GoE",
#"200_CombatShouts/":"combat/CS_HostilesE",
#"200_CombatShouts/":"combat/CS_MoveE",
#"200_CombatShouts/":"combat/CS_MoveOutE",
#"200_CombatShouts/":"combat/CS_MovingE",
#"200_CombatShouts/":"combat/CS_MovinOutE",
#"200_CombatShouts/":"combat/CS_OKLetsGo",
#"200_CombatShouts/":"combat/CS_EngagingE",
}

DIRECTION_DirectionCompass1 = {
"DirectionCompass1/east_1":"East",
"DirectionCompass1/northEast_1":"Northeast",
"DirectionCompass1/north_1":"North",
"DirectionCompass1/northWest_1":"Northwest",
"DirectionCompass1/southEast_1":"Southeast",
"DirectionCompass1/south_1":"South",
"DirectionCompass1/southWest_1":"Southwest",
"DirectionCompass1/west_1":"West",
#"East":"DirectionCompass1/east_2",
#"Northeast":"DirectionCompass1/northEast_2",
#"North":"DirectionCompass1/north_2",
#"Northwest":"DirectionCompass1/northWest_2",
#"Southeast":"DirectionCompass1/southEast_2",
#"South":"DirectionCompass1/south_2",
#"Southwest":"DirectionCompass1/southWest_2",
#"West":"DirectionCompass1/west_2",
}
DEFAULT_DirectionCompass2 = {
"DirectionCompass2/bearing000":"direction/North",
"DirectionCompass2/bearing015":"direction/North",
"DirectionCompass2/bearing030":"direction/Northeast",
"DirectionCompass2/bearing045":"direction/Northeast",
"DirectionCompass2/bearing060":"direction/Northeast",
"DirectionCompass2/bearing075":"direction/East",
"DirectionCompass2/bearing090":"direction/East",
"DirectionCompass2/bearing105":"direction/East",
"DirectionCompass2/bearing120":"direction/Southeast",
"DirectionCompass2/bearing135":"direction/Southeast",
"DirectionCompass2/bearing150":"direction/Southeast",
"DirectionCompass2/bearing165":"direction/South",
"DirectionCompass2/bearing180":"direction/South",
"DirectionCompass2/bearing195":"direction/South",
"DirectionCompass2/bearing210":"direction/Southwest",
"DirectionCompass2/bearing225":"direction/Southwest",
"DirectionCompass2/bearing240":"direction/Southwest",
"DirectionCompass2/bearing255":"direction/West",
"DirectionCompass2/bearing270":"direction/West",
"DirectionCompass2/bearing285":"direction/West",
"DirectionCompass2/bearing300":"direction/Northwest",
"DirectionCompass2/bearing315":"direction/Northwest",
"DirectionCompass2/bearing330":"direction/Northwest",
"DirectionCompass2/bearing345":"direction/North",
"DirectionCompass2/bearing360":"direction/North",
}
DIRECTION_Unused = {
#"Close":"",
#"Far":"",
#"front":"",
#"MediumRange":"",
#"rear":"",
}

FORMATION_100_Commands = {
"100_Commands/FormColumn":"FormColumn",
"100_Commands/FormDiamond":"FormDiamond",
"100_Commands/FormEcholonLeft":"FormEcholonLeft",
"100_Commands/FormEcholonRight":"FormEcholonRight",
"100_Commands/FormFile":"FormFile",
"100_Commands/FormLine":"FormLine",
"100_Commands/FormStaggeredColumn":"FormStaggeredColumn",
"100_Commands/FormWedge":"FormWedge",
"100_Commands/FormVee":"FormWedge",
}

MAPCOORDS = {
"Eight2":"",
"Five2":"",
"Four2":"",
"nine2":"",
"One2":"",
"Seven2":"",
"Six2":"",
"Three2":"",
"Two2":"",
"Zero2":"",
}

NUMBERS_025_Numbers = {
#"All":025:"",
"025_Numbers/eighteen":"Eighteen",
"025_Numbers/eight":"Eight",
"025_Numbers/eighty":"Eighty",
"025_Numbers/eleven":"Eleven",
"025_Numbers/fifteen":"Fifteen",
"025_Numbers/fifty":"Fifty",
"025_Numbers/five":"Five",
"025_Numbers/forty":"Forty",
"025_Numbers/four":"Four",
"025_Numbers/fourteen":"Fourteen",
"025_Numbers/hundred":"Hundred",
"025_Numbers/nine":"nine",
"025_Numbers/nineteen":"Nineteen",
"025_Numbers/ninety":"Ninety",
"025_Numbers/one":"One",
"025_Numbers/seven":"Seven",
"025_Numbers/seventeen":"Seventeen",
"025_Numbers/seventy":"Seventy",
"025_Numbers/six":"Six",
"025_Numbers/sixteen":"Sixteen",
"025_Numbers/sixty":"Sixty",
"025_Numbers/ten":"Ten",
"025_Numbers/thirteen":"Thirteen",
"025_Numbers/thirty":"Thirty",
"025_Numbers/three":"Three",
"025_Numbers/twelve":"Twelve",
"025_Numbers/twenty":"Twenty",
"025_Numbers/two":"Two",
"025_Numbers/zero":"Zero",
}

DEFAULT_OBJECTS = {
#"ammocrate":"",
#"building":"",
#"bunker":"",
#"bush":"",
#"cargoContainer":"",
#"church":"",
#"cross":"",
#"fence":"",
#"flag":"",
#"house":"",
#"LaserTarget":"",
#"object":"",
#"rock":"",
#"ruin":"",
#"structure":"",
#"target":"",
#"tent":"",
#"tower":"",
#"tree":"",
#"wall":"",
#"wreck":"",
}

DEFAULT_SIDE = {
#"Enemy":"",vihollisia
#"Friendly":"",omia
#"Neutral":"",puolueettomia
#"Unknown":"",tuntemattomia
}

SOM_220_Support = {
"220_Support/SupportRequestRGCASHelicopter":"RequestingCloseAirSupportAtGrid",
"220_Support/SupportRequestRGArty":"RequestingFireSupportAtGrid",
#"":"RequestingReinforcementsToOurPositionGrid",
"220_Support/SupportRequestRGSupplyDrop":"RequestingSupplyDropAtGrid",
}

TEAM_030_Teams = {
#"allGroup":"",
"030_Teams/blueTeam":"blueTeam",
"030_Teams/greenTeam":"greenTeam",
"030_Teams/redTeam":"redTeam",
"030_Teams/whiteTeam":"whiteTeam",
"030_Teams/yellowTeam":"yellowTeam",
}

VEHICLES_010_Vehicles = {
"010_Vehicles/veh_air_s":"aircraft",
"010_Vehicles/veh_air_p":"aircrafts",
"010_Vehicles/veh_plane_s":"airplane",
"010_Vehicles/veh_plane_p":"airplanes",
"010_Vehicles/veh_vehicle_APC_s":"APC",
"010_Vehicles/veh_vehicle_APC_p":"APCs",
"010_Vehicles/veh_ship_boat_s":"boat",
"010_Vehicles/veh_ship_boat_p":"boats",
"010_Vehicles/veh_vehicle_car_s":"car",
"010_Vehicles/veh_vehicle_car_p":"cars",
"010_Vehicles/veh_air_gunship_s":"gunship",
"010_Vehicles/veh_air_gunship_p":"gunships",
"010_Vehicles/veh_helicopter_s":"helicopter",
"010_Vehicles/veh_helicopter_p":"helicopters",
"010_Vehicles/veh_infantry_AA_s":"launcherSoldier",
"010_Vehicles/veh_infantry_AA_p":"launcherSoldiers",
"010_Vehicles/veh_infantry_AT_s":"launcherSoldier",
"010_Vehicles/veh_infantry_AT_p":"launcherSoldiers",
"010_Vehicles/veh_infantry_medic_s":"Medic",
"010_Vehicles/veh_infantry_medic_p":"Medics",
"010_Vehicles/veh_infantry_MG_s":"MGunner",
"010_Vehicles/veh_infantry_MG_p":"Mgunners",
"010_Vehicles/veh_infantry_officer_s":"officer",
"010_Vehicles/veh_infantry_officer_p":"officers",
"010_Vehicles/veh_air_parachute_s":"parachute",
"010_Vehicles/veh_air_parachute_p":"parachutes",
"010_Vehicles/veh_infantry_pilot_s":"pilot",
"010_Vehicles/veh_infantry_pilot_p":"pilots",
"010_Vehicles/veh_ship_s":"ship",
"010_Vehicles/veh_ship_p":"ships",
"010_Vehicles/veh_submarine_s":"ship",
"010_Vehicles/veh_submarine_p":"ships",
"010_Vehicles/veh_infantry_Sniper_s":"Sniper",
"010_Vehicles/veh_infantry_Sniper_p":"Snipers",
"010_Vehicles/veh_infantry_s_1":"soldier",
"010_Vehicles/veh_infantry_p_1":"soldiers",
"010_Vehicles/veh_infantry_SF_s":"SpecialForce",
"010_Vehicles/veh_infantry_SF_p":"SpecialForces",
"010_Vehicles/veh_static_AA_s":"staticAALauncher",
"010_Vehicles/veh_static_AA_p":"staticAALaunchers",
"010_Vehicles/veh_static_AA_s":"staticATLauncher",
"010_Vehicles/veh_static_AA_p":"staticATLaunchers",
"010_Vehicles/veh_static_cannon_s":"staticCannon",
"010_Vehicles/veh_static_cannon_p":"staticCannons",
"010_Vehicles/veh_static_GL_s":"staticgrenadelauncher",
"010_Vehicles/veh_static_GL_p":"staticgrenadelaunchers",
"010_Vehicles/veh_static_p":"staticLaunchers",
"010_Vehicles/veh_Static_MG_s":"StaticMGWeapon",
"010_Vehicles/veh_Static_MG_p":"StaticMGWeapons",
"010_Vehicles/veh_Static_mortar_s":"StaticMortar",
"010_Vehicles/veh_Static_mortar_p":"StaticMortars",
"010_Vehicles/veh_vehicle_tank_s":"tank",
"010_Vehicles/veh_vehicle_tank_p":"tanks",
"010_Vehicles/veh_vehicle_armedcar_s":"technical",
"010_Vehicles/veh_vehicle_armedcar_p":"technicals",
"010_Vehicles/veh_vehicle_truck_s":"truck",
"010_Vehicles/veh_vehicle_truck_p":"trucks",
"010_Vehicles/veh_air_uav_s":"UAV",
"010_Vehicles/veh_air_uav_p":"UAVs",
"010_Vehicles/veh_vehicle_s":"vehicle",
"010_Vehicles/veh_vehicle_p":"vehicles",
}

VEHICLES_ENGAGE = {
"veh_air_s":"aircraft",
"veh_plane_s":"airplane",
"veh_vehicle_APC_s":"APC",
"veh_ship_boat_s":"boat",
"veh_vehicle_car_s":"car",
"veh_air_gunship_s":"gunship",
"veh_helicopter_s":"helicopter",
"veh_infantry_AA_s":"launcherSoldier",
"veh_infantry_AT_s":"launcherSoldier",
"veh_infantry_medic_s":"Medic",
"veh_infantry_MG_s":"MGunner",
"veh_infantry_officer_s":"officer",
"veh_air_parachute_s":"parachute",
"veh_infantry_pilot_s":"pilot",
"veh_ship_s":"ship",
"veh_submarine_s":"ship",
"veh_infantry_Sniper_s":"Sniper",
"veh_infantry_s_1":"soldier",
"veh_infantry_SF_s":"SpecialForce",
"veh_static_AA_s":"staticAALauncher",
"veh_static_AA_s":"staticATLauncher",
"veh_static_cannon_s":"staticCannon",
"veh_static_GL_s":"staticgrenadelauncher",
"veh_Static_MG_s":"StaticMGWeapon",
"veh_Static_mortar_s":"StaticMortar",
"veh_vehicle_tank_s":"tank",
"veh_vehicle_armedcar_s":"technical",
"veh_vehicle_truck_s":"truck",
"veh_air_uav_s":"UAV",
"veh_vehicle_s":"vehicle",
}

WEAPONS_005_Weapons = {
#"AALauncher":,
#"ATLauncher":,
#"Backpack":,
#"Binocular":,
#"Charge":,
#"Flare":,
#"GrenadeLauncher":,
#"Grenade":,
#"HandGrenade":,
#"Handgun":,
#"LaserDesignator":,
#"Magazine":,
#"Mine":,
#"NVG":,
#"Rifle":,
#"Smoke":,
#"SmokeShell":,
#"SniperRifle":,
"005_Weapons/Bombs":"weapons/Bombs",
"005_Weapons/cannon":"weapons/cannonHigh",
"005_Weapons/cannonHigh":"weapons/cannonHigh",
"005_Weapons/cannonLow":"weapons/cannonLow",
"005_Weapons/Flares":"weapons/Flares",
"005_Weapons/mgun":"weapons/MachineGun",
"005_Weapons/missiles":"weapons/Missiles",
"005_Weapons/Rockets":"weapons/Rockets",
"005_Weapons/RocketsPairs":"weapons/Rockets",
"005_Weapons/RocketsSalvo":"weapons/Rockets",
}
DISTANCE_DistanceAbsolute1 = {
"DistanceAbsolute1/dist1000_1":"distance/dist1000",
"DistanceAbsolute1/dist2000_1":"distance/dist2000",
"DistanceAbsolute1/dist2500_1":"distance/distFar", #touchup, does not match
"DistanceAbsolute1/dist800_1":"distance/dist1000", #touchup, does not match
"DistanceAbsolute1/dist1500_1":"distance/dist2000", #touchup, does not match
}
DISTANCE_DistanceAbsolute1_CONCAT = {
"DistanceAbsolute1/dist100_1":"distance/dist100",
"DistanceAbsolute1/dist200_1":"distance/dist200",
"DistanceAbsolute1/dist500_1":"distance/dist500",
"DistanceAbsolute1/dist75_1":"distance/dist50", #touchup, does not match
"DistanceAbsolute1/dist300_1":"distance/dist200", #touchup, does not match
"DistanceAbsolute1/dist400_1":"distance/dist500", #touchup, does not match
"DistanceAbsolute1/dist600_1":"distance/dist500", #touchup, does not match
"DistanceAbsolute1/dist700_1":"distance/dist500", #touchup, does not match
}
DISTANCE_040_MoveDistanceAbsolute1_CONCAT = {
"040_MoveDistanceAbsolute1/dist100_1":"distance/dist100",
"040_MoveDistanceAbsolute1/dist200_1":"distance/dist200",
"040_MoveDistanceAbsolute1/dist500_1":"distance/dist500",
"040_MoveDistanceAbsolute1/dist75_1":"distance/dist50", #touchup, does not match
"040_MoveDistanceAbsolute1/dist300_1":"distance/dist200", #touchup, does not match
"040_MoveDistanceAbsolute1/dist400_1":"distance/dist500", #touchup, does not match
"040_MoveDistanceAbsolute1/dist600_1":"distance/dist500", #touchup, does not match
"040_MoveDistanceAbsolute1/dist700_1":"distance/dist500", #touchup, does not match
}
DEFAULT_070_MoveDirectionRelative1 = {
"070_MoveDirectionRelative1/moveBack_1":"Reverse",
"070_MoveDirectionRelative1/moveBack_2":"Reverse",
"070_MoveDirectionRelative1/moveLeft_1":"Left",
"070_MoveDirectionRelative1/moveLeft_2":"Left",
"070_MoveDirectionRelative1/moveRight_1":"Right",
"070_MoveDirectionRelative1/moveRight_2":"Right",
"070_MoveDirectionRelative1/moveUp_1":"Advance",
"070_MoveDirectionRelative1/moveUp_2":"Advance",
}
TWICE = {"_1","_2"}
FILETYPES = {".ogg",".lip"}

STATES_CONTACT = {"CombatContact","NormalContact"}
STATES_ENGAGE = {"NormalEngage","CombatEngage","StealthEngage"}
STATES_TARGET = {"NormalTarget"}
STATES_DirectionRelative2 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","Stealth","StealthEngage"}
STATES_NUMBERSGRID = {"Combat","CombatEngage","Normal","NormalEngage","Stealth","StealthEngage"}
STATES_TEAMS = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}
STATES_080_MoveAlphabet = {"Normal","Stealth"}
STATES_ALL = {"Combat","CombatContact","CombatEngage","Normal","NormalContact","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}

srcfolders = ["default/","default/alphabet/","default/clockfacing/","default/combat/","default/direction/","default/distance/","default/formation/","default/mapcoords/","default/numbers/","default/objects/","default/side/","default/SOM/","default/team/","default/vehicles/","default/weapons/"]

def concatenate_audio_moviepy(path1, path2, output_path):
	first = AudioFileClip(path1) 
	last = AudioFileClip(path2)
	final_clip = concatenate_audioclips([first,last])
	final_clip.write_audiofile(output_path)
def concatenate_audio_moviepy_three(path1, path2, path3, output_path):
	first = AudioFileClip(path1) 
	second = AudioFileClip(path2)
	third = AudioFileClip(path3)
	final_clip = concatenate_audioclips([first,second,third])
	final_clip.write_audiofile(output_path)
def checkdirs():
    print("Checking directories")
    global DIR_CHECK_RESULT
    if (os.path.isdir(A2_DIR+"/default")) and (os.path.isdir(A2_DIR+"/stealth")):
        DIR_CHECK_RESULT = 1
        return
    else:
        DIR_CHECK_RESULT = 0
        return
def convert_clockfacing():
    for ext in FILETYPES:
        for state in STATES_DirectionRelative2:
            for renamed_file, original_file in CLOCKFACING_DirectionRelative2.items():
                #print(A2_DIR + "default/clockfacing/" + original_file + ext,A3_DIR + state + "/" +  renamed_file + ext)
                shutil.copyfile(A2_DIR + "default/clockfacing/" + original_file + ext,A3_DIR + state + "/" +  renamed_file + ext)
def concat_080_MoveAlphabet():
	for state in STATES_080_MoveAlphabet:
		for n in DEFAULT_ALPHABET:
			start = A2_DIR + "default/MoveTo.ogg"
			end = A2_DIR + "default/alphabet/"+ n + ".ogg"
			output = A3_DIR + state + "/080_MoveAlphabet/" + n + ".ogg"
			concatenate_audio_moviepy(start, end, output)
			#TODO move to stealth 
def concat_Engage_010_Vehicles():
	for state in STATES_ENGAGE:
		for n, m in VEHICLES_ENGAGE.items():
			start = A2_DIR + "default/AttackThat.ogg"
			end = A2_DIR + "default/vehicles/"+ m + ".ogg"
			output = A3_DIR + state + "/010_Vehicles/" + n + ".ogg"
			concatenate_audio_moviepy(start, end, output)
def concat_Contact_010_Vehicles():
	global A2_DIR, A3_DIR
	for state in STATES_CONTACT:
		for n, m in VEHICLES_ENGAGE.items():
			start = A2_DIR + "default/ContactE.ogg"
			end = A2_DIR + "default/vehicles/"+ m + ".ogg"
			output = A3_DIR + state + "/010_Vehicles/" + n + ".ogg"
			concatenate_audio_moviepy(start, end, output)
def concat_Target_010_Vehicles():
	for state in STATES_TARGET:
		for n, m in VEHICLES_ENGAGE.items():
			start = A2_DIR + "default/TargetThat.ogg"
			end = A2_DIR + "default/vehicles/"+ m + ".ogg"
			output = A3_DIR + state + "/010_Vehicles/" + n + ".ogg"
			concatenate_audio_moviepy(start, end, output)
			
def concat_DistanceAbsolute1():
	for state in STATES_DistanceAbsolute1:
		for n, m in DISTANCE_DistanceAbsolute1_CONCAT.items():
			start = A2_DIR + "default/"+ m + ".ogg"
			end = A2_DIR + "default/distance/Meters.ogg"
			output = A3_DIR + state + "/" + n + ".ogg"
			concatenate_audio_moviepy(start, end, output)

def concat_040_MoveDistanceAbsolute1():
	for state in STATES_040_MoveDistanceAbsolute1:
		for n, m in DISTANCE_040_MoveDistanceAbsolute1_CONCAT.items():
			advance = A2_DIR + "default/Advance.ogg"
			number = A2_DIR + "default/"+ m + ".ogg"
			meters = A2_DIR + "default/distance/Meters.ogg"
			output = A3_DIR + state + "/" + n + ".ogg"
			concatenate_audio_moviepy_three(advance, number, meters, output)
			
def concat_035_NumbersGrid():
	for state in STATES_NUMBERSGRID:
		#todo make the concats run only once and copy files to all the destionations
		for n, m in NUMBERS_FIRST_035_NumbersGrid.items():
			grid = A2_DIR + "default/Grid.ogg"
			number = A2_DIR + "default/numbers/"+ m + ".ogg"
			output = A3_DIR + state + "/035_NumbersGrid/" + n + ".ogg"
			concatenate_audio_moviepy(grid, number, output)
		for n, m in NUMBERS_FIRST_035_NumbersGrid_2.items():
			grid = A2_DIR + "default/Grid.ogg"
			number = A2_DIR + "default/numbers/"+ m + ".ogg"
			output = A3_DIR + state + "/035_NumbersGrid/" + n + ".ogg"
			concatenate_audio_moviepy(grid, number, output)
		for n, m in NUMBERS_MOVE_035_NumbersGrid.items():
			moveto = A2_DIR + "default/MoveTo.ogg"
			grid = A2_DIR + "default/Grid.ogg"
			number = A2_DIR + "default/numbers/"+ m + ".ogg"
			output = A3_DIR + state + "/035_NumbersGrid/" + n + ".ogg"
			concatenate_audio_moviepy_three(moveto, grid, number, output)
		for n, m in NUMBERS_LIST_035_NumbersGrid.items():
			number = A2_DIR + "default/numbers/"+ m + ".ogg"
			output = A3_DIR + state + "/035_NumbersGrid/" + n + ".ogg"
			shutil.copyfile(number,output)

def convert_030_Teams():
	global A2_DIR, A3_DIR
	for ext in FILETYPES:
		for state in STATES_TEAMS:
			for n, m in TEAM_030_Teams.items():
				shutil.copyfile(A2_DIR + "default/team/" + m + ext, A3_DIR + state + "/" + n + ext)
def fileexists():
	filename= Path(A2_DIR + "default/Advance.ogg")
	if filename.exists():
		print(filename)
def createdirs(*arg):
	global A3_DIR
	loop = {0:"Combat/",1:"CombatContact/",2:"CombatEngage/",3:"Normal/",4:"NormalContact/",5:"NormalEngage/",6:"NormalTarget/",7:"NormalWatch/",8:"Stealth/",9:"StealthEngage/",10:"StealthWatch/"}
	for i, folder in loop.items():
		for n in arg[i]:
			os.makedirs(A3_DIR + folder + n)

def convert(sources, states, srcfolder):
	global A2_DIR, A3_DIR
	for ext in FILETYPES:
		for state in states:
			for n, m in sources.items():
				shutil.copyfile(A2_DIR + srcfolder + m + ext, A3_DIR + state + "/"+ n + ext)

def convert_nolip(sources, states, srcfolder):
	global A2_DIR, A3_DIR
	for state in states:
		for n, m in sources.items():
			shutil.copyfile(A2_DIR + srcfolder + m + ".ogg", A3_DIR + state + "/"+ n + ".ogg")

def convert_directionrelative(sources, states):
	global A2_DIR, A3_DIR
	#back, front, left, right
	for ext in FILETYPES:
		for state in states:
			shutil.copyfile(A2_DIR + srcfolder + "back" + ext, A3_DIR + state + "/"+ n + ext)
			
def convert_preview():
	global A3_BASE
	shutil.copyfile(A2_DIR + "default/RepeatLast.ogg", A3_BASE + "preview.ogg")

print("Creating directories...")
createdirs(DIRS_Combat, DIRS_CombatContact, DIRS_CombatEngage, DIRS_Normal, DIRS_NormalContact, DIRS_NormalEngage, DIRS_NormalTarget, DIRS_NormalWatch, DIRS_Stealth, DIRS_StealthEngage, DIRS_StealthWatch)
print("Moving files...")
#-----
convert_preview()
#-----
STATES_030_Teams = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}
convert(TEAM_030_Teams, STATES_030_Teams, srcfolders[12])
#-----
STATES_110_Com_Announce = {"Combat","Normal","Stealth"}
convert(DEFAULT_110_Com_Announce, STATES_110_Com_Announce, srcfolders[0])
#-----
STATES_100_Commands = {"Combat","Normal","Stealth"}
convert(FORMATION_100_Commands,STATES_100_Commands, srcfolders[6])
#-----
STATES_015_Targeting = {"Combat","Normal","Stealth"}
convert(DEFAULT_015_Targeting, STATES_015_Targeting, srcfolders[0])
#-----
STATES_100_Commands = {"Combat","Normal","Stealth"}
convert(DEFAULT_100_Commands, STATES_100_Commands, srcfolders[0])
#-----
STATES_025_Numbers = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}
convert(NUMBERS_025_Numbers, STATES_025_Numbers, srcfolders[8])
#-----
STATES_120_Com_Ask = {"Normal","Stealth"}
convert(DEFAULT_120_Com_Ask, STATES_120_Com_Ask, srcfolders[0])
#-----
STATES_130_Com_Reply = {"Combat","Normal","Stealth"}
convert(DEFAULT_130_Com_Reply, STATES_130_Com_Reply, srcfolders[0])
#-----
STATES_010_Vehicles = {"Combat","Normal","Stealth"}
convert_nolip(VEHICLES_010_Vehicles, STATES_010_Vehicles, srcfolders[13])
#-----
STATES_DirectionCompass1 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}
convert(DIRECTION_DirectionCompass1, STATES_DirectionCompass1, srcfolders[4])
#-----
STATES_DirectionCompass2 = {"Normal","Stealth"}
convert(DEFAULT_DirectionCompass2, STATES_DirectionCompass2, srcfolders[0])
#-----
STATES_DirectionRelative1 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","Stealth","StealthEngage"}
convert(CLOCKFACING_DirectionRelative1, STATES_DirectionRelative1, srcfolders[2])
#-----
STATES_DirectionRelative3 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","Stealth","StealthEngage"}
convert(CLOCKFACING_DirectionRelative3, STATES_DirectionRelative3, srcfolders[2])
#-----
STATES_150_Reporting = {"Normal","Stealth"}
convert(DEFAULT_150_Reporting, STATES_150_Reporting, srcfolders[0])
#-----
STATES_140_Com_Status = {"Normal","Stealth"}
convert(DEFAULT_140_Com_Status, STATES_140_Com_Status, srcfolders[0])
#-----
STATES_220_Support = {"Normal","Stealth"}
convert(SOM_220_Support,STATES_220_Support,srcfolders[11])
#-----
STATES_200_CombatShouts = {"Combat","Stealth"}
convert(DEFAULT_200_CombatShouts, STATES_200_CombatShouts, srcfolders[0])
#-----
STATES_005_Weapons = {"Normal"}
convert(WEAPONS_005_Weapons, STATES_005_Weapons, srcfolders[0])
#-----
STATES_DistanceAbsolute1 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","Stealth","StealthEngage"}
convert(DISTANCE_DistanceAbsolute1,STATES_DistanceAbsolute1, srcfolders[0])
#-----
STATES_070_MoveDirectionRelative1 = {"Combat","Normal","Stealth"}
convert(DEFAULT_070_MoveDirectionRelative1,STATES_070_MoveDirectionRelative1, srcfolders[0])
#-----
STATES_040_MoveDistanceAbsolute1 = {"Combat","Normal","Stealth"}
print("Concatenating files...")
concat_040_MoveDistanceAbsolute1()
concat_DistanceAbsolute1()
convert_clockfacing()
convert_030_Teams()
concat_Contact_010_Vehicles()
concat_Engage_010_Vehicles()
concat_Target_010_Vehicles()
concat_035_NumbersGrid()
concat_080_MoveAlphabet()
print("All done!")
