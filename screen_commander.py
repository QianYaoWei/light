#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client
import util.curses as uc


class ScreenCommander(threading.Thread):
    def __init__(self, port = None):
        super(ScreenCommander, self).__init__()
        self._channel = Client()
        self._port = port

    def run(self):

        uc.set_win()
        if self._port is not None:
            self._channel.connect_local(port=self._port)
            request, listen_for_reply = self._channel.request()

            while True:
                ch = uc.stdscr.getch()
                request(chr(ch))
                response = next(listen_for_reply)
                if ch == ord('q'):
                    print "quit"
                    break
        else:
            while True:
                ch = uc.stdscr.getch()
                if ch == ord('q'):
                    print "quit"
                    break
        uc.unset_win()

if __name__ == "__main__":
    commander = ScreenCommander()
    commander.start()
