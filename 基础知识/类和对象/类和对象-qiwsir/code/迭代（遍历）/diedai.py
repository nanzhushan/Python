#coding:utf-8
#迭代:指的是按照某种顺序逐个访问列表中的每一项，比如for循环
#所以建议还是用for循环迭代进行遍历吧

#第一种实现方法
lst = ['a','c','d']
#for h in list:
#    print h
    

#第二种实现方法
a_iter = iter(lst)    #对原来的list实施了一个iter()

#print a_iter

#print a_iter.next()   #手工一个一个手动点击访问,可以成功,可以使用while循环遍历

while True:
    print a_iter.next()       ##报错，官方解释如下：


'''
看官还要关注iter()...next()迭代的一个特点。
当迭代对象lst_iter被迭代结束，即每个元素都读取了一遍之后，
指针就移动到了最后一个元素的后面。如果再访问，指针并没有自动返回到首位置，
而是仍然停留在末位置，所以报StopIteration，想要再开始，需要重新载入迭代对象。所以，
当我在上面重新进行迭代对象赋值之后，又可以继续了。这在for等类型的迭代工具中是没有的。
'''

    
    

    
    
