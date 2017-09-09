#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
import util


def main(stdscr):
    sender = util.CursesSender(stdscr)
    sender.start()

    reciever = util.CommandReciever()
    reciever.start()

    sender.join()
    reciever.join()

if __name__ == "__main__":
    import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
    curses.wrapper(main)
