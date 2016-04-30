#!/usr/bin/python
#coding=utf-8

import paramiko 
hostname='192.168.2.91'
username='root'
password='root'

client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect(hostname=hostname,username=username, password=password, timeout=4) 
stdin, stdout, stderr = client.exec_command('date') 

#for std in stdout.readlines(): 
#   print std, 
print stdout.read()
client.close() 