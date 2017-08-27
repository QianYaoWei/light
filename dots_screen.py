#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import curses
import time
import sched
import sys

from util.conf import ScreenConf as conf
import util.curses_win as uc
import util


class DotsScreen():
    def __init__(self):
        self._dots = np.zeros(conf.ScreenRow * conf.ScreenColumn, dtype=np.bool).\
                     reshape(conf.ScreenRow, conf.ScreenColumn)

        self._sched = sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

        self._curPoint = (0, 0)
        self._exit = False

    def Init(self, reciever):
        reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        reciever.MsgRegister('k', self.__OnKeyUp)
        reciever.MsgRegister(curses.KEY_DOWN, self.__OnKeyDown)
        reciever.MsgRegister('j', self.__OnKeyDown)
        reciever.MsgRegister(curses.KEY_LEFT, self.__OnKeyLeft)
        reciever.MsgRegister('h', self.__OnKeyLeft)
        reciever.MsgRegister(curses.KEY_RIGHT, self.__OnKeyRight)
        reciever.MsgRegister('l', self.__OnKeyRight)
        reciever.MsgRegister('q', self.__OnExit)

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
        sys.exit(0)


def main():
    try:
        uc.set_win()
        reciever = util.CommandReciever()
        dots = DotsScreen()
        dots.Init(reciever)
        reciever.start()

        sender = util.CommandSender()
        sender.start()

        dots.Sched.run()
    except Exception, e:
        print str(e)

    finally:
        uc.unset_win()

if __name__ == "__main__":
    main()
