#!/usr/bin/env python
# -*- coding:utf-8 -*-

import util

# record type
Called = 1
Coming = 2
Missed = 3
All = 4


class CallRecored(util.OrmObj):
    def __init__(self, id, **kargs):
        super(CallRecored, self).__init__(id, "call_recored")

        self._dbFields["name"] = kargs.get("name", "")
        self._dbFields["phone_num"] = kargs.get("phone_num", "")
        self._dbFields["type"] = kargs.get("type", 0)
        self._dbFields["time"] = kargs.get("time", 0)


@util.singleton
class CallRecordList(object):
    def __init__(self):
        self._records = {}

    def RecordList(self, recType):
        recordList = []
        for _, record in self._records.items():
            if record.GetField("type") == recType or\
               recType == All:

                recordList.append(record)

        recordList.sort(key=lambda el: el.GetField("time"), reverse=True)
        return recordList

    def GetReocrd(self, id):
        return self._records.get(id, None)

    def Add(self, record):
        if record.Id in self._records:
            return False
        self._records[record.Id] = record
        record.InsertIntoDB()
        return True

    def Del(self, id):
        if id not in self._records:
            return False
        self._records[id].DelFromDB()
        self._records.pop(id)
