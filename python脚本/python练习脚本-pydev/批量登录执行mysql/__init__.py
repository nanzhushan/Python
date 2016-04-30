#!/usr/bin/env python
#encoding:utf8
#ssh_concurrent.py

import multiprocessing
import sys
import os
import time
import paramiko
import db


def ssh_cmd(host,port,user,passwd,cmd):
    msg = "\033[;32m-----------Result:%s----------\033[0m" % host
    #32m��ʾ��ɫ
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(host,22,user,passwd,timeout=5)
        stdin,stdout,stderr = s.exec_command(cmd)

        cmd_result = stdout.read(),stderr.read()
        print msg
        for line in cmd_result:
                print line,

        s.close()
    except paramiko.AuthenticationException:
        print msg
        print 'AuthenticationException Failed'
    except paramiko.BadHostKeyException:
        print msg
        print "Bad host key"

result = []
p = multiprocessing.Pool(processes=50)
cmd=raw_input('CMD:')
#cmd=sys.argv[1]
for IP in db.rows:
    host=IP[1]
    port=int(IP[2])
    user=IP[3]
    passwd=IP[4]
    result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd)))

p.close()


for res in result:
    res.get(timeout=35)
