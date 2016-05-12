#coding:utf8
import redis

rc = redis.Redis(host='192.168.2.101',port=6379)

ps = rc.pubsub()

ps.subscribe(['foo', 'bar'])  #订阅两个频道

rc.publish('foo', 'hello worlduuu')