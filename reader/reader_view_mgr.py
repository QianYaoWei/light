#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import curses
import time
import sched
import util
import util.win as win
from util.conf import ReaderConf
from line_view import LineView
from txt_view import TxtView


class ReaderViewMgr(win.ViewMgr):
    def __init__(self, stdscr, sch=None):
        super(ReaderViewMgr, self).__init__(stdscr, sch)

    def OpenBook(self, book):
        if book:
            book.Open()
            self.MoveToTop(TxtView_id)
            self._views[TxtView_id].Book = book
            self._views[TxtView_id].RefreshWin()

def main(stdscr):
    g_reader = ReaderViewMgr(stdscr)
    view = LineView(ReaderConf.ShelfPath, stdscr, g_reader.Sched)
    view.RefreshCurDir()
    view.RefreshWin()
    view.ViewMgr = g_reader
    g_reader.AddView(LineView_id, view)

    view = TxtView(stdscr, g_reader.Sched)
    view.ViewMgr = g_reader
    g_reader.AddView(TxtView_id, view)

    InitColor()

    reciever = util.CommandReciever()
    g_reader.Init(reciever)
    reciever.start()

    sender = util.CommandSender(stdscr)
    sender.start()

    g_reader.Sched.run()

    reciever.join()
    sender.join()


if __name__ == "__main__":
    curses.wrapper(main)
