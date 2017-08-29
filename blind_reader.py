#!/usr/bin/env python
# -*- coding:utf-8 -*-

from book import Book
from zeroless import Client
import util
from util import conf
from util import Message
import util.curses_win as uc
from txt_screen import TxtScreen


class BlindReader(object):
    def __init__(self, recieverPort=None):
        self.curDir = conf.ReaderConf.ShelfPath
        self._books = {}
        self._curBookID = 0

        self._client = Client()
        self._port = recieverPort if recieverPort is not None else conf.CommanderConf.Port

    def Init(self, reciever):
        reciever.MsgRegister('f', self.__PageNext)
        reciever.MsgRegister('b', self.__PagePre)
        self._client.connect_local(self._port)

        # reciever.MsgRegister('g', self.JumpToPage)
        # reciever.MsgRegister('G', self.JumpToPage)

    def GetCurBook(self):
        return self._books.get(self._curBookID, None)

    def __SendMsg(self, msgID, msg):
        request, listen_for_reply = self._client.request()
        m = Message(msgID, msg)
        request(m.EncodeMsg())

    def __PageNext(self):
        book = self.GetCurBook()
        if book:
            msg = book.PageNext()
            if msg:
                self.__SendMsg('t', msg)

    def __PagePre(self):
        book = self.GetCurBook()
        if book:
            msg = book.PagePre()
            if msg:
                self.__SendMsg('t', msg)

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

    def CloseBook(self, id):
        if id != self._curBookID:
            return

        book = self._books.get(id, None)
        if book is not None and \
           book.Status == book.OPEN:

            book.SyncToDB()
            book.Close()
            self._curBookID = 0

    def OpenBook(self, id):
        if 0 != self._curBookID:
            # 当前已经打开其它书
            return

        book = self._books.get(id, None)
        if book is not None and \
           book.Status == book.CLOSE:

            book.Open()

            self._curBookID = id

    def DelBook(self, id):
        book = self._books.get(id, None)
        if book is not None:
            if book.Status == book.OPEN:
                book.Close()
            book.DelFromDB()
            self._books.pop(id)

            if id == self._curBookID:
                self._curBookID = 0

if __name__ == "__main__":
    # book = Book(1, path="/tmp1", page=1)
    # book.InsertIntoDB()
    # book.SyncToDB()
    # book = Book(2, path="/tmp2", page=2)
    # book.InsertIntoDB()
    # book.SyncToDB()
    # book = Book(3, path="/tmp3", page=3)
    # book.InsertIntoDB()
    # book.SyncToDB()

    reciever = util.CommandReciever()

    book = Book(1, path="/Users/terencewei/my_src/br/book_mark.py", cur_page=0)
    reader = BlindReader()
    reader.Init(reciever)
    reader.AddBook(book)
    reader.OpenBook(1)
    page = book.CurPage()

    ts = TxtScreen(page)
    ts.Init(reciever)

    reciever.start()

    sender = uc.CursesSender()
    sender.start()

    ts.Sched.run()
    # li = book.SelectAllFromDB()
    # for el in li:
    #     print el
