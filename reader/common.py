#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("..")

import curses

NoColor = 0

Red = 1

Green = 2

Blue = 3

def InitColor():
    curses.init_pair(Red, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.init_pair(Green, curses.COLOR_GREEN, curses.COLOR_BLACK)

    curses.init_pair(Blue, curses.COLOR_BLUE, curses.COLOR_BLACK)


LineView_id = 1

TxtView_id = 2
