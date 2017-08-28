#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client
from .. import Message
from ..conf import CommanderConf as conf
from curses_win import *

class CursesSender(threading.Thread):
    def __init__(self, port=None):
        super(CursesSender, self).__init__()
        self._client = Client()
        self._port = port if port is not None else conf.Port

    def run(self):

        set_win()
        self._client.connect_local(port=self._port)
        request, listen_for_reply = self._client.request()

        while True:
            ch = stdscr.getch()
            m = Message(chr(ch))
            request(m.EncodeMsg())
            response = next(listen_for_reply)
            if m.MsgID == 'q':
                print "sender quit"
                break
        # else:
        #     while True:
        #         ch = stdscr.getch()
        #         if ch == ord('q'):
        #             print "sender quit"
        #             break
        unset_win()
