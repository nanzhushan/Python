#默认参数
def aa(name='knight',words='让编程改变世界'):
	print(name + '->' + words)


aa()   #不加值显示，'kngiht,让编程改变世界'
aa('苍井空')  # 显示，'苍井空，让编程改变世界'
aa('苍井空','我脱光衣服躺在镜头前,是为了生存，而你衣冠楚楚站在镜头前，却只是为了私欲和欺骗')   #有参数就不会执行默认参数
