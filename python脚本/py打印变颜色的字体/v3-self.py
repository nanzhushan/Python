#!/usr/bin/env python
#coding:utf8

class Logger:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'


    def __init__(self,name):
        self.name = name

    def log_normal(self):
        print (Logger.okblue + self.name + Logger.endc)

    def log_high(self):
        print (Logger.okgreen + self.name + Logger.endc)

    def log_fail(self):
        print (Logger.fail + self.name + Logger.endc)

p = Logger("不同的颜色")
p.log_normal()
p.log_fail()
p.log_high()