#!/usr/bin/env python
# -*- coding:utf-8 -*-

from point import *
from wins import Wins


def rectangle(win, ulx, uly, lrx, lry):
    """Draw a rectangle with corners at the provided upper-left
    and lower-right coordinates.
    """
    win.vline(ulx + 1, uly, '|', lrx - ulx - 1)
    win.vline(ulx + 1, lry, '|', lrx - ulx - 1)

    win.hline(ulx, uly + 1, '-', lry - uly - 1)
    win.hline(lrx, uly + 1, '-', lry - uly - 1)

    win.addch(ulx, uly, '+')
    win.addch(ulx, lry, '+')
    win.addch(lrx, uly, '+')
    win.addch(lrx, lry, '+')


class Win(object):
    def __init__(self, stdscr, x, y, height, width):
        self._x = x
        self._y = y
        self._height = height
        self._width = width

        # one win has only one parent win
        self._parent = None
        self._subWins = []
        # all the points that the win can conctrol, include those belong to
        # subwins
        self._points = {}
        self._stdscr = stdscr

    def __str__(self):
        return ",".join([str(self._x), str(self._y),
                         str(self._height), str(self._width)])

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, win):
        self._parent = win

    @property
    def Points(self):
        return self._points

    def AddPoint(self, point):
        if point:
            self._points[point.Key] = point

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, x):
        self._x = x

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, y):
        self._y = y

    @property
    def SubWins(self):
        return self._subWins

    def Touch(self):
        pass

    def IsInRange(self, x, y):
        if self._x <= x < self._x + self._height and\
           self._y <= y < self._y + self._width:
            return True
        else:
            return False

    def Draw(self, x, y):
        rectangle(self._stdscr,  self._x,  self._y,
                  self._x + self._height, self._y + self._width)
        for w in self._subWins:
            w.Draw(x, y)

        # TODO
        # for k in self._points:
        #     if self.IsInRange(x, y):
        #         self._points[k].Draw('.')
        #     else:
        #         self._points[k].Draw('x')

    def Close(self):
        # TODO
        for w in self._subWins:
            w.Close()

    def RelativePosForPoints(self, rx, ry):
        g_ps = ScreenPoints(self._stdscr)
        for k, p in g_ps.Points.items():
            p.RelativePos(rx, ry)

    @classmethod
    def CreateWin(cls, stdscr, name, topWinPos=None):
        winConf = Wins.get(name, None)
        print winConf
        if winConf:
            if not topWinPos:
                topWinPos = (winConf["x"], winConf["y"])
            w = Win(stdscr, winConf["x"], winConf["y"],
                    winConf["height"], winConf["width"])

            for s in winConf.get("subwins", []):
                if type(s) == str:
                    subwin = cls.CreateWin(stdscr, s, topWinPos)
                elif type(s) == dict:
                    subwin = Win(stdscr, s["x"], s["y"],
                                 s["height"], s["width"])
                else:
                    continue

                if subwin:
                    w._subWins.append(subwin)
                    subwin.Parent = w
                    subwin.X = subwin.X + topWinPos[0]
                    subwin.Y = subwin.Y + topWinPos[1]

            for p in winConf.get("points", []):
                xy = p.split(',')
                g_ps = ScreenPoints(stdscr)
                point = g_ps.GetPoint(int(xy[0]), int(xy[1]))
                w.AddPoint(point)

            for s in w._subWins:
                for k, p in s.Points.items():
                    w.AddPoint(p)

            return w
