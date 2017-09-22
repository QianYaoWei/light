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
        self._dotsStatus = None

    def DecodeDots(self, rx, ry, dots):
        '''implement'''
        dotsStatus = self.GenerateDotsStatus(dots)
        if dotsStatus is not None:
            self._dotsStatus = dotsStatus

        for _, dot in self._dots.items():
            dot.RelativePos(rx, ry)

    def GenerateDotsStatus(self, dots):
        if not dots or len(dots) != DotCoutANum:
            return

        dotsStatus = {}
        for i in range(0, DotCoutANum / ColumnCount):
            for j in range(0, ColumnCount):
                g_ps = ScreenDots(self._stdscr)
                dot = g_ps.GetDot(self.OriginX + i, self.OriginY + j)
                self.AddDot(dot)
                if dots[i * ColumnCount + j] == '.':
                    dotsStatus[dot.Key] = True
                else:
                    dotsStatus[dot.Key] = False
        return dotsStatus

    def RefreshDots(self, dots=None):
        dotsStatus = self.GenerateDotsStatus(dots) if dots else self._dotsStatus

        ds = dotsStatus if dotsStatus else self._dotsStatus
        for k, status in ds.items():
            if status:
                self._dots[k].Activate()
            else:
                self._dots[k].Inactivate()
