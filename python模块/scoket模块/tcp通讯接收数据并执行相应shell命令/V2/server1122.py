#coding:utf8
import socket
from time import ctime
import sys
import os


bufsize = 1024
host = '127.0.0.1'
port = 8100
address = (host,port)

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen(1)

while True:
    print 'waiting for connection...'
    clientsock,addr = server_sock.accept()
    print 'received from :',addr

    while True:
        data = clientsock.recv(bufsize)
        print ' 收到客户端传过来的数据,并将传过来的数据执行相应命令---->%s' %(data)
        if data == "update":
            f = open(data,'w')
        else:
            print "请重新输入.."
        # f = open(data, 'w')
        clientsock.send(data)
    clientsock.close()

server_sock.close()