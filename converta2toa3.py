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


#The format is "sourcefilename":"destionationfilename", 
#
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
DEFAULT_005_Weapons = {}
DEFAULT_010_Vehicles = {}
DEFAULT_015_Targeting = {
"AttackE":"Attack_1",
#"AttackE":"Attack_2",
"CancelTarget":"CancelTarget_1",
#"CancelTarget":"CancelTarget_2",
"EngageE":"Engage_1",
#"EngageThat":"Engage_2",
"FireE":"Fire_2",
#"Fire":"Fire_1",
"NoTarget":"NoTarget_1",
#"NoTarget":"NoTarget_2",
}

#no fdf DEFAULT_020_Names = {}
#no fdf DEFAULT_025_Numbers = {}
DEFAULT_030_Teams = {}
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
NUMBERS_035_NumbersGrid = {}
DEFAULT_040_MoveDistanceAbsolute1 = {}
DEFAULT_070_MoveDirectionRelative1 = {}
DEFAULT_080_MoveAlphabet = {}
DEFAULT_090_MoveLocations = {}
DEFAULT_100_Commands = {
"Advance":"100_Commands/Advance",
"AssembleThat":"100_Commands/AssembleThatWeapon",
"CancelManualFire":"100_Commands/CancelManualFire_1",
"CancelManualFire":"100_Commands/CancelManualFire_2",
"CancelManualFire":"100_Commands/CancelManualFire_3",
"CeaseFireE":"100_Commands/CeaseFire_1",
"CeaseFireE":"100_Commands/CeaseFire_2",
"CheckYourFireE":"100_Commands/CheckYourFire",
"DangerE":"100_Commands/Danger",
"DeactivateCharge":"100_Commands/DeactivateCharge",
"DetonateCharge":"100_Commands/DetonateCharge",
"DisarmThatMine":"100_Commands/DisarmThatMine",
"DisassembleThat":"100_Commands/DisassembleThatWeapon",
"Disembark":"100_Commands/Dismount_2",
"Disengage":"100_Commands/Disengage",
"Dismount":"100_Commands/Dismount_1",
"Driver":"100_Commands/GetInThatVehicleDriver",
"EjectE":"100_Commands/Eject_1",
#"EjectE":"100_Commands/Eject_2",
"EngageAtWill":"100_Commands/EngageAtWill",
"Commander":"100_Commands/GetInThatVehicleCommander",
"CopyMyStance":"100_Commands/CopyMyStance",
"FallBackE":"100_Commands/FallBack",
"Fast":"100_Commands/VehFast_1",
#"Fast":"100_Commands/VehFast_2",
#"Fast":"100_Commands/VehFast_3",
"FireAtWill":"100_Commands/FireAtWill",
"FlankLeft":"100_Commands/FlankLeft",
"FlankRight":"100_Commands/FlankRight",
"FlashlightsOff":"100_Commands/FlashlightsOff",
"FlashlightsOn":"100_Commands/FlashlightsOn",
"FormOnMeE":"100_Commands/FormOnMe",
"Forward":"100_Commands/VehForward_1",
#"Forward":"100_Commands/VehForward_2",
"FreeToEngage":"100_Commands/FreeToEngage",
"GetDownE":"100_Commands/GoProne_1",
"GetInThat":"100_Commands/GetInThatVehicle",
"GetSupportAt":"100_Commands/GetSupport",
"GoProne":"100_Commands/GoProne",
"Gunner":"100_Commands/GetInThatVehicleGunner",
"Halt":"100_Commands/Halt",
"HealThat":"100_Commands/HealThatSoldier",
"HitTheDirt":"100_Commands/GoProne_2",
"HoldFire":"100_Commands/HoldFire",
"LasersOff":"100_Commands/PointersOff.ogg",
"LasersOn":"100_Commands/PointersOn.ogg",
"Left":"100_Commands/VehLeft_1",
#"Left":"100_Commands/VehLeft_2",
#"Left":"100_Commands/VehLeft_3",
"LightThatFire":"100_Commands/LightThatFire",
"ManualFire":"100_Commands/ManualFire_1",
"ManualFire":"100_Commands/ManualFire_2",
"ManualFire":"100_Commands/ManualFire_3",
"ObserveThatPosition":"100_Commands/ObserveThatPosition",
"OpenUpE":"100_Commands/SuppressiveFire",
"Pilot":"100_Commands/GetInThatVehiclePilot",
"PutOutThatFire":"100_Commands/PutOutThatFire",
"RearmAt":"100_Commands/Rearm",
"RegroupE":"100_Commands/Regroup",
"RequestingSupportTo":"100_Commands/RequestingSupport",
"ReturnToFormationE":"100_Commands/ReturnToFormation",
"Reverse":"100_Commands/VehBackward_1",
"Right":"100_Commands/VehRight_1",
"Right":"100_Commands/VehRight_2",
"Right":"100_Commands/VehRight_3",
"ScanHorizon":"100_Commands/ScanHorizon",
"SetACharge":"100_Commands/SetCharge",
"SetTheTimer":"100_Commands/SetTheTimer",
"Slow":"100_Commands/VehSlow_1",
#"Slow":"100_Commands/VehSlow_2",
"StayAlert":"100_Commands/StayAlert",
"StayBack":"100_Commands/StayBack",
"Stealth":"100_Commands/CommStealth",
"StopE":"100_Commands/Stop",
"StopE":"100_Commands/VehStop_1",
"StopE":"100_Commands/VehStop_2",
"StopE":"100_Commands/VehStop_3",
"TakeCoverE":"100_Commands/TakeCoverE",
"WeaponsFree":"100_Commands/WeaponsFree",
}
DEFAULT_110_Com_Announce = {
"AreaClear":"110_Com_Announce/AreaClear",
"Clear":"110_Com_Announce/Clear",
"EyesOnTarget":"110_Com_Announce/EyesOnTarget",
"HesDownE":"110_Com_Announce/HeIsDown",
"HostileDownE":"110_Com_Announce/HostileDown",
"ImTheNewActual":"110_Com_Announce/IAmTheNewActual",
"IveGotHimE":"110_Com_Announce/HeIsDown",
"Ready":"110_Com_Announce/Ready",
"ReadyToFire":"110_Com_Announce/ReadyToFire",
"ScratchOneE":"110_Com_Announce/ScratchOne",
"StandingBy":"110_Com_Announce/StandingBy",
"TakingCommand":"110_Com_Announce/TakingCommand",
"TargetAcquired":"110_Com_Announce/TargetAcquired",
"TargetEliminated":"110_Com_Announce/TargetEliminated",
"TargetInSight":"110_Com_Announce/TargetInSight",
"Waiting":"110_Com_Announce/Waiting",
}
DEFAULT_120_Com_Ask = {
"RepeatLast":"RepeatLastOver",
"ReportPositionE":"ReportPosition",
"ReportStatus":"ReportIn",
"SayAgain":"SayAgainOver",
"WhereAreYouQ":"WhatIsYourLocationQ",
}
DEFAULT_130_Com_Reply = {
"AttackingE":"Attacking",
"CannotFire":"CannotFire",
"Copy":"Confirmation1_1",
"Copy":"Confirmation1_2",
"Copy":"Confirmation1_4",
"Copy":"Confirmation1_5",
"Copy":"Confirmation1_6",
"Copy":"Confirmation1_7",
"Copy":"Confirmation1_8",
"Copy":"Confirmation1_9",
"Copy":"Confirmation1_10",
"EngagingE":"Engaging",
"EngagingTargetE":"EngagingTarget",
"Negative":"Negative_1",
"Negative":"Negative_2",
"Negative":"Negative_3",
"NoCanDo":"NoCanDo_1",
"NoCanDo":"NoCanDo_2",
"OnTheWay":"OnTheWay_1",
"OnTheWay":"OnTheWay_2",
"OnTheWay":"OnTheWay_3",
"Roger":"Confirmation2_1",
"Roger":"Confirmation2_2",
"Roger":"Confirmation2_3",
"Roger":"Confirmation2_4",
"Roger":"Confirmation2_5",
"Roger":"Confirmation2_6",
"Roger":"Confirmation2_7",
"Roger":"Confirmation2_8",
"Roger":"Confirmation2_9",
"Roger":"Confirmation2_10",
"SolidCopy":"Confirmation1_2",
"Understood":"Confirmation1_3",

}
DEFAULT_140_Com_Status = {
"BingoFuel":"FuelLow_1",
"BingoFuel":"FuelLow_2",
"CriticalDamageE":"CriticalDamage_1",
"CriticalDamageE":"CriticalDamage_2",
"Injured":"HealthInjured",
"IsDead":"HeIsDeadE",
"IsDownE":"HeIsHitE",
"MedicE":"HealthMedic",
"MedicE":"HealthNeedMedicNow",
"NeedHelpE":"HealthINeedHelpNow",
"NoMoreAmmoE":"AmmoCritical_1",
"NoMoreAmmoE":"AmmoCritical_3",
"OutOfAmmoE":"AmmoCritical_2",
"OutOfFuelE":"FuelCritical_1",
"RunningOutOfAmmo":"AmmoLow",
"RunningOutOfFuel":"FuelCritical_2",
"SomebodyHelpMeE":"HealthINeedSomeHelpHere",
"WoundedE":"HealthIAmWounded",
}
DEFAULT_150_Reporting = {
"HostilesE":"EnemyDetected_1",
"HostilesE":"EnemyDetected_2",
"HostilesE":"EnemyDetected_3",
"HostilesE":"EnemyDetected_4",
"HostilesE":"EnemyDetected_5",
"HostilesE":"EnemyDetected_6",
"HostilesE":"EnemyDetected_7",
"HostilesE":"EnemyDetected_8",
"HostilesE":"EnemyDetected_9",
"HostilesE":"EnemyDetected_10",
}
DEFAULT_200_CombatShouts = {
"UnderFireE":"200_CombatShouts/UnderFireE"
}
DEFAULT_220_Support = {}
DEFAULT_230_GenericRadioMessages = {}
DirectionCompass1 = {}
DirectionCompass2 = {}
DirectionRelative1 = {}
DirectionRelative2 = {}
DirectionRelative3 = {}
ListDistanceAbsolute1 = {}


