import pandas as pd
from numpy import nan

TEST_DF = pd.DataFrame(
    {
        "AC": {
            12535: 125.8102,
            12536: 126.4008,
            30344: 133.9253,
            30345: 137.9073,
            48749: 140.8219,
            48750: 140.0843,
            69538: 136.7872,
            69539: 138.2639,
            87126: 152.8697,
            87127: 152.9971,
        },
        "BS": {
            12535: 12.25,
            12536: 12.25,
            30344: 17.5,
            30345: 17.5,
            48749: nan,
            48750: nan,
            69538: 12.25,
            69539: 12.25,
            87126: 12.25,
            87127: 12.25,
        },
        "DENC": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            48749: nan,
            48750: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DEPTH": {
            12535: 2100.4256,
            12536: 2100.578,
            30344: 2141.22,
            30345: 2141.3724,
            48749: 1087.118,
            48750: 1087.2704,
            69538: 2090.5196,
            69539: 2090.672,
            87126: 1450.086,
            87127: 1450.2384,
        },
        "GR": {
            12535: 99.78,
            12536: 100.49,
            30344: 108.207,
            30345: 108.0328,
            48749: 61.900180000000006,
            48750: 62.496930000000006,
            69538: 55.46915,
            69539: 60.19225,
            87126: 56.51378,
            87127: 57.95339,
        },
        "NEU": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            48749: nan,
            48750: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "RDEP": {
            12535: 0.77,
            12536: 0.73,
            30344: 0.4615473,
            30345: 0.5001374,
            48749: 1.874956,
            48750: 1.868164,
            69538: 0.525528,
            69539: 0.5493600000000001,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED": {
            12535: 0.7,
            12536: 0.6800001,
            30344: 0.4679713,
            30345: 0.5017649000000001,
            48749: 1.741518,
            48750: 1.720216,
            69538: 0.71134,
            69539: 0.67108,
            87126: 0.7484,
            87127: 0.7484,
        },
        "lsuName": {
            12535: "ROGALAND",
            12536: "ROGALAND",
            30344: "HORDALAND",
            30345: "HORDALAND",
            48749: "HORDALAND",
            48750: "HORDALAND",
            69538: "HORDALAND",
            69539: "HORDALAND",
            87126: "HORDALAND",
            87127: "HORDALAND",
        },
        "well_name": {
            12535: "30/6-26",
            12536: "30/6-26",
            30344: "30/11-8 S",
            30345: "30/11-8 S",
            48749: "25/4-9 S",
            48750: "25/4-9 S",
            69538: "30/11-6 S",
            69539: "30/11-6 S",
            87126: "25/7-4 S",
            87127: "25/7-4 S",
        },
    }
)

TRAIN_DF = pd.DataFrame(
    {
        "AC": {
            12535: 125.8102,
            12536: 126.4008,
            30344: 133.9253,
            30345: 137.9073,
            69538: 136.7872,
            69539: 138.2639,
            87126: 152.8697,
            87127: 152.9971,
        },
        "BS": {
            12535: 12.25,
            12536: 12.25,
            30344: 17.5,
            30345: 17.5,
            69538: 12.25,
            69539: 12.25,
            87126: 12.25,
            87127: 12.25,
        },
        "DENC": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DEPTH": {
            12535: 2100.4256,
            12536: 2100.578,
            30344: 2141.22,
            30345: 2141.3724,
            69538: 2090.5196,
            69539: 2090.672,
            87126: 1450.086,
            87127: 1450.2384,
        },
        "GR": {
            12535: 99.78,
            12536: 100.49,
            30344: 108.207,
            30345: 108.0328,
            69538: 55.46915,
            69539: 60.19225,
            87126: 56.51378,
            87127: 57.95339,
        },
        "NEU": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "RDEP": {
            12535: 0.77,
            12536: 0.73,
            30344: 0.4615473,
            30345: 0.5001374,
            69538: 0.525528,
            69539: 0.5493600000000001,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED": {
            12535: 0.7,
            12536: 0.6800001,
            30344: 0.4679713,
            30345: 0.5017649000000001,
            69538: 0.71134,
            69539: 0.67108,
            87126: 0.7484,
            87127: 0.7484,
        },
        "lsuName": {
            12535: "ROGALAND",
            12536: "ROGALAND",
            30344: "HORDALAND",
            30345: "HORDALAND",
            69538: "HORDALAND",
            69539: "HORDALAND",
            87126: "HORDALAND",
            87127: "HORDALAND",
        },
        "well_name": {
            12535: "30/6-26",
            12536: "30/6-26",
            30344: "30/11-8 S",
            30345: "30/11-8 S",
            69538: "30/11-6 S",
            69539: "30/11-6 S",
            87126: "25/7-4 S",
            87127: "25/7-4 S",
        },
    }
)

