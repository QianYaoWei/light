#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses

stdscr = curses.initscr()

Color1 = 1
Color2 = 2

def set_win():
    '''''控制台设置'''
    global stdscr

    curses.keypad(True)
    # 使用颜色首先需要调用这个方法
    curses.start_color()
    # 文字和背景色设置，设置了两个color pair，分别为1和2
    curses.init_pair(Color1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color2, curses.COLOR_RED, curses.COLOR_BLACK)
    # 关闭屏幕回显
    curses.noecho()
    # 输入时不需要回车确认
    curses.cbreak()
    # 设置nodelay，使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
    # stdscr.nodelay(1)


def unset_win():
    '''控制台重置'''
    global stdstr
    # 恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    # 结束窗口
    curses.endwin()
