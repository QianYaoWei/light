#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
from dot import *
from win_event import *
from ..conf import WinConf

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
    def __init__(self, stdscr, id, oriX, oriY, height, width):
        self._id = id
        self._originX = oriX
        self._originY = oriY
        self._x = oriX
        self._y = oriY

        self._height = height
        self._width = width

        # one win has only one parent win
        self._parent = None
        self._subWins = {}

        # all the dots that the win can conctrol, include those belong to
        # subwins
        self._dots = {}
        self._stdscr = stdscr
        self._disable = False

        self._winEventList = []
        self._cursorEntered = False

        self._cursorEntered = False

        self._txt = None

        self._color = 0

    def __str__(self):
        return ",".join([str(self._x), str(self._y),
                         str(self._height), str(self._width)])

    @property
    def ID(self):
        return self._id

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, win):
        self._parent = win

    @property
    def Color(self):
        return self._color

    @Color.setter
    def Color(self, color):
        self._color = color

    def AddWinEvent(self, we):
        self._winEventList.append(we)

    def Disable(self):
        self._disable = True

    def Enable(self):
        self._disable = False

    @property
    def Dots(self):
        return self._dots

    def AddDot(self, dot):
        if dot:
            self._dots[dot.Key] = dot

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
        '''override it to update the dots status'''
        pass

    def OnClick(self, x, y):
        for _, w in self._subWins.items():
            if w.IsInRange(x, y):
                w.OnClick(x, y)
        for we in self._winEventList:
            if we.EventID == eClickTheWin:
                we.OnCallBack()

    def IsInRange(self, x, y):
        if self._x <= x < self._x + self._height and\
           self._y <= y < self._y + self._width:
            return True
        else:
            return False

    def Draw(self, x, y):
        if WinConf.ShowWinBorder:
            rectangle(self._stdscr,  self._x,  self._y,
                      self._x + self._height, self._y + self._width)

        for _, w in self._subWins.items():
            w.Draw(x, y)

        if not self._disable:
            if WinConf.ShowMode == 1:
                # TODO
                for k in self._dots:
                    if self.IsInRange(x, y):
                        if not self._cursorEntered:
                            self._cursorEntered = True
                            for we in self._winEventList:
                                if we.EventID == eEnterTheWin:
                                    we.OnCallBack()

                        self._dots[k].Draw()
                    else:
                        if self._cursorEntered:
                            self._cursorEntered = False
                            for we in self._winEventList:
                                if we.EventID == eLeaveTheWin:
                                    we.OnCallBack()

                        self._dots[k].Draw()
            elif WinConf.ShowMode == 2:
                if self._txt:
                    self._stdscr.addch(self.X, self.Y, self._txt, curses.color_pair(self._color))


    def Close(self):
        # TODO
        for _, w in self._subWins.items():
            w.Close()
