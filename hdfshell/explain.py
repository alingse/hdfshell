#coding=utf-8
#author@alingse
#2016.08.08

import argparse


class commandExplain(object):
    """docstring for command"""
    def __init__(self, name, parser):
        self.name = name
        self.parser = parser

    def isVaild(self,args):        
        args = self.parser.parse_args(args)
        return args

    
    
class LS(commandExplain):
    """ docstring for ls """
    def __init__(self):
        name = 'ls'
        ls_parser = argparse.ArgumentParser()
        ls_parser.add_argument('path', nargs='+', help='hdfs path')
        
        super(LS, self).__init__(name,ls_parser)

    def translate(self,args,env):
        cluster = env['cluster']
        paths = []
        if args == []:
            uri = cluster.uri
            paths.append(uri)

        cmd = 'hadoop fs -{} '.format(self.name)+' '.join(paths)
        return cmd



class EXIT(commandExplain):
    """ docstring for exit """
    def __init__(self):
        name = 'exit'
        exit_parser = argparse.ArgumentParser()        
        super(EXIT, self).__init__(name,exit_parser)

    def translate(self,args,env):
        pass



ls = LS()
exit = EXIT()

