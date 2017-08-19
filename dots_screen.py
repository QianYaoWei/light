#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import curses
import time
import sched
import threading
from zeroless import Server

import util

conf = util.ScreenConf


class DotsScreen(threading.Thread):
    def __init__(self):
        super(DotsScreen, self).__init__()

        self._dots = np.zeros(conf.ScreenRow * conf.ScreenColumn, dtype=np.bool).\
                    reshape(conf.ScreenRow, conf.ScreenColumn)
        self._sched = sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

        self._curPoint = (0, 0)

        self._exit = False

        # self._win = curses.newwin(conf.ScreenRow, conf.ScreenColumn, 10, 10)
        # self._sched.enter(0.1, 1, self.OnLoop, ())

    @classmethod
    def InitWin(cls):
        cls._stdScreen = curses.initscr()
        cls._stdScreen.keypad(True)

        curses.noecho()
        curses.cbreak()
        curses.start_color()

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    @classmethod
    def UninitWin(cls):
        curses.endwin()

    @classmethod
    def Refresh(cls):
        cls._stdScreen.refresh()

    def Show(self):
        if self._exit:
            return

        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                if self._curPoint == (i, j):
                    DotsScreen._stdScreen.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "x",
                                           curses.color_pair(2) | curses.A_BOLD)
                    continue

                if 0 == self._dots[i, j]:
                    DotsScreen._stdScreen.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "_",
                                           curses.color_pair(1) | curses.A_BOLD)
                else:
                    DotsScreen._stdScreen.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "*",
                                           curses.color_pair(2) | curses.A_BOLD)
        DotsScreen.Refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    # def OnLoop(self):
    #     self._sched.enter(0.1, 1, self.OnLoop, ())

    @staticmethod
    def DecodeMsg(msg):
        try:
            m = np.array(np.mat(msg), dtype=np.bool)
        except Exception, e:
            print(str(e))
            return None

        return m

    def SchedRun(self):
        self._sched.run()

    def run(self):
        '''thread run'''
        reply, listen_for_request = Server(port=conf.Port).reply()
        for msg in listen_for_request:

            ch = msg
            dealingFunc = {
                curses.KEY_UP: self.OnKeyUp,
                'k': self.OnKeyUp,


                curses.KEY_DOWN: self.OnKeyDown,
                'j': self.OnKeyDown,


                curses.KEY_LEFT: self.OnKeyLeft,
                'h': self.OnKeyLeft,


                curses.KEY_RIGHT: self.OnKeyRight,
                'l': self.OnKeyRight,

                'q': self.OnExit,

            }.get(ch, None)

            reply("")
            if dealingFunc is None:
                ret = DotsScreen.DecodeMsg(msg)
                print(ret)
            else:
                dealingFunc()

    def Exit():
        pass

    def OnKeyUp(self):
        index = self._curPoint[0] - 1
        if index < 0:
            index = conf.ScreenRow - 1
        self._curPoint = index, self._curPoint[1]

    def OnKeyDown(self):
        index = self._curPoint[0] + 1
        if index >= conf.ScreenRow:
            index = 0
        self._curPoint = index, self._curPoint[1]

    def OnKeyLeft(self):
        index = self._curPoint[1] - 1
        if index < 0:
            index = conf.ScreenColumn - 1
        self._curPoint = self._curPoint[0], index

    def OnKeyRight(self):
        index = self._curPoint[1] + 1
        if index >= conf.ScreenColumn:
            index = 0
        self._curPoint = self._curPoint[0], index

    def OnExit(self):
        self._exit = True
        exit(0)

    # def __str__(self):
    #     return str(self._dots)

    # def IsSet(self, x, y):
    #     return self._dots[x, y] != 0

    # def Set(self, x, y):
    #     self._dots[x, y] = 1

    # def Clear(self, x, y):
    #     self._dots[x, y] = 0


def main():
    try:
        DotsScreen.InitWin()

        dots = DotsScreen()
        dots.start()
        dots.SchedRun()

    except Exception, e:
        print str(e)

    finally:
        DotsScreen.UninitWin()


if __name__ == "__main__":
    main()
