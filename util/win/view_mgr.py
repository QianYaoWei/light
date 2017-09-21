#!/usr/bin/env python
# -*- coding:utf-8 -*-
import curses
import time
import sched
import util
from operation import Operation
from ..conf import ScreenConf


class ViewMgr(Operation):
    def __init__(self, stdscr, sch=None):
        super(ViewMgr, self).__init__()
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
