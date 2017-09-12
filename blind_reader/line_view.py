#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import curses
import os
import util
import util.win as win



NoColor = 0

Red = 1

Green = 2

Blue = 3

def InitColor():
    curses.init_pair(Red, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.init_pair(Green, curses.COLOR_GREEN, curses.COLOR_BLACK)

    curses.init_pair(Blue, curses.COLOR_BLUE, curses.COLOR_BLACK)


class LineInfo(object):
    def __init__(self, path, txt):
        self._path = path
        self._txt = txt

    def __str__(self):
        return ",".join([str(self._path), str(self._txt)])

    @property
    def Txt(self):
        return self._txt

    def Open(self, view):
        '''override this func'''
        pass


class DirInfo(LineInfo):
    global Blue
    Color = Blue
    def __init__(self, path, txt):
        super(DirInfo, self).__init__(path, txt)

    def Open(self, view):
        '''override this func'''
        view.CurDir = self._path
        view.RefreshCurDir()
        view.RefreshWin()


class BookInfo(LineInfo):
    global NoColor
    Color = NoColor
    def __init__(self, path, txt):
        super(BookInfo, self).__init__(path, txt)

    def Open(self, view):
        '''override this func'''
        pass


class LineView(win.View):
    __rowCount = win.Line4_id - win.Line0_id + 1

    def __init__(self, stdscr, dir):
        super(LineView, self).__init__(stdscr, win.RowScr_id)
        self._curDir = dir
        self._curLine = 0
        self._lineList = []
        self.__RegisterWinEvent()

    def __RegisterWinEvent(self):
        self._win.AddWinEvent(win.WinEvent(win.Line0_id, win.eClickTheWin,
                                           self.__OnWinClick, 0))
        self._win.AddWinEvent(win.WinEvent(win.Line1_id, win.eClickTheWin,
                                           self.__OnWinClick, 1))
        self._win.AddWinEvent(win.WinEvent(win.Line2_id, win.eClickTheWin,
                                           self.__OnWinClick, 2))
        self._win.AddWinEvent(win.WinEvent(win.Line3_id, win.eClickTheWin,
                                           self.__OnWinClick, 3))
        self._win.AddWinEvent(win.WinEvent(win.Line4_id, win.eClickTheWin,
                                           self.__OnWinClick, 4))

    def __OnWinClick(self, pos):
        cp = self.CurPage
        if 0 <= pos < len(cp):
            cp[pos].Open(self)

    @property
    def CurPage(self):
        return self._lineList[self._curLine:self._curLine + self.__rowCount]

    @property
    def CurDir(self):
        return self._curDir

    @CurDir.setter
    def CurDir(self, dir):
        self._curDir = dir

    def RefreshCurDir(self):
        li = os.listdir(self._curDir)
        if self._curLine >= len(li):
            self._curLine = len(li) - 1

        del self._lineList[:]
        # os.path.sep
        for el in li:
            if os.path.isdir(el):
                info = DirInfo(el, el)
                self._lineList.append(info)
                continue
            if os.path.isfile(el):
                info = BookInfo(el, el)
                self._lineList.append(info)
                continue

    def RefreshWin(self):
        for i, li in enumerate(self.CurPage):
            # TODO
            txt = ','.join(list(li.Txt))
            for _, w in self._win.SubWins[win.Line0_id + i].SubWins.items():
                w.Color = li.Color
            self._win.SubWins[win.Line0_id + i].OnMessage(txt)

    def NextLine(self):
        if len(self._lineList[self._curLine + 1:]) < self.__rowCount:
            return
        self._curLine += 1
        self.RefreshWin()


    def PreLine(self):
        if self._curLine <= 0:
            return
        self._curLine -= 1
        self.RefreshWin()


    def NextPage(self):
        if len(self._lineList[self._curLine + self.__rowCount:]) < \
           self.__rowCount:
            if len(self._lineList) >= self.__rowCount:
                self._curLine = len(self._lineList) - self.__rowCount
            else:
                self._curLine = 0
        else:
            self._curLine += self.__rowCount
        self.RefreshWin()

    def PrePage(self):
        if self._curLine - self.__rowCount >= 0:
            self._curLine -= self.__rowCount
        else:
            self._curLine = 0
        self.RefreshWin()

    @before_operation
    def _OnForward(self):
        '''implement this func'''
        self.NextPage()

    def _OnBackward(self):
        '''implement this func'''
        self.PrePage()

    def _OnUp(self):
        '''implement this func'''
        self.PreLine()

    def _OnDown(self):
        '''implement this func'''
        self.NextLine()



def main(stdscr):
    InitColor()

    view = LineView(stdscr, ".")
    view.RefreshCurDir()
    view.RefreshWin()

    reciever = util.CommandReciever()
    view.Init(reciever)
    reciever.start()

    sender = util.CommandSender(stdscr)
    sender.start()

    view.Sched.run()

    reciever.join()
    sender.join()


if __name__ == "__main__":
    curses.wrapper(main)
