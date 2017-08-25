#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import sys
import curses
import time
import sched
import threading
from zeroless import Server

from util import ScreenConf as conf
from screen_commander import ScreenCommander


class DotsScreen(threading.Thread):
    def __init__(self):
        super(DotsScreen, self).__init__()

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

    @property
    def StdScreen(self):
        return self._stdScreen

    @classmethod
    def UninitWin(cls):
        curses.endwin()

    @classmethod
    def Refresh(cls):
        cls._stdScreen.refresh()

    def Show(self):
        if self._exit:
            return

        for i, ch in enumerate(self._data[self._curPos:]):
            y = i % self._width
            x = i / self._width
            if x >= self._height:
                break
            DotsScreen._stdScreen.addstr(x, y, ch, curses.A_BOLD)
        DotsScreen.Refresh()
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
                print(ret)
            else:
                dealingFunc()

    def Exit():
        pass

    def OnKeyUp(self):
        index = self._curPos - self._width
        self._curPos = index if index >= 0 else 0
        print self._curPos

    def OnKeyDown(self):
        index = self._curPos + self._width
        self._curPos = index if index < len(self._data) else len(self._data) - 1
        print self._curPos

    def OnKeyLeft(self):
        index = self._curPos - 1
        self._curPos = index if index >= 0 else 0
        print self._curPos

    def OnKeyRight(self):
        index = self._curPos + 1
        self._curPos = index if index < len(self._data) else len(self._data) - 1
        print self._curPos

    def OnExit(self):
        self._exit = True
        sys.exit(0)


def main():
    try:
        DotsScreen.InitWin()

        dots = DotsScreen()
        dots.start()

        commander = ScreenCommander(dots.StdScreen)
        commander.start()

        dots.Sched.run()

    except Exception, e:
        print str(e)

    finally:
        DotsScreen.UninitWin()


if __name__ == "__main__":
    main()

