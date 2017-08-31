#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client
from .. import Message
from ..conf import CommanderConf as conf
import curses

class CursesSender(threading.Thread):
    def __init__(self, stdscr, port=None):
        super(CursesSender, self).__init__()
        self._client = Client()
        self._port = port if port is not None else conf.Port
        self._stdscr = stdscr

    def run(self):
        # def Run(self):
        self._client.connect_local(port=self._port)
        request, listen_for_reply = self._client.request()

        while True:
            ch = self._stdscr.getch()
            m = Message(chr(ch))
            request(m.EncodeMsg())
            response = next(listen_for_reply)
            if m.MsgID == 'q':
                print "sender quit"
                break
