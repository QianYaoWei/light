#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import util.win as win
import util.win.view as view


class IncommingCallView(view.View):
    def __init__(self, stdscr, sch=None):
        super(IncommingCallView, self).__init__(stdscr,
                                                win.IncommingCallScr_id, sch)
        self._name = ""
        self._phoneName = ""
        self._address = ""

        self.__RegisterWinEvent()

    def __RegisterWinEvent(self):
        self.Win.SubWins[win.BackWin_id].AddWinEvent(
            win.WinEvent(win.eClickTheWin, self.__OnWinClick, win.BackWin_id))

        self.Win.SubWins[win.ForwardWin_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, win.ForwardWin_id))

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    @property
    def PhoneName(self):
        return self._phoneName

    @PhoneName.setter
    def PhoneName(self, name):
        self._phoneName = name

    @property
    def Address(self):
        return self._address

    @Address.setter
    def Address(self, addr):
        self._address = addr

    def RefreshWin(self):
        '''implement this func'''
        for _, w in self.Win.SubWins.items():
            w.RefreshDots()

    def _OnForward(self):
        '''implement this func'''
        pass

    def _OnBackward(self):
        '''implement this func'''
        pass

    def __OnWinClick(self, id):
        # self._inputtedNums.append(num)
        # self.StdScr.clear()
        pass
