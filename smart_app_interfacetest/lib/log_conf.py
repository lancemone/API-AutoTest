#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 下午9:10
# @Author  : motao
# @Site    : 
# @File    : log_conf.py
# @Software: PyCharm

import os
import logging
from datetime import datetime

report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "TestReport")
pro_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(os.path.join(pro_dir, "TestReport"), "logout")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, "%s.log" % (str(datetime.now().strftime("%Y%m%d%H%M%S"))))
logger = logging.getLogger("AutoTest")
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')  # 定义日志输出格式
ch = logging.StreamHandler()  # 日志输出到屏幕控制台
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
fh = logging.FileHandler(log_file)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

logger.info(" start logging")
logger.info(" start print log")


def case_start(case_name):
    '''

    :param case_name:
    :return:
    '''
    logger.info("%s start test" % case_name)


def case_end(case_name):
    '''

    :param case_name:
    :return:
    '''
    logger.info("%s test end" % case_name)
