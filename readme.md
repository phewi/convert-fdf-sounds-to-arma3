# Convert Arma 2 FDF sounds to Arma 3 (WIP)

Convert Arma 2 FDF sounds to Arma 3 by renaming and concatenating voice files. Quick and dirty.
Heavily in progress, probably will make a release when it's doing everything it's supposed to do

# Usage

`python3 converta2toa3.py --input <directory> --output <directory>`

# TODO

- [x] Use args for input and output instead of hardcoding them
- [x] Add creating arma 3 folders
- [x] Grid numbers concat and move
- [ ] Finish up cataloging all the arma 2 sound files and arma3 destinations
- [ ] Collect a list of the sound-files that need to be manually touched up
- [ ] Check for compatibility for linux and windows
- [ ] Write instructions

# Destination folder conversion progress

- [ ] ├── Combat
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [ ] │   ├── 040_MoveDistanceAbsolute1
- [ ] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 130_Com_Reply
- [ ] │   ├── 200_CombatShouts
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [ ] ├── CombatContact
- [ ] │   └── 010_Vehicles
- [ ] ├── CombatEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [ ] ├── Normal
- [ ] │   ├── 005_Weapons
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [ ] │   ├── 040_MoveDistanceAbsolute1
- [ ] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 080_MoveAlphabet
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 120_Com_Ask
- [x] │   ├── 130_Com_Reply
- [ ] │   ├── 140_Com_Status
- [ ] │   ├── 150_Reporting
- [ ] │   ├── 220_Support
- [ ] │   ├── 230_GenericRadioMessages
- [x] │   ├── DirectionCompass1
- [ ] │   ├── DirectionCompass2
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [ ] ├── NormalContact
- [ ] │   └── 010_Vehicles
- [ ] ├── NormalEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [ ] ├── NormalTarget
- [ ] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [x] ├── NormalWatch
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   └── DirectionCompass1
- [ ] ├── Stealth
- [x] │   ├── 010_Vehicles
- [x] │   ├── 015_Targeting
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [ ] │   ├── 040_MoveDistanceAbsolute1
- [ ] │   ├── 070_MoveDirectionRelative1
- [x] │   ├── 080_MoveAlphabet
- [x] │   ├── 100_Commands
- [x] │   ├── 110_Com_Announce
- [x] │   ├── 120_Com_Ask
- [x] │   ├── 130_Com_Reply
- [ ] │   ├── 140_Com_Status
- [ ] │   ├── 150_Reporting
- [ ] │   ├── 200_CombatShouts
- [ ] │   ├── 220_Support
- [x] │   ├── DirectionCompass1
- [ ] │   ├── DirectionCompass2
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
- [ ] ├── StealthEngage
- [x] │   ├── 010_Vehicles
- [x] │   ├── 025_Numbers
- [x] │   ├── 030_Teams
- [x] │   ├── 035_NumbersGrid
- [x] │   ├── DirectionCompass1
- [x] │   ├── DirectionRelative1
- [x] │   ├── DirectionRelative2
- [x] │   ├── DirectionRelative3
- [ ] │   └── DistanceAbsolute1
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
