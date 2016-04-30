#!/usr/bin/python2
# coding: utf-8

STR = 'Used        :39728      Free      :11503'


def str2dict(s):
    i = iter(s.split())
    return dict((k, v.lstrip(':')) for k, v in zip(i, i))


DIC = str2dict(STR)
print DIC

# {'Used': '39728', 'Free': '11503'}