PREPROCESSED_DF = pd.DataFrame(
    {
        "AC": {
            12535: 125.8102,
            12536: 126.4008,
            30344: 133.9253,
            30345: 137.9073,
            69538: 136.7872,
            69539: 138.2639,
            87126: 152.8697,
            87127: 152.9971,
        },
        "BS": {
            12535: 12.25,
            12536: 12.25,
            30344: 17.5,
            30345: 17.5,
            69538: 12.25,
            69539: 12.25,
            87126: 12.25,
            87127: 12.25,
        },
        "DENC": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DENC_gradient": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DENC_log": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DENC_window_max": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DENC_window_mean": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DENC_window_min": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "DEPTH": {
            12535: 2100.4256,
            12536: 2100.578,
            30344: 2141.22,
            30345: 2141.3724,
            69538: 2090.5196,
            69539: 2090.672,
            87126: 1450.086,
            87127: 1450.2384,
        },
        "GR_gradient": {
            12535: 4.723100000000002,
            12536: 4.723100000000002,
            30344: -4.723099999999626,
            30345: -4.723099999999626,
            69538: 4.723100000000002,
            69539: 4.723100000000002,
            87126: 4.723100000000031,
            87127: 4.723100000000031,
        },
        "GR_log": {
            12535: 2.00337435401975,
            12536: 2.006423252507643,
            30344: 2.038250476866334,
            30345: 2.037557165061478,
            69538: 1.751811250582852,
            69539: 1.7866964222213135,
            87126: 1.759771911836876,
            87127: 1.7705087834084305,
        },
        "GR_window_max": {
            12535: 55.46915,
            12536: 60.19225,
            30344: 60.19224999999982,
            30345: 60.19224999999982,
            69538: 55.46915,
            69539: 60.19225,
            87126: 55.469149999999985,
            87127: 60.192250000000016,
        },
        "GR_window_mean": {
            12535: 55.46915,
            12536: 57.8307,
            30344: 60.19224999999982,
            30345: 57.83070000000001,
            69538: 55.46915,
            69539: 57.8307,
            87126: 55.469149999999985,
            87127: 57.8307,
        },
        "GR_window_min": {
            12535: 55.46915,
            12536: 55.46915,
            30344: 60.19224999999982,
            30345: 55.46915000000019,
            69538: 55.46915,
            69539: 55.46915,
            87126: 55.469149999999985,
            87127: 55.469149999999985,
        },
        "NEU": {
            12535: nan,
            12536: nan,
            30344: nan,
            30345: nan,
            69538: nan,
            69539: nan,
            87126: nan,
            87127: nan,
        },
        "RAVG": {
            12535: 0.735,
            12536: 0.70500005,
            30344: 0.4647593,
            30345: 0.50095115,
            69538: 0.6184339999999999,
            69539: 0.61022,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RDEP": {
            12535: 0.77,
            12536: 0.73,
            30344: 0.4615473,
            30345: 0.5001374,
            69538: 0.525528,
            69539: 0.5493600000000001,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RDEP_gradient": {
            12535: -0.040000000000000036,
            12536: -0.040000000000000036,
            30344: 0.03859009999999996,
            30345: 0.03859009999999996,
            69538: 0.023832000000000075,
            69539: 0.023832000000000075,
            87126: 0.0,
            87127: 0.0,
        },
        "RDEP_log": {
            12535: 1.0,
            12536: 0.8806263045702858,
            30344: 0.0,
            30345: 0.13610041322629352,
            69538: 0.22375205234737505,
            69539: 0.30470593208530605,
            87126: 0.9358773034207699,
            87127: 0.9358773034207699,
        },
        "RDEP_window_max": {
            12535: 0.77,
            12536: 0.77,
            30344: 0.4615473,
            30345: 0.5001374,
            69538: 0.525528,
            69539: 0.5493600000000001,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RDEP_window_mean": {
            12535: 0.77,
            12536: 0.75,
            30344: 0.4615473,
            30345: 0.48084235,
            69538: 0.525528,
            69539: 0.537444,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RDEP_window_min": {
            12535: 0.77,
            12536: 0.73,
            30344: 0.4615473,
            30345: 0.4615473,
            69538: 0.525528,
            69539: 0.525528,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED": {
            12535: 0.7,
            12536: 0.6800001,
            30344: 0.4679713,
            30345: 0.5017649000000001,
            69538: 0.71134,
            69539: 0.67108,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED_gradient": {
            12535: -0.01999989999999996,
            12536: -0.01999989999999996,
            30344: 0.03379360000000009,
            30345: 0.03379360000000009,
            69538: -0.04025999999999996,
            69539: -0.04025999999999996,
            87126: 0.0,
            87127: 0.0,
        },
        "RMED_log": {
            12535: 0.2304489213782739,
            12536: 0.2253093075767241,
            30344: 0.16671756486242714,
            30345: 0.17660194956274478,
            69538: 0.2333363014491707,
            69539: 0.22299724147142588,
            87126: 0.24264079781761497,
            87127: 0.24264079781761497,
        },
        "RMED_window_max": {
            12535: 0.7,
            12536: 0.7,
            30344: 0.4679713,
            30345: 0.5017649000000001,
            69538: 0.71134,
            69539: 0.71134,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED_window_mean": {
            12535: 0.7,
            12536: 0.69000005,
            30344: 0.4679713,
            30345: 0.4848681,
            69538: 0.71134,
            69539: 0.69121,
            87126: 0.7484,
            87127: 0.7484,
        },
        "RMED_window_min": {
            12535: 0.7,
            12536: 0.6800001,
            30344: 0.4679713,
            30345: 0.4679713,
            69538: 0.71134,
            69539: 0.67108,
            87126: 0.7484,
            87127: 0.7484,
        },
        "lsuName": {
            12535: 21,
            12536: 21,
            30344: 14,
            30345: 14,
            69538: 14,
            69539: 14,
            87126: 14,
            87127: 14,
        },
        "well_name": {
            12535: "30/6-26",
            12536: "30/6-26",
            30344: "30/11-8 S",
            30345: "30/11-8 S",
            69538: "30/11-6 S",
            69539: "30/11-6 S",
            87126: "25/7-4 S",
            87127: "25/7-4 S",
        },
    }
)

