#!/usr/bin/env python
# -*- coding:utf-8 -*-
import curses
import time
import sched
from functools import wraps
from operation import Operation
from ..conf import ScreenConf
from ..win import WinMgr


def view_clear(func):
    @wraps(func)
    def wrapper(self, *args):
        self.StdScr.clear()
        return func(self, *args)
    return wrapper


class View(Operation):
    def __init__(self, stdscr, winID=0, sch=None):
        super(View, self).__init__()

        self._sched = sch if sch else sched.scheduler(time.time, time.sleep)
        self._sched.enter(ScreenConf.RefreshInterval, 1, self.Show, ())
        self._stdscr = stdscr

        g_scr = WinMgr(self._stdscr)
        self._win = g_scr.CreateWin(stdscr, winID)
        self._curPosX = self._win.X
        self._curPosY = self._win.Y
        self._testID = 1

        self._viewMgr = None

    def Show(self):
        if self._exit:
            return

        self._win.Draw(self._curPosX, self._curPosY)
        self._stdscr.addch(self._curPosX, self._curPosY, '*')

        self._stdscr.refresh()
        self._sched.enter(ScreenConf.RefreshInterval, 1, self.Show, ())

    def _OnClick(self):
        def OnClick(self):
            if self._win.IsInRange(self._curPosX, self._curPosY):
                self._win.OnClick(self._curPosX, self._curPosY)
        self._sched.enter(0, 1, OnClick, (self, ))

    @property
    def Sched(self):
        return self._sched

    @property
    def StdScr(self):
        return self._stdscr

    @property
    def Win(self):
        return self._win

    @property
    def ViewMgr(self):
        return self._viewMgr

    @ViewMgr.setter
    def ViewMgr(self, mgr):
        self._viewMgr = mgr

    @view_clear
    def _OnKeyUp(self):
        def OnKeyUp(self):
            self._curPosX -= 1
            if self._curPosX < self._win.X:
                self._curPosX = self._win.X
        self._sched.enter(0, 1, OnKeyUp, (self, ))

    @view_clear
    def _OnKeyDown(self):
        def OnKeyDown(self):
            self._curPosX += 1
            if self._curPosX > self._win.X + ScreenConf.ScreenRow - 1:
                self._curPosX = self._win.X + ScreenConf.ScreenRow - 1
        self._sched.enter(0, 1, OnKeyDown, (self, ))

    @view_clear
    def _OnKeyLeft(self):
        def KeyLeft(self):
            self._curPosY -= 1
            if self._curPosY < self._win.Y:
                self._curPosY = self._win.Y
        self._sched.enter(0, 1, KeyLeft, (self, ))

    @view_clear
    def _OnKeyRight(self):
        def KeyRight(self):
            self._curPosY += 1
            if self._curPosY > self._win.Y + ScreenConf.ScreenColumn - 1:
                self._curPosY = self._win.Y + ScreenConf.ScreenColumn - 1
        self._sched.enter(0, 1, KeyRight, (self, ))

    def RefreshWin(self):
        '''override this func'''
        pass

    def _OnForward(self):
        '''override this func'''
        pass

    def _OnBackward(self):
        '''override this func'''
        pass

    def _OnUp(self):
        '''override this func'''
        pass

    def _OnDown(self):
        '''override this func'''
        pass

    def _OnSwitch(self):
        '''override this func'''
        pass
