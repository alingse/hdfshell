#coding=utf-8
#author@alingse
#2016.07.20

from cluster import hdfs_schema
from cluster import file_schema

import argparse


class commandExplain(object):

    def __init__(self,name,praser):
        self.name = name
        self.parser = praser

    def isValid(self,*args,**kwargs):
        pass

    def translate(self,*args,**kwargs):
        pass




class commandProxy(object):
    """ 代理 命令 shell 命令 解释器"""
    def __init__(self,hdfs):
        self.hdfs = hdfs
        self.explains = {}
        self._head = 'hadoop fs '
        self.lock = None

    def add_explain(self,explain):
        name = explain.name
        if name in self.explains:
            pass
        self.explains[name] = explain

    def remove_explain(self,name):
        pass

    def proxy(self,*args):
        pass
        #for exp in self.explains

    def 