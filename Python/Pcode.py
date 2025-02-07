import time
import os

A = [
    16,
    85,
    60,
    71,
    79,
    94,
    96,
    81,
    23,
    7,
    34,
    36,
    72,
    84,
    25,
    85,
    56,
    43,
    48,
    33,
    66,
    98,
    96,
    90,
    26,
    56,
    51,
    58,
    80,
    91,
    54,
    40,
    38,
    17,
    57,
    86,
    59,
    56,
    38,
    42,
    36,
    39,
    13,
    37,
    40,
    61,
    82,
    24,
    89,
    70,
    85,
    63,
    22,
    21,
    59,
    80,
    23,
    9,
    62,
    70,
    33,
    58,
    64,
    37,
    45,
    84,
    15,
    67,
    17,
    78,
    12,
    2,
    20,
    34,
    67,
    98,
    50,
    9,
    11,
    56,
    67,
    63,
    75,
    29,
    56,
    49,
    39,
    44,
    54,
    68,
    4,
    10,
    94,
    74,
    52,
    89,
    20,
    26,
    48,
    48,
    12,
    75,
    92,
    25,
    90,
    52,
    59,
    80,
    24,
    58,
    55,
    92,
    59,
    65,
    70,
    17,
    17,
    64,
    33,
    31,
    39,
    91,
    46,
    65,
    81,
    28,
    86,
    14,
    0,
    41,
    16,
    19,
    33,
    65,
    60,
    18,
    19,
    88,
    65,
    2,
    57,
    75,
    10,
    41,
    69,
    82,
    6,
    76,
    14,
    21,
    14,
    17,
    74,
    71,
    75,
    69,
    19,
    76,
    62,
    69,
    7,
    57,
    41,
    2,
    72,
    27,
    95,
    13,
    70,
    82,
    22,
    53,
    12,
    35,
    43,
    41,
    60,
    38,
    52,
    93,
    96,
    76,
    1,
    94,
    51,
    84,
    53,
    86,
    60,
    31,
    74,
    13,
    41,
    67,
    22,
    98,
    84,
    43,
    10,
    85,
    74,
    72,
    28,
    84,
    52,
    98,
    70,
    44,
    20,
    11,
    30,
    53,
    93,
    74,
    60,
    0,
    8,
    67,
    61,
    89,
    66,
    24,
    30,
    71,
    94,
    24,
    63,
    30,
    64,
    26,
    86,
    87,
    76,
    63,
    49,
    21,
    91,
    11,
    38,
    63,
    77,
    5,
    26,
    47,
    54,
    55,
    86,
    17,
    21,
    11,
    1,
    58,
    62,
    72,
    38,
    34,
    93,
    86,
    42,
    96,
    83,
    13,
    30,
    52,
    8,
    14,
    10,
    44,
    9,
    0,
    61,
    39,
    77,
    48,
    27,
    54,
    38,
    81,
    95,
    52,
    26,
    79,
    28,
    62,
    48,
    87,
    41,
    46,
    12,
    43,
    75,
    17,
    3,
    5,
    68,
    67,
    70,
    49,
    63,
    37,
    63,
    68,
    11,
    18,
    3,
    46,
    12,
    57,
    36,
    80,
    3,
    42,
    84,
    90,
    56,
    14,
    33,
    82,
    83,
    30,
    96,
    51,
    95,
    96,
    50,
    5,
    90,
    97,
    96,
    13,
    64,
    67,
    59,
    59,
    35,
    3,
    79,
    70,
    96,
    79,
    52,
    86,
    99,
    61,
    41,
    31,
    78,
    75,
    88,
    74,
    86,
    97,
    62,
    89,
    6,
    35,
    53,
    84,
    68,
    88,
    9,
    40,
    86,
    96,
    38,
    46,
    83,
    7,
    59,
    0,
    29,
    13,
    80,
    36,
    92,
    72,
    69,
    28,
    70,
    0,
    60,
    85,
    76,
    3,
    84,
    7,
    55,
    24,
    18,
    19,
    6,
    17,
    16,
    97,
    88,
    45,
    44,
    68,
    28,
    71,
    88,
    74,
    40,
    32,
    46,
    45,
    39,
    71,
    17,
    18,
    87,
    97,
    25,
    12,
    89,
    65,
    74,
    88,
    32,
    40,
    60,
    60,
    18,
    30,
    94,
    38,
    71,
    19,
    14,
    88,
    83,
    11,
    27,
    98,
    12,
    42,
    22,
    0,
    50,
    14,
    95,
    42,
    48,
    54,
    29,
    59,
    47,
    44,
    80,
    19,
    2,
    10,
    76,
    7,
    3,
    2,
    69,
    26,
    65,
    49,
    47,
    91,
    36,
    99,
    69,
    47,
    76,
    96,
    81,
    99,
    7,
    93,
    0,
    66,
    57,
    35,
    28,
    20,
    15,
    50,
    57,
    83,
    54,
    88,
    91,
    34,
    41,
    2,
    70,
    39,
    79,
    55,
    33,
    9,
    20,
    64,
    98,
    86,
    43,
    51,
    65,
    15,
    33,
    1,
    69,
    77,
    99,
    6,
    62,
    5,
    12,
    77,
    54,
    66,
    22,
    99,
    95,
    81,
    49,
    76,
    34,
    55,
    70,
    27,
    82,
    99,
    89,
    84,
    28,
    20,
    50,
    31,
    49,
    76,
    21,
    22,
    16,
    76,
    84,
    99,
    59,
    5,
    0,
    14,
    62,
    93,
    76,
    28,
    45,
    49,
    47,
    4,
    97,
    93,
    26,
    8,
    89,
    63,
    42,
    0,
    11,
    82,
    85,
    34,
    13,
    77,
    76,
    77,
    34,
    1,
    24,
    28,
    58,
    39,
    56,
    18,
    48,
    51,
    88,
    18,
    76,
    47,
    68,
    10,
    3,
    26,
    64,
    6,
    37,
    99,
    48,
    2,
    92,
    70,
    71,
    47,
    59,
    79,
    36,
    21,
    14,
    31,
    85,
    71,
    87,
    27,
    50,
    6,
    62,
    46,
    55,
    19,
    96,
    56,
    83,
    95,
    58,
    25,
    77,
    43,
    76,
    7,
    40,
    71,
    13,
    27,
    32,
    26,
    64,
    6,
    2,
    63,
    97,
    84,
    60,
    31,
    63,
    25,
    8,
    2,
    41,
    62,
    46,
    1,
    42,
    56,
    79,
    77,
    66,
    0,
    84,
    79,
    73,
    92,
    31,
    53,
    88,
    32,
    96,
    99,
    94,
    25,
    81,
    97,
    89,
    42,
    1,
    37,
    24,
    22,
    28,
    18,
    33,
    98,
    41,
    74,
    37,
    69,
    49,
    23,
    3,
    93,
    77,
    44,
    52,
    78,
    10,
    48,
    86,
    99,
    43,
    10,
    30,
    58,
    24,
    47,
    44,
    85,
    36,
    82,
    47,
    59,
    24,
    78,
    65,
    91,
    87,
    84,
    84,
    76,
    23,
    58,
    65,
    91,
    98,
    15,
    62,
    81,
    7,
    0,
    27,
    25,
    7,
    11,
    31,
    98,
    31,
    21,
    72,
    16,
    38,
    63,
    27,
    90,
    73,
    59,
    10,
    36,
    24,
    69,
    56,
    96,
    32,
    85,
    75,
    50,
    51,
    3,
    55,
    4,
    73,
    78,
    44,
    3,
    60,
    15,
    77,
    21,
    4,
    87,
    53,
    27,
    31,
    57,
    7,
    51,
    15,
    23,
    68,
    7,
    58,
    79,
    24,
    64,
    95,
    71,
    45,
    52,
    11,
    64,
    53,
    14,
    7,
    56,
    99,
    17,
    78,
    79,
    68,
    74,
    72,
    51,
    66,
    89,
    47,
    11,
    3,
    68,
    14,
    9,
    37,
    8,
    81,
    77,
    9,
    54,
    63,
    37,
    91,
    65,
    53,
    96,
    36,
    74,
    37,
    66,
    78,
    66,
    57,
    14,
    70,
    52,
    32,
    92,
    2,
    92,
    85,
    43,
    36,
    49,
    38,
    92,
    94,
    88,
    61,
    38,
    61,
    79,
    75,
    26,
    46,
    30,
    90,
    34,
    58,
    94,
    86,
    39,
    72,
    47,
    66,
    12,
    48,
    95,
    11,
    19,
    52,
    50,
    2,
    62,
    94,
    97,
    96,
    30,
    65,
    83,
    95,
    33,
    85,
    49,
    31,
    6,
    21,
    27,
    61,
    99,
    31,
    71,
    40,
    37,
    7,
    42,
    74,
    65,
    3,
    27,
    8,
    27,
    37,
    49,
    2,
    93,
    21,
    18,
    83,
    15,
    69,
    27,
    88,
    86,
    80,
    80,
    29,
    96,
    33,
    50,
    71,
    76,
    98,
    77,
    12,
    12,
    49,
    20,
    37,
    97,
    19,
    5,
    67,
    3,
    92,
    24,
    1,
    21,
    27,
    94,
    86,
    6,
    19,
    83,
    76,
    87,
    70,
    15,
    50,
    7,
    12,
    68,
    61,
    38,
    43,
    72,
    67,
    20,
    4,
    46,
    93,
    67,
    66,
    24,
    94,
    89,
    81,
    18,
    42,
    60,
    0,
    1,
    2,
    94,
    44,
    7,
    66,
    37,
    74,
    64,
    22,
    43,
    96,
    75,
    62,
    41,
    39,
    59,
    50,
    80,
    69,
    12,
    17,
    30,
    64,
    11,
    28,
    82,
    24,
    94,
    31,
    62,
    71,
    76,
    17,
    42,
    53,
    13,
    81,
    91,
    90,
    21,
    30,
    62,
]

directorio = os.path.dirname(os.path.abspath(__file__))

archivo = os.path.join(directorio, "resultado_python.txt")

inicio = time.time()

for i in range(len(A) - 1):
    for j in range(len(A) - 1 - i):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp

fin = time.time()

tiempo = (fin - inicio) * 1000

with open(archivo, "w") as file:
    for i in A:
        file.write(str(i))
        file.write(",")

print("Python " + str(tiempo) + "ms")
