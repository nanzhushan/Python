#coding:utf8
import  MySQLdb

#查询操作

db = MySQLdb.connect("localhost","root","root","blog" )
## 使用cursor()方法获取操作游标 
cursor = db.cursor()
sql = "select * from student"
#执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
for i in results:
    print i



