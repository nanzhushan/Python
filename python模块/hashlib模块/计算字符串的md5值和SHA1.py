#!/usr/bin/env python
#coding:utf8

import hashlib
cc = hashlib.md5()
cc.update('how to use md5 in py hashlib?')

print "字符串的md5值是:",cc.hexdigest()

dd = hashlib.sha1()
dd.update('how to use sha1 in py hashlib?')
print "字符串的sha1值：" + dd.hexdigest()