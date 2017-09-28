#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import util.win as win
import util.win.view as view


class CallListView(view.LineView):
    def __init__(self, stdscr, sch=None):
        super(CallListView, self).__init__(stdscr, sch)
