# coding:utf8
# 操作mongodb
import pymongo
from pymongo import MongoClient
client = MongoClient('192.168.2.101', 27017)

# print client

db = client.test   # 链接test库
new_posts = {
    "id": "1",
    "author": "Knight"
}

posts = db. posts
posts.insert(new_posts)   # 把new_posts数据插入posts聚合(表)中

print db.collection_names()   # 查询所有聚合名称
print db.posts.find()  # 查询posts中所有内容
for i in db.posts.find():
    print i

# db.posts.remove()  # 删除posts聚合(表)中所有数据
db.posts.remove({'id': 1})  # 删除posts聚合(表)中id为1的数据





