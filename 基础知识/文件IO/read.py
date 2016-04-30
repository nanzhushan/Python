#coding:utf-8

# 打开一个文件
fo = open("d:\\1.txt", "r")
#str = fo.read(10);  #读取前10个单词
str = fo.read();
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()