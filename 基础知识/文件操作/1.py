#coding:utf8
#读文件的另一种写法
import re
with open('c:\\d.txt') as f:
        t=f.read()

print t

# a = []
# for i in re.split(r'\n\n\n#*#\n',t):
#         a.append(i.split('\n'))
# print a