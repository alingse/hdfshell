#coding=utf-8
#author@aingse
#2016.08.09

from __future__ import print_function

from cluster import hdfsCluster
from execute import initRunEnv
from execute import readline
from proxy import proxyer

env = {}

def hdfsh():

    runbox = initRunEnv()
    env = {}
    env['cluster'] = hdfsCluster()

    while True:

        command = raw_input('box-sh$')
        cmd = proxyer.translate(command,env)
        if cmd == None:
            continue
        if cmd == False:
            print('this command not in ',command)
            continue

        child = runbox(cmd)
        for line in readline(child):
            print(line,end = '')
        print(child.poll())

if __name__ == '__main__':
    hdfsh()
