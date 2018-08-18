#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 下午9:27
# @Author  : motao
# @Site    : 
# @File    : LogOut.py
# @Software: PyCharm

import os
import logging
from datetime import datetime
import threading


class Log:
    def __init__(self):
        global log_dir, log_file, report_path
        report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "TestReport")
        pro_dir = os.path.dirname(os.path.dirname(__file__))
        log_dir = os.path.join(os.path.join(pro_dir, "TestReport"), "logout")
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file = os.path.join(log_dir, "%s.log" % (str(datetime.now().strftime("%Y%m%d%H%M%S"))))
        self.logger = logging.getLogger()  # 定义对应的程序模块名name，默认是root
        ch = logging.StreamHandler()  # 日志输出到屏幕控制台
        ch.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')  # 定义日志输出格式
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        """
               get logger
               :return:
               """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name + " - Code:" + code + " - msg:" + msg)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
