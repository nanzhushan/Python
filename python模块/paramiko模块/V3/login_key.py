#!/usr/bin/python
#coding:utf8
#采用ssh key的方式登录
import paramiko
hostname='192.168.2.101'
port=22
username='root'
pkey='/root/.ssh/id_rsa'

key=paramiko.RSAKey.from_private_key_file(pkey)
s=paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr=s.exec_command('hostname')
  
print stdout.read()