#!/usr/bin/env python
# -*- coding:utf-8 -*-
from win import Win
from ..conf import WinConf


class BrailleSquareWin(Win):

    __byteMask = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20)

    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(BrailleSquareWin, self).__init__(stdscr, name, oriX, oriY,
                                               height, width)
        self._sortedKeys = None

    def OnMessage(self, byte):
        '''override'''
        if not self._sortedKeys:
            self._sortedKeys = sorted(self._dots.keys())

        if WinConf.ShowMode == 1:
            # definitely the win has 6 dots
            for i, m in enumerate(self.__byteMask):
                if byte is None or (byte & m) == 0:
                    self._dots[self._sortedKeys[i]].Inactivate()
                else:
                    self._dots[self._sortedKeys[i]].Activate()

        elif WinConf.ShowMode == 2:
            self._txt = byte if byte else None
