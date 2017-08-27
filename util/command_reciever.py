#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Server
from conf import CommanderConf as conf
from message import Message

class CommandReciever(threading.Thread):
    def __init__(self, port=None):
        super(CommandReciever, self).__init__()
        self._port = port if port is not None else conf.Port
        self._server = Server(port=self._port)

        self._msgCallBack = {}

    def run(self):
        reply, listen_for_request = self._server.reply()
        for msg in listen_for_request:
            reply("")
            m = Message.DecodeMsg(msg)
            funs = self._msgCallBack.get(m.MsgID, None)
            if funs:
                for f in funs:
                    if m.MsgData:
                        f(m.MsgData)
                    else:
                        f()
            if m.MsgID == 'q':
                print "reciever quit"
                break

    def MsgRegister(self, msg, callback):
        if not callable(callback):
            return

        funs = self._msgCallBack.get(msg, None)
        if funs is None:
            self._msgCallBack[msg] = []
            self._msgCallBack[msg].append(callback)
        else:
            funs.append(callback)