FORMATION_TOPS_MAPPER = {
    "25/10-10": {
        "formation_labels": [
            "Utsira Formation",
            "UNKNOWN",
            "Skade Formation",
            "UNKNOWN",
            "Grid Formation",
            "UNKNOWN",
            "Balder Formation",
            "Sele Formation",
            "Lista Formation",
            "Heimdal Formation",
            "Lista Formation",
            "Heimdal Formation",
            "Lista Formation",
            "Ty Formation",
            "Tor Formation",
            "UNKNOWN",
            "Skagerrak Formation",
            "Smith Bank Formation",
        ],
        "formation_labels_chronostrat": [
            "Miocene",
            "UNKNOWN",
            "Oligocene",
            "UNKNOWN",
            "Eocene",
            "UNKNOWN",
            "Eocene",
            "Paleocene",
            "Paleocene",
            "Paleocene",
            "Paleocene",
            "Paleocene",
            "Paleocene",
            "Paleocene",
            "Upper Cretaceous",
            "UNKNOWN",
            "Triassic",
            "Triassic",
        ],
        "formation_levels": [
            575.0,
            710.0,
            777.0,
            1270.0,
            1505.0,
            1518.0,
            1768.0,
            1813.0,
            1851.0,
            1856.0,
            1913.0,
            1940.0,
            1991.0,
            2036.0,
            2069.0,
            2072.0,
            2173.0,
            2368.0,
            2432.0,
        ],
        "group_labels": [
            "Nordland Group",
            "Hordaland Group",
            "Rogaland Group",
            "Shetland Group",
            "Statfjord Group",
            "UNKNOWN",
            "Zechstein Group",
        ],
        "group_labels_chronostrat": [
            "Cenozoic",
            "Paleogene",
            "Paleogene",
            "Upper Cretaceous",
            "Lower Jurassic",
            "UNKNOWN",
            "Permian",
        ],
        "group_levels": [164.0, 777.0, 1768.0, 2069.0, 2072.0, 2173.0, 2488.0, 2513.0],
    },
}

