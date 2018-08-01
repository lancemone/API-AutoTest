#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午2:24
# @Author  : motao
# @Site    : 
# @File    : run_allcases.py
# @Software: PyCharm

# 通过discover生成测试用例集合，调用报告，发送邮件
import time
import os
from smart_app_interfacetest.lib.HTMLTestRunner import HTMLTestRunner
import unittest

# 指定测试用例的目录
test_suite_dir = './app_test_cases'

# 指定用例结果报告目录
report_dir = '/Users/taomo/PycharmProjects/AutoTest/smart_app_interfacetest/TestReport'


def creat_suite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找目录
    test_dir = test_suite_dir
    # 定义discover方法参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # discover方法筛选出来的用例，添加的测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
        return testunit


alltestnames = creat_suite()

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # os.chdir(report_dir)
    filename = report_dir + '/report_' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Smart Interface Test Report',
                            description='接口测试执行结果 ', verbosity=1)
    runner.run(alltestnames)
    fp.close()
