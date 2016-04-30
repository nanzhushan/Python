#coding:utf-8

fp=open('d:\\dd.txt','r')
arr=[]
for lines in fp.readlines():
    #print lines
    arr.append(lines)
fp.close()

print '列表的第一个元素是,',arr[0] + "列表的第二个元素是,",arr[1]
