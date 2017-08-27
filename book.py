#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import util
from util.conf import BookConf as conf

class Book(util.OrmObj):
    # <<<<<<the book status<<<<<<
    CLOSE = 0
    OPEN = 1
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>

    def __init__(self, id, **kargs):
        super(Book, self).__init__(id, "book")

        self._dbFields["path"] = kargs.get("path", "")
        self._dbFields["cur_page"] = kargs.get("cur_page", 0)

        self._endPage = 0
        self._fd = None
        self._status = self.CLOSE

    def Init(self, reciever):
        reciever.MsgRegister('f', self.PageNext)
        reciever.MsgRegister('b', self.PagePre)
        # reciever.MsgRegister('g', self.JumpToPage)
        # reciever.MsgRegister('G', self.JumpToPage)

    @property
    def Status(self):
        return self._status

    def __GetPageMsg(self, pos):
        self._fd.seek(pos)
        msg = self._fd.read(conf.PageRow * conf.PageCol)
        self._fd.seek(pos)
        return msg

    def GetBookName(self):
        return os.path.basename(self._dbFields["path"])

    def Open(self):
        self._fd = open(self._dbFields["path"], "r")
        self._fd.seek(0, os.SEEK_END)
        fileLong = self._fd.tell()
        self._endPage = fileLong / (conf.PageRow * conf.PageCol)

        pagePos = self.GetPagePos(self._dbFields["cur_page"])
        self._fd.seek(pagePos)
        self._status = self.OPEN

    def Close(self):
        self._fd.close()
        self._status = self.CLOSE

    @staticmethod
    def GetPagePos(page):
        return page * (conf.PageRow * conf.PageCol)

    def CurPage(self):
        pagePos = self.GetPagePos(self._dbFields["cur_page"])
        self._fd.seek(pagePos)
        msg = self._fd.read(conf.PageRow * conf.PageCol)
        self._fd.seek(pagePos)
        return msg

    def PageNext(self):
        if self._dbFields["cur_page"] < self._endPage:
            self._dbFields["cur_page"] += 1
            pagePos = self.GetPagePos(self._dbFields["cur_page"])
            msg = self.__GetPageMsg(pagePos)
            self.SyncToDB()
            return msg

    def PagePre(self):
        if self._dbFields["cur_page"] >= 1:
            self._dbFields["cur_page"] -= 1
            pagePos = self.GetPagePos(self._dbFields["cur_page"])
            msg = self.__GetPageMsg(pagePos)
            self.SyncToDB()
            return msg

    def JumpToPage(self, page):
        if self._dbFields["cur_page"] <= page <= self._endPage:
            self._dbFields["cur_page"] = page
            pagePos = self.GetPagePos(self._dbFields["cur_page"])
            msg = self.__GetPageMsg(pagePos)
            self.SyncToDB()
            return msg

if __name__ == "__main__":
    for e in '今天，是一个大喜的日子今天，是一个大喜的日子':
        print e,
