#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import curses
import time
import sched
import threading
from zeroless import Server
import sys

from util.conf import ScreenConf as conf
import util.curses as uc
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

    def Show(self):
        if self._exit:
            return

        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                if self._curPoint == (i, j):
                    # import pudb; pudb.set_trace()  # XXX BREAKPOINT
                    uc.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "x",
                                           curses.color_pair(uc.Color2) | curses.A_BOLD)
                    continue

                if 0 == self._dots[i, j]:
                    uc.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "_",
                                           curses.color_pair(uc.Color1) | curses.A_BOLD)
                else:
                    uc.stdscr.addstr(i + conf.BeginX,
                                           j * conf.ColSpread + conf.BeginY,
                                           "*",
                                           curses.color_pair(uc.Color1) | curses.A_BOLD)
        uc.stdscr.refresh()
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

        uc.set_win()
        reply, listen_for_request = Server(port=conf.Port).reply()
        for msg in listen_for_request:

            ch = msg
            dealingFunc = {
                curses.KEY_UP: self.__OnKeyUp,
                'k': self.__OnKeyUp,


                curses.KEY_DOWN: self.__OnKeyDown,
                'j': self.__OnKeyDown,


                curses.KEY_LEFT: self.__OnKeyLeft,
                'h': self.__OnKeyLeft,


                curses.KEY_RIGHT: self.__OnKeyRight,
                'l': self.__OnKeyRight,

                'q': self.__OnExit,

            }.get(ch, None)

            reply("")
            if dealingFunc is None:
                ret = DotsScreen.DecodeMsg(msg)
            else:
                dealingFunc()

    def __OnKeyUp(self):
        index = self._curPoint[0] - 1
        if index < 0:
            index = conf.ScreenRow - 1
        self._curPoint = index, self._curPoint[1]

    def __OnKeyDown(self):
        index = self._curPoint[0] + 1
        if index >= conf.ScreenRow:
            index = 0
        self._curPoint = index, self._curPoint[1]

    def __OnKeyLeft(self):
        index = self._curPoint[1] - 1
        if index < 0:
            index = conf.ScreenColumn - 1
        self._curPoint = self._curPoint[0], index

    def __OnKeyRight(self):
        index = self._curPoint[1] + 1
        if index >= conf.ScreenColumn:
            index = 0
        self._curPoint = self._curPoint[0], index

    def __OnExit(self):
        self._exit = True
        uc.unset_win()
        sys.exit(0)


def main():
    try:
        dots = DotsScreen()
        dots.start()

        commander = ScreenCommander(conf.Port)
        commander.start()

        dots.Sched.run()

    except Exception, e:
        print str(e)

    finally:
        pass

if __name__ == "__main__":
    main()
