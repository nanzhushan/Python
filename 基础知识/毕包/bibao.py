#coding:utf8
#函数里再套函数

"""
func是一个函数，里面又嵌套了一个函数func2，外部函数传过来的a参数，这个变量会绑定到函数func2。
func函数以内层函数func2作为返回值，然后把func函数存储到f变量中。
当外层函数调用内层函数时，内层函数才会执行（func()()），就创建了一个闭包。

"""
def fun(a):
	def fun2(b):
		return a* b
	return fun2

f= fun(2)  #函数赋值给变量   

print f(5)
