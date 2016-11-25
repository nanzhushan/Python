#!/usr/bin/python
#coding:utf8
import time
import os
import subprocess

i = 0
count = 0

while (i < 6):
    i += 1
    #res = subprocess.Popen("ps -ef | grep /sbin/sshd|grep -v grep",stdout=subprocess.PIPE,shell=True) 
    res = subprocess.Popen("ps -ef | grep /sbin/sshdcc|grep -v grep",stdout=subprocess.PIPE,shell=True) 
    cc=res.stdout.readlines()
    count=len(cc)
    if (count < 1):
        time.sleep(2)
        continue
    break

if (count < 1):
    print "重启进程...."

print "最后的进程值为:",count