DEFAULT_ALPHABET = {
"alpha",
"bravo",
"charlie",
"delta",
"echo",
"fotxtrot",
"golf",
"hotel",
"india",
"juliet",
"kilo",
"lima",
"mike",
"november",
"oscar",
"papa",
"quebec",
"romeo",
"sierra",
"tango",
"uniform",
"whiskey",
"xray",
"yankee",
"zulu",
}

#TODO
CLOCKFACING_DirectionRelative2 = {
"at10":"DirectionRelative2/at10",
"at11":"DirectionRelative2/at11",
"at12":"DirectionRelative2/at12",
"at1":"DirectionRelative2/at1",
"at2":"DirectionRelative2/at2",
"at3":"DirectionRelative2/at3",
"at4":"DirectionRelative2/at4",
"at5":"DirectionRelative2/at5",
"at6":"DirectionRelative2/at6",
"at7":"DirectionRelative2/at7",
"at8":"DirectionRelative2/at8",
"at9":"DirectionRelative2/at9",
}

#TODO
COMBAT_200_CombatShouts = {
"CS_ChangingMagsE":"200_CombatShouts/ReloadingE",
"CS_ContactE":"ContactE",
"CS_CoveringFireE":"CoveringE_1",
"CS_CoveringGoE":"CoveringE_2",
"CS_CoverMeE":"CoverMeE",
"CS_CoverMeWhileIReloadE":"ReloadingE_3",
"CS_EngagingE":"",
"CS_FireInTheHoleE":"ThrowingGrenadeE_1",
"CS_GoE":"",
"CS_GoILLCoverE":"CoveringE_3",
"CS_GoImCoveringE":"CoveringE_4",
"CS_HostilesE":"",
"CS_IgottaReloadE":"ReloadingE_2",
"CS_MoveE":"",
"CS_MoveOutE":"",
"CS_MovingE":"",
"CS_MovinOutE":"",
"CS_OKLetsGo":"",
"CS_ReloadingE":"ReloadingE_1",
"CS_SuppresiveFireE":"SuppressingE_1",
}

