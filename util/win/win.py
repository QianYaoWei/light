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

        self._subWinSortedKeys = []
        self._dotsSortedKeys = []

        self._winMgr = None

        self._defDotsStatus = None

    def __str__(self):
        return ",".join([str(self._x), str(self._y),
                         str(self._height), str(self._width)])

    def Init(self):
        self._subWinSortedKeys.extend(sorted(self.SubWins.keys()))
        self._dotsSortedKeys.extend(sorted(self._dots.keys()))

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

    @property
    def SubwinKeys(self):
        return self._subWinSortedKeys

    @property
    def DotsKeys(self):
        return self._dotsSortedKeys

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

    @property
    def WinMgr(self):
        return self._winMgr

    @WinMgr.setter
    def WinMgr(self, mgr):
        self._winMgr = mgr

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
                    self._stdscr.addch(self.X, self.Y, self._txt,
                            curses.color_pair(self._color) | curses.A_BOLD)

    def DecodeDots(self, rx, ry, dots):
        '''implement'''
        dotsStatus = self.GenerateDotsStatus(dots)
        if dotsStatus is not None:
            self._defDotsStatus = dotsStatus

        for _, dot in self._dots.items():
            dot.RelativePos(rx, ry)

    def GenerateDotsStatus(self, dots):
        if not dots or \
           len(dots) != self._height * self._width:
            return {}

        dotsStatus = {}
        for i in range(0, self._height):
            for j in range(0, self._width):
                g_ps = ScreenDots(self._stdscr)
                dot = g_ps.GetDot(self.OriginX + i, self.OriginY + j)
                self.AddDot(dot)
                if dots[i * self._width + j] == '.':
                    dotsStatus[dot.Key] = True
                else:
                    dotsStatus[dot.Key] = False
        return dotsStatus

    def RefreshDots(self, dots=None):
        dotsStatus = self.GenerateDotsStatus(dots) if dots else self._defDotsStatus

        ds = dotsStatus if dotsStatus else self._defDotsStatus
        for k, status in ds.items():
            if status:
                self._dots[k].Activate()
            else:
                self._dots[k].Inactivate()

    # def DecodeDots(self, rx, ry, dots):
    #     '''override this func'''
    #     if dots:
    #         for d in dots:
    #             xy = d.split(',')
    #             g_ps = ScreenDots(self._stdscr)
    #             dot = g_ps.GetDot(int(xy[0]), int(xy[1]))
    #             dot.RelativePos(rx, ry)
    #             self.AddDot(dot)

    def Close(self):
        # TODO
        for _, w in self._subWins.items():
            w.Close()

    def InactivateDots(self):
        for k, d in self._dots.items():
            d.Inactivate()
