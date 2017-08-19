#!/usr/bin/env python
# -*- coding:utf-8 -*-

import zmq
import numpy as np

class MsgChannel(object):

    def __init__(self, address):
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)
        self._socket.bind(address)


    def DecodeMsg(self, msg):
        try:
            m = np.array(np.mat(msg), dtype=np.bool)
        except Exception, e:
            return None

        return m


    @property
    def Socket(self):
        return self._socket
