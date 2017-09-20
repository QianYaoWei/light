
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import *
import util
import util.win as win


class InputtedNumsView(win.View):
    def __init__(self, stdscr, sch=None):
        super(InputtedNumsView, self).__init__(stdscr, win.InputNumScr_id, sch)

        self._inputtedNums = []

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
        # view = self.ViewMgr.GetView(TxtView_id)
        # if view and view.Book:
        #     self.ViewMgr.MoveToTop(TxtView_id)
        pass
