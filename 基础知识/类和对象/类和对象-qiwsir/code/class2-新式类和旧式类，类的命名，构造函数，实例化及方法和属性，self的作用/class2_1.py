#coding:utf-8
#没有传入参数，就是用默认值

class Person:
    def __init__(self, name, lang="golang", website="gg.knight.ren"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "1093381395@qq.com"

knight = Person("Knight.Zhou")     
info = Person("xiaozhou",lang="python",website="www.github.com/knight-zhou")

print "knight.name=",knight.name
print "info.name=",info.name
print "-------"
print "knight.lang=",knight.lang
print "info.lang=",info.lang
print "-------"
print "knight.website=",knight.website
print "info.website=",info.website