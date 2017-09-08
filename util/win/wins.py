#!/usr/bin/env python
# -*- coding:utf-8 -*-

from braille_square_win import *
from line_win import *
from reader_win import ReaderWin
from row_win import RowWin

Wins = {
    "ReaderWin": ReaderWin,

    "BrailleSquare0_0":  BrailleSquare0_0,
    "BrailleSquare0_1":  BrailleSquare0_1,
    "BrailleSquare0_2":  BrailleSquare0_2,
    "BrailleSquare0_3":  BrailleSquare0_3,
    "BrailleSquare0_4":  BrailleSquare0_4,
    "BrailleSquare0_5":  BrailleSquare0_5,
    "BrailleSquare0_6":  BrailleSquare0_6,
    "BrailleSquare0_7":  BrailleSquare0_7,
    "BrailleSquare0_8":  BrailleSquare0_8,
    "BrailleSquare0_9":  BrailleSquare0_9,
    "BrailleSquare0_10": BrailleSquare0_10,
    "BrailleSquare0_11": BrailleSquare0_11,
    "BrailleSquare0_12": BrailleSquare0_12,
    "BrailleSquare0_13": BrailleSquare0_13,
    "BrailleSquare0_14": BrailleSquare0_14,
    "BrailleSquare0_15": BrailleSquare0_15,
    "BrailleSquare1_0":  BrailleSquare1_0,
    "BrailleSquare1_1":  BrailleSquare1_1,
    "BrailleSquare1_2":  BrailleSquare1_2,
    "BrailleSquare1_3":  BrailleSquare1_3,
    "BrailleSquare1_4":  BrailleSquare1_4,
    "BrailleSquare1_5":  BrailleSquare1_5,
    "BrailleSquare1_6":  BrailleSquare1_6,
    "BrailleSquare1_7":  BrailleSquare1_7,
    "BrailleSquare1_8":  BrailleSquare1_8,
    "BrailleSquare1_9":  BrailleSquare1_9,
    "BrailleSquare1_10": BrailleSquare1_10,
    "BrailleSquare1_11": BrailleSquare1_11,
    "BrailleSquare1_12": BrailleSquare1_12,
    "BrailleSquare1_13": BrailleSquare1_13,
    "BrailleSquare1_14": BrailleSquare1_14,
    "BrailleSquare1_15": BrailleSquare1_15,
    "BrailleSquare2_0":  BrailleSquare2_0,
    "BrailleSquare2_1":  BrailleSquare2_1,
    "BrailleSquare2_2":  BrailleSquare2_2,
    "BrailleSquare2_3":  BrailleSquare2_3,
    "BrailleSquare2_4":  BrailleSquare2_4,
    "BrailleSquare2_5":  BrailleSquare2_5,
    "BrailleSquare2_6":  BrailleSquare2_6,
    "BrailleSquare2_7":  BrailleSquare2_7,
    "BrailleSquare2_8":  BrailleSquare2_8,
    "BrailleSquare2_9":  BrailleSquare2_9,
    "BrailleSquare2_10": BrailleSquare2_10,
    "BrailleSquare2_11": BrailleSquare2_11,
    "BrailleSquare2_12": BrailleSquare2_12,
    "BrailleSquare2_13": BrailleSquare2_13,
    "BrailleSquare2_14": BrailleSquare2_14,
    "BrailleSquare2_15": BrailleSquare2_15,
    "BrailleSquare3_0":  BrailleSquare3_0,
    "BrailleSquare3_1":  BrailleSquare3_1,
    "BrailleSquare3_2":  BrailleSquare3_2,
    "BrailleSquare3_3":  BrailleSquare3_3,
    "BrailleSquare3_4":  BrailleSquare3_4,
    "BrailleSquare3_5":  BrailleSquare3_5,
    "BrailleSquare3_6":  BrailleSquare3_6,
    "BrailleSquare3_7":  BrailleSquare3_7,
    "BrailleSquare3_8":  BrailleSquare3_8,
    "BrailleSquare3_9":  BrailleSquare3_9,
    "BrailleSquare3_10": BrailleSquare3_10,
    "BrailleSquare3_11": BrailleSquare3_11,
    "BrailleSquare3_12": BrailleSquare3_12,
    "BrailleSquare3_13": BrailleSquare3_13,
    "BrailleSquare3_14": BrailleSquare3_14,
    "BrailleSquare3_15": BrailleSquare3_15,
    "BrailleSquare4_0":  BrailleSquare4_0,
    "BrailleSquare4_1":  BrailleSquare4_1,
    "BrailleSquare4_2":  BrailleSquare4_2,
    "BrailleSquare4_3":  BrailleSquare4_3,
    "BrailleSquare4_4":  BrailleSquare4_4,
    "BrailleSquare4_5":  BrailleSquare4_5,
    "BrailleSquare4_6":  BrailleSquare4_6,
    "BrailleSquare4_7":  BrailleSquare4_7,
    "BrailleSquare4_8":  BrailleSquare4_8,
    "BrailleSquare4_9":  BrailleSquare4_9,
    "BrailleSquare4_10": BrailleSquare4_10,
    "BrailleSquare4_11": BrailleSquare4_11,
    "BrailleSquare4_12": BrailleSquare4_12,
    "BrailleSquare4_13": BrailleSquare4_13,
    "BrailleSquare4_14": BrailleSquare4_14,
    "BrailleSquare4_15": BrailleSquare4_15,

    "LineWin0": LineWin0,
    "LineWin1": LineWin1,
    "LineWin2": LineWin2,
    "LineWin3": LineWin3,
    "LineWin4": LineWin4,

    "RowWin": RowWin,
}
