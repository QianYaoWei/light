#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import util.win as win

class ContentWin(win.LineWin):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(ContentWin, self).__init__(stdscr, name, oriX, oriY, height, width)

    def OnTouch(self):
        pass