#TODO
DIRECTION_DirectionCompass1 = {
"East":"DirectionCompass1/east_1",
"Northeast":"DirectionCompass1/northEast_1",
"North":"DirectionCompass1/north_1",
"Northwest":"DirectionCompass1/northWest_1",
"Southeast":"DirectionCompass1/southEast_1",
"South":"DirectionCompass1/south_1",
"Southwest":"DirectionCompass1/southWest_1",
"West":"DirectionCompass1/west_1",
#"East":"DirectionCompass1/east_2",
#"Northeast":"DirectionCompass1/northEast_2",
#"North":"DirectionCompass1/north_2",
#"Northwest":"DirectionCompass1/northWest_2",
#"Southeast":"DirectionCompass1/southEast_2",
#"South":"DirectionCompass1/south_2",
#"Southwest":"DirectionCompass1/southWest_2",
#"West":"DirectionCompass1/west_2",
}
DIRECTION_Unused = {
#"Close":"",
#"Far":"",
#"front":"",
#"MediumRange":"",
#"rear":"",
}

#TODO
DISTANCE_DistanceAbsolute1 = {
"dist1000":"dist1000_1",
"dist100":"dist100_1",
"dist2000":"dist2000_1",
"dist200":"dist200_1",
"dist500":"dist500_1",
"distFar":"dist2500_1",
#"dist1000":"dist1000_2",
#"dist100":"dist100_2",
#"dist2000":"dist2000_2",
#"dist200":"dist200_2",
#"dist500":"dist500_2",
#"dist50":"",
#"distFar":"dist2500_2",
#"Meters":"",
}

