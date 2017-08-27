#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Message():
    def __init__(self, msgID, msgData=""):
        self._msgID = msgID
        self._msgData = msgData

    def __str__(self):
        return self.EncodeMsg()

    def EncodeMsg(self):
        return "%s,%s" % (str(self._msgID), self._msgData)

    @staticmethod
    def DecodeMsg(msg):
        index = msg.find(',')
        if index < 0:
            return Message(msg, "")
        return Message(msg[0:index], msg[index + 1:])

    @property
    def MsgID(self):
        return self._msgID

    @property
    def MsgData(self):
        return self._msgData


if __name__ == "__main__":
    m = Message("123", "qwe")
    print m
    m = Message(13, "kd")
    print m

    m = Message.DecodeMsg("24,48jgd")
    print m.MsgID
    print m.MsgData
