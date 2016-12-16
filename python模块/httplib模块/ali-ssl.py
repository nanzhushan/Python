#!/usr/bin/env python
#coding:utf8

import httplib
import json
import ssl
import socket

'''
https://iosprod.quncaotech.com/homepage/nearbyPlayerList.api
{"ver":"1.0","protocol_ver":1,"lng":110.16545,"lat":22.464,"cityId":6,"pageNum":0,"pageSize":50}
'''

url="iosprod.quncaotech.com"
conn = httplib.HTTPSConnection(url)
sock = socket.create_connection((conn.host, conn.port))
conn.sock = ssl.wrap_socket(sock, conn.key_file, conn.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

params = {"ver":"1.0","protocol_ver":1,"lng":110.16545,"lat":22.464,"cityId":6,"pageNum":0,"pageSize":50}
data = json.dumps(params)

conn.request("POST", '/homepage/nearbyPlayerList.api',data)

print conn.getresponse().read()