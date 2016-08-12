#coding=utf-8
#author@alingse
#2016.08.08

from cluster import hdfs_schema,file_schema
import argparse



class commandExplain(object):
    """docstring for command"""
    def __init__(self, name, parser, lineable=False):
        self.name = name
        self.parser = parser
        self.lineable = lineable

    @property
    def head(self):
        return 'hadoop fs -{} '.format(self.name)


    def isVaild(self,args):
        pass
        #args = self.parser.parse_args(args)
        #return args

    
    
class LS(commandExplain):
    """ docstring for ls """
    def __init__(self):
        name = 'ls'
        parser = argparse.ArgumentParser()
        parser.add_argument('paths', nargs='*', help='hdfs path')        
        super(LS, self).__init__(name,parser,lineable=True)

    def translate(self,args,env):
        cluster = env['cluster']
        uri = cluster.uri
        uri_head = cluster.uri_head

        _args = self.parser.parse_args(args)

        paths = []
        for path in _args.paths:
            if path.startswith('/'):
                paths.append(uri_head+path)
            elif path.startswith(hdfs_schema):
                paths.append(path)
            elif path.startswith(file_schema):
                paths.append(path)
            else:
                paths.append(uri+path)
        if paths == []:
            paths.append(uri)

        quote = lambda p:"'{}'".format(p)
        paths = map(quote,paths)
        cmd = self.head + ' '.join(paths)
        return True,cmd

    def tranline(self,line):
        pass

    def tranout(self,out):
        pass

    def tranerr(self,err):
        pass


class Enter(commandExplain):
    """docstring for Enter"""
    def __init__(self):
        name = ''
        parser = argparse.ArgumentParser()
        super(Enter, self).__init__(name,parser)

    def translate(self,args,env):
        pass

    def tranline(self,line):
        pass

    def tranout(self,out):
        pass

    def tranerr(self,err):
        pass

        
class EXIT(commandExplain):
    """ docstring for exit """
    def __init__(self):
        name = 'exit'
        parser = argparse.ArgumentParser()
        parser.add_argument('status',nargs='?',default=0,type=int,help='status must be int')
        super(EXIT, self).__init__(name,parser)

    def translate(self,args,env):
        try:
            _args = self.parser.parse_args(args)
        except Exception as e:
            return False,str(e).split('\n')[-1]
        #for exit
        return 'EXIT',_args.status

    def tranline(self,line):
        pass

    def tranout(self,out):
        pass

    def tranerr(self,err):
        pass


ls = LS()
exit = EXIT()
enter = Enter()

explainList = []
explainList.append(ls)
explainList.append(exit)
explainList.append(enter)
