#!/usr/bin/env python
# -*- coding:utf-8 -*-

RealMachine = 1

Curses = 2

class ScreenConf(object):
    ScreenRow = 16

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
    ShelfPath = "/tmp/reader"

    DBPath = "/tmp/reader/reader.db"


class BookConf(object):
    PageRow = 16
    PageCol = 32
