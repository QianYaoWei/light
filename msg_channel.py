#!/usr/bin/env python
# -*- coding:utf-8 -*-

import util
import util.curses_win as uc

if __name__ == "__main__":
    reciever = util.CommandReciever()
    reciever.start()

    sender = uc.CursesSender()
    sender.start()
