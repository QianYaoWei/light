#!/usr/bin/env python
# -*- coding:utf-8 -*-
from win import Win


class LineWin(Win):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(LineWin, self).__init__(stdscr, name, oriX, oriY, height, width)

    def OnMessage(self, msg):
        '''override'''
        ks = sorted(self._subWins.keys())
        li = msg.split(',')
        m = min(len(ks), len(li))
        for i in range(0, m):
            self._subWins[ks[i]].OnMessage(ord(li[i]))
