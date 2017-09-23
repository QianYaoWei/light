#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..win_ids import *
from ..win import Win
from back_forward_win import *

IncommingCallScr = {
    "x": 10,
    "y": 10,
    "height": 16,
    "width": 32,

    "subwins": [
        BackWin_id,
        ForwardWin_id
    ]
}


# class IncommingCallWin(Win):
#     def __init__(self, stdscr, name, oriX, oriY, height, width):
#         super(IncommingCallWin, self).__init__(stdscr, name, oriX, oriY,
#                                                height, width)
#         self._name = ""
#         self._phoneName = ""
#         self._address = ""
