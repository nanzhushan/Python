#coding:utf-8
#python 对象编码成json对象
import demjson
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
b = ['fd','ffdsaf','fdsafd']
print type(data)        #list
print len(data)
print len(b)

json = demjson.encode(data)
print type(json)            #unicode
print json