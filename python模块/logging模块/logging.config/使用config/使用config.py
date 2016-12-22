#!/usr/bin/env python
#coding:utf8
import logging
import logging.config



def log_test02():
    CONF_LOG = "./logging.conf"
    logging.config.fileConfig(CONF_LOG);  # 采用配置文件
    logger = logging.getLogger("xzs")
    logger.debug("Hello xzs")          #设置debug的日志输出

    logger = logging.getLogger()
    logger.info("Hello root")        #设置info的日志输出


if __name__ == "__main__":
    log_test02()