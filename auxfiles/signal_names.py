LAYOUT_SIZE = {
    1: (1, 1),
    7: (3, 3),
    5: (1, 5),
    10: (2, 5),
    12: (3,4),
    16: (4, 4),
    20: (4, 5),
    24: (4, 6),
    25: (5, 5),
    28: (4, 7),
    29: (5, 6),
    32: (4, 8),
}

SIGNAL_NAMES = {
    "Diagnostics": [
        "IACCEL1",
        "Ip_b4_",
        "MIR5C",
        "IACCEL2",
        "W_b4_corr_",
        "ECE10",
        "GR",
        "DENCM0_",
        "RX109",
        "GR2",
        "Densidad2_",
        "ABOL8",
    ],
    "MIR5C": ["MIR5C"],
    "Mirnov - Helical - Upper - T": [
        "H1T01",
        "H1T02",
        "H1T03",
        "H1T04",
        "H1T05",
        "H1T06",
        "H1T07",
        "H2T08",
        "H2T09",
        "H2T10",
        "H2T11",
        "H2T12",
        "H2T13",
        "H2T14",
        "H2T15",
        "H2T16",
        "H3T17",
        "H3T18",
        "H3T19",
        "H3T20",
        "H3T21",
        "H3T22",
        "H3T23",
        "H3T24",
        "H3T25",
        "H4T26",
        "H4T27",
        "H4T28",
        "H4T29",
        "H4T30",
        "H4T31",
        "H4T32",
    ],
    "Mirnov - Helical - Upper - P": [
        "H1P01",
        "H1P02",
        "H1P03",
        "H1P04",
        "H1P05",
        "H1P06",
        "H1P07",
        "H2P08",
        "H2P09",
        "H2P10",
        "H2P11",
        "H2P12",
        "H2P13",
        "H2P14",
        "H2P15",
        "H2P16",
        "H3P17",
        "H3P18",
        "H3P19",
        "H3P20",
        "H3P21",
        "H3P22",
        "H3P23",
        "H3P24",
        "H3P25",
        "H4P26",
        "H4P27",
        "H4P28",
        "H4P29",
        "H4P30",
        "H4P31",
        "H4P32",
    ],
    "Mirnov - Helical - Upper - R": [
        "H1R01",
        "H1R02",
        "H1R03",
        "H1R04",
        "H1R05",
        "H1R06",
        "H1R07",
        "H2R08",
        "H2R09",
        "H2R10",
        "H2R11",
        "H2R12",
        "H2R13",
        "H2R14",
        "H2R15",
        "H2R16",
        "H3R17",
        "H3R18",
        "H3R19",
        "H3R20",
        "H3R21",
        "H3R22",
        "H3R23",
        "H3R24",
        "H3R25",
        "H4R26",
        "H4R27",
        "H4R28",
        "H4R29",
        "H4R30",
        "H4R31",
        "H4R32",
    ],
    "Mirnov - Helical - Lower - T": [
        "H5T33",
        "H5T34",
        "H5T35",
        "H5T36",
        "H5T37",
        "H5T38",
        "H5T39",
        "H6T40",
        "H6T41",
        "H6T42",
        "H6T43",
        "H6T44",
        "H6T45",
        "H6T46",
        "H6T47",
        "H6T48",
        "H7T49",
        "H7T50",
        "H7T51",
        "H7T52",
        "H7T53",
        "H7T54",
        "H7T55",
        "H7T56",
        "H7T57",
        "H8T58",
        "H8T59",
        "H8T60",
        "H8T61",
        "H8T62",
        "H8T63",
        "H8T64",
    ],
    "Mirnov - Helical - Lower - P": [
        "H5P33",
        "H5P34",
        "H5P35",
        "H5P36",
        "H5P37",
        "H5P38",
        "H5P39",
        "H6P40",
        "H6P41",
        "H6P42",
        "H6P43",
        "H6P44",
        "H6P45",
        "H6P46",
        "H6P47",
        "H6P48",
        "H7P49",
        "H7P50",
        "H7P51",
        "H7P52",
        "H7P53",
        "H7P54",
        "H7P55",
        "H7P56",
        "H7P57",
        "H8P58",
        "H8P59",
        "H8P60",
        "H8P61",
        "H8P62",
        "H8P63",
        "H8P64",
    ],
    "Mirnov - Helical - Lower - R": [
        "H5R33",
        "H5R34",
        "H5R35",
        "H5R36",
        "H5R37",
        "H5R38",
        "H5R39",
        "H6R40",
        "H6R41",
        "H6R42",
        "H6R43",
        "H6R44",
        "H6R45",
        "H6R46",
        "H6R47",
        "H6R48",
        "H7R49",
        "H7R50",
        "H7R51",
        "H7R52",
        "H7R53",
        "H7R54",
        "H7R55",
        "H7R56",
        "H7R57",
        "H8R58",
        "H8R59",
        "H8R60",
        "H8R61",
        "H8R62",
        "H8R63",
        "H8R64",
    ],
    "Mirnov - Poloidal": [
        "MID5P_05",
        "MID5P_04",
        "MID5P_03",
        "MID5P_02",
        "MID5P_01",
        "MID5P1",
        "MID5P2",
        "MID5P3",
        "MID5P4",
        "MID5P5",
        "MID5P6",
        "MID5P7",
        "MID5P8",
        "MID5P9",
        "MID5P10",
        "MID5P11",
        "MID5P12",
        "MID5P13",
        "MID5P14",
        "MID5P15",
        "MID5P16",
        "MID5P17",
        "MID5P18",
        "MID5P19",
        "MID5P20",
    ],
    "Mirnov - Straight": [
        "MIR1C",
        "MIR2C",
        "MIR3C",
        "MIR4C",
        "MIR5C",
        "MIR6C",
        "MIR7C",
        "MIR8C",
        "MIR9C",
        "MIR10C",
        "MIR11C",
        "MIR12C",
        "MIB5Z1",
        "MIB5R1",
        "MIB5F1",
        "MIB5Z2",
        "MIB5R2",
        "MIB5F2",
        "MIB5Z3",
        "MIB5R3",
        "MIB5F3",
        "MIB5Z4",
        "MIB5R4",
        "MIB5F4",
    ],
    "ECE + FILD": [
        "ECE1",
        "ECE2",
        "ECE3",
        "ECE4",
        "ECE5",
        "ECE6",
        "ECE7",
        "ECE8",
        "ECE9",
        "ECE10",
        "ECE11",
        "ECE12",
        "ECE13",
        "ECE14",
        "FILD_CAM",
        "FILD_PMT",
    ],
    "Currents": [
        "TFI",
        "CCI",
        "HX1I",
        "HX2I",
        "VFI",
    ],
    "Bolometry - A": [
        "ABOL1",
        "ABOL2",
        "ABOL3",
        "ABOL4",
        "ABOL5",
        "ABOL6",
        "ABOL7",
        "ABOL8",
        "ABOL9",
        "ABOL10",
        "ABOL11",
        "ABOL12",
        "ABOL13",
        "ABOL14",
        "ABOL15",
        "ABOL16",
    ],
    "Bolometry - B": ["BOL1", "BOL2", "BOL3", "BOL4", "BOL5", "BOL6", "BOL7"],
    "Bolometry - C": [
        "CBOL1",
        "CBOL2",
        "CBOL3",
        "CBOL4",
        "CBOL5",
        "CBOL6",
        "CBOL7",
        "CBOL8",
        "CBOL9",
        "CBOL10",
        "CBOL11",
        "CBOL12",
        "CBOL13",
        "CBOL14",
        "CBOL15",
        "CBOL16",
    ],
    "Bolometry - S7 - 1": [
        "BO101",
        "BO102",
        "BO103",
        "BO104",
        "BO105",
        "BO106",
        "BO107",
        "BO108",
        "BO109",
        "BO110",
        "BO111",
        "BO112",
        "BO113",
        "BO114",
        "BO115",
        "BO116",
        "BO117",
        "BO118",
        "BO119",
        "BO120",
    ],
    "Bolometry - S7 - 2": [
        "BO201",
        "BO202",
        "BO203",
        "BO204",
        "BO205",
        "BO206",
        "BO207",
        "BO208",
        "BO209",
        "BO210",
        "BO211",
        "BO212",
        "BO213",
        "BO214",
        "BO215",
        "BO216",
        "BO217",
        "BO218",
        "BO219",
        "BO220",
    ],
    "Bolometry - S7 - 3": [
        "BO301",
        "BO302",
        "BO303",
        "BO304",
        "BO305",
        "BO306",
        "BO307",
        "BO308",
        "BO309",
        "BO310",
        "BO311",
        "BO312",
        "BO313",
        "BO314",
        "BO315",
        "BO316",
    ],
    "RX - 1": [
        "RX101",
        "RX102",
        "RX103",
        "RX104",
        "RX105",
        "RX106",
        "RX107",
        "RX108",
        "RX109",
        "RX110",
        "RX111",
        "RX112",
        "RX113",
        "RX114",
        "RX115",
        "RX116",
    ],
    "RX - 2": [
        "RX201",
        "RX202",
        "RX203",
        "RX204",
        "RX205",
        "RX206",
        "RX207",
        "RX208",
        "RX209",
        "RX210",
        "RX211",
        "RX212",
        "RX213",
        "RX214",
        "RX215",
        "RX216",
    ],
    "RX - 3": [
        "RX301",
        "RX302",
        "RX303",
        "RX304",
        "RX305",
        "RX306",
        "RX307",
        "RX308",
        "RX309",
        "RX310",
        "RX311",
        "RX312",
        "RX313",
        "RX314",
        "RX315",
        "RX316",
    ],
    "RX - 4": [
        "RX401",
        "RX402",
        "RX403",
        "RX404",
        "RX405",
        "RX406",
        "RX407",
        "RX408",
        "RX409",
        "RX410",
        "RX411",
        "RX412",
        "RX413",
        "RX414",
        "RX415",
        "RX416",
    ],
    "RX - 5": [
        "RX501",
        "RX502",
        "RX503",
        "RX504",
        "RX505",
        "RX506",
        "RX507",
        "RX508",
        "RX509",
        "RX510",
        "RX511",
        "RX512",
        "RX513",
        "RX514",
        "RX515",
        "RX516",
    ],
    "Langmuir": [
        "LOP01",
        "LOP02",
        "LOP03",
        "LOP04",
        "LOP05",
        "LOP06",
        "LOP07",
        "LOP08",
        "LOP09",
        "LOP10",
        "LOP101",
        "LOP102",
        "LOP103",
        "LOP104",
        "LOP105",
        "LOP106",
        "LOP107",
        "LOP108",
        "LOP109",
        "LOP11",
        "LOP110",
        "LOP111",
        "LOP12",
        "LOP13",
        "LOP14",
        "LOP15",
        "LOP16",
        "LOP17",
        "LOP18",
    ],
    "T01 - T16": [
        "H1T01",
        "H1T02",
        "H1T03",
        "H1T04",
        "H1T05",
        "H1T06",
        "H1T07",
        "H2T08",
        "H2T09",
        "H2T10",
        "H2T11",
        "H2T12",
        "H2T13",
        "H2T14",
        "H2T15",
        "H2T16",
    ],
    "T17 - T32": [
        "H3T17",
        "H3T18",
        "H3T19",
        "H3T20",
        "H3T21",
        "H3T22",
        "H3T23",
        "H3T24",
        "H3T25",
        "H4T26",
        "H4T27",
        "H4T28",
        "H4T29",
        "H4T30",
        "H4T31",
        "H4T32",
    ],
    "T33 - T48": [
        "H5T33",
        "H5T34",
        "H5T35",
        "H5T36",
        "H5T37",
        "H5T38",
        "H5T39",
        "H6T40",
        "H6T41",
        "H6T42",
        "H6T43",
        "H6T44",
        "H6T45",
        "H6T46",
        "H6T47",
        "H6T48",
    ],
    "T49 - T64": [
        "H7T49",
        "H7T50",
        "H7T51",
        "H7T52",
        "H7T53",
        "H7T54",
        "H7T55",
        "H7T56",
        "H7T57",
        "H8T58",
        "H8T59",
        "H8T60",
        "H8T61",
        "H8T62",
        "H8T63",
        "H8T64",
    ],
    "P01 - P16": [
        "H1P01",
        "H1P02",
        "H1P03",
        "H1P04",
        "H1P05",
        "H1P06",
        "H1P07",
        "H2P08",
        "H2P09",
        "H2P10",
        "H2P11",
        "H2P12",
        "H2P13",
        "H2P14",
        "H2P15",
        "H2P16",
    ],
    "P17 - P32": [
        "H3P17",
        "H3P18",
        "H3P19",
        "H3P20",
        "H3P21",
        "H3P22",
        "H3P23",
        "H3P24",
        "H3P25",
        "H4P26",
        "H4P27",
        "H4P28",
        "H4P29",
        "H4P30",
        "H4P31",
        "H4P32",
    ],
    "P33 - P48": [
        "H5P33",
        "H5P34",
        "H5P35",
        "H5P36",
        "H5P37",
        "H5P38",
        "H5P39",
        "H6P40",
        "H6P41",
        "H6P42",
        "H6P43",
        "H6P44",
        "H6P45",
        "H6P46",
        "H6P47",
        "H6P48",
    ],
    "P49 - P64": [
        "H7P49",
        "H7P50",
        "H7P51",
        "H7P52",
        "H7P53",
        "H7P54",
        "H7P55",
        "H7P56",
        "H7P57",
        "H8P58",
        "H8P59",
        "H8P60",
        "H8P61",
        "H8P62",
        "H8P63",
        "H8P64",
    ],
    "R01 - R16": [
        "H1R01",
        "H1R02",
        "H1R03",
        "H1R04",
        "H1R05",
        "H1R06",
        "H1R07",
        "H2R08",
        "H2R09",
        "H2R10",
        "H2R11",
        "H2R12",
        "H2R13",
        "H2R14",
        "H2R15",
        "H2R16",
    ],
    "R17 - R32": [
        "H3R17",
        "H3R18",
        "H3R19",
        "H3R20",
        "H3R21",
        "H3R22",
        "H3R23",
        "H3R24",
        "H3R25",
        "H4R26",
        "H4R27",
        "H4R28",
        "H4R29",
        "H4R30",
        "H4R31",
        "H4R32",
    ],
    "R33 - R48": [
        "H5R33",
        "H5R34",
        "H5R35",
        "H5R36",
        "H5R37",
        "H5R38",
        "H5R39",
        "H6R40",
        "H6R41",
        "H6R42",
        "H6R43",
        "H6R44",
        "H6R45",
        "H6R46",
        "H6R47",
        "H6R48",
    ],
    "R49 - R64": [
        "H7R49",
        "H7R50",
        "H7R51",
        "H7R52",
        "H7R53",
        "H7R54",
        "H7R55",
        "H7R56",
        "H7R57",
        "H8R58",
        "H8R59",
        "H8R60",
        "H8R61",
        "H8R62",
        "H8R63",
        "H8R64",
    ],
    "Mirnov - all": [
        "H1P01",
        "H1P02",
        "H1P03",
        "H1P04",
        "H1P05",
        "H1P06",
        "H1P07",
        "H1R01",
        "H1R02",
        "H1R03",
        "H1R04",
        "H1R05",
        "H1R06",
        "H1R07",
        "H1T01",
        "H1T02",
        "H1T03",
        "H1T04",
        "H1T05",
        "H1T06",
        "H1T07",
        "H2P08",
        "H2P09",
        "H2P10",
        "H2P11",
        "H2P12",
        "H2P13",
        "H2P14",
        "H2P15",
        "H2P16",
        "H2R08",
        "H2R09",
        "H2R10",
        "H2R11",
        "H2R12",
        "H2R13",
        "H2R14",
        "H2R15",
        "H2R16",
        "H2T08",
        "H2T09",
        "H2T10",
        "H2T11",
        "H2T12",
        "H2T13",
        "H2T14",
        "H2T15",
        "H2T16",
        "H3P17",
        "H3P18",
        "H3P19",
        "H3P20",
        "H3P21",
        "H3P22",
        "H3P23",
        "H3P24",
        "H3P25",
        "H3R17",
        "H3R18",
        "H3R19",
        "H3R20",
        "H3R21",
        "H3R22",
        "H3R23",
        "H3R24",
        "H3R25",
        "H3T17",
        "H3T18",
        "H3T19",
        "H3T20",
        "H3T21",
        "H3T22",
        "H3T23",
        "H3T24",
        "H3T25",
        "H4P26",
        "H4P27",
        "H4P28",
        "H4P29",
        "H4P30",
        "H4P31",
        "H4P32",
        "H4R26",
        "H4R27",
        "H4R28",
        "H4R29",
        "H4R30",
        "H4R31",
        "H4R32",
        "H4T26",
        "H4T27",
        "H4T28",
        "H4T29",
        "H4T30",
        "H4T31",
        "H4T32",
        "H5P33",
        "H5P34",
        "H5P35",
        "H5P36",
        "H5P37",
        "H5P38",
        "H5P39",
        "H5R33",
        "H5R34",
        "H5R35",
        "H5R36",
        "H5R37",
        "H5R38",
        "H5R39",
        "H5T33",
        "H5T34",
        "H5T35",
        "H5T36",
        "H5T37",
        "H5T38",
        "H5T39",
        "H6P40",
        "H6P41",
        "H6P42",
        "H6P43",
        "H6P44",
        "H6P45",
        "H6P46",
        "H6P47",
        "H6P48",
        "H6R40",
        "H6R41",
        "H6R42",
        "H6R43",
        "H6R44",
        "H6R45",
        "H6R46",
        "H6R47",
        "H6R48",
        "H6T40",
        "H6T41",
        "H6T42",
        "H6T43",
        "H6T44",
        "H6T45",
        "H6T46",
        "H6T47",
        "H6T48",
        "H7P49",
        "H7P50",
        "H7P51",
        "H7P52",
        "H7P53",
        "H7P54",
        "H7P55",
        "H7P56",
        "H7P57",
        "H7R49",
        "H7R50",
        "H7R51",
        "H7R52",
        "H7R53",
        "H7R54",
        "H7R55",
        "H7R56",
        "H7R57",
        "H7T49",
        "H7T50",
        "H7T51",
        "H7T52",
        "H7T53",
        "H7T54",
        "H7T55",
        "H7T56",
        "H7T57",
        "H8P58",
        "H8P59",
        "H8P60",
        "H8P61",
        "H8P62",
        "H8P63",
        "H8P64",
        "H8R58",
        "H8R59",
        "H8R60",
        "H8R61",
        "H8R62",
        "H8R63",
        "H8R64",
        "H8T58",
        "H8T59",
        "H8T60",
        "H8T61",
        "H8T62",
        "H8T63",
        "H8T64",
        "MIB5F1",
        "MIB5F2",
        "MIB5F3",
        "MIB5F4",
        "MIB5R1",
        "MIB5R2",
        "MIB5R3",
        "MIB5R4",
        "MIB5Z1",
        "MIB5Z2",
        "MIB5Z3",
        "MIB5Z4",
        "MID5P1",
        "MID5P10",
        "MID5P11",
        "MID5P12",
        "MID5P13",
        "MID5P14",
        "MID5P15",
        "MID5P16",
        "MID5P17",
        "MID5P18",
        "MID5P19",
        "MID5P2",
        "MID5P20",
        "MID5P3",
        "MID5P4",
        "MID5P5",
        "MID5P6",
        "MID5P7",
        "MID5P8",
        "MID5P9",
        "MID5P_01",
        "MID5P_02",
        "MID5P_03",
        "MID5P_04",
        "MID5P_05",
        "MIR10C",
        "MIR11C",
        "MIR12C",
        "MIR1C",
        "MIR2C",
        "MIR3C",
        "MIR4C",
        "MIR5C",
        "MIR6C",
        "MIR7C",
        "MIR8C",
        "MIR9C",
    ],
}
