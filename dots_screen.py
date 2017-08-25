#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import curses
import time
import sched
import threading
from zeroless import Server
import sys

import util
from util import ScreenConf as conf
from screen_commander import ScreenCommander


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

    def Show(self):
        if self._exit:
            return

        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                if self._curPoint == (i, j):
                    # import pudb; pudb.set_trace()  # XXX BREAKPOINT
                    util.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "x",
                                           curses.color_pair(util.Color2) | curses.A_BOLD)
                    continue

                if 0 == self._dots[i, j]:
                    util.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "_",
                                           curses.color_pair(util.Color1) | curses.A_BOLD)
                else:
                    util.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "*",
                                           curses.color_pair(util.Color1) | curses.A_BOLD)
        util.stdscr.refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    @property
    def Sched(self):
        return self._sched

    @staticmethod
    def DecodeMsg(msg):
        try:
            m = np.array(np.mat(msg), dtype=np.bool)
        except Exception, e:
            print(str(e))
            return None

        return m

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
        sys.exit(0)

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
        util.set_win()

        dots = DotsScreen()
        dots.start()

        commander = ScreenCommander(util.stdscr)
        commander.start()

        dots.Sched.run()

    except Exception, e:
        print str(e)

    finally:
        util.unset_win()

if __name__ == "__main__":
    main()