FORMATION_DF = pd.DataFrame(
    {
        "DEPTH": {
            650372: 575.0052000000002,
            651258: 710.0316,
            651698: 777.0876000000002,
            654933: 1270.1016,
            656475: 1505.1024,
            658201: 1768.1448,
            658496: 1813.1028,
            658745: 1851.0504,
            658778: 1856.0796,
            659959: 2036.064,
            660176: 2069.1348,
            660195: 2072.0304,
            660858: 2173.0716,
            662138: 2368.1436,
        },
        "FORMATION": {
            650372: "Utsira Formation",
            651258: "UNKNOWN",
            651698: "Skade Formation",
            654933: "UNKNOWN",
            656475: "Grid Formation",
            658201: "Balder Formation",
            658496: "Sele Formation",
            658745: "Lista Formation",
            658778: "Heimdal Formation",
            659959: "Ty Formation",
            660176: "Tor Formation",
            660195: "UNKNOWN",
            660858: "Skagerrak Formation",
            662138: "Smith Bank Formation",
        },
        "GROUP": {
            650372: "Nordland Group",
            651258: "Nordland Group",
            651698: "Hordaland Group",
            654933: "Hordaland Group",
            656475: "Hordaland Group",
            658201: "Rogaland Group",
            658496: "Rogaland Group",
            658745: "Rogaland Group",
            658778: "Rogaland Group",
            659959: "Rogaland Group",
            660176: "Shetland Group",
            660195: "Statfjord Group",
            660858: "UNKNOWN",
            662138: "UNKNOWN",
        },
        "well_name": {
            650372: "25/10-10",
            651258: "25/10-10",
            651698: "25/10-10",
            654933: "25/10-10",
            656475: "25/10-10",
            658201: "25/10-10",
            658496: "25/10-10",
            658745: "25/10-10",
            658778: "25/10-10",
            659959: "25/10-10",
            660176: "25/10-10",
            660195: "25/10-10",
            660858: "25/10-10",
            662138: "25/10-10",
        },
    }
)


