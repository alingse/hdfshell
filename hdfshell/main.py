#coding=utf-8
#author@aingse
#2016.08.09

from __future__ import print_function

from cluster import hdfsCluster
from execute import initRunEnv
from execute import readline,readerr,readall

from explain import explainList
from proxy import commandProxy



def hdfsh():

    runbox = initRunEnv()
    
    env = {}
    env['cluster'] = hdfsCluster('hadoop70')
    
    proxyer = commandProxy(explainList,env)

    while True:
        command = raw_input('box-sh$')
        
        cmd = proxyer.translate(command,env)

        if cmd == None:
            continue

        if cmd == False:
            print('this command not in ',command)
            continue

        child = runbox(cmd)
        if proxyer.explainer.lineable :
            for line in readline(child):
                print(line,end = '')
            if child.poll() != 0:
                err = readerr(child)
                sys.stderr.write(err)
        else:
            out,err = readall(child)
            sys.stdout.write(out)
            sys.stderr.write(err)

if __name__ == '__main__':
    hdfsh()
