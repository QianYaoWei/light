#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..conf import ScreenConf
from ..conf import WinConf
from .. import singleton


def Key(x, y):
    return (x, y)


@singleton
class ScreenDots(object):
    def __init__(self, stdscr):
        self._stdscr = stdscr
        self._dots = {}
        for i in range(0, ScreenConf.ScreenRow):
            for j in range(0, ScreenConf.ScreenColumn):
                self._dots[(i, j)] = Dot(stdscr, i, j)

    def GetDot(self, x, y):
        return self._dots.get((x, y), None)

    @property
    def Dots(self):
        return self._dots


class Dot(object):
    def __init__(self, stdscr, x, y, rx=0, ry=0):
        '''(rx, ry) are relative pos which is the base of (x, y)'''

        self._x = x
        self._y = y
        self._status = False
        self._stdscr = stdscr
        self._rx = 0
        self._ry = 0

    def __str__(self):
        return ",".join([str(self._x), str(self._y), str(self._status)])

    def RelativePos(self, rx, ry):
        self._rx = rx
        self._ry = ry

    @property
    def Status(self):
        return self._status

    def Activate(self):
        self._status = True

    def Inactivate(self):
        self._status = False

    @property
    def Key(self):
        return Key(self._x, self._y)

    def Draw(self):
        if WinConf.ShowMode == 1:
            if self._status:
                # TODO
                self._stdscr.addch(self._rx + self._x, self._ry + self._y,
                                   WinConf.DotUp_Ch)
            else:
                # TODO
                self._stdscr.addch(self._rx + self._x, self._ry + self._y,
                                   WinConf.DotDown_Ch)
        elif WinConf.ShowMode == 2:
            pass
