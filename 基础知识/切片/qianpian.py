#coding:utf8
b= [1,2,3,4,5,6,7,8]

#切片
print b[0::2]   #从索引0开始，每两个取一个 也可以省略0
print b[1::2]   #从索引1开始，每两个取一个
print b[:4:2]    #前四个，每两个取一个
print "取前三个元素",b[0:3]      #其中0可以省略

print b[2:4]      #索引2到4之间的元素
print len(b)       #列表长度

print "倒数第一个元素是:",b[-1]
print "倒数第二个元素是:",b[-2]



#print b
# c = zip(b[::2], b[1::2])
# d = []
# for i in c:
#     d.append(list(i))
# print d

