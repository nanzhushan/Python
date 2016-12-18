#coding:utf-8
#下面两个语句等价，语法是不是简洁多了
#使用with ....as...  极大的简化了每次写finally的工作,使代码更加优雅

with open('d:\\1.txt','r') as f:   ##第一语句   #该语句 在处理完了之后会自动 会关闭文件.
    print f


########################    
try:                                   #第二语句        
    f1 = open('d"\\1.txt','r')
except:
    pass
else:
    print "没有文件，也就没有不需要关闭"
finally:
    f.close()    #有文件才能进行关闭
    