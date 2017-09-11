#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import curses
import os
import util
import util.win as win


class LineInfo(object):
    def __init__(self, path, txt):
        self._path = path
        self._txt = txt

    def __str__(self):
        return ",".join([str(self._path), str(self._txt)])

    def Open(self, view):
        '''override this func'''
        pass


class DirInfo(LineInfo):
    def __init__(self, path, txt):
        super(DirInfo, self).__init__(path, txt)

    def Open(self, view):
        '''override this func'''
        pass


class BookInfo(LineInfo):
    def __init__(self, path, txt):
        super(BookInfo, self).__init__(path, txt)

    def Open(self, view):
        '''override this func'''
        pass


class LineView(object):
    __rowCount = win.Line4_id - win.Line0_id + 1

    def __init__(self, stdscr, dir):
        g_scr = win.WinMgr(stdscr)
        self._win = g_scr.CreateWin(stdscr, win.RowScr_id)
        self._curDir = dir
        self._curLine = 0
        self._lineList = []

    def RegisterWinEvent(self):
        win.WinEvent(win.Line0_id, eClickTheWin, self.__OnClick, 0)
        win.WinEvent(win.Line1_id, eClickTheWin, self.__OnClick, 1)
        win.WinEvent(win.Line2_id, eClickTheWin, self.__OnClick, 2)
        win.WinEvent(win.Line3_id, eClickTheWin, self.__OnClick, 3)
        win.WinEvent(win.Line4_id, eClickTheWin, self.__OnClick, 4)

    def __OnClick(self, pos):
        cp = self.CurPage
        if 0 <= pos < len(cp):
            cp[pos].Open(self)

    @property
    def CurPage(self):
        return self._lineList[self._curLine:]

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
            self._win.SubWins[win.Line0_id + i].OnMessage('1,2,3,4,5,6')

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
        if len(self._lineList[self._curLine + self.__rowCount:]) < self.__rowCount:
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


def main(stdscr):
    view = LineView(stdscr, ".")
    view.RefreshCurDir()
    print view.CurPage


if __name__ == "__main__":
    # curses.wrapper(main)
    main('')
