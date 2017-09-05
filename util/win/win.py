#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
from win_desc import Wins

def rectangle(win, ulx, uly, lrx, lry):
    """Draw a rectangle with corners at the provided upper-left
    and lower-right coordinates.
    """
    win.vline(ulx + 1, uly, '|', lrx - ulx - 1)
    win.vline(ulx + 1, lry, '|', lrx - ulx - 1)

    win.hline(ulx, uly + 1, '-', lry - uly - 1)
    win.hline(lrx, uly + 1, '-', lry - uly - 1)

    win.addch(ulx, uly, '+')
    win.addch(ulx, lry, '+')
    win.addch(lrx, uly, '+')
    win.addch(lrx, lry, '+')


class Win(object):
    def __init__(self, stdscr, x, y, height, width):
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        self._subWins = []
        self._points = []
        self._stdscr = stdscr

    def __str__(self):
        return ",".join([str(self._x), str(self._y), str(self._height), str(self._width)])

    @property
    def X(self):
        return self._x

    @property
    def Y(self):
        return self._y

    @property
    def SubWins(self):
        return self._subWins

    def Touch(self):
        pass

    def IsInRange(self, x, y):
        if self._x <= x < self._x + height and self._y <= y < self._y + width:
            return True
        else:
            return False

    def Draw(self):
        rectangle(self._stdscr, self._x, self._y, self._x + self._height, self._y + self._width)

        # TODO
        for p in self._points:
            p.Draw()

        for w in self._subWins:
            w.Draw()

    def Close(self):
        # TODO
        for w in self._subWins:
            w.Close()


    @staticmethod
    def CreateWin(stdscr, name):
        win = Wins.get(name, None)
        if win:
            w = Win(stdscr, win["x"], win["y"], win["height"], win["width"])
            for s in win["subwins"]:
                w._subWins.append(Win(stdscr, w.X + s["x"], w.Y + s["y"], s["height"], s["width"]))
            return w


def main(stdscr):
    w = Win.CreateWin(stdscr, "win1")
    w.Draw()
    stdscr.refresh()
    len(w.SubWins)
    # print w
    # for s in w.SubWins:
    #     print s


if __name__ == "__main__":
    curses.wrapper(main)
