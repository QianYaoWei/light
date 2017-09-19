#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import *
import util
import util.win as win


class DailPanelView(win.View):
    def __init__(self, stdscr, sch=None):
        super(DailPanelView, self).__init__(stdscr, win.DailPanelScr_id, sch)

    def RefreshWin(self):
        for _, w in self.Win.SubWins.items():
            w.RefreshDots()


def main(stdscr):
    view = DailPanelView(stdscr)

    reciever = util.CommandReciever()
    view.Init(reciever)
    view.RefreshWin()
    reciever.start()

    sender = util.CommandSender(stdscr)
    sender.start()

    view.Sched.run()

    reciever.join()
    sender.join()

if __name__ == "__main__":
    curses.wrapper(main)
