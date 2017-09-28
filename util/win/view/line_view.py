#!/usr/bin/env python
# -*- coding:utf-8 -*-

from view import View
import util.win as win


class LineView(View):
    __rowCount = win.Line4_id - win.Line0_id + 1

    def __init__(self, stdscr, sch=None):
        super(LineView, self).__init__(stdscr, win.RowScr_id, sch)
        self._curLine = 0
        self._lineList = []
        self.__RegisterWinEvent()

    def __RegisterWinEvent(self):
        self.Win.SubWins[win.Line0_id].AddWinEvent(
            win.WinEvent(win.eClickTheWin, self._OnWinClick, 0))

        self.Win.SubWins[win.Line1_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self._OnWinClick, 1))

        self.Win.SubWins[win.Line2_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self._OnWinClick, 2))

        self.Win.SubWins[win.Line3_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self._OnWinClick, 3))

        self.Win.SubWins[win.Line4_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self._OnWinClick, 4))

    def _OnWinClick(self, pos):
        '''override this func'''
        pass

    @property
    def CurPage(self):
        return self._lineList[self._curLine:self._curLine + self.__rowCount]

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
