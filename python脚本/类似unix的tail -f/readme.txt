本文介绍如何使用Python动态监控程序日志的内容，这里的动态指的是日志文件不断的追加新的日志内容，动态监控是指监控日志新追加的日志内容
日志文件一般是按天产生，则通过在程序中判断文件的产生日期与当前时间，更换监控的日志文件
程序只是简单的示例一下，监控test1.log 10秒，转向监控test2.log
程序监控使用是linux的命令tail -f来动态监控新追加的日志，

Github上有一个项目，使用Python实现的类似unix系统的tail -f(Unix tail follow implementation in Python) 项目地址是：https://github.com/kasun/python-tail