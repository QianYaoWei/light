#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..win import Win
from ..dot import *

class DialNumWin(Win):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(DialNumWin, self).__init__(stdscr, name, oriX,
                                         oriY, height, width)

    # def DecodeDots(self, rx, ry, dots):
    #     '''implement'''
    #     dotsStatus = self.GenerateDotsStatus(dots)
    #     if dotsStatus is not None:
    #         self._defDotsStatus = dotsStatus

    #     for _, dot in self._dots.items():
    #         dot.RelativePos(rx, ry)

    # def GenerateDotsStatus(self, dots):
    #     if not dots or \
    #        len(dots) != self._height * self._width:
    #         return

    #     dotsStatus = {}
    #     for i in range(0, self._height):
    #         for j in range(0, self._width):
    #             g_ps = ScreenDots(self._stdscr)
    #             dot = g_ps.GetDot(self.OriginX + i, self.OriginY + j)
    #             self.AddDot(dot)
    #             if dots[i * self._width + j] == '.':
    #                 dotsStatus[dot.Key] = True
    #             else:
    #                 dotsStatus[dot.Key] = False
    #     return dotsStatus

