designFile = "C:/Development/power-module/PowerModule/PDNAnalyzer_Output/PowerModule/odb.tgz"

powerNets = ["VIN", "VCC", "SW1_5V", "+5V", "SW2_5V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J2", "pdna_pin_1_1"), ("J2", "pdna_pin_1_2") ],
"ground_pins": [ ("J2", "pdna_pin_2_1"), ("J2", "pdna_pin_2_2") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J1", "5"), ("J1", "6"), ("J1", "7"), ("J1", "8") ],
"ground_pins": [ ("J1", "pdna_pin_SHLD_1"), ("J1", "pdna_pin_SHLD_2"), ("J1", "pdna_pin_SHLD_3"), ("J1", "pdna_pin_SHLD_4"), ("J1", "1"), ("J1", "2"), ("J1", "3"), ("J1", "4") ],
"current": 3,
"Rpin": 0.177777777777778,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("J1", "5"), ("J1", "6"), ("J1", "7"), ("J1", "8") ],
"ground_pins": [ ("J1", "pdna_pin_SHLD_1"), ("J1", "pdna_pin_SHLD_2"), ("J1", "pdna_pin_SHLD_3"), ("J1", "pdna_pin_SHLD_4"), ("J1", "1"), ("J1", "2"), ("J1", "3"), ("J1", "4") ],
"current": 3,
"Rpin": 0.177777777777778,
}
,
{
"id": "3",
"type": "source",
"power_pins": [ ("L1_5V", "1") ],
"ground_pins": [ ("U1_5V", "F3"), ("U1_5V", "E3"), ("U1_5V", "D3"), ("U1_5V", "C4"), ("U1_5V", "C3"), ("U1_5V", "B3"), ("U1_5V", "A3") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U1_5V", "A1"), ("U1_5V", "F1"), ("U1_5V", "E4"), ("U1_5V", "E1"), ("U1_5V", "D1"), ("U1_5V", "C1"), ("U1_5V", "B1") ],
"ground_pins": [ ("U1_5V", "F3"), ("U1_5V", "E3"), ("U1_5V", "D3"), ("U1_5V", "C4"), ("U1_5V", "C3"), ("U1_5V", "B3"), ("U1_5V", "A3") ],
"current": 1.45261525085915,
"Rpin": 0.48188947457765,
}
,
{
"id": "5",
"type": "source",
"power_pins": [ ("L2_5V", "1") ],
"ground_pins": [ ("U1_5V", "F3"), ("U1_5V", "E3"), ("U1_5V", "D3"), ("U1_5V", "C4"), ("U1_5V", "C3"), ("U1_5V", "B3"), ("U1_5V", "A3") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U1_5V", "A1"), ("U1_5V", "F1"), ("U1_5V", "E4"), ("U1_5V", "E1"), ("U1_5V", "D1"), ("U1_5V", "C1"), ("U1_5V", "B1") ],
"ground_pins": [ ("U1_5V", "F3"), ("U1_5V", "E3"), ("U1_5V", "D3"), ("U1_5V", "C4"), ("U1_5V", "C3"), ("U1_5V", "B3"), ("U1_5V", "A3") ],
"current": 1.50228716039229,
"Rpin": 0.465956188973358,
}
]


voltage_regulators = [
{
"id": "7",
"type": "linear",

"in": [ ("U2", "5") ],
"out": [ ("U2", "6") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0049,
}
,
{
"id": "8",
"type": "linear",

"in": [ ("L1_5V", "1") ],
"out": [ ("L1_5V", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.012,
}
,
{
"id": "9",
"type": "linear",

"in": [ ("L2_5V", "1") ],
"out": [ ("L2_5V", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.012,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'GND', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.5, 'Thickness': 0.001265},
        {'name': 'POWER', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
