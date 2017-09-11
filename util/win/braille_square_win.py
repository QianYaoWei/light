#!/usr/bin/env python
# -*- coding:utf-8 -*-
from win import Win


class BrailleSquareWin(Win):

    __byteMask = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20)

    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(BrailleSquareWin, self).__init__(stdscr, name, oriX, oriY,
                                               height, width)
        self._sortedKeys = None

    def OnMessage(self, byte):
        '''override'''
        if not self._sortedKeys:
            self._sortedKeys = sorted(self._points.keys())

        # definitely the win has 6 points
        for i, m in enumerate(self.__byteMask):
            if (byte & m) != 0:
                self._points[self._sortedKeys[i]].Activate()
            else:
                self._points[self._sortedKeys[i]].Inactivate()
