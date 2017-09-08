#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
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
        self._subWins = []
        self._points = {}
        self._stdscr = stdscr
        self._parent = None

    def __str__(self):
        return ",".join([str(self._x), str(self._y), str(self._height), str(self._width)])

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, win):
        self._parent = win

    def AddPoint(self, point):
        self._points[point.Key] = point

    @property
    def X(self):
        return self._x

    @property
    def Y(self):
        return self._y

    @property
    def SubWins(self):
        return self._subWins

    def Touch(self):
        pass

    def IsInRange(self, x, y):
        if self._x <= x < self._x + self._height and self._y <= y < self._y + self._width:
            return True
        else:
            return False

    def Draw(self, x, y):
        for w in self._subWins:
            w.Draw(x, y)

        # TODO
        for k in self._points:
            if self.IsInRange(x, y):
                self._points[k].Draw('.')
            else:
                self._points[k].Draw('x')

    def Close(self):
        # TODO
        for w in self._subWins:
            w.Close()

    def RelativePosForPoints(self, rx, ry):
        g_ps = ScreenPoints(self._stdscr)
        for k, p in g_ps.Points.items():
            p.RelativePos(rx, ry)

    @classmethod
    def CreateWin(cls, stdscr, name):
        win = Wins.get(name, None)
        if win:
            w = Win(stdscr, win["x"], win["y"], win["height"], win["width"])
            for s in win.get("subwins", []):
                if type(s) == str:
                    subwin = cls.CreateWin(stdscr, s)
                    w._subWins.append(subwin)
                    subwin.Parent = w
                elif type(s) == dict:
                    subwin = Win(stdscr, w.X + s["x"], w.Y + s["y"], s["height"], s["width"])
                    w._subWins.append(subwin)
                    subwin.Parent = w

                    for p in s.get("points", []):
                        xy = p.split(',')
                        g_ps = ScreenPoints(stdscr)
                        point = g_ps.GetPoint(int(xy[0]), int(xy[1]))
                        subwin.AddPoint(point)
            return w
