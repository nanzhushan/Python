#coding:utf8
# 匹配符合条件的行 并输出，这个使用search方法。如果只是想找出特殊关键条件用findall

import re
f = open("c:\\d.txt",'r')
for i in f.readlines():
    m = re.search(r'^555.*',i)
    if m:
        print m.group()
f.close()