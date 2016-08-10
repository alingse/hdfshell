#coding=utf-8
#author@alingse
#2016.08.01
from __future__ import print_function

from subprocess import PIPE
import subprocess

def initRunEnv(executable='bash',shell=True,cwd=None):
    def runbox(command):
        child = subprocess.Popen(command,
                    stdout=PIPE,
                    stderr=PIPE,
                    executable=executable,
                    shell=shell,
                    universal_newlines=True)

        return child

    return runbox

def readline(child):
    while child.poll() == None:
        out = child.stdout.readline()
        yield out


if __name__ == '__main__':
    import os
    cwd = os.path.dirname(__file__)
    runbox = initRunEnv(cwd = cwd)

    child = runbox('ls -lh')
    print(child.communicate()[0])

    child = runbox('df -h && sleep 1 && ls -lh && sleep 1 && df -h')
    for line in readline(child):
        print(line,end = '')