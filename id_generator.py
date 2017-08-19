#!/usr/bin/env python
# -*- coding:utf-8 -*-

import util


class IDGenerator(util.OrmObj):
    def __init__(self):
        super(IDGenerator, self).__init__(1, "glob_id")
        self._dbFields["cur_id"] = None

        self.SelectFromDB()
        if self._dbFields["cur_id"] is None:
            self._dbFields["cur_id"] = 5
            self.InsertIntoDB()
            self.SyncToDB()

    def GenerateID(self):
        self._dbFields["cur_id"] = self._dbFields["cur_id"] + 1
        self.SyncToDB()
        return self._dbFields["cur_id"]

if __name__ == "__main__":
    gen = IDGenerator()
    gen.GenerateID()
    gen.GenerateID()
    gen.GenerateID()

    print gen.GetField("cur_id")
