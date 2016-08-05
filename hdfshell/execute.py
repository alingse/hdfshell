#coding=utf-8
#author@alingse
#2016.08.01

from __future__ import print_function
import subprocess
from subprocess import PIPE


class executeCmd(object):

    """ 用来执行 shell cmd"""

    def __init__(self, executable='bash',shell=True):
        self.executable = executable
        self.shell = shell
        self.child = None

    def runcmd(self,command):
        p = subprocess.Popen(command,
                    stdout=PIPE,
                    stderr=PIPE,
                    executable=self.executable,
                    shell=self.shell,
                    universal_newlines=True)

        self.child = p

    def read(self):
        if self.child == None:
            return False,False
        outdata,errdata = self.child.communicate()
        return outdata,errdata
    
    def readline(self):
        while self.child.poll() == None:
            out = self.child.stdout.readline()
            yield out

if __name__ == '__main__':
    exe = executeCmd()
    exe.runcmd('ls -lh')
    out,_ = exe.read()
    print(out)
    exe.runcmd('sleep 1 && df -h && sleep 3 && ls -lh')
    #out,_ = exe.read()
    #print(out)
    for line in exe.readline():
        print(line,end = '')