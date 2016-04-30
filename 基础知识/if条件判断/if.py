#coding:utf8
danger = ('rm', 'reboot', 'init ', 'shutdown')
arg = 'rm'
argcheck = arg not in danger

# print "这是测试arg命令",argcheck

host = ('11','33','44','78')
tgt = '33'
tgtcheck = tgt  in host

# print "这是测试tgt,在host列表:",tgtcheck        #在host列表


if argcheck and tgtcheck:     ##如果两个check都为真，就执行语句。
    print "执行语句，不是危险命令，主机也存在"

elif not tgtcheck:   ##不在host里为真
    print "tgtcheck取反为真，也就是主机不在host列表里"

elif not  argcheck:
    print "这是危险命令"


#使用if 多条件判断
##使用 and语句

# if argcheck=='False' and tgtcheck=='False':
#     print "两个条件同时成立"
# elif not argcheck:
#     print "aaa"
# elif not tgtcheck:
#     print "ttt"
# else:
#     pass
###########################

#
# if argcheck:
#     print "arg 为真"
# elif tgtcheck:
#     print "tgt 为真"
# else:
#     print "都不是真"

##使用条件语句的取反
# if not argcheck:
#     print "not arg的值为真"
# elif not tgtcheck:
#     print "not tgt 的值为真"
# else:
#     print "not两个都不是真，也就是两个都是真"







# a = 5
# b = [1, 2, 3]
# if a not in b:
#     print "hello"

