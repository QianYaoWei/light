#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
import sched
import time
from util.conf import ScreenConf as conf
import util
import util.curses_win as uc

Color1 = 1

Color2 = 2

class TxtScreen(object):
    def __init__(self, stdscr, txt="", Sched=None):
        self._width = 32
        self._height = conf.ScreenRow
        self._txt = txt
        self._curPos = 0
        self._sched = Sched if Sched else sched.scheduler(time.time, time.sleep)
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())
        self._stdscr = stdscr


        curses.init_pair(Color1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(Color2, curses.COLOR_RED, curses.COLOR_BLACK)

    def Init(self, reciever):
        # reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        # reciever.MsgRegister('k', self.__OnKeyUp)
        # reciever.MsgRegister(curses.KEY_DOWN, self.__OnKeyDown)
        # reciever.MsgRegister('j', self.__OnKeyDown)
        # reciever.MsgRegister(curses.KEY_LEFT, self.__OnKeyLeft)
        # reciever.MsgRegister('h', self.__OnKeyLeft)
        # reciever.MsgRegister(curses.KEY_RIGHT, self.__OnKeyRight)
        # reciever.MsgRegister('l', self.__OnKeyRight)
        reciever.MsgRegister('t', self.__OnTXT)
        reciever.MsgRegister('q', self.__OnExit)

    def Show(self):
        curPos = self._curPos
        ln = len(self._txt[curPos:])
        for i in range(0, conf.ScreenRow):
            for j in range(0, conf.ScreenColumn):
                index = i * conf.ScreenColumn + j
                if index >= ln:
                    self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(Color2) | curses.A_BOLD)
                else:
                    self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, self._txt[curPos + index], curses.color_pair(Color1) | curses.A_BOLD)

        self._stdscr.refresh()
        self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    # def Show(self):
    #     curPos = self._curPos
    #     ln = len(self._txt[curPos:])
    #     curIndex = 0
    #     for i in range(0, conf.ScreenRow):
    #         changeLine = False
    #         for j in range(0, conf.ScreenColumn):
    #             # index = i * conf.ScreenColumn + j
    #             if curIndex >= ln:
    #                 self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(Color1) | curses.A_BOLD)
    #             elif self._txt[curPos + curIndex] != '\n':
    #                 self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, self._txt[curPos + curIndex], curses.A_BOLD)
    #                 curIndex += 1
    #             else:
    #                 self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(Color1) | curses.A_BOLD)
    #                 changeLine = True
    #                 continue
    #         if changeLine:
    #             curIndex += 1

    #             # index = i * conf.ScreenColumn + j
    #             # if index >= ln:
    #             #     self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, "_", curses.color_pair(Color1) | curses.A_BOLD)
    #             # else:
    #             #     self._stdscr.addstr(i + conf.BeginX, j + conf.BeginY, self._txt[curPos + index], curses.A_BOLD)

    #     self._stdscr.refresh()
    #     self._sched.enter(conf.RefreshInterval, 1, self.Show, ())

    @property
    def Sched(self):
        return self._sched

    @property
    def TXT(self):
        return self._txt

    @property
    def StdScr(self):
        return self._stdscr

    def UpdateTXT(self, txt):
        self._curPos = 0
        self._txt = txt

    def __OnKeyUp(self):
        def OnKeyUp(self):
            index = self._curPos - self._width
            start = index if index >= 0 else 0

            index = self._curPos
            self._curPos = start
            for i in range(index, start - 1, -1):
                if self._txt[i] == '\n':
                    self._curPos = i - 1
                    break

            if self._curPos < start:
                self._curPos = start
        self._sched.enter(0, 1, OnKeyUp, (self, ))

    def __OnKeyDown(self):
        def OnKeyDown(self):
            index = self._curPos + self._width
            end = index if index < len(self._txt) else len(self._txt) - 1

            index = self._curPos
            self._curPos = end
            for i in range(index, end + 1):
                if self._txt[i] == '\n':
                    self._curPos = i + 1
                    break

            if self._curPos > end:
                self._curPos = end
        self._sched.enter(0, 1, OnKeyDown, (self, ))

    def __OnKeyLeft(self):
        def KeyLeft(self):
            index = self._curPos - 1
            self._curPos = index if index >= 0 else 0
        self._sched.enter(0, 1, KeyLeft, (self, ))

    def __OnKeyRight(self):
        def KeyRight(self):
            index = self._curPos + 1
            self._curPos = index if index < len(self._txt) else len(self._txt) - 1
        self._sched.enter(0, 1, KeyRight, (self, ))

    def __OnTXT(self, txt):
        self._sched.enter(0, 1, self.UpdateTXT, (txt, ))

    def __OnExit(self):
        exit(0)


def main():
    ts = curses.wrapper(TxtScreen, txt='welcome here...')
    reciever = util.CommandReciever()
    ts.Init(reciever)
    reciever.start()
    sender = uc.CursesSender(ts.StdScr)
    sender.start()
    ts.Sched.run()

if __name__ == "__main__":
    main()
