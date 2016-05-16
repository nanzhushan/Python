#coding:utf8
import MySQLdb
#查询操作

db = MySQLdb.connect("localhost","root","root","qxian3" )
## 使用cursor()方法获取操作游标
cursor = db.cursor()

ddd = 2
# print type(ddd)

sql = "SELECT * from auth_user_groups where user_id =%s" %(ddd)
#执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()   ##是个元组
r1 = results[0]
group_id = r1[2]
print group_id



