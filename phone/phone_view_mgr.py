#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import curses
import time
import sched
import util
import util.win as win
from dail_panel_view import DailPanelView
from input_num_view import InputtedNumsView
from incomming_call_view import IncommingCallView


class PhoneViewMgr(win.ViewMgr):
    def __init__(self, stdscr, sch=None):
        super(PhoneViewMgr, self).__init__(stdscr, sch)


def main(stdscr):
    g_phone = PhoneViewMgr(stdscr)
    view = DailPanelView(stdscr, g_phone.Sched)
    view.RefreshWin()
    view.ViewMgr = g_phone
    g_phone.AddView(DailPanelView_id, view)

    view = InputtedNumsView(stdscr, g_phone.Sched)
    view.ViewMgr = g_phone
    g_phone.AddView(InputtedNumsView_id, view)

    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    view = IncommingCallView(stdscr, g_phone.Sched)
    view.ViewMgr = g_phone
    g_phone.AddView(IncommingCallScr_id, view)

    reciever = util.CommandReciever()
    g_phone.Init(reciever)
    reciever.start()


    sender = util.CommandSender(stdscr)
    sender.start()

    g_phone.Sched.run()

    reciever.join()
    sender.join()

if __name__ == "__main__":
    curses.wrapper(main)
