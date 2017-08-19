#!/usr/bin/env python
# -*- coding:utf-8 -*-

from zeroless import Client
import util

conf = util.ScreenConf

client = Client()
client.connect_local(port=conf.Port)

request, listen_for_reply = client.request()

while True:
    com = raw_input("command: ")
    request(com)
    next(listen_for_reply)
    # print(response)
