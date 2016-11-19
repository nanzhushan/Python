#coding:utf8
import re
a = 'this'
text = 'Dos this text match the pattern?'
cc = re.search(a,text)
# print cc
print "文件索引开始位置",cc.start()
print "文件索引结束位置",cc.end()
print "打印出匹配的文本d",text[cc.start():cc.end()]
