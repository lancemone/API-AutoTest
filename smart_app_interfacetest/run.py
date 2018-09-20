#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 上午10:34
# @Author  : motao
# @Site    : 
# @File    : run.py
# @Software: PyCharm


import os
import unittest
import time
from smart_app_interfacetest.lib.HTMLTestRunner import HTMLTestRunner
from smart_app_interfacetest.lib import SendEmail
from smart_app_interfacetest.config import read_conf
from smart_app_interfacetest.lib import api_module
from smart_app_interfacetest.lib import log_conf

logger = log_conf.logger


class Run:
    def __init__(self):
        global report_dir, test_dir
        # 指定用例结果报告目录
        report_dir = os.path.join(os.path.join(os.path.dirname(__file__), "TestReport"), "HtmlReport")
        # 指定测试用例的目录
        test_dir = os.path.join(os.path.join(os.path.dirname(__file__)), 'app_test_cases')
        self.conf = read_conf.Read_conf()
        self.api = api_module.Api_module()
        self.on_off = self.conf.get_email("on_off")
        self.caseList = []
        self.header = self.api.set_header()
        self.username = self.conf.get_params(name="username")
        self.password = self.conf.get_params(name="password")

    def set_caselist(self):
        '''
        set_caselist
        :return:
        '''
        listpath = os.path.join(os.path.join(os.path.dirname(__file__), "config"), "caselist.txt")
        fb = open(listpath, "r")
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
            fb.close()

    def set_suite(self):
        '''
        set_suite
        :return:
        '''
        self.set_caselist()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case
            discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern=case_name, top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTests(test_name)
                    logger.info(test_suite)
                    return test_suite
        else:
            return None

    # 配置token
    def set_asscess_token(self):
        '''
        set_asscess_token
        :return:
        '''
        path1 = "/api/basic/json-rpc/views"
        path2 = "/oauth/v1/sign_in"
        path3 = "/oauth/v1/token"
        url1 = self.api.set_url(path1)
        url2 = self.api.set_url(path2)
        url3 = self.api.set_url(path3)
        data1 = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "common_getTenantByUsername",
            "params": ["%s" % self.username]
        }
        r1 = self.api.https_json_post(url=url1, header=self.header, data=data1, value_name="json")
        result1 = r1.get("result")
        tenantid = result1[0].get("tenantId")
        self.conf.set_value(v_type="PARAMS", name="tenant_id", value=tenantid)
        data2 = {
            "provider": "password",
            "tenant_id": tenantid,
            "username": self.username,
            "password": self.password
        }
        self.header["content-type"] = "application/x-www-form-urlencoded"
        re_header = self.api.https_post(url=url2, header=self.header, data=data2, value_name="header")
        user_token = re_header.get("X-User-Token")
        self.conf.set_header(name="x-user-token", value=user_token)
        data3 = {
            "grant_type": "user_token",
            "client_id": self.conf.get_params("fmp_client_id"),
            "user_token": user_token,
        }
        response = self.api.https_post(url=url3, header=self.header, data=data3, value_name="json")
        token_type = response["token_type"]
        access_token = response["access_token"]
        print(access_token)
        self.conf.set_header(name="fmp_authorization", value=token_type + ' ' + access_token)

    # 创建测试报告
    def run(self):
        '''

        run test
        :return:
        '''
        try:
            suite = self.set_suite()
            if suite is not None:
                logger.info("<<<<<<<<<<<<<<<TEST START>>>>>>>>>>>>>>>")
                now = time.strftime("%Y-%m-%d %H:%M:%S")
                os.chdir(report_dir)
                filename = report_dir + '/report-' + now + '-result.html'
                fp = open(filename, 'wb')
                runner = HTMLTestRunner(stream=fp, title=u'Smart Interface Test Report',
                                        description=u'接口测试执行结果 ', verbosity=1)
                runner.run(suite)
                fp.close()
            else:
                logger.info("Have no case to test")
        except Exception as ex:
            logger.error(ex)
        finally:
            logger.info("<<<<<<<<<<<<<<<TEST END>>>>>>>>>>>>>>>")
            # send test report by email
            if self.on_off == 'on':
                file_new = SendEmail.new_report(report_dir)
                SendEmail.send_file(file_new)
                logger.info(">>>>>>Send E-mail Successful")
            elif self.on_off == 'off':
                logger.info(">>>>>>Doesn't send report email to developer")


if __name__ == '__main__':
    obj = Run()
    obj.set_asscess_token()
    obj.run()