FORMATION_100_Commands = {
"FormColumn":"100_Commands/FormColumn",
"FormDiamond":"100_Commands/FormDiamond",
"FormEcholonLeft":"100_Commands/FormEcholonLeft",
"FormEcholonRight":"100_Commands/FormEcholonRight",
"FormFile":"100_Commands/FormFile",
"FormLine":"100_Commands/FormLine",
"FormStaggeredColumn":"100_Commands/FormStaggeredColumn",
"FormWedge":"100_Commands/FormWedge",
"FormWedge":"100_Commands/FormVee",
}

#TODO
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
"Eighteen":"025_Numbers/eighteen",
"Eight":"025_Numbers/eight",
"Eighty":"025_Numbers/eighty",
"Eleven":"025_Numbers/eleven",
"Fifteen":"025_Numbers/fifteen",
"Fifty":"025_Numbers/fifty",
"Five":"025_Numbers/five",
"Forty":"025_Numbers/forty",
"Four":"025_Numbers/four",
"Fourteen":"025_Numbers/fourteen",
"Hundred":"025_Numbers/hundred",
"nine":"025_Numbers/nine",
"Nineteen":"025_Numbers/nineteen",
"Ninety":"025_Numbers/ninety",
"One":"025_Numbers/one",
"Seven":"025_Numbers/seven",
"Seventeen":"025_Numbers/seventeen",
"Seventy":"025_Numbers/seventy",
"Six":"025_Numbers/six",
"Sixteen":"025_Numbers/sixteen",
"Sixty":"025_Numbers/sixty",
"Ten":"025_Numbers/ten",
"Thirteen":"025_Numbers/thirteen",
"Thirty":"025_Numbers/thirty",
"Three":"025_Numbers/three",
"Twelve":"025_Numbers/twelve",
"Twenty":"025_Numbers/twenty",
"Two":"025_Numbers/two",
"Zero":"025_Numbers/zero",
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

DEFAULT_SOM = {
"RequestingCloseAirSupportAtGrid":"220_Support/SupportRequestRGCASHelicopter",
"RequestingFireSupportAtGrid":"220_Support/SupportRequestRGArty",
#"RequestingReinforcementsToOurPositionGrid":"",
"RequestingSupplyDropAtGrid":"220_Support/SupportRequestRGSupplyDrop",
}

TEAM_030_Teams = {
#"allGroup":"",
"blueTeam":"030_Teams/blueTeam",
"greenTeam":"030_Teams/greenTeam",
"redTeam":"030_Teams/redTeam",
"whiteTeam":"030_Teams/whiteTeam",
"yellowTeam":"030_Teams/yellowTeam",
}

