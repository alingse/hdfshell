#coding=utf-8
#author@shibin
#2016.06.17

import sys
import traceback


class ShellException(Exception):
    """Base Exception of this package"""
    def __init__(self, message=None):
        super(ShellException, self).__init__(message)