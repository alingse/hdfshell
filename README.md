# hdfshell

一个hdfs 的 shell 执行

希望达到如同操作终端文件系统那样的效果

```
hdfsh$ ls /hive
data user node info
hdfsh$ cd data
hdfsh$ ls
iteminfo.20160101 iteminfo.20160102
hdfsh$ mv iteminfo.20160101 ../
hdfsh$ ls ../
data user node info iteminfo.20160101

```
说简单讲就是 用 `ls` 替代`hadoop fs -ls` 复杂讲，还希望它有 `cd `／ `hdfssh user@passwd`之类的当前的操作。

像`bash`/`zsh` 下操作文件系统那样操作`hdfs` 文件系统


## 构想

1. 利用 pty 来做终端
2. 写命令解释器
3. 状态保持以及 `bash` `hdfsh` 的无缝切换

## 参考
  hadoop fs 命令大全  
 [稳定版](http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/FileSystemShell.html)  
 [1.04](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html#ls)
  
 
 **先实现** 1.04 吧
  
  