#coding=utf-8
#author@alingse
#2016.07.20

from cluster import hdfs_schema
from cluster import file_schema

import shlex

from explain import ls,exit



explainList = []
explainList.append(ls)
explainList.append(exit)



class commandProxy(object):

    def __init__(self,explains):
        self.explainDict = {}
        for _explain in explains:
            self.explainDict[_explain.name] = _explain
        #run time
        self._explain = None
        self._env = None
        
        #h
        self.cmdList = []

    def translate(self,command,env):
        args = shlex.split(command)
        if args == []:
            return None
        head = args.pop(0)
        if head not in self.explainDict:
            return False
        _explain = self.explainDict[head]
        cmd = _explain.translate(args,env)
        self._explain = _explain
        self._env = env
        self.cmdList.append(command)
        return cmd

    def readout(self,lines):
        if self._explain == None or self._env == None:
            raise Exception('no status')
        out = self._explain.readout(lines)
        return out

proxyer = commandProxy(explainList)