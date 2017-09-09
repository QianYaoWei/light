#!/usr/bin/env python
# -*- coding:utf-8 -*-

from win_elem.braille_square import *
from win_elem.line import *
from win_elem.square_8x8 import *
from point import *

from win_elem.braille_square_scr import BrailleSquareScr
from win_elem.row_scr import RowScr
from win_elem.x8x8_scr import X8x8Scr
from win import Win
from braille_square_win import BrailleSquareWin
from line_win import LineWin
from x8x8_square_win import X8x8Win
from .. import singleton

Wins = {
    "BrailleSquare0_0":  (BrailleSquare0_0, BrailleSquareWin),
    "BrailleSquare0_1":  (BrailleSquare0_1, BrailleSquareWin),
    "BrailleSquare0_2":  (BrailleSquare0_2, BrailleSquareWin),
    "BrailleSquare0_3":  (BrailleSquare0_3, BrailleSquareWin),
    "BrailleSquare0_4":  (BrailleSquare0_4, BrailleSquareWin),
    "BrailleSquare0_5":  (BrailleSquare0_5, BrailleSquareWin),
    "BrailleSquare0_6":  (BrailleSquare0_6, BrailleSquareWin),
    "BrailleSquare0_7":  (BrailleSquare0_7, BrailleSquareWin),
    "BrailleSquare0_8":  (BrailleSquare0_8, BrailleSquareWin),
    "BrailleSquare0_9":  (BrailleSquare0_9, BrailleSquareWin),
    "BrailleSquare0_10": (BrailleSquare0_10, BrailleSquareWin),
    "BrailleSquare0_11": (BrailleSquare0_11, BrailleSquareWin),
    "BrailleSquare0_12": (BrailleSquare0_12, BrailleSquareWin),
    "BrailleSquare0_13": (BrailleSquare0_13, BrailleSquareWin),
    "BrailleSquare0_14": (BrailleSquare0_14, BrailleSquareWin),
    "BrailleSquare0_15": (BrailleSquare0_15, BrailleSquareWin),
    "BrailleSquare1_0":  (BrailleSquare1_0, BrailleSquareWin),
    "BrailleSquare1_1":  (BrailleSquare1_1, BrailleSquareWin),
    "BrailleSquare1_2":  (BrailleSquare1_2, BrailleSquareWin),
    "BrailleSquare1_3":  (BrailleSquare1_3, BrailleSquareWin),
    "BrailleSquare1_4":  (BrailleSquare1_4, BrailleSquareWin),
    "BrailleSquare1_5":  (BrailleSquare1_5, BrailleSquareWin),
    "BrailleSquare1_6":  (BrailleSquare1_6, BrailleSquareWin),
    "BrailleSquare1_7":  (BrailleSquare1_7, BrailleSquareWin),
    "BrailleSquare1_8":  (BrailleSquare1_8, BrailleSquareWin),
    "BrailleSquare1_9":  (BrailleSquare1_9, BrailleSquareWin),
    "BrailleSquare1_10": (BrailleSquare1_10, BrailleSquareWin),
    "BrailleSquare1_11": (BrailleSquare1_11, BrailleSquareWin),
    "BrailleSquare1_12": (BrailleSquare1_12, BrailleSquareWin),
    "BrailleSquare1_13": (BrailleSquare1_13, BrailleSquareWin),
    "BrailleSquare1_14": (BrailleSquare1_14, BrailleSquareWin),
    "BrailleSquare1_15": (BrailleSquare1_15, BrailleSquareWin),
    "BrailleSquare2_0":  (BrailleSquare2_0, BrailleSquareWin),
    "BrailleSquare2_1":  (BrailleSquare2_1, BrailleSquareWin),
    "BrailleSquare2_2":  (BrailleSquare2_2, BrailleSquareWin),
    "BrailleSquare2_3":  (BrailleSquare2_3, BrailleSquareWin),
    "BrailleSquare2_4":  (BrailleSquare2_4, BrailleSquareWin),
    "BrailleSquare2_5":  (BrailleSquare2_5, BrailleSquareWin),
    "BrailleSquare2_6":  (BrailleSquare2_6, BrailleSquareWin),
    "BrailleSquare2_7":  (BrailleSquare2_7, BrailleSquareWin),
    "BrailleSquare2_8":  (BrailleSquare2_8, BrailleSquareWin),
    "BrailleSquare2_9":  (BrailleSquare2_9, BrailleSquareWin),
    "BrailleSquare2_10": (BrailleSquare2_10, BrailleSquareWin),
    "BrailleSquare2_11": (BrailleSquare2_11, BrailleSquareWin),
    "BrailleSquare2_12": (BrailleSquare2_12, BrailleSquareWin),
    "BrailleSquare2_13": (BrailleSquare2_13, BrailleSquareWin),
    "BrailleSquare2_14": (BrailleSquare2_14, BrailleSquareWin),
    "BrailleSquare2_15": (BrailleSquare2_15, BrailleSquareWin),
    "BrailleSquare3_0":  (BrailleSquare3_0, BrailleSquareWin),
    "BrailleSquare3_1":  (BrailleSquare3_1, BrailleSquareWin),
    "BrailleSquare3_2":  (BrailleSquare3_2, BrailleSquareWin),
    "BrailleSquare3_3":  (BrailleSquare3_3, BrailleSquareWin),
    "BrailleSquare3_4":  (BrailleSquare3_4, BrailleSquareWin),
    "BrailleSquare3_5":  (BrailleSquare3_5, BrailleSquareWin),
    "BrailleSquare3_6":  (BrailleSquare3_6, BrailleSquareWin),
    "BrailleSquare3_7":  (BrailleSquare3_7, BrailleSquareWin),
    "BrailleSquare3_8":  (BrailleSquare3_8, BrailleSquareWin),
    "BrailleSquare3_9":  (BrailleSquare3_9, BrailleSquareWin),
    "BrailleSquare3_10": (BrailleSquare3_10, BrailleSquareWin),
    "BrailleSquare3_11": (BrailleSquare3_11, BrailleSquareWin),
    "BrailleSquare3_12": (BrailleSquare3_12, BrailleSquareWin),
    "BrailleSquare3_13": (BrailleSquare3_13, BrailleSquareWin),
    "BrailleSquare3_14": (BrailleSquare3_14, BrailleSquareWin),
    "BrailleSquare3_15": (BrailleSquare3_15, BrailleSquareWin),
    "BrailleSquare4_0":  (BrailleSquare4_0, BrailleSquareWin),
    "BrailleSquare4_1":  (BrailleSquare4_1, BrailleSquareWin),
    "BrailleSquare4_2":  (BrailleSquare4_2, BrailleSquareWin),
    "BrailleSquare4_3":  (BrailleSquare4_3, BrailleSquareWin),
    "BrailleSquare4_4":  (BrailleSquare4_4, BrailleSquareWin),
    "BrailleSquare4_5":  (BrailleSquare4_5, BrailleSquareWin),
    "BrailleSquare4_6":  (BrailleSquare4_6, BrailleSquareWin),
    "BrailleSquare4_7":  (BrailleSquare4_7, BrailleSquareWin),
    "BrailleSquare4_8":  (BrailleSquare4_8, BrailleSquareWin),
    "BrailleSquare4_9":  (BrailleSquare4_9, BrailleSquareWin),
    "BrailleSquare4_10": (BrailleSquare4_10, BrailleSquareWin),
    "BrailleSquare4_11": (BrailleSquare4_11, BrailleSquareWin),
    "BrailleSquare4_12": (BrailleSquare4_12, BrailleSquareWin),
    "BrailleSquare4_13": (BrailleSquare4_13, BrailleSquareWin),
    "BrailleSquare4_14": (BrailleSquare4_14, BrailleSquareWin),
    "BrailleSquare4_15": (BrailleSquare4_15, BrailleSquareWin),

    "Square8x8_0_0":  (Square8x8_0_0, X8x8Win),
    "Square8x8_0_8":  (Square8x8_0_8, X8x8Win),
    "Square8x8_0_16": (Square8x8_0_16, X8x8Win),
    "Square8x8_0_24": (Square8x8_0_24, X8x8Win),
    "Square8x8_8_0":  (Square8x8_8_0, X8x8Win),
    "Square8x8_8_8":  (Square8x8_8_8, X8x8Win),
    "Square8x8_8_16": (Square8x8_8_16, X8x8Win),
    "Square8x8_8_24": (Square8x8_8_24, X8x8Win),

    "Line0": (Line0, LineWin),
    "Line1": (Line1, LineWin),
    "Line2": (Line2, LineWin),
    "Line3": (Line3, LineWin),
    "Line4": (Line4, LineWin),

    "RowScr": RowScr,
    "BrailleSquareScr": BrailleSquareScr,
    "X8x8Scr": X8x8Scr,
}

