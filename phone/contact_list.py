#!/usr/bin/env python
# -*- coding:utf-8 -*-

import util


class Contact(util.OrmObj):
    def __init__(self, id, **kargs):
        super(Contact, self).__init__(id, "contact")

        self._dbFields["name"] = kargs.get("name", "")
        self._dbFields["phone_num"] = kargs.get("phone_num", "")


@util.singleton
class ContactList(object):
    def __init__(self):
        self._contacts = {}

    @property
    def Contacts(self):
        return self._contacts.values()

    def Init(self):
        c = Contact(0)
        objs = c.SelectAllFromDB()
        for el in objs:
            self._contacts[el.Id] = el

    def GetContact(self, id):
        return self._contacts.get(id, None)

    def Add(self, contact):
        if contact.Id in self._contacts:
            return False
        self._contacts[contact.Id] = contact
        contact.InsertIntoDB()
        return True

    def Del(self, id):
        if id not in self._contacts:
            return False
        self._contacts[id].DelFromDB()
        self._contacts.pop(id)
