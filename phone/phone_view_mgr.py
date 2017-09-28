#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import curses
import time
import sched
import util
import util.win as win
import util.win.view as view
from dial_panel_view import DialPanelView
from input_num_view import InputtedNumsView
from incomming_call_view import IncommingCallView


class PhoneViewMgr(view.ViewMgr):
    def __init__(self, stdscr, sch=None):
        super(PhoneViewMgr, self).__init__(stdscr, sch)


def main(stdscr):
    g_phone = PhoneViewMgr(stdscr)
    # v = DialPanelView(stdscr, g_phone.Sched)
    # v.RefreshWin()
    # v.ViewMgr = g_phone
    # g_phone.AddView(DailPanelView_id, v)

    # v = InputtedNumsView(stdscr, g_phone.Sched)
    # v.ViewMgr = g_phone
    # g_phone.AddView(InputtedNumsView_id, v)

    v = IncommingCallView(stdscr, g_phone.Sched)
    v.RefreshWin()
    v.ViewMgr = g_phone
    g_phone.AddView(IncommingCallView_id, v)

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
