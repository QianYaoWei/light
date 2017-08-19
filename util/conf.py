#!/usr/bin/env python
# -*- coding:utf-8 -*-

RealMachine = 1

Curses = 2

class ScreenConf(object):
    ScreenRow = 24

    ScreenColumn = 48

    ScreenMode = Curses

    BeginX = 5

    BeginY = 5

    ColSpread = 2

    RefreshInterval = 0.01

    ChannelAddress = "tcp://127.0.0.1:6666"

    Port = 6666


class ReaderConf(object):
    ShelfPath = "/tmp/reader"

    DBPath = "/Users/terencewei/my_src/br/sql/reader.db"


class BookConf(object):
    PageRow = 5
    PageCol = 2
