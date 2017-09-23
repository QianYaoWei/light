#!/usr/bin/env python
# -*- coding:utf-8 -*-

BackWin = {
    "x": 4,
    "y": 0,
    "height": 5,
    "width": 4,

    "dots": "OO.O"
            "O.OO"
            "...."
            "O.OO"
            "OO.O"
}

ForwardWin = {
    "x": 4,
    "y": 26,
    "height": 5,
    "width": 4,

    "dots": "O.OO"
            "OO.O"
            "...."
            "OO.O"
            "O.OO"
}


class BackForwardWin(Win):
    def __init__(self, stdscr, name, oriX, oriY, height, width):
        super(BackForwardWin, self).__init__(stdscr, name, oriX,
                                         oriY, height, width)
