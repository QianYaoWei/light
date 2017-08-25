#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import curses
import time
import sched
import threading
from zeroless import Server

import util
from util import ScreenConf as conf
from screen_commander import ScreenCommander


class TxtScreen(threading.Thread):
    def __init__(self):
        super(TxtScreen, self).__init__()

        self._width = 32
        self._height = 16
        self._data = '''hello worldhello worldhello worldhello
                        worldhello worldhello worldhello world
                        worldhello worldhello worldhello world
                        worldhello worldhello worldhello world
                        worldhello worldhello worldhello world
                        worldhello worldhello worldhello world'''
        self._curPos = 0
        self._sched = sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())
        self._exit = False

    def Show(self):
        if self._exit:
            return

        curPos = self._curPos
        ln = len(self._data[curPos:])
        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                index = i * conf.ScreenColumn + j
                if index >= ln:
                    util.stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(util.Color2) | curses.A_BOLD)
                else:
                    util.stdscr.addstr(i + conf.BeginX, j + conf.BeginY, self._data[curPos + index], curses.A_BOLD)

        util.stdscr.refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    @property
    def Sched(self):
        return self._sched

    def run(self):
        '''thread run'''
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
            if dealingFunc:
                dealingFunc()

    def __OnKeyUp(self):
        index = self._curPos - self._width
        self._curPos = index if index >= 0 else 0
        # print self._curPos

    def __OnKeyDown(self):
        index = self._curPos + self._width
        self._curPos = index if index < len(self._data) else len(self._data) - 1
        # print self._curPos

    def __OnKeyLeft(self):
        index = self._curPos - 1
        self._curPos = index if index >= 0 else 0
        # print self._curPos

    def __OnKeyRight(self):
        index = self._curPos + 1
        self._curPos = index if index < len(self._data) else len(self._data) - 1
        # print self._curPos

    def __OnExit(self):
        self._exit = True
        sys.exit(0)


def main():
    txt = TxtScreen()
    txt.start()

    commander = ScreenCommander(conf.Port)
    commander.start()

    txt.Sched.run()

if __name__ == "__main__":
    main()
