#coding:utf-8
'''
raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）

input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回
'''
str = raw_input("请输入:")
print str


#输入 [x*5 for x in range(2,10,2)]
str1 = input("请输入:")
print "你输入的内容是",str1

