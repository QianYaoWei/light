#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client

from util import ScreenConf as conf


class ScreenCommander(threading.Thread):
    def __init__(self, stdscr):
        super(ScreenCommander, self).__init__()
        self._channel = Client()
        self._stdscr = stdscr

    @property
    def Channel(self):
        return self._channel

    def run(self):
        self._channel.connect_local(port=conf.Port)
        request, listen_for_reply = self._channel.request()

        while True:
            #ch = self._stdscr.getch()
            ch = raw_input()
            request(chr(ch))
            response = next(listen_for_reply)
            print(response)
