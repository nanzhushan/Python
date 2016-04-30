#coding:utf8
import base64

ys = "abc123"

s1 = base64.encodestring(ys)
s2 = base64.decodestring(s1)
print s1
print s2


