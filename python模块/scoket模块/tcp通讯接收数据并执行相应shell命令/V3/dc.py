#coding:utf8
from socket import *
from time import ctime

raw_input

bufsize = 1024
host = '192.168.2.101'
port = 3456
addr = (host,port)

client_sock = socket(AF_INET,SOCK_STREAM)
client_sock.connect(addr)

while True:
    data = raw_input("发送---->")
    if not data:
        break
    else:
        client_sock.send(data)
        data = client_sock.recv(bufsize)
        print '收到---->%s\n%s' %(ctime(),data)

client_sock.close()