@singleton
class WinMgr(object):
    def __init__(self, stdscr):
        # k:winName, v:win
        self._wins = {}

    def CreateWin(self, stdscr, name, topWinPos=None):
        w = self._wins.get(name, None)
        if w:
            return w
        global Wins
        el = Wins.get(name, None)
        WinCls = Win
        if type(el) == tuple:
            winConf = el[0]
            WinCls =el[1]
        elif type(el) == dict:
            winConf = el
        if winConf:
            if not topWinPos:
                topWinPos = (winConf["x"], winConf["y"])
            w = WinCls(stdscr, name, winConf["x"], winConf["y"],
                    winConf["height"], winConf["width"])

            for s in winConf.get("subwins", []):
                if type(s) == str:
                    subwin = self.CreateWin(stdscr, s, topWinPos)
                elif type(s) == dict:
                    subwin = WinCls(stdscr, s["name"], s["x"], s["y"],
                                 s["height"], s["width"])
                else:
                    continue
                if subwin:
                    w._subWins[subwin.Name] = subwin
                    subwin.Parent = w
                    subwin.X = subwin.OriginX + topWinPos[0]
                    subwin.Y = subwin.OriginY + topWinPos[1]

            for p in winConf.get("points", []):
                xy = p.split(',')
                g_ps = ScreenPoints(stdscr)
                point = g_ps.GetPoint(int(xy[0]), int(xy[1]))
                point.RelativePos(topWinPos[0], topWinPos[1])
                w.AddPoint(point)

            for _, s in w._subWins.items():
                for k, p in s.Points.items():
                    w.AddPoint(p)
            self._wins[name] = w
            return w
