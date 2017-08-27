#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from zeroless import Client
import curses_win as uc
from conf import CommanderConf as conf
from message import Message
from command_reciever import CommandReciever

class CommandSender(threading.Thread):
    def __init__(self, port=None):
        super(CommandSender, self).__init__()
        self._client = Client()
        self._port = port if port is not None else conf.Port

    def run(self):

        uc.set_win()
        self._client.connect_local(port=self._port)
        request, listen_for_reply = self._client.request()

        while True:
            ch = uc.stdscr.getch()
            m = Message(chr(ch))
            request(m.EncodeMsg())
            response = next(listen_for_reply)
            if m.MsgID == 'q':
                print "sender quit"
                break
        # else:
        #     while True:
        #         ch = uc.stdscr.getch()
        #         if ch == ord('q'):
        #             print "sender quit"
        #             break
        uc.unset_win()


if __name__ == "__main__":
    reciever = CommandReciever()
    reciever.start()

    sender = CommandSender()
    sender.start()