VERTICAL_DEPTHS_MAPPER = {
    "25/10-10": {
        "MD": [
            0.0,
            163.5,
            165.54,
            174.34,
            191.3,
            220.04,
            281.42,
            313.96,
            337.97,
            367.32,
            395.15,
            423.67,
            451.72,
            479.85,
            508.86,
            536.44,
            564.94,
            593.19,
            621.59,
            650.67,
            678.42,
            707.45,
            735.79,
            764.14,
            819.09,
            849.06,
            877.3,
            905.69,
            933.72,
            961.97,
            1018.28,
            1046.95,
            1075.71,
            1086.51,
            1121.52,
            1150.26,
            1178.46,
            1206.35,
            1234.23,
            1319.36,
            1346.9,
            1375.51,
            1460.23,
            1543.81,
            1573.42,
            1601.76,
            1630.08,
            1686.61,
            1714.56,
            1742.87,
            1772.11,
            1800.22,
            1885.65,
            1913.77,
            1942.51,
            1970.64,
            1999.51,
            2027.2,
            2055.23,
            2073.89,
            2083.94,
            2140.17,
            2169.33,
            2196.6,
            2253.54,
            2310.08,
            2338.59,
            2368.91,
            2423.94,
            2453.52,
            2480.8,
            2513.0,
        ],
        "TVDKB": [
            0.0,
            163.5,
            165.54,
            174.3395,
            191.2982,
            220.0358,
            281.4055,
            313.9397,
            337.9461,
            367.2915,
            395.1163,
            423.631,
            451.6766,
            479.8024,
            508.808,
            536.3838,
            564.8801,
            593.1278,
            621.5269,
            650.606,
            678.3532,
            707.3805,
            735.7193,
            764.0688,
            819.0166,
            848.9839,
            877.2217,
            905.6089,
            933.6362,
            961.8849,
            1018.1935,
            1046.8627,
            1075.6176,
            1086.4142,
            1121.4162,
            1150.1526,
            1178.3488,
            1206.2355,
            1234.1142,
            1319.2432,
            1346.7829,
            1375.3929,
            1460.1129,
            1543.6928,
            1573.3028,
            1601.6428,
            1629.9627,
            1686.4927,
            1714.4427,
            1742.7527,
            1771.9927,
            1800.1027,
            1885.5327,
            1913.6527,
            1942.3927,
            1970.5226,
            1999.3926,
            2027.0826,
            2055.1126,
            2073.7726,
            2083.8226,
            2140.0526,
            2169.2126,
            2196.4826,
            2253.4226,
            2309.9625,
            2338.4725,
            2368.7925,
            2423.8225,
            2453.4024,
            2480.6824,
            2512.8824,
        ],
        "TVDSS": [
            -40.0,
            123.5,
            125.54,
            134.3395,
            151.2982,
            180.0358,
            241.4055,
            273.9397,
            297.9461,
            327.2915,
            355.1163,
            383.631,
            411.6766,
            439.8024,
            468.808,
            496.3838,
            524.8801,
            553.1278,
            581.5269,
            610.606,
            638.3532,
            667.3805,
            695.7193,
            724.0688,
            779.0166,
            808.9839,
            837.2217,
            865.6089,
            893.6362,
            921.8849,
            978.1935,
            1006.8627,
            1035.6176,
            1046.4142,
            1081.4162,
            1110.1526,
            1138.3488,
            1166.2355,
            1194.1142,
            1279.2432,
            1306.7829,
            1335.3929,
            1420.1129,
            1503.6928,
            1533.3028,
            1561.6428,
            1589.9627,
            1646.4927,
            1674.4427,
            1702.7527,
            1731.9927,
            1760.1027,
            1845.5327,
            1873.6527,
            1902.3927,
            1930.5226,
            1959.3926,
            1987.0826,
            2015.1126,
            2033.7726,
            2043.8226,
            2100.0526,
            2129.2126,
            2156.4826,
            2213.4226,
            2269.9625,
            2298.4725,
            2328.7925,
            2383.8225,
            2413.4024,
            2440.6824,
            2472.8824,
        ],
        "TVDBML": [
            -163.5,
            0.0,
            2.0400000000000063,
            10.839499999999987,
            27.79820000000001,
            56.535799999999995,
            117.90549999999999,
            150.43970000000002,
            174.4461,
            203.79149999999998,
            231.61630000000002,
            260.131,
            288.1766,
            316.3024,
            345.308,
            372.8838,
            401.38009999999997,
            429.6278,
            458.02689999999996,
            487.106,
            514.8532,
            543.8805,
            572.2193,
            600.5688,
            655.5166,
            685.4839,
            713.7217,
            742.1089,
            770.1362,
            798.3849,
            854.6935,
            883.3627,
            912.1176,
            922.9141999999999,
            957.9161999999999,
            986.6525999999999,
            1014.8488,
            1042.7355,
            1070.6142,
            1155.7432,
            1183.2829,
            1211.8929,
            1296.6129,
            1380.1928,
            1409.8028,
            1438.1428,
            1466.4627,
            1522.9927,
            1550.9427,
            1579.2527,
            1608.4927,
            1636.6027,
            1722.0327,
            1750.1527,
            1778.8927,
            1807.0226,
            1835.8926,
            1863.5826,
            1891.6126,
            1910.2726,
            1920.3226,
            1976.5526,
            2005.7125999999998,
            2032.9825999999998,
            2089.9226,
            2146.4625,
            2174.9725,
            2205.2925,
            2260.3225,
            2289.9024,
            2317.1824,
            2349.3824,
        ],
    }
}

