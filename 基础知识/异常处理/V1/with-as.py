#coding:utf-8
#下面两个语句等价，语法是不是简洁多了

with open('d:\\1.txt','r') as f:   ##第一语句
    print f
    
try:                                   #第二语句        
    f1 = open('d"\\1.txt','r')
except:
    pass
else:
    print "hello"
finally:
    f.close()
    