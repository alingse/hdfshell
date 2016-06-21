#coding=utf-8
#author@shibin
#2016.06.21

class hdfsCluster:
    """ 一个hdfs 资源
        a hdfs uri

    """
    def __init__(self,host,port):
        """ 目前只需要host和port"""
        self.host = host
        self.port = port

    @property
    def uri_head(self):
        """ 返回 uri 的 head"""
        uri_head = 'hdfs://{}:{}'.format(self.host,self.port)
        return uri_head

