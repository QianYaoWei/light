#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

class ScreenConf(object):
    ScreenRow = 16

    ScreenColumn = 32

    BeginX = 5

    BeginY = 5

    ColSpread = 2

    RefreshInterval = 0.01


class CommanderConf(object):
    ChannelAddress = "tcp://127.0.0.1:6666"
    Port = 6666


class ReaderConf(object):
    ShelfPath = os.path.dirname(__file__) + "/../../"
    ShelfPath = os.path.abspath(ShelfPath)

    DBPath = os.path.dirname(__file__) + "/../../sql/reader.db"
    DBPath = os.path.abspath(DBPath)


class BookConf(object):
    PageRow = 16
    PageCol = 32


class WinConf(object):
    ShowWinBorder = False

    # 1 dot mode
    # 2 txt mode
    ShowMode = 2

    DotUp_Ch = '.'

    DotDown_Ch = ' '
