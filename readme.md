# Convert Arma 2 FDF sounds to Arma 3 (WIP)

Convert Arma 2 FDF sounds to Arma 3 by renaming and concatenating voice files. Quick and dirty.
Heavily in progress, probably will make a release when it's doing everything it's supposed to do

# Usage

`python3 converta2toa3.py --input <directory> --output <directory>`

...or configure the folders in runall.py and run it

# TODO

- [x] Use args for input and output instead of hardcoding them
- [x] Add creating arma 3 folders
- [x] Grid numbers concat and move
- [x] Finish up cataloging all the arma 2 sound files and arma3 destinations
- [x] Convert the files using the script
- [ ] Collect a list of the sound-files that need to be manually touched up (partially done)
- [ ] Check for compatibility for linux and windows
- [ ] Write instructions for script usage
- [ ] Touch up sound files
- [ ] Write config.cpp
- [ ] Automate file additions (config.cpp, %PREFIX%, BIS_AddonInfo.hpp, etc.)
- [ ] Package as pbo
- [ ] Some sound files are not working in arsenal (BUG)
- [ ] Contact-directories should only say the "targetname", no need to concatenate "contact + targetname" (IMPROVEMENT)

# Destination folder conversion progress

- [x] ├── Combat
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── 040_MoveDistanceAbsolute1
- [x] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 130_Com_Reply
- [x] │   ├── 200_CombatShouts
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── CombatContact
- [x] │   └── 010_Vehicles
- [x] ├── CombatEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── Normal
- [x] │   ├── 005_Weapons
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── 040_MoveDistanceAbsolute1
- [x] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 080_MoveAlphabet
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 120_Com_Ask
- [x] │   ├── 130_Com_Reply
- [x] │   ├── 140_Com_Status
- [x] │   ├── 150_Reporting
- [x] │   ├── 220_Support
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionCompass2
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── NormalContact
- [x] │   └── 010_Vehicles
- [x] ├── NormalEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── NormalTarget
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── NormalWatch
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   └── DirectionCompass1
- [x] ├── Stealth
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── 040_MoveDistanceAbsolute1
- [x] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 080_MoveAlphabet
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 120_Com_Ask
- [x] │   ├── 130_Com_Reply
- [x] │   ├── 140_Com_Status
- [x] │   ├── 150_Reporting
- [x] │   ├── 200_CombatShouts
- [x] │   ├── 220_Support
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionCompass2
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── StealthEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [x] │   └── DistanceAbsolute1
- [x] ├── StealthWatch
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   └── DirectionCompass1

# Excluded destination folders

No origin file available in FDF

- ├── Combat
- │   ├── 020_Names
- ├── CombatEngage
- │   ├── 020_Names
- ├── Normal
- │   ├── 020_Names
- │   ├── 090_MoveLocations
- │   ├── 230_GenericRadioMessages
- ├── NormalEngage
- │   ├── 020_Names
- ├── NormalTarget
- │   ├── 020_Names
- ├── NormalWatch
- │   ├── 020_Names
- ├── Stealth
- │   ├── 020_Names
- │   ├── 090_MoveLocations
- ├── StealthEngage
- │   ├── 020_Names
- ├── StealthWatch
- │   ├── 020_Names
