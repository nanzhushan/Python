#!/usr/bin/env python 
#coding=utf-8
#ip.txt必须按照格式写非常不方便，代码有待重写

import paramiko 
import os 
import datetime 
from ConfigParser import ConfigParser 
ConfigFile='c:\ip.txt' 

config=ConfigParser() 
config.read(ConfigFile) 

hostname1=(config.get('IP','ipaddress'))
#print hostname1
address=hostname1.split(';') 
#print address 


username='root' 
password='root' 
port=22 
#local_dir='/tmp/' 
#remote_dir='/tmp/test/' 
if __name__=="__main__": 
        for ip in address: 
                #print ip
                paramiko.util.log_to_file('c:\paramiko.log') 
                s=paramiko.SSHClient() 
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                s.connect(hostname=ip,username=username,password=password) 
                stdin,stdout,stderr=s.exec_command('date') 
                print stdout.read() 
                s.close() 