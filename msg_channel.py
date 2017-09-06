#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
import util.win as win


def main(stdscr):
    w = win.Win.CreateWin(stdscr, "ReaderWin")
    w.RelativePosForPoints(w.X, w.Y)
    w.Draw()
    stdscr.refresh()

if __name__ == "__main__":
    # reciever = util.CommandReciever()
    # reciever.start()

    # sender = uc.CursesSender()
    # sender.start()
    curses.wrapper(main)
