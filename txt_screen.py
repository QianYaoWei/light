#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
import time
import sched
import sys
import util.curses_win as uc
from util.conf import ScreenConf as conf
import util


class TxtScreen():
    def __init__(self, txt):
        # super(TxtScreen, self).__init__()
        self._width = 32
        self._height = conf.ScreenRow
        self._txt = txt
        self._curPos = 0
        self._sched = sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())
        self._exit = False

    def Init(self, reciever):
        reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        reciever.MsgRegister('k', self.__OnKeyUp)
        reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        reciever.MsgRegister('k', self.__OnKeyUp)
        reciever.MsgRegister(curses.KEY_DOWN, self.__OnKeyDown)
        reciever.MsgRegister('j', self.__OnKeyDown)
        reciever.MsgRegister(curses.KEY_LEFT, self.__OnKeyLeft)
        reciever.MsgRegister('h', self.__OnKeyLeft)
        reciever.MsgRegister(curses.KEY_RIGHT, self.__OnKeyRight)
        reciever.MsgRegister('l', self.__OnKeyRight)
        reciever.MsgRegister('q', self.__OnExit)
        reciever.MsgRegister('t', self.__OnTXT)


    def Show(self):
        if self._exit:
            return

        curPos = self._curPos
        ln = len(self._txt[curPos:])
        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                index = i * conf.ScreenColumn + j
                if index >= ln:
                    uc.stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(uc.Color2) | curses.A_BOLD)
                else:
                    uc.stdscr.addstr(i + conf.BeginX, j + conf.BeginY, self._txt[curPos + index], curses.A_BOLD)

        uc.stdscr.refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    @property
    def Sched(self):
        return self._sched

    @property
    def TXT(self):
        return self._txt

    def __OnKeyUp(self):
        index = self._curPos - self._width
        self._curPos = index if index >= 0 else 0
        # print self._curPos

    def __OnKeyDown(self):
        index = self._curPos + self._width
        self._curPos = index if index < len(self._txt) else len(self._txt) - 1
        # print self._curPos

    def __OnKeyLeft(self):
        index = self._curPos - 1
        self._curPos = index if index >= 0 else 0
        # print self._curPos

    def __OnKeyRight(self):
        index = self._curPos + 1
        self._curPos = index if index < len(self._txt) else len(self._txt) - 1
        # print self._curPos

    def __OnExit(self):
        self._exit = True
        sys.exit(0)

    def __OnTXT(self, txt):
        self._curPos = 0
        self._txt = txt


def main():
    try:
        uc.set_win()
        reciever = util.CommandReciever()
        txt = '''welcome here...'''
        ts = TxtScreen(txt)
        ts.Init(reciever)
        reciever.start()

        sender = util.CommandSender()
        sender.start()

        ts.Sched.run()
    except Exception, e:
        print str(e)

    finally:
        uc.unset_win()

if __name__ == "__main__":
    main()
