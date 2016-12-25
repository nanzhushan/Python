def myfun(name):
	'函数定义过程中的name是形参'
	# print('传递进来的' + name + '这是实参，因为是具体的参数值')
	return name 

print(myfun('knight'))

#打印函数文档
myfun.__doc__
help(myfun)
