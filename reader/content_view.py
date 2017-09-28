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


class ContentView(view.LineView):
    __rowCount = win.Line4_id - win.Line0_id + 1

    def __init__(self, dir, stdscr, sch=None):
        super(ContentView, self).__init__(stdscr, sch)
        self._dirList = [dir, ]

    def _OnWinClick(self, pos):
        '''implement this func'''
        cp = self.CurPage
        if 0 <= pos < len(cp):
            cp[pos].OnClick(self)
        self.StdScr.clear()

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

    def _OnSwitch(self):
        '''implement this func'''
        v = self.ViewMgr.GetView(TxtView_id)
        if v and v.Book:
            self.ViewMgr.MoveToTop(TxtView_id)
        self.StdScr.clear()


def main(stdscr):
    InitColor()
    path = os.path.realpath(ReaderConf.ShelfPath)
    v = ContentView(path, stdscr)
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
