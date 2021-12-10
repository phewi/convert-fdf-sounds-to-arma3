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

# Folder conversion progress

├── Combat [ ]
│   ├── 010_Vehicles [ ]
│   ├── 015_Targeting [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── 040_MoveDistanceAbsolute1 [ ]
│   ├── 070_MoveDirectionRelative1 [ ]
│   ├── 100_Commands [ ]
│   ├── 110_Com_Announce [ ]
│   ├── 130_Com_Reply [ ]
│   ├── 200_CombatShouts [ ]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── CombatContact [ ]
│   └── 010_Vehicles [ ]
├── CombatEngage [ ]
│   ├── 010_Vehicles [x]
│   ├── 020_Names [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── Normal [ ]
│   ├── 005_Weapons [ ]
│   ├── 010_Vehicles [ ]
│   ├── 015_Targeting [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── 040_MoveDistanceAbsolute1 [ ]
│   ├── 070_MoveDirectionRelative1 [ ]
│   ├── 080_MoveAlphabet [x]
│   ├── 090_MoveLocations [ ]
│   ├── 100_Commands [ ]
│   ├── 110_Com_Announce [ ]
│   ├── 120_Com_Ask [ ]
│   ├── 130_Com_Reply [ ]
│   ├── 140_Com_Status [ ]
│   ├── 150_Reporting [ ]
│   ├── 220_Support [ ]
│   ├── 230_GenericRadioMessages [ ]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionCompass2 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── NormalContact [ ]
│   └── 010_Vehicles [ ]
├── NormalEngage [ ]
│   ├── 010_Vehicles [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── NormalTarget [ ]
│   ├── 010_Vehicles [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── NormalWatch [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   └── DirectionCompass1 [ ]
├── Stealth [ ]
│   ├── 010_Vehicles [ ]
│   ├── 015_Targeting [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── 040_MoveDistanceAbsolute1 [ ]
│   ├── 070_MoveDirectionRelative1 [ ]
│   ├── 080_MoveAlphabet [x]
│   ├── 090_MoveLocations [ ]
│   ├── 100_Commands [ ]
│   ├── 110_Com_Announce [ ]
│   ├── 120_Com_Ask [ ]
│   ├── 130_Com_Reply [ ]
│   ├── 140_Com_Status [ ]
│   ├── 150_Reporting [ ]
│   ├── 200_CombatShouts [ ]
│   ├── 220_Support [ ]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionCompass2 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
├── StealthEngage [ ]
│   ├── 010_Vehicles [ ]
│   ├── 025_Numbers [ ]
│   ├── 030_Teams [ ]
│   ├── 035_NumbersGrid [x]
│   ├── DirectionCompass1 [ ]
│   ├── DirectionRelative1 [ ]
│   ├── DirectionRelative2 [x]
│   ├── DirectionRelative3 [ ]
│   └── DistanceAbsolute1 [ ]
└── StealthWatch [ ]
    ├── 025_Numbers [ ]
    ├── 030_Teams [ ]
    └── DirectionCompass1 [ ]

# Excluded folders

├── Combat
│   ├── 020_Names
├── CombatEngage
│   ├── 020_Names
├── Normal
│   ├── 020_Names
├── NormalEngage
│   ├── 020_Names
├── NormalTarget
│   ├── 020_Names
├── NormalWatch
│   ├── 020_Names
├── Stealth
│   ├── 020_Names
├── StealthEngage
│   ├── 020_Names
└── StealthWatch
	├── 020_Names
