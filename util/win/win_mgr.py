#!/usr/bin/env python
# -*- coding:utf-8 -*-
from win_elem.braille_square import *
from win_elem.line import *
from win_elem.square_8x8 import *
from win_elem.dail_panel import *

from win_elem.braille_square_scr import BrailleSquareScr
from win_elem.row_scr import RowScr
from win_elem.x8x8_scr import X8x8Scr
from braille_square_win import BrailleSquareWin
from line_win import LineWin
from x8x8_square_win import X8x8Win
from win import Win
from dot import *
from win_event import *
from .. import singleton

Wins = {
    BrailleSquare0_0_id:  (BrailleSquare0_0, BrailleSquareWin),
    BrailleSquare0_1_id:  (BrailleSquare0_1, BrailleSquareWin),
    BrailleSquare0_2_id:  (BrailleSquare0_2, BrailleSquareWin),
    BrailleSquare0_3_id:  (BrailleSquare0_3, BrailleSquareWin),
    BrailleSquare0_4_id:  (BrailleSquare0_4, BrailleSquareWin),
    BrailleSquare0_5_id:  (BrailleSquare0_5, BrailleSquareWin),
    BrailleSquare0_6_id:  (BrailleSquare0_6, BrailleSquareWin),
    BrailleSquare0_7_id:  (BrailleSquare0_7, BrailleSquareWin),
    BrailleSquare0_8_id:  (BrailleSquare0_8, BrailleSquareWin),
    BrailleSquare0_9_id:  (BrailleSquare0_9, BrailleSquareWin),
    BrailleSquare0_10_id: (BrailleSquare0_10, BrailleSquareWin),
    BrailleSquare0_11_id: (BrailleSquare0_11, BrailleSquareWin),
    BrailleSquare0_12_id: (BrailleSquare0_12, BrailleSquareWin),
    BrailleSquare0_13_id: (BrailleSquare0_13, BrailleSquareWin),
    BrailleSquare0_14_id: (BrailleSquare0_14, BrailleSquareWin),
    BrailleSquare0_15_id: (BrailleSquare0_15, BrailleSquareWin),
    BrailleSquare1_0_id:  (BrailleSquare1_0, BrailleSquareWin),
    BrailleSquare1_1_id:  (BrailleSquare1_1, BrailleSquareWin),
    BrailleSquare1_2_id:  (BrailleSquare1_2, BrailleSquareWin),
    BrailleSquare1_3_id:  (BrailleSquare1_3, BrailleSquareWin),
    BrailleSquare1_4_id:  (BrailleSquare1_4, BrailleSquareWin),
    BrailleSquare1_5_id:  (BrailleSquare1_5, BrailleSquareWin),
    BrailleSquare1_6_id:  (BrailleSquare1_6, BrailleSquareWin),
    BrailleSquare1_7_id:  (BrailleSquare1_7, BrailleSquareWin),
    BrailleSquare1_8_id:  (BrailleSquare1_8, BrailleSquareWin),
    BrailleSquare1_9_id:  (BrailleSquare1_9, BrailleSquareWin),
    BrailleSquare1_10_id: (BrailleSquare1_10, BrailleSquareWin),
    BrailleSquare1_11_id: (BrailleSquare1_11, BrailleSquareWin),
    BrailleSquare1_12_id: (BrailleSquare1_12, BrailleSquareWin),
    BrailleSquare1_13_id: (BrailleSquare1_13, BrailleSquareWin),
    BrailleSquare1_14_id: (BrailleSquare1_14, BrailleSquareWin),
    BrailleSquare1_15_id: (BrailleSquare1_15, BrailleSquareWin),
    BrailleSquare2_0_id:  (BrailleSquare2_0, BrailleSquareWin),
    BrailleSquare2_1_id:  (BrailleSquare2_1, BrailleSquareWin),
    BrailleSquare2_2_id:  (BrailleSquare2_2, BrailleSquareWin),
    BrailleSquare2_3_id:  (BrailleSquare2_3, BrailleSquareWin),
    BrailleSquare2_4_id:  (BrailleSquare2_4, BrailleSquareWin),
    BrailleSquare2_5_id:  (BrailleSquare2_5, BrailleSquareWin),
    BrailleSquare2_6_id:  (BrailleSquare2_6, BrailleSquareWin),
    BrailleSquare2_7_id:  (BrailleSquare2_7, BrailleSquareWin),
    BrailleSquare2_8_id:  (BrailleSquare2_8, BrailleSquareWin),
    BrailleSquare2_9_id:  (BrailleSquare2_9, BrailleSquareWin),
    BrailleSquare2_10_id: (BrailleSquare2_10, BrailleSquareWin),
    BrailleSquare2_11_id: (BrailleSquare2_11, BrailleSquareWin),
    BrailleSquare2_12_id: (BrailleSquare2_12, BrailleSquareWin),
    BrailleSquare2_13_id: (BrailleSquare2_13, BrailleSquareWin),
    BrailleSquare2_14_id: (BrailleSquare2_14, BrailleSquareWin),
    BrailleSquare2_15_id: (BrailleSquare2_15, BrailleSquareWin),
    BrailleSquare3_0_id:  (BrailleSquare3_0, BrailleSquareWin),
    BrailleSquare3_1_id:  (BrailleSquare3_1, BrailleSquareWin),
    BrailleSquare3_2_id:  (BrailleSquare3_2, BrailleSquareWin),
    BrailleSquare3_3_id:  (BrailleSquare3_3, BrailleSquareWin),
    BrailleSquare3_4_id:  (BrailleSquare3_4, BrailleSquareWin),
    BrailleSquare3_5_id:  (BrailleSquare3_5, BrailleSquareWin),
    BrailleSquare3_6_id:  (BrailleSquare3_6, BrailleSquareWin),
    BrailleSquare3_7_id:  (BrailleSquare3_7, BrailleSquareWin),
    BrailleSquare3_8_id:  (BrailleSquare3_8, BrailleSquareWin),
    BrailleSquare3_9_id:  (BrailleSquare3_9, BrailleSquareWin),
    BrailleSquare3_10_id: (BrailleSquare3_10, BrailleSquareWin),
    BrailleSquare3_11_id: (BrailleSquare3_11, BrailleSquareWin),
    BrailleSquare3_12_id: (BrailleSquare3_12, BrailleSquareWin),
    BrailleSquare3_13_id: (BrailleSquare3_13, BrailleSquareWin),
    BrailleSquare3_14_id: (BrailleSquare3_14, BrailleSquareWin),
    BrailleSquare3_15_id: (BrailleSquare3_15, BrailleSquareWin),
    BrailleSquare4_0_id:  (BrailleSquare4_0, BrailleSquareWin),
    BrailleSquare4_1_id:  (BrailleSquare4_1, BrailleSquareWin),
    BrailleSquare4_2_id:  (BrailleSquare4_2, BrailleSquareWin),
    BrailleSquare4_3_id:  (BrailleSquare4_3, BrailleSquareWin),
    BrailleSquare4_4_id:  (BrailleSquare4_4, BrailleSquareWin),
    BrailleSquare4_5_id:  (BrailleSquare4_5, BrailleSquareWin),
    BrailleSquare4_6_id:  (BrailleSquare4_6, BrailleSquareWin),
    BrailleSquare4_7_id:  (BrailleSquare4_7, BrailleSquareWin),
    BrailleSquare4_8_id:  (BrailleSquare4_8, BrailleSquareWin),
    BrailleSquare4_9_id:  (BrailleSquare4_9, BrailleSquareWin),
    BrailleSquare4_10_id: (BrailleSquare4_10, BrailleSquareWin),
    BrailleSquare4_11_id: (BrailleSquare4_11, BrailleSquareWin),
    BrailleSquare4_12_id: (BrailleSquare4_12, BrailleSquareWin),
    BrailleSquare4_13_id: (BrailleSquare4_13, BrailleSquareWin),
    BrailleSquare4_14_id: (BrailleSquare4_14, BrailleSquareWin),
    BrailleSquare4_15_id: (BrailleSquare4_15, BrailleSquareWin),

    Square8x8_0_0_id:  (Square8x8_0_0, X8x8Win),
    Square8x8_0_8_id:  (Square8x8_0_8, X8x8Win),
    Square8x8_0_16_id: (Square8x8_0_16, X8x8Win),
    Square8x8_0_24_id: (Square8x8_0_24, X8x8Win),
    Square8x8_8_0_id:  (Square8x8_8_0, X8x8Win),
    Square8x8_8_8_id:  (Square8x8_8_8, X8x8Win),
    Square8x8_8_16_id: (Square8x8_8_16, X8x8Win),
    Square8x8_8_24_id: (Square8x8_8_24, X8x8Win),

    Line0_id: (Line0, LineWin),
    Line1_id: (Line1, LineWin),
    Line2_id: (Line2, LineWin),
    Line3_id: (Line3, LineWin),
    Line4_id: (Line4, LineWin),

    RowScr_id: RowScr,
    BrailleSquareScr_id: BrailleSquareScr,
    X8x8Scr_id: X8x8Scr,

    DailNum1_id: DailNum1,
    DailNum2_id: DailNum2,
    DailNum3_id: DailNum3,
    DailNum4_id: DailNum4,
    DailNum5_id: DailNum5,
    DailNum6_id: DailNum6,
    DailNum7_id: DailNum7,
    DailNum8_id: DailNum8,
    DailNum9_id: DailNum9,
    DailNum0_id: DailNum0,
    DailAsterisk_id: DailAsterisk,
    DailSharp_id: DailSharp,
}

