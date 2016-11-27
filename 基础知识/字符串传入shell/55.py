#!/usr/bin/python
#coding:utf8
import sys,os
import shutil
import time

time = time.strftime("%Y%m%d-%H%M")
s1 = '/root/tt'
s2 = 'tt'
x = 'tt'
d1 = '/server'

#shutil.copytree('s%','/server/tt_%s' %(s1,time))

#os.system('cp -r s% /server' %s1)

os.system('cp -r  %s %s_%s_a' %(s1,x,time))
