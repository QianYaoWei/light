#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
import util

def main(stdscr):
    sender = util.CommandSender(stdscr)
    sender.start()

if __name__ == "__main__":
    curses.wrapper(main)
    # reciever = util.CommandReciever()
    # reciever.start()

    # curses.wrapper(main)
