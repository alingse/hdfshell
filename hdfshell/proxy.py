#coding=utf-8
#author@alingse
#2016.07.20


import shlex

class commandProxy(object):

    def __init__(self,explains,env):
        self.explainDict = {}
        for _explain in explains:
            self.explainDict[_explain.name] = _explain
        self.env = env
        #run time
        self.explainer = None
        #h
        self.cmdList = []

    def translate(self,command):
        args = shlex.split(command)
        head = ''
        if args != []:
            head = args.pop(0)

        if head not in self.explainDict:
            return False,'this command not in '+ head

        _explain = self.explainDict[head]
        status,cmd = _explain.translate(args,self.env)
        if status != False:
            self.explainer = _explain
            self.cmdList.append(command)
        return status,cmd

    def readout(self,lines):
        if self._explain == None or self._env == None:
            raise Exception('no status')
        out = self._explain.readout(lines)
        return out
