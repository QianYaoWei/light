#!/usr/bin/env python
# -*- coding:utf-8 -*-


def Key(x, y):
    return (x, y)


class Point(object):
    def __init__(self, stdscr, x, y):
        self._x = x
        self._y = y
        self._status = False
        self._stdscr = stdscr

    @property
    def Status(self):
        return self._status

    @property
    def Key(self):
        return Key(self._x, self._y)

    def Activate(self):
        self._status = True

    def InActivate(self):
        self._status = False

    def Draw(self):
        # TODO
        pass
