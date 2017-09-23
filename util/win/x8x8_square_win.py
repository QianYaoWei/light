#!/usr/bin/env python
# -*- coding:utf-8 -*-

from win import Win


class X8x8Win(Win):
    __byteMask = (
        0x1, 0x2, 0x4, 0x8,
        0x10, 0x20, 0x40, 0x80,

        0x1 << 8, 0x2 << 8, 0x4 << 8, 0x8 << 8,
        0x10 << 8, 0x20 << 8, 0x40 << 8, 0x80 << 8,

        0x1 << 16, 0x2 << 16, 0x4 << 16, 0x8 << 16,
        0x10 << 16, 0x20 << 16, 0x40 << 16, 0x80 << 16,

        0x1 << 24, 0x2 << 24, 0x4 << 24, 0x8 << 24,
        0x10 << 24, 0x20 << 24, 0x40 << 24, 0x80 << 24,

        0x1 << 32, 0x2 << 32, 0x4 << 32, 0x8 << 32,
        0x10 << 32, 0x20 << 32, 0x40 << 32, 0x80 << 32,

        0x1 << 40, 0x2 << 40, 0x4 << 40, 0x8 << 40,
        0x10 << 40, 0x20 << 40, 0x40 << 40, 0x80 << 40,

        0x1 << 48, 0x2 << 48, 0x4 << 48, 0x8 << 48,
        0x10 << 48, 0x20 << 48, 0x40 << 48, 0x80 << 48,

        0x1 << 56, 0x2 << 56, 0x4 << 56, 0x8 << 56,
        0x10 << 56, 0x20 << 56, 0x40 << 56, 0x80 << 56)

    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(X8x8Win, self).__init__(stdscr, name, oriX, oriY,
                                      height, width)
        self._dotKeys = None

    def OnMessage(self, byte_8):
        '''override'''
        # definitely the win has 64 dots
        if not self._dotKeys:
            self._dotKeys = sorted(self._dots.keys())

        for i, m in enumerate(self.__byteMask):
            if (byte_8 & m) != 0:
                self._dots[self._dotKeys[i]].Activate()
            else:
                self._dots[self._dotKeys[i]].Inactivate()

    def OnTouch(self):
        for w, p in self._dots.items():
            if p.Status:
                p.Inactivate()
            else:
                p.Activate()
