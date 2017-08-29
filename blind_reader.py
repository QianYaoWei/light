#!/usr/bin/env python
# -*- coding:utf-8 -*-

from book import Book
from zeroless import Client
import util
from util import conf
from util import Message
import util.curses_win as uc
from txt_screen import TxtScreen


class BlindReader(util.OrmObj):
    def __init__(self, id=1, recieverPort=None, **kargs):
        super(BlindReader, self).__init__(id, "reader")
        self._dbFields["cur_book_id"] = kargs.get("cur_book_id", 0)

        self.curDir = conf.ReaderConf.ShelfPath
        self._books = {}

        self._client = Client()
        self._port = recieverPort if recieverPort is not None else conf.CommanderConf.Port

    def Init(self, reciever):
        reciever.MsgRegister('f', self.__PageNext)
        reciever.MsgRegister('b', self.__PagePre)
        # reciever.MsgRegister('g', self.JumpToPage)
        # reciever.MsgRegister('G', self.JumpToPage)
        self._client.connect_local(self._port)

        # books = book.SelectAllFromDB()
        # for el in books:
        #     AddBook(self, el)

    def GetCurBook(self):
        return self._books.get(self.GetField("cur_book_id"), None)

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
        if id != self.GetField("cur_book_id"):
            return

        book = self._books.get(id, None)
        if book is not None and book.Status == book.OPEN:

            book.SyncToDB()
            book.Close()
            self.SyncToDB()

    def OpenBook(self, id):
        if 0 != self.GetField("cur_book_id"):
            # 当前已经打开其它书
            return

        book = self._books.get(id, None)
        if book is not None and book.Status == book.CLOSE:
            book.Open()
            self.DBFields["cur_book_id"] = id
            self.SyncToDB()

    def DelBook(self, id):
        book = self._books.get(id, None)
        if book is not None:
            if book.Status == book.OPEN:
                book.Close()
            book.DelFromDB()
            self._books.pop(id)

            if id == self.GetField("cur_book_id"):
                self.DBFields["cur_book_id"] = 0


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

    r = BlindReader()
    reader = None
    ret = r.SelectAllFromDB()
    print ret
    if not ret:
        r.InsertIntoDB()
        r.SyncToDB()
        reader = r
    else:
        reader = ret[0]
    print reader

    reciever = util.CommandReciever()

    book = Book(1, path="/home/wei/gitsrc/light/book_mark.py", cur_page=0)
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
