#coding:utf8
'''

记得以前个网友提问怎么去除海量列表里重复元素，
用hash来解决也行，只不过感觉在性能上不是很高，
用set 可以完美解决

'''

a = [11,22,33,44,11,22]
b = set(a)    #集合是一个无重复无序的元素集

print b

c = [i for i in b]

print type(c)
print c