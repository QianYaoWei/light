#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import util.win as win


class InputtedNumsView(win.View):
    def __init__(self, stdscr, sch=None):
        super(InputtedNumsView, self).__init__(stdscr, win.InputNumScr_id, sch)

        self._inputtedNums = []

        self._num2winIDMapping = {
            Num1: win.DailNum1_id,
            Num2: win.DailNum2_id,
            Num3: win.DailNum3_id,
            Num4: win.DailNum4_id,
            Num5: win.DailNum5_id,
            Num6: win.DailNum6_id,
            Num7: win.DailNum7_id,
            Num8: win.DailNum8_id,
            Num9: win.DailNum9_id,
            Num0: win.DailNum0_id,
            NumAsterisk: win.DailAsterisk_id,
            NumSharp: win.DailSharp_id,
        }

    @property
    def Nums(self):
        return self._inputtedNums

    @Nums.setter
    def Nums(self, nums):
        self._inputtedNums = nums

    def _OnForward(self):
        '''implement this func'''
        # Dial TODO
        pass

    def _OnBackward(self):
        '''implement this func'''
        if self._inputtedNums:
            self._inputtedNums.pop()

    def _OnSwitch(self):
        '''implement this func'''
        # Dial TODO
        # view = self.ViewMgr.GetView(DailPanelView_id)
        # if view and view.Book:
        #     self.ViewMgr.MoveToTop(TxtView_id)
        pass

    def RefreshWin(self):
        '''implement this func'''

        l = len(self.Win.SubwinKeys)
        for i, num in enumerate(self._inputtedNums):
            if i >= l:
                break
            numWin = self._num2winIDMapping.get(i, None)
            if numWin is None:
                continue

            k = self.Win.SubwinKeys[i]
            w = self.Win.SubWins[k]
            numWin.RefreshDots(w.DotsStatus)
