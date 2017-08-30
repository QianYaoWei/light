#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from book import Book
from zeroless import Client
import util
from util import conf
from util import Message
import util.curses_win as uc
from txt_screen import TxtScreen

BookReading = 1

DirReading = 2

class BlindReader(util.OrmObj):
    def __init__(self, id=1, recieverPort=None, **kargs):
        super(BlindReader, self).__init__(id, "reader")
        self._dbFields["cur_book_id"] = kargs.get("cur_book_id", 0)
        self._curDir = conf.ReaderConf.ShelfPath
        self._books = {}
        self._client = Client()
        self._port = recieverPort if recieverPort is not None else conf.CommanderConf.Port
        self._readingType = DirReading


    def Init(self, reciever, Sched=None, conn=None):
        super(BlindReader, self).Init(Sched, conn)

        reciever.MsgRegister('f', self.__PageNext)
        reciever.MsgRegister('b', self.__PagePre)
        reciever.MsgRegister('c', self.__CloseBook)

        # reciever.MsgRegister('g', self.JumpToPage)
        # reciever.MsgRegister('G', self.JumpToPage)

        self._client.connect_local(self._port)

        # books = book.SelectAllFromDB()
        # for el in books:
        #     AddBook(self, el)

    def __SendMsg(self, msgID, msg):
        request, listen_for_reply = self._client.request()
        m = Message(msgID, msg)
        request(m.EncodeMsg())

    def __PageNext(self):
        if self._readingType != BookReading:
            return
        book = self.GetCurBook()
        if book:
            msg = book.PageNext()
            if msg:
                self.__SendMsg('t', msg)

    def __PagePre(self):
        if self._readingType != BookReading:
            return
        book = self.GetCurBook()
        if book:
            msg = book.PagePre()
            if msg:
                self.__SendMsg('t', msg)

    def __CloseBook(self):
        if self._readingType != BookReading:
            return
        id = self.GetField("cur_book_id")
        if 0 == id:
            return

        book = self._books.get(id, None)
        if book is not None and book.Status == book.OPEN:
            book.Close()
            self.DBFields["cur_book_id"] = 0
            self.SyncToDB()
            self._readingType = DirReading

    def GetCurBook(self):
        return self._books.get(self.GetField("cur_book_id"), None)

    def AddBook(self, book, syncToDB=False):
        if book.Id in self._books:
            return
        if syncToDB:
            book.InsertIntoDB()
            book.SyncToDB()
        self._books[book.Id] = book

        return book

    def GetBook(self, id):
        return self._books.get(id, None)

    def OpenBook(self, id):
        if 0 != self.GetField("cur_book_id"):
            # 当前已经打开其它书
            return

        book = self._books.get(id, None)
        if book is not None and book.Status == book.CLOSE:
            book.Open()
            self.SyncToDB()

            self.DBFields["cur_book_id"] = id
            self._readingType = BookReading

    def DelBook(self, id):
        book = self._books.get(id, None)
        if book is not None:
            if book.Status == book.OPEN:
                book.Close()
            book.DelFromDB()
            self._books.pop(id)

            if id == self.GetField("cur_book_id"):
                self.DBFields["cur_book_id"] = 0
                self._readingType = DirReading


if __name__ == "__main__":

    reciever = util.CommandReciever()
    reader = BlindReader()
    reader.Init(reciever)

    if not reader.SelectFromDB():
        reader.InsertIntoDB()
        reader.SyncToDB()

    f = os.path.dirname(__file__) + "/book_mark.py"
    book = Book(1, path=f, cur_page=0)

    reader.AddBook(book)
    reader.OpenBook(1)
    page = book.CurPage()

    ts = TxtScreen(page, reader.Sched)
    ts.Init(reciever)

    reciever.start()

    sender = uc.CursesSender()
    sender.start()

    reader.Sched.run()
