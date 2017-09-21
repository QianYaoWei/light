#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import *
import util
import util.win as win


class DailPanelView(win.View):
    def __init__(self, stdscr, sch=None):
        super(DailPanelView, self).__init__(stdscr, win.DailPanelScr_id, sch)

        self._inputtedNums = []

        self.__RegisterWinEvent()

    def __RegisterWinEvent(self):
        self.Win.SubWins[win.DailNum1_id].AddWinEvent(
            win.WinEvent(win.eClickTheWin, self.__OnWinClick, Num1))

        self.Win.SubWins[win.DailNum2_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num2))

        self.Win.SubWins[win.DailNum3_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num3))

        self.Win.SubWins[win.DailNum4_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num4))

        self.Win.SubWins[win.DailNum5_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num5))

        self.Win.SubWins[win.DailNum6_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num6))

        self.Win.SubWins[win.DailNum7_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num7))

        self.Win.SubWins[win.DailNum8_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num8))

        self.Win.SubWins[win.DailNum9_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num9))

        self.Win.SubWins[win.DailNum0_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, Num0))

        self.Win.SubWins[win.DailAsterisk_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, NumAsterisk))

        self.Win.SubWins[win.DailSharp_id].AddWinEvent(win.WinEvent(
            win.eClickTheWin, self.__OnWinClick, NumSharp))

    @win.view_clear
    def __OnWinClick(self, num):
        self._inputtedNums.append(num)

    def RefreshWin(self):
        '''implement this func'''
        for _, w in self.Win.SubWins.items():
            w.RefreshDots()

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
        pass


def main(stdscr):
    view = DailPanelView(stdscr)

    reciever = util.CommandReciever()
    view.Init(reciever)
    view.RefreshWin()
    reciever.start()

    # sender = util.CommandSender(stdscr)
    # sender.start()

    view.Sched.run()

    reciever.join()
    # sender.join()

if __name__ == "__main__":
    curses.wrapper(main)
