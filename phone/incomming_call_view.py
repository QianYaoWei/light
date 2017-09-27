#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import util.win as win


class IncommingCallView(win.View):
    def __init__(self, stdscr, sch=None):
        super(IncommingCallView, self).__init__(stdscr,
                                                win.IncommingCallScr_id, sch)
        self._name = ""
        self._phoneName = ""
        self._address = ""

    def RefreshWin(self):
        '''implement this func'''
        for _, w in self.Win.SubWins.items():
            w.RefreshDots()
