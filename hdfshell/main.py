#coding=utf-8
#author@aingse
#2016.08.09

from __future__ import print_function

from cluster import hdfsCluster
from execute import initRunEnv
from execute import readline,readerr,readall

from explain import explainList
from proxy import commandProxy

from sys import stdout,stderr



def hdfsh():

    runbox = initRunEnv(debug=True)
    
    env = {}
    env['cluster'] = hdfsCluster('hadoop70')

    proxyer = commandProxy(explainList,env)

    while True:
        command = raw_input('box-sh$')
        
        status,cmd = proxyer.translate(command)
        if status == None:
            continue

        if status == False:
            _err = cmd
            print(_err)
            continue

        if status == 'EXIT':
            n = int(cmd)
            exit(n)

        child = runbox(cmd)
        if proxyer.explainer.lineable :
            for line in readline(child):
                print(line,end = '')
            if child.poll() != 0:
                err = readerr(child)
                stderr.write(err)
        else:
            out,err = readall(child)
            stdout.write(out)
            stderr.write(err)

if __name__ == '__main__':
    hdfsh()
