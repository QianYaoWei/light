#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client

import util
from util import ScreenConf as conf


class ScreenCommander(threading.Thread):
    def __init__(self, stdscr):
        super(ScreenCommander, self).__init__()
        self._channel = Client()

    def run(self):
        self._channel.connect_local(port=conf.Port)
        request, listen_for_reply = self._channel.request()

        while True:
            ch = util.stdscr.getch()
            if ch == ord('e'):
                print ch
                # exit(0)

            # request(chr(ch))
            # response = next(listen_for_reply)
            # print(response)

def main():
    try:
        print "fuck"
        # util.set_win()
        commander = ScreenCommander(None)
        commander.start()
    except Exception, e:
        print str(e)
    finally:
        pass
        # util.unset_win()

if __name__ == "__main__":
    main()
