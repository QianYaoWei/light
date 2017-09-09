#!/usr/bin/env python
# -*- coding:utf-8 -*-
from point import *

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
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        self._name = name
        self._originX = oriX
        self._originY = oriY
        self._x = oriX
        self._y = oriY

        self._height = height
        self._width = width

        # one win has only one parent win
        self._parent = None
        self._subWins = {}
        # all the points that the win can conctrol, include those belong to
        # subwins
        self._points = {}
        self._stdscr = stdscr
        self._disable = False

    def __str__(self):
        return ",".join([str(self._x), str(self._y),
                         str(self._height), str(self._width)])

    @property
    def Name(self):
        return self._name

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, win):
        self._parent = win

    def Disable(self):
        self._disable = True

    def Enable(self):
        self._disable = False

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
    def OriginX(self):
        return self._originX

    @OriginX.setter
    def OriginX(self, x):
        self._originX = x

    @property
    def OriginY(self):
        return self._originY

    @OriginY.setter
    def OriginY(self, y):
        self._originY = y

    @property
    def SubWins(self):
        return self._subWins

    def OnMessage(self, msg):
        '''override it to update the points status'''
        pass

    def Touch(self):
        pass

    def IsInRange(self, x, y):
        if self._x <= x < self._x + self._height and\
           self._y <= y < self._y + self._width:
            return True
        else:
            return False

    def Draw(self, x, y):
        # rectangle(self._stdscr,  self._x,  self._y,
        #           self._x + self._height, self._y + self._width)
        for _, w in self._subWins.items():
            w.Draw(x, y)

        if not self._disable:
            # TODO
            for k in self._points:
                if self.IsInRange(x, y):
                    self._points[k].Draw('.')
                else:
                    self._points[k].Draw('x')

    def Close(self):
        # TODO
        for _, w in self._subWins.items():
            w.Close()
