#coding:utf-8
#set中的元素无次序，不可重复。

s2 = set([123,"google","face","book","facebook","book"])
#print s2[1]  ##报错set也就是集合中无序列
print s2
#增加一个元素
s2.add("knight")
print s2

#print help(set.add)

for i in s2:
    print i
    
    
