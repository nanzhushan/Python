#coding:utf-8
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.92",22,"root", "root")
stdin, stdout, stderr = ssh.exec_command("hostname")
print stdout.readlines()
ssh.close()