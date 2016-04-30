#encoding=utf-8
import MySQLdb
import sys

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='',port=3306)    # 定义连接
#conn=MySQLdb.connect(unix_socket='/var/run/mysqld/mysqld.sock',user='root',passwd='123456')   # 使用socket文件链接
cur=conn.cursor()                                            # 定义游标
conn.select_db('test')                                  	 # 选择数据库
sqlcmd = cur.execute('select * from HOST;')          				 # 定义sql命令
rows=cur.fetchall()         # 接收全部返回结果
