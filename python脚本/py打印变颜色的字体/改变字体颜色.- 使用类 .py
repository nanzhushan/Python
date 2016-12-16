#!/usr/bin/env python
#coding:utf8


class Logger:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'

    @staticmethod
    def log_normal(info):
        print (Logger.okblue + info + Logger.endc)

    @staticmethod
    def log_high(info):
        print (Logger.okgreen + info + Logger.endc)

    @staticmethod
    def log_fail(info):
        print (Logger.fail + info + Logger.endc)



Logger.log_normal("这是正常的字体颜色")
Logger.log_fail("这是失败的字体颜色")
Logger.log_high("这是高亮的字体颜色")
