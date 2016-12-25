def odd(x):
	return x % 2

temp = range(10)
show = filter(odd,temp)
#过滤出等于0的
print(list(show))