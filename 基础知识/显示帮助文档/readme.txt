1、dir函数式可以查看对象的属性，使用方法很简单，举str类型为例，在Python命令窗口输入 dir(str) 即可查看str的属性，

2、如何查看对象某个属性的帮助文档 ？如要查看str的split属性，可以用__doc__， 使用方法为print(str.split.__doc__)，

3、查看对象的某个属性还可以用help函数，使用方法为help(str.split)


总结：万一我们不记得这个函数或者基础的用户可以使用如下:

print max.__doc__

print help(max)