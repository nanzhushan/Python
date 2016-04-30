#coding:utf-8
#print __name__  # 输出__main__

#其次看name属性的常用方法
#__name__属性是系统自定义的
#一个等号是赋值，两个等号是等号

if __name__ == "__main__":   #如果__name__属性的值是main的话，代表它是主模块(主模块没有被其他模块调用)
    print "it is main "
else:
    print "it is not main"

##采用导入方式
import lname





#如果要自己写模块也就是自定义模块的话，写好之后直接放在lib目录下即可