#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import sched
import sqlite3
from conf import ReaderConf as conf

class OrmObj(object):
    """ subclass needs to implement def DBFields() """
    def __init__(self, id, tableName):
        self.__id = id
        self.__tableName = tableName
        self._dbFields = {}

    def __str__(self):
        return str(self._dbFields.values())

    def Init(self, Sched=None, conn=None):
        try:
            self._sched = Sched if Sched else sched.scheduler(time.time, time.sleep)
            self._dbCon = conn if conn else sqlite3.connect(conf.DBPath)
        except Exception, e:
            print(str(e))
            exit(0)

        assert self._sched, "sched not initialization!"
        assert self._dbCon, "database %s not connected!" % conf.DBPath

    @property
    def Id(self):
        return self.__id

    @property
    def DBFields(self):
        return self._dbFields

    @property
    def DBCon():
        return self._dbCon

    @property
    def Sched(self):
        return self._sched

    def GetField(self, field):
        return self._dbFields.get(field, None)

    def SelectFromDB(self):
        # def Select(self):
        keys = self._dbFields.keys()
        sql = "select %s from %s where id=%d;" \
            % (",".join(keys), self.__tableName, self.__id)
        try:
            cursor = self._dbCon.cursor()
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is None:
                return False

            for i, el in enumerate(ret):
                self._dbFields[keys[i]] = el

            return True
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()
        # self._sched.enter(0, 1, Select, (self, ))

    def SelectAllFromDB(self):
        # def SelectAll(self, func):
        objList = []
        if not self._dbFields:
            # func(objList)
            return objList

        keys = ["id"]
        keys.extend(self._dbFields.keys())
        sql = "select %s from %s;" \
            % (",".join(keys), self.__tableName)
        try:
            cursor = self._dbCon.cursor()
            cursor.execute(sql)
            retList = cursor.fetchall()
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

        # func(objList)
        return objList
        # self._sched.enter(0, 1, SelectAll, (self, func))

    def InsertIntoDB(self):
        def Insert(self):
            sql = "insert into %s(id) values(%d);" \
                % (self.__tableName, self.__id)
            try:
                cursor = self._dbCon.cursor()
                cursor.execute(sql)
                self._dbCon.commit()
            except Exception, e:
                print(str(e))
            finally:
                cursor.close()
        self._sched.enter(0, 1, Insert, (self, ))

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
        def Sync(self):
            if not self._dbFields:
                return
            updateFields = [self.__UpdateFieldStr(k, v)
                            for k, v in self._dbFields.items()]
            sql = "update %s set %s where id=%d;" \
                % (self.__tableName, ",".join(updateFields), self.__id)
            try:
                cursor = self._dbCon.cursor()
                cursor.execute(sql)
                self._dbCon.commit()
            except Exception, e:
                print(str(e))
            finally:
                cursor.close()
        self._sched.enter(0, 1, Sync, (self, ))

    def DelFromDB(self):
        sql = "delete from %s where id=%d;" \
            % (self.__tableName, self.__id)
        try:
            cursor = self._dbCon.cursor()
            cursor.execute(sql)
            self._dbCon.commit()
        except Exception, e:
            print(str(e))
        finally:
            cursor.close()
