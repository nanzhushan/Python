#收集参数

def test(*par):
	print('参数的长度是：',len(par));
	print('第二个参数是：',par[1]);

test(1,'knight',3.14,8,9)


def test2(*par,exp):
	print('参数的长度是：',len(par));
	print('第二个参数是：',par[1]);


test2(1,'haha',5,8,9)    #这样会报错，因为没有指定关键字参数
test2(1,'haha',5,8,exp='9')


