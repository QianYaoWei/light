#!/usr/bin/env python
# -*- coding:utf-8 -*-
from win import Win


class LineWin(Win):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(LineWin, self).__init__(stdscr, name, oriX, oriY, height, width)

    def OnMessage(self, msg):
        '''override'''
        if not msg:
            for _, w in self.SubWins.items():
                w.OnMessage(None)
            return

        li = msg.split(',')
        m = min(len(self._subWinSortedKeys), len(li))
        for i in range(0, m):
            k = self._subWinSortedKeys[i]
            self.SubWins[k].OnMessage(ord(li[i]))

        for k in self._subWinSortedKeys[m:]:
            self.SubWins[k].OnMessage(None)
