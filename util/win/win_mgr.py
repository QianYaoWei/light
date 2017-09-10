#!/usr/bin/env python
# -*- coding:utf-8 -*-

from win import Win
from point import *
from wins import *
from .. import singleton

@singleton
class WinMgr(object):
    def __init__(self, stdscr):
        # k:winName, v:win
        self._wins = {}

    def CreateWin(self, stdscr, id, topWinPos=None):
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
                    subwin = self.CreateWin(stdscr, s, topWinPos)
                elif type(s) == dict:
                    subwin = WinCls(stdscr, s["id"], s["x"], s["y"],
                                 s["height"], s["width"])
                else:
                    continue
                if subwin:
                    w._subWins[subwin.ID] = subwin
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
            self._wins[id] = w
            return w
