#!/usr/bin/env python
# -*- coding:utf-8 -*-
import curses
import time
import sched
from functools import wraps
from ..conf import ScreenConf as conf
from ..win import WinMgr


class View(object):
    def __init__(self, stdscr, winID=0, Sched=None):
        self._sched = Sched if Sched else sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())
        self._stdscr = stdscr
        self._exit = False

        g_scr = WinMgr(self._stdscr)
        self._win = g_scr.CreateWin(stdscr, winID)
        self._curPosX = self._win.X
        self._curPosY = self._win.Y
        self._testID = 1

    def Init(self, reciever):
        reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        reciever.MsgRegister('k', self.__OnKeyUp)
        # reciever.MsgRegister(curses.KEY_DOWN, self.__OnKeyDown)
        reciever.MsgRegister('j', self.__OnKeyDown)
        # reciever.MsgRegister(curses.KEY_LEFT, self.__OnKeyLeft)
        reciever.MsgRegister('h', self.__OnKeyLeft)
        # reciever.MsgRegister(curses.KEY_RIGHT, self.__OnKeyRight)
        reciever.MsgRegister('l', self.__OnKeyRight)
        reciever.MsgRegister('q', self.__OnExit)
        reciever.MsgRegister('e', self.__OnClick)

        reciever.MsgRegister('f', self._OnForward)
        reciever.MsgRegister('b', self._OnBackward)
        reciever.MsgRegister('u', self._OnUp)
        reciever.MsgRegister('d', self._OnDown)

    def before_operation(func):
        @wraps(func)
        def wrapper(self):
            # import pudb; pudb.set_trace()  # XXX BREAKPOINT
            stdscr = self.StdScr
            stdscr.clear()
            return func(self)
        return wrapper

    def Show(self):
        if self._exit:
            return
        self._win.Draw(self._curPosX, self._curPosY)
        self._stdscr.addch(self._curPosX, self._curPosY, '*')

        self._stdscr.refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    def __OnExit(self):
        self._exit = True

    def __OnClick(self):
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

    def __OnTest(self):
        def OnTest(self):
            w = self._win.SubWins.get("Square8x8_0_8", None)
            if w:
                w.OnMessage(2 ** self._testID)
                self._testID += 1
        self._sched.enter(0, 1, OnTest, (self, ))

    @before_operation
    def __OnKeyUp(self):
        def OnKeyUp(self):
            self._curPosX -= 1
            if self._curPosX < self._win.X:
                self._curPosX = self._win.X
        self._sched.enter(0, 1, OnKeyUp, (self, ))

    @before_operation
    def __OnKeyDown(self):
        def OnKeyDown(self):
            self._curPosX += 1
            if self._curPosX > self._win.X + conf.ScreenRow - 1:
                self._curPosX = self._win.X + conf.ScreenRow - 1
        self._sched.enter(0, 1, OnKeyDown, (self, ))

    @before_operation
    def __OnKeyLeft(self):
        def KeyLeft(self):
            self._curPosY -= 1
            if self._curPosY < self._win.Y:
                self._curPosY = self._win.Y
        self._sched.enter(0, 1, KeyLeft, (self, ))

    @before_operation
    def __OnKeyRight(self):
        def KeyRight(self):
            self._curPosY += 1
            if self._curPosY > self._win.Y + conf.ScreenColumn - 1:
                self._curPosY = self._win.Y + conf.ScreenColumn - 1
        self._sched.enter(0, 1, KeyRight, (self, ))

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
