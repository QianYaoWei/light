#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..conf import ScreenConf as conf
from .. import singleton

def Key(x, y):
    return (x, y)

@singleton
class ScreenPoints(object):
    def __init__(self, stdscr):
        self._stdscr = stdscr
        self._points = {}
        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                self._points[(i, j)] = Point(stdscr, i, j)

    def GetPoint(self, x, y):
        return self._points.get((x, y), None)

    @property
    def Points(self):
        return self._points


class Point(object):
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

    @property
    def Key(self):
        return Key(self._x, self._y)

    def Activate(self):
        self._status = True

    def InActivate(self):
        self._status = False

    def Draw(self, ch='.'):
        self._stdscr.addch(self._rx + self._x, self._ry + self._y, ch)
        # TODO
        pass
