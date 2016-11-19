#coding:utf8
import re
text = 'aaabbccc'
patter = 'ab'
for a in re.findall(patter,text):
    print a

print re.findall(patter,text)