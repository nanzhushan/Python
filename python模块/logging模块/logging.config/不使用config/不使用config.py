#!/usr/bin/env python
#coding:utf8
#不使用配置文件
import logging
import logging.handlers


def log_test01():
    LOG_FILE = "./test01.log"
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=20 * 1024 * 1024, backupCount=10);  # 实例化handler
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"   #定义日志格式
    formatter = logging.Formatter(fmt);  # 实例化formatter
    handler.setFormatter(formatter);  # 为handler添加formatter

    logger = logging.getLogger('xzs');  # 获取名为xzs的logger
    logger.addHandler(handler);  # 为logger添加handler
    logger.setLevel(logging.DEBUG)

    logger.debug("Hello boy, Debug");
    logger.info("Hello boy, Info");


if __name__ == "__main__":
    log_test01()