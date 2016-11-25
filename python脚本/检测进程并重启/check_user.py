#!/usr/bin/python
#coding:utf8
import time
import os
import subprocess

i = 0
count = 0

while (i < 6):
    i += 1
    res = subprocess.Popen("ps -ef | grep user-pre.jar|grep -v grep",stdout=subprocess.PIPE,shell=True) 
    cc=res.stdout.readlines()
    count=len(cc)
    if (count < 1):
        time.sleep(2)
        continue
    break

if (count < 1):
    print "重启进程...."
    os.system('cd /opt/user/ && /bin/bash user-run.sh')

print "最后的进程数值为:",count
