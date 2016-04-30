#coding:utf-8
#eclipse的运行快键键，用ctrl+F11,eclips上面有一排的快捷图标，自己点一点看罗
#Counter作为一个容器,可以跟踪相同的值增加了多少次。
import collections
x = ['a','b','c','b','b','a']
print collections.Counter(x)

#如果不提供任何参数，可以构造一个空的Counter，然后通过update（）方法填充 。
c = collections.Counter()
print 'first:',c
c.update('aaabbbc')
print 'second:',c
#访问计数，一旦填充了Counter,可以使用字典API获取它的值
d = collections.Counter('abcdaab')
print d['a']    #a出现的次数

#for i in 'abced':      #遍历元素出现的次数
#    print i+" :",d[i]  #字符串连接

###算数操作,Counter实例支持算术和集合操作来完成结果的聚集
c1 = collections.Counter(['a','a','b','c','a','c'])
c2 = collections.Counter('altpbet')
#print "这是c1的打印结果：",c1
#print "c1中a的出现次数:",c1['a']
d12 = c1 + c2
print "c1+c2的结果：",d12
print "聚集中的a的个数：",d12['a']

##减法操作
d13 = c1 - c2
print "聚集减法中的a的个数：",d13['a']