@singleton
class WinMgr(object):
    def __init__(self, stdscr):
        # k:winName, v:win
        self._wins = {}

    def CreateWin(self, stdscr, id, winEventList=None, topWinPos=None):
        w = self._wins.get(id, None)
        if w:
            return w
        global Wins
        el = Wins.get(id, None)
        WinCls = Win
        if type(el) == tuple:
            winConf = el[0]
            WinCls =el[1]
        elif type(el) == dict:
            winConf = el
        if winConf:
            if not topWinPos:
                topWinPos = (winConf["x"], winConf["y"])
            w = WinCls(stdscr, id, winConf["x"], winConf["y"],
                    winConf["height"], winConf["width"])

            for s in winConf.get("subwins", []):
                if type(s) == int:
                    subwin = self.CreateWin(stdscr, s, winEventList, topWinPos)
                elif type(s) == dict:
                    subwin = WinCls(stdscr, s["id"], s["x"], s["y"],
                                 s["height"], s["width"])
                else:
                    continue
                if subwin:
                    w.SubWins[subwin.ID] = subwin
                    subwin.Parent = w
                    subwin.X = subwin.OriginX + topWinPos[0]
                    subwin.Y = subwin.OriginY + topWinPos[1]

            for p in winConf.get("dots", []):
                xy = p.split(',')
                g_ps = ScreenDots(stdscr)
                dot = g_ps.GetDot(int(xy[0]), int(xy[1]))
                dot.RelativePos(topWinPos[0], topWinPos[1])
                w.AddDot(dot)

            for _, s in w.SubWins.items():
                for k, p in s.Dots.items():
                    w.AddDot(p)
            self._wins[id] = w
            if winEventList:
                for we in winEventList:
                    if we.WinID == id:
                        w.AddWinEvent(we)
            w.Init()
            return w
