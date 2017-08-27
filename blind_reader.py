#!/usr/bin/env python
# -*- coding:utf-8 -*-

from book import Book
from util.conf import ReaderConf as conf


class BlindReader(object):
    def __init__(self):
        self.curDir = conf.ReaderConf.ShelfPath
        self._books = {}
        self._curBookID = 0

    def AddBook(self, id, path):
        if id in self._books:
            return

        book = Book(id, path)
        book.InsertIntoDB()
        book.SyncToDB()
        self._books[id] = book
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

    book = Book(1, path="/tmp1", page=1)
    li = book.SelectAllFromDB()
    for el in li:
        print el