VERTICAL_DF = pd.DataFrame(
    {
        "DEPTH": {
            1142969: 1090.3664,
            1142970: 1090.5184,
            1142971: 1090.6704,
            1142972: 1090.8224,
            1142973: 1090.9744,
            1142974: 1091.1264,
            1142975: 1091.2784,
            1142976: 1091.4304,
            1142977: 1091.5824,
            1142978: 1091.7344,
            1142979: 1091.8864,
            1142980: 1092.0384,
            1142981: 1092.1904,
        },
        "TVDKB": {
            1142969: 1090.2697187889175,
            1142970: 1090.4216840559839,
            1142971: 1090.5736493230504,
            1142972: 1090.7256145901172,
            1142973: 1090.8775798571837,
            1142974: 1091.0295451242503,
            1142975: 1091.1815103913166,
            1142976: 1091.3334756583831,
            1142977: 1091.48544092545,
            1142978: 1091.6374061925164,
            1142979: 1091.789371459583,
            1142980: 1091.9413367266493,
            1142981: 1092.093301993716,
        },
        "TVDSS": {
            1142969: 1050.2697187889175,
            1142970: 1050.4216840559839,
            1142971: 1050.5736493230504,
            1142972: 1050.7256145901172,
            1142973: 1050.8775798571837,
            1142974: 1051.0295451242503,
            1142975: 1051.1815103913166,
            1142976: 1051.3334756583831,
            1142977: 1051.48544092545,
            1142978: 1051.6374061925164,
            1142979: 1051.789371459583,
            1142980: 1051.9413367266493,
            1142981: 1052.093301993716,
        },
        "TVDBML": {
            1142969: 926.7697187889175,
            1142970: 926.9216840559839,
            1142971: 927.0736493230505,
            1142972: 927.2256145901171,
            1142973: 927.3775798571837,
            1142974: 927.5295451242503,
            1142975: 927.6815103913166,
            1142976: 927.8334756583832,
            1142977: 927.9854409254498,
            1142978: 928.1374061925164,
            1142979: 928.289371459583,
            1142980: 928.4413367266494,
            1142981: 928.593301993716,
        },
        "well_name": {
            1142969: "25/10-10",
            1142970: "25/10-10",
            1142971: "25/10-10",
            1142972: "25/10-10",
            1142973: "25/10-10",
            1142974: "25/10-10",
            1142975: "25/10-10",
            1142976: "25/10-10",
            1142977: "25/10-10",
            1142978: "25/10-10",
            1142979: "25/10-10",
            1142980: "25/10-10",
            1142981: "25/10-10",
        },
    }
)
