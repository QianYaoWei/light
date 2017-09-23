#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import *
import curses
import util
import util.win as win
from book import Book


class TxtView(win.View):
    def __init__(self, stdscr, sch=None):
        super(TxtView, self).__init__(stdscr, win.BrailleSquareScr_id, sch)
        self._book = None
        self._txtList = []
        self._curPost = 0

    @property
    def Book(self):
        return self._book

    @Book.setter
    def Book(self, book):
        self._book = book
        del self._txtList[:]
        msg = self.Book.CurPage()
        if msg:
            self._txtList.extend(list(msg))

    def _OnForward(self):
        '''implement this func'''
        msg = self.Book.PageNext()
        if msg:
            del self._txtList[:]
            self._curPost = 0
            self._txtList.extend(list(msg))
            self.RefreshWin()
        self.StdScr.clear()

    def _OnBackward(self):
        '''implement this func'''
        msg = self.Book.PagePre()
        if msg:
            del self._txtList[:]
            self._curPost = 0
            self._txtList.extend(list(msg))
            self.RefreshWin()
        self.StdScr.clear()

    def _OnUp(self):
        '''implement this func'''
        num = len(self.Win.SubWins)
        if self._curPost - num < 0:
            self._curPost = 0;
        else:
            self._curPost -= num
        self.RefreshWin()
        self.StdScr.clear()

    def _OnDown(self):
        '''implement this func'''
        num = len(self.Win.SubWins)
        if self._curPost + num < len(self._txtList):
            self._curPost += num
        self.RefreshWin()
        self.StdScr.clear()

    def _OnSwitch(self):
        '''implement this func'''
        self.ViewMgr.MoveToTop(LineView_id)

    def RefreshWin(self):
        for _, w in self.Win.SubWins.items():
            w.OnMessage(None)

        m = min(len(self.Win.SubwinKeys), len(self._txtList[self._curPost:]))
        for i in range(0, m):
            k = self.Win.SubwinKeys[i]
            self.Win.SubWins[k].OnMessage(self._txtList[self._curPost + i])


def main(stdscr):
    view = TxtView(stdscr)
    b = Book(1, path="blind_reader.py")
    b.Open()
    view.Book = b
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
