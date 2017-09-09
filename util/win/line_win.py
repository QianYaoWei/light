#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import Win


class LineWin(Win):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(LineWin, self).__init__(stdscr, name, oriX, oriY, height, width)

    def OnMessage(self, msg):
        '''override'''
        subwins = self._subWins
        li = msg.split(',')
        m = min(len(subwins), len(li))
        for i in range(0, m):
            subwins[i].OnMessage(li[i])
