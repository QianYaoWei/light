#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Operation(object):

    def __init__(self):
        self._exit = False

    def Init(self, reciever):
        # reciever.MsgRegister(curses.KEY_UP, self.__OnKeyUp)
        reciever.MsgRegister('k', self._OnKeyUp)
        # reciever.MsgRegister(curses.KEY_DOWN, self._OnKeyDown)
        reciever.MsgRegister('j', self._OnKeyDown)
        # reciever.MsgRegister(curses.KEY_LEFT, self.__OnKeyLeft)
        reciever.MsgRegister('h', self.__OnKeyLeft)
        # reciever.MsgRegister(curses.KEY_RIGHT, self._OnKeyRight)
        reciever.MsgRegister('l', self._OnKeyRight)
        reciever.MsgRegister('q', self._OnExit)
        reciever.MsgRegister('e', self._OnClick)

        reciever.MsgRegister('f', self._OnForward)
        reciever.MsgRegister('b', self._OnBackward)
        reciever.MsgRegister('u', self._OnUp)
        reciever.MsgRegister('d', self._OnDown)

    def _OnKeyUp(self):
        '''override this func'''
        pass

    def _OnKeyDown(self):
        '''override this func'''
        pass

    def __OnKeyLeft(self):
        '''override this func'''
        pass

    def _OnKeyRight(self):
        '''override this func'''
        pass

    def _OnExit(self):
        '''override this func'''
        self._exit = True

    def _OnClick(self):
        '''override this func'''
        pass

    def _OnForward(self):
        '''override this func'''
        pass

    def _OnBackward(self):
        '''override this func'''
        pass

    def _OnUp(self):
        '''override this func'''
        pass

    def _OnDown(self):
        '''override this func'''
        pass

