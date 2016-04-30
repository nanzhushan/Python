#coding:utf8
#字符串替换
import re

#方法一
cc = ("../a","../b")
dd = cc.__str__()
print dd

#方法二
strinfo = re.compile('../a')
strinfo1 = re.compile('../b')
print strinfo.sub('111',dd)
print strinfo1.sub('222',dd)