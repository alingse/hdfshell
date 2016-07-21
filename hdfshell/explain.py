#coding=utf-8
#author@alingse
#2016.07.20

from cluster import hdfs_schema,file_schema

class commandExplain(object):
    """ 代理 命令 shell 命令 解释器"""
    def __init__(self,hdfs):
        self.hdfs = hdfs
        self.in_explain = False
        self._head = 'hadoop fs '

    def start(self):
        self.in_explain = True

    def ls(self,*paths):
        #do check && clean


        uri = self.hdfs.uri
        uri_head = self.hdfs.uri_head

        _paths = []
        for path in paths:
            if path.startswith(file_schema):
                _paths.append(path)
            #other hdfs
            elif path.startswith(hdfs_schema):
                _paths.append(path)
            #from /
            elif path.startswith('/'):
                _path.append(uri_head+path)
            #from relative
            else:
                _path.append(uri+path)

        command = self._head + ' -ls ' + ' '.join(_path)

        return command

    def explain(self,argv):
        pass