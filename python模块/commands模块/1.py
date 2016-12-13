#!/usr/bin/python
#coding:utf-8
import json
import commands

(status, output) = commands.getstatusoutput('date')
print status
print output
print type(output)

