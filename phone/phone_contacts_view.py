#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import *
import util.win as win
import util.win.view as view


class PhoneContactsView(view.LineView):
    def __init__(self, stdscr, sch=None):
        super(PhoneContactsView, self).__init__(stdscr, sch)
