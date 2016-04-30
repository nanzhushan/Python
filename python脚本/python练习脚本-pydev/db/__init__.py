#coding=utf-8
import MySQLdb
import sys

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test',port=3306)   
cur=conn.cursor()                                          
conn.select_db('test')                                   
sqlcmd = cur.execute('show databases;')
print sqlcmd                          
rows=cur.fetchall()       
