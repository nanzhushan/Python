#!/usr/bin/env python
#coding:utf8
__author__ = "knight"

import hashlib
import sys

'''
设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

name    | password
--------+----------
michael | 123456
bob     | abc999
alice   | alice2008
'''

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'rose': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    cc = hashlib.md5()
    cc.update(password)
    if user  in db.keys() and cc.hexdigest() in db.values():
        return u"用户名和密码都匹配"
    elif user in db.keys() and cc.hexdigest() not in db.values():
        return u"用户存在，但是密码不匹配"

    else:
        return u"用户不存在"

print login(sys.argv[1],sys.argv[2])