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


class PhoneViewMgr(win.ViewMgr):
    def __init__(self, stdscr, sch=None):
        super(PhoneViewMgr, self).__init__(stdscr, sch)


def main(stdscr):
    g_phone = PhoneViewMgr(stdscr)
    view = InputtedNumsView(stdscr, g_phone.Sched)
    view.ViewMgr = g_phone
    g_phone.AddView(InputtedNumsView_id, view)

    view = DailPanelView(stdscr, g_phone.Sched)
    view.ViewMgr = g_phone
    g_phone.AddView(DailPanelView_id, view)


if __name__ == "__main__":
    curses.wrapper(main)
