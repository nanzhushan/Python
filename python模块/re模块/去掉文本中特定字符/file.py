#coding:utf8
import re
f = open('d:\\file')
for line in f.readlines():
  print  re.sub("\| \d+ 行","",line)
