#!/usr/bin/env python
# -*- coding:utf-8 -*-

from win import Win
from dot import *


DotCoutANum = 20
ColumnCount = 5


class DialNumWin(Win):

    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(DialNumWin, self).__init__(stdscr, name, oriX,
                                         oriY, height, width)
        self._dotsStatus = {}

    def DecodeDots(self, rx, ry, dots):
        '''override'''
        if dots:
            if len(dots) != DotCoutANum:
                return
            for i in range(0, DotCoutANum / ColumnCount):
                for j in range(0, ColumnCount):
                    g_ps = ScreenDots(self._stdscr)
                    dot = g_ps.GetDot(self.OriginX + i, self.OriginY + j)
                    dot.RelativePos(rx, ry)
                    self.AddDot(dot)

                    if dots[i * ColumnCount + j] == '.':
                        self._dotsStatus[dot.Key] = True
                    else:
                        self._dotsStatus[dot.Key] = False

    def RefreshDots(self):
        for k, status in self._dotsStatus.items():
            if status:
                self._dots[k].Activate()
            else:
                self._dots[k].Inactivate()
