#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import curses
import time
import sched
import util
# from util import singleton
from util.conf import ScreenConf
from util.conf import ReaderConf
from line_view import LineView
from txt_view import TxtView

class ReaderViewMgr(util.win.Operation):
    def __init__(self, stdscr, sch=None):
        super(ReaderViewMgr, self).__init__()
        self._stdscr = stdscr
        self._sched = sch if sch else sched.scheduler(time.time, time.sleep)
        self._sched.enter(ScreenConf.RefreshInterval, 1, self.Show, ())

        self._views = {}
        self._viewIDLayer = []

    def AddView(self, id, view):
        self._viewIDLayer.append(id)
        self._views[id] = view

    def MoveToTop(self, viewID):
        index = self._viewIDLayer.index(viewID)
        if index > 0:
            self._viewIDLayer[0], self._viewIDLayer[index] = \
                self._viewIDLayer[index], self._viewIDLayer[0]
            self._views[viewID].RefreshWin()

    @property
    def StdScr(self):
        return self._stdscr

    @property
    def Sched(self):
        return self._sched

    def GetView(self, id):
        return self._views.get(id, None)

    def OpenBook(self, book):
        if book:
            book.Open()
            self.MoveToTop(TxtView_id)
            self._views[TxtView_id].Book = book
            self._views[TxtView_id].RefreshWin()

    def Show(self):
        if self._exit:
            return

        topID = self._viewIDLayer[0]
        self._views[topID].Show()
        self._sched.enter(ScreenConf.RefreshInterval, 1, self.Show, ())

    def _OnKeyUp(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnKeyUp()

    def _OnKeyDown(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnKeyDown()

    def _OnKeyLeft(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnKeyLeft()

    def _OnKeyRight(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnKeyRight()

    def _OnForward(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnForward()

    def _OnBackward(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnBackward()

    def _OnUp(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnUp()

    def _OnDown(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnDown()

    def _OnClick(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnClick()

    def _OnSwitch(self):
        topID = self._viewIDLayer[0]
        self._views[topID]._OnSwitch()


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
