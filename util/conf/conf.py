#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

RealMachine = 1

Curses = 2

class ScreenConf(object):
    ScreenRow = 15

    ScreenColumn = 32

    ScreenMode = Curses

    BeginX = 5

    BeginY = 5

    ColSpread = 2

    RefreshInterval = 0.01


class CommanderConf(object):
    ChannelAddress = "tcp://127.0.0.1:6666"
    Port = 6666


class ReaderConf(object):
    ShelfPath = os.path.dirname(__file__) + "/../../"

    DBPath = os.path.dirname(__file__) + "/../../sql/reader.db"


class BookConf(object):
    PageRow = 16
    PageCol = 32
