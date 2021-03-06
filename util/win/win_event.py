#!/usr/bin/env python
# -*- coding:utf-8 -*-

eClickTheWin = 1

eEnterTheWin = 2

eLeaveTheWin = 3


class WinEvent(object):
    def __init__(self, msgID, callBackFunc, *args):
        self._eventID = msgID
        self._callBackFunc = callBackFunc
        self._args = args

    def __str__(self):
        return ",".join([str(self._winID), str(self._eventID)])

    @property
    def EventID(self):
        return self._eventID

    def OnCallBack(self):
        self._callBackFunc(*self._args)
