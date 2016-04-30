#coding:utf8
import socket
from time import ctime
import sys
import os


bufsize = 1024
host = ''
port = 3456
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
        print ' 收到客户端传过来的数据为---->%s' %(data)
        if data == "update":
            os.system("touch 111.txt")             #执行shell命令
        else:
            data = "请按指令正确输入"

        clientsock.send(data)               #发送结果给客户端
    clientsock.close()

server_sock.close()
