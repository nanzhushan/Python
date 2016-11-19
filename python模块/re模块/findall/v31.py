#coding:utf8
import re

#正则匹配
r1 = re.compile('\d+')
print re.findall(r1,"hello[hi]heldf67sdsf[iwonder]lo")
print re.findall('(?<=www)',"afdsfwwwfkdjfsdfsdwww")

