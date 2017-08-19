#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
from conf import ReaderConf

conf = ReaderConf

try:
    g_conn = sqlite3.connect(conf.DBPath)
except Exception, e:
    print(str(e))
    exit(0)

assert g_conn, "database %s not connected!" % conf.DBPath


class OrmObj(object):
    """ subclass needs to implement def DBFields() """
    def __init__(self, id, tableName):
        self.__id = id
        self.__tableName = tableName
        self._dbFields = {}

    def __str__(self):
        return str(self._dbFields.values())

    @property
    def Id(self):
        return self.__id

    @property
    def DBFields(self):
        return self._dbFields

    def GetField(self, field):
        return self._dbFields.get(field, None)


    def SelectFromDB(self):
        keys = self._dbFields.keys()
        sql = "select %s from %s where id=%d;" \
            % (",".join(keys), self.__tableName, self.__id)
        try:
            cursor = g_conn.cursor()
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is None:
                return

            for i, el in enumerate(ret):
                self._dbFields[keys[i]] = el

        except Exception, e:
            print(str(e))
        finally:
            cursor.close()

    def SelectAllFromDB(self):
        if not self._dbFields:
            return
        keys = ["id"]
        keys.extend(self._dbFields.keys())
        sql = "select %s from %s;" \
              % (",".join(keys), self.__tableName)
        try:
            cursor = g_conn.cursor()
            cursor.execute(sql)
            retList = cursor.fetchall()
            objList = []
            for row in retList:
                dbFields = {}
                id = row[0]
                for i, el in enumerate(row):
                    if i != 0:
                        dbFields[keys[i]] = el
                objList.append(self.__class__(id, **dbFields))
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()

        return objList

    def InsertIntoDB(self):
        sql = "insert into %s(id) values(%d);" \
            % (self.__tableName, self.__id)
        try:
            cursor = g_conn.cursor()
            cursor.execute(sql)
            g_conn.commit()
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()

    @staticmethod
    def __UpdateFieldStr(field, data):
        if type(data) == int:
            return "%s=%d" % (field, data)
        elif type(data) == float:
            return "%s=%f" % (field, data)
        elif type(data) == str:
            return '%s="%s"' % (field, data)
        else:
            return ""

    def SyncToDB(self):
        if not self._dbFields:
            return

        updateFields = [self.__UpdateFieldStr(k, v)
                        for k, v in self._dbFields.items()]
        sql = "update %s set %s where id=%d;" \
            % (self.__tableName, ",".join(updateFields), self.__id)
        try:
            cursor = g_conn.cursor()
            cursor.execute(sql)
            g_conn.commit()
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()

    def DelFromDB(self):
        sql = "delete from %s where id=%d;" \
            % (self.__tableName, self.__id)
        try:
            cursor = g_conn.cursor()
            cursor.execute(sql)
            g_conn.commit()
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()


class Book(OrmObj):
    def __init__(self, id):
        super(Book, self).__init__(id, "book")

        self._dbFields["path"] = "/tmp/"

        self._dbFields["curPage"] = 3


if __name__ == "__main__":
    b = Book(1)

    b.SelectFromDB()
    b.InsertIntoDB()
    b.SyncToDB()
    b.DelFromDB()