#TODO tarkista käyttämättömät
VEHICLES = {
"aircraft":"010_Vehicles/veh_air_s",
"aircrafts":"010_Vehicles/veh_air_p",
"airplane":"010_Vehicles/veh_plane_s",
"airplanes":"010_Vehicles/veh_plane_p",
"APC":"010_Vehicles/veh_vehicle_APC_s",
"APCs":"010_Vehicles/veh_vehicle_APC_p",
"boat":"010_Vehicles/veh_ship_boat_s",
"boats":"010_Vehicles/veh_ship_boat_p",
"car":"010_Vehicles/veh_vehicle_car_s",
"cars":"010_Vehicles/veh_vehicle_car_p",
"gunship":"010_Vehicles/veh_air_gunship_s",
"gunships":"010_Vehicles/veh_air_gunship_p",
"helicopter":"010_Vehicles/veh_helicopter_s",
"helicopters":"010_Vehicles/veh_helicopter_p",
"launcherSoldier":"010_Vehicles/veh_infantry_AA_s",
"launcherSoldiers":"010_Vehicles/veh_infantry_AA_p",
"launcherSoldier":"010_Vehicles/veh_infantry_AT_s",
"launcherSoldiers":"010_Vehicles/veh_infantry_AT_p",
"Medic":"010_Vehicles/veh_infantry_medic_s",
"Medics":"010_Vehicles/veh_infantry_medic_p",
"MGunner":"010_Vehicles/veh_infantry_MG_s",
"Mgunners":"010_Vehicles/veh_infantry_MG_p",
"officer":"010_Vehicles/veh_infantry_officer_s",
"officers":"010_Vehicles/veh_infantry_officer_p",
"parachute":"010_Vehicles/veh_air_parachute_s",
"parachutes":"010_Vehicles/veh_air_parachute_p",
"pilot":"010_Vehicles/veh_infantry_pilot_s",
"pilots":"010_Vehicles/veh_infantry_pilot_p",
"ship":"010_Vehicles/veh_ship_s",
"ships":"010_Vehicles/veh_ship_p",
"ship":"010_Vehicles/veh_submarine_s",
"ships":"010_Vehicles/veh_submarine_p",
"Sniper":"010_Vehicles/veh_infantry_Sniper_s",
"Snipers":"010_Vehicles/veh_infantry_Sniper_p",
"soldier":"010_Vehicles/veh_infantry_s_1",
"soldiers":"010_Vehicles/veh_infantry_p_1",
"SpecialForce":"010_Vehicles/veh_infantry_SF_s",
"SpecialForces":"010_Vehicles/veh_infantry_SF_p",
"staticAALauncher":"010_Vehicles/veh_static_AA_s",
"staticAALaunchers":"010_Vehicles/veh_static_AA_p",
"staticATLauncher":"010_Vehicles/veh_static_AA_s",
"staticATLaunchers":"010_Vehicles/veh_static_AA_p",
"staticCannon":"010_Vehicles/veh_static_cannon_s",
"staticCannons":"010_Vehicles/veh_static_cannon_p",
"staticgrenadelauncher":"010_Vehicles/veh_static_GL_s",
"staticgrenadelaunchers":"010_Vehicles/veh_static_GL_p",
"staticLaunchers":"010_Vehicles/veh_static_p",
"StaticMGWeapon":"010_Vehicles/veh_Static_MG_s",
"StaticMGWeapons":"010_Vehicles/veh_Static_MG_p",
"StaticMortar":"010_Vehicles/veh_Static_mortar_s",
"StaticMortars":"010_Vehicles/veh_Static_mortar_p",
"tank":"010_Vehicles/veh_vehicle_tank_s",
"tanks":"010_Vehicles/veh_vehicle_tank_p",
"technical":"010_Vehicles/veh_vehicle_armedcar_s",
"technicals":"010_Vehicles/veh_vehicle_armedcar_p",
"truck":"010_Vehicles/veh_vehicle_truck_s",
"trucks":"010_Vehicles/veh_vehicle_truck_p",
"UAV":"010_Vehicles/veh_air_uav_s",
"UAVs":"010_Vehicles/veh_air_uav_p",
"vehicle":"010_Vehicles/veh_vehicle_s",
"vehicles":"010_Vehicles/veh_vehicle_p",
}

VEHICLES_ENGAGE = {
"aircraft":"veh_air_s",
"airplane":"veh_plane_s",
"APC":"veh_vehicle_APC_s",
"boat":"veh_ship_boat_s",
"car":"veh_vehicle_car_s",
"gunship":"veh_air_gunship_s",
"helicopter":"veh_helicopter_s",
"launcherSoldier":"veh_infantry_AA_s",
"launcherSoldier":"veh_infantry_AT_s",
"Medic":"veh_infantry_medic_s",
"MGunner":"veh_infantry_MG_s",
"officer":"veh_infantry_officer_s",
"parachute":"veh_air_parachute_s",
"pilot":"veh_infantry_pilot_s",
"ship":"veh_ship_s",
"ship":"veh_submarine_s",
"Sniper":"veh_infantry_Sniper_s",
"soldier":"veh_infantry_s_1",
"SpecialForce":"veh_infantry_SF_s",
"staticAALauncher":"veh_static_AA_s",
"staticATLauncher":"veh_static_AA_s",
"staticCannon":"veh_static_cannon_s",
"staticgrenadelauncher":"veh_static_GL_s",
"StaticMGWeapon":"veh_Static_MG_s",
"StaticMortar":"veh_Static_mortar_s",
"tank":"veh_vehicle_tank_s",
"technical":"veh_vehicle_armedcar_s",
"truck":"veh_vehicle_truck_s",
"UAV":"veh_air_uav_s",
"vehicle":"veh_vehicle_s",
}

