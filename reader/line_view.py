#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import *
import os
import util
import util.win as win
import util.win.view as view
from util.conf import ReaderConf
from book import Book


class LineInfo(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    @property
    def Name(self):
        return self._name

    def OnClick(self, v):
        '''override this func'''
        pass


class DirInfo(LineInfo):
    global Blue
    Color = Blue

    def __init__(self, name):
        super(DirInfo, self).__init__(name)

    def OnClick(self, v):
        '''override this func'''
        v.LowerDir(self._name)
        v.RefreshCurDir()
        v.RefreshWin()


class UpperDir(LineInfo):
    global Blue
    Color = Blue

    def __init__(self):
        super(UpperDir, self).__init__('..')

    def OnClick(self, v):
        '''override this func'''
        v.UpperDir()
        v.RefreshCurDir()
        v.RefreshWin()


class BookInfo(LineInfo):
    global NoColor
    Color = NoColor

    def __init__(self, name):
        super(BookInfo, self).__init__(name)

    def OnClick(self, v):
        '''override this func'''
        p = v.CurDir + os.path.sep + self._name
        book = Book(1, path=p, cur_page=0)
        v.ViewMgr.OpenBook(book)


class LineView(view.View):
    __rowCount = win.Line4_id - win.Line0_id + 1

    def __init__(self, dir, stdscr, sch=None):
        super(LineView, self).__init__(stdscr, win.RowScr_id, sch)
        self._dirList = [dir, ]
        self._curLine = 0
        self._lineList = []
        self.__RegisterWinEvent()

    def __RegisterWinEvent(self):
        self.Win.SubWins[win.Line0_id].AddWinEvent(
            win.WinEvent(win.eClickTheWin, self.__OnWinClick, 0))

        self.Win.SubWins[win.Line1_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, 1))

        self.Win.SubWins[win.Line2_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, 2))

        self.Win.SubWins[win.Line3_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, 3))

        self.Win.SubWins[win.Line4_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, 4))

    def __OnWinClick(self, pos):
        cp = self.CurPage
        if 0 <= pos < len(cp):
            cp[pos].OnClick(self)
        self.StdScr.clear()

    @property
    def CurPage(self):
        return self._lineList[self._curLine:self._curLine + self.__rowCount]

    @property
    def CurDir(self):
        return os.path.sep.join(self._dirList)

    def IsTopDir(self):
        return len(self._dirList) == 1

    def LowerDir(self, dir):
        self._dirList.append(dir)

    def UpperDir(self):
        if len(self._dirList) >= 1:
            self._dirList.pop()

    def RefreshCurDir(self):
        curDir = self.CurDir
        self._curLine = 0
        li = os.listdir(curDir)

        del self._lineList[:]

        if not self.IsTopDir():
            self._lineList.append(UpperDir())

        for el in li:
            path = curDir + os.path.sep + el
            if os.path.isdir(path):
                info = DirInfo(el)
                self._lineList.append(info)
                continue
            if os.path.isfile(path):
                info = BookInfo(el)
                self._lineList.append(info)
                continue

    def RefreshWin(self):
        '''implement this func'''
        for _, w in self.Win.SubWins.items():
            w.OnMessage(None)
            w.RefreshDots()

        for i, li in enumerate(self.CurPage):
            # TODO
            txt = ','.join(list(li.Name))
            for _, w in self.Win.SubWins[win.Line0_id + i].SubWins.items():
                w.Color = li.Color
            self.Win.SubWins[win.Line0_id + i].OnMessage(txt)

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

    def _OnForward(self):
        '''implement this func'''
        self.NextPage()
        self.StdScr.clear()

    def _OnBackward(self):
        '''implement this func'''
        self.PrePage()
        self.StdScr.clear()

    def _OnUp(self):
        '''implement this func'''
        self.PreLine()
        self.StdScr.clear()

    def _OnDown(self):
        '''implement this func'''
        self.NextLine()
        self.StdScr.clear()

    def _OnSwitch(self):
        '''implement this func'''
        v = self.ViewMgr.GetView(TxtView_id)
        if v and v.Book:
            self.ViewMgr.MoveToTop(TxtView_id)
        self.StdScr.clear()


def main(stdscr):
    InitColor()
    path = os.path.realpath(ReaderConf.ShelfPath)
    v = LineView(path, stdscr)
    # print v .CurDir

    v.RefreshCurDir()
    v.RefreshWin()

    reciever = util.CommandReciever()
    v.Init(reciever)
    reciever.start()

    sender = util.CommandSender(stdscr)
    sender.start()

    v.Sched.run()

    reciever.join()
    sender.join()


if __name__ == "__main__":
    curses.wrapper(main)
