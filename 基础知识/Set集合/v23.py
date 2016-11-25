#coding:utf8
#创建集合
s = set([3,5,8,10])
t = set("hello")

#添加一项
t.add('x')
print t

#在s中添加多项
s.update([10,37,88])

print s,len(s)

#删除一项
t.remove('h')
print t