WEAPONS = {
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
"Bombs":"005_Weapons/Bombs",
"cannonHigh":"005_Weapons/cannonHigh",
"cannonLow":"005_Weapons/cannonLow",
"Flares":"005_Weapons/Flares",
"MachineGun":"005_Weapons/MachineGun",
"Missiles":"005_Weapons/Missiles",
"Rockets":"005_Weapons/Rockets",
"Mine":"150_Reporting/MineDetected",
}
TWICE = {"_1","_2"}
FILETYPES = {".ogg",".lip"}

#states by states
STATES_ALL = {"Combat","CombatContact","CombatEngage","Normal","NormalContact","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}
STATES_COMBAT = {"Combat","CombatContact","CombatEngage"}
STATES_NORMAL = {"Normal","NormalContact","NormalEngage","NormalTarget","NormalWatch"}
STATES_STEALTH = {"Stealth","StealthEngage","StealthWatch"}
STATES_CONTACT = {"CombatContact","NormalContact"}
STATES_ENGAGE = {"NormalEngage","CombatEngage"}
STATES_TARGET = {"NormalTarget"}
STATES_WATCH = {"NormalWatch","StealthWatch"}

#states by destination folders
STATES_DirectionRelative2 = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","Stealth","StealthEngage"}
STATES_NUMBERSGRID = {"Combat","CombatEngage","Normal","NormalEngage","Stealth","StealthEngage"}
STATES_TEAMS = {"Combat","CombatEngage","Normal","NormalEngage","NormalTarget","NormalWatch","Stealth","StealthEngage","StealthWatch"}

#TODO yhtenäistä konversiofunktio
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
def copy_clockfacing():
    for ext in FILETYPES:
        for state in STATES_DirectionRelative2:
            for original_file, renamed_file in CLOCKFACING_DirectionRelative2.items():
                shutil.copyfile(A2_DIR + "default/clockfacing/" + original_file + ext,A3_DIR + state + "/" +  renamed_file + ext)
def concat_080_MoveAlphabet():
	for n in DEFAULT_ALPHABET:
		start = A2_DIR + "default/MoveTo.ogg"
		end = A2_DIR + "default/alphabet/"+ n + ".ogg"
		output = A3_DIR + "Normal/" + n + ".ogg"
		concatenate_audio_moviepy(start, end, output)
def concat_Engage_010_Vehicles():
	for state in STATES_ENGAGE:
		for n, m in VEHICLES_ENGAGE.items():
			start = A2_DIR + "default/AttackThat.ogg"
			end = A2_DIR + "default/vehicles/"+ n + ".ogg"
			output = A3_DIR + state + "/010_Vehicles/" + m + ".ogg"
			concatenate_audio_moviepy(start, end, output)
def convert_035_NumbersGrid():
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
				shutil.copyfile(A2_DIR + "default/team/" + n + ext, A3_DIR + state + "/" + m + ext)
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
def convert(sources, states):
	#todo unified function for all operations? 
	for state in states:
		for file in sources:
			print(state + " ja " + file)
def convert_005_Weapons():
	#todo
	global A2_DIR, A3_DIR	
def convert_015_Targeting():
	#todo
	global A2_DIR, A3_DIR	
def convert_010_Vehicles():
	#todo
	global A2_DIR, A3_DIR	
def convert_100_Commands():
	#todo
	global A2_DIR, A3_DIR	
def convert_110_Com_Announce():
	#todo
	global A2_DIR, A3_DIR	
def convert_120_Com_Ask():
	#todo
	global A2_DIR, A3_DIR	
def convert_130_Com_Reply():
	#todo
	global A2_DIR, A3_DIR	
def convert_140_Com_Status():
	#todo
	global A2_DIR, A3_DIR	
def convert_200_CombatShouts():
	#todo
	global A2_DIR, A3_DIR		
	
	
createdirs(DIRS_Combat, DIRS_CombatContact, DIRS_CombatEngage, DIRS_Normal, DIRS_NormalContact, DIRS_NormalEngage, DIRS_NormalTarget, DIRS_NormalWatch, DIRS_Stealth, DIRS_StealthEngage, DIRS_StealthWatch)



#checkdirs()
#convert_005_Weapons()
#convert(DEFAULT_100_Commands, STATES_ALL)

#----------working funcions under this line------------
concat_080_MoveAlphabet()
convert_030_Teams()
concat_Engage_010_Vehicles()
copy_clockfacing()
convert_035_NumbersGrid()
print("All done!")
