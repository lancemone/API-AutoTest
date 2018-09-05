#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 下午8:31
# @Author  : motao
# @Site    : 
# @File    : test_app_login.py
# @Software: PyCharm

import unittest
import sys
import time
from smart_app_interfacetest.config import read_conf
from smart_app_interfacetest.lib import api_module
from smart_app_interfacetest.lib.LogOut import MyLog


class Test_App_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        MyLog.get_log().get_logger().info(">>>>>>>>>>Test_App_Login Start<<<<<<<<<<")

    @classmethod
    def tearDownClass(cls):
        MyLog.get_log().get_logger().info(">>>>>>>>>>Test_App_Login End<<<<<<<<<<")

    def setUp(self):
        '''

        :return:
        '''
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.api = api_module.Api_module()
        self.conf = read_conf.Read_conf()
        self.logger.info("%s start run" % sys._getframe().f_code.co_name)
        self.tenantid = self.conf.get_params(name="tenant_id")
        self.header = self.api.set_header()
        self.username = self.conf.get_params(name="username")
        self.password = self.conf.get_params(name="password")

    def tearDown(self):
        # time.sleep(1)
        self.logger.info("test end")

    def test_01_tenantid(self):
        '''

        :return:
        '''
        path = "/api/basic/json-rpc/views"
        url = self.api.set_url(path)
        data = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "common_getTenantByUsername",
            "params": ["%s" % self.username]
        }
        code = self.api.https_json_post(url=url, header=self.header, data=data, value_name="status_code")
        response = self.api.https_json_post(url=url, header=self.header, data=data, value_name="json")
        result = response.get("result")
        re_id = response["id"]
        tenantid = result[0].get("tenantId")
        self.assertEqual(code, 200, msg="返回状态码为%s" % code)
        self.assertEqual(re_id, 1)
        self.assertIsNotNone(result)
        self.conf.set_value(v_type="PARAMS", name="tenant_id", value=tenantid)

    def test_02_get_usertoken(self):
        '''

        :return:
        '''
        path = "/oauth/v1/sign_in"
        url = self.api.set_url(path)
        header = self.header
        header["content-type"] = "application/x-www-form-urlencoded"
        data = {
            "provider": "password",
            "tenant_id": self.tenantid,
            "username": self.username,
            "password": self.password
        }
        code = self.api.https_post(url=url, header=self.header, data=data, value_name="status_code")
        re_header = self.api.https_post(url=url, header=self.header, data=data, value_name="header")
        user_token = re_header.get("X-User-Token")
        self.conf.set_header(name="x-user-token", value=user_token)
        self.assertEqual(code, 200)
        self.assertIn("Set-Cookie", re_header)

    def test_03_get_accesstoken(self):
        '''

        :return:
        '''
        self.logger.info("%s start run" % sys._getframe().f_code.co_name)
        path = "/oauth/v1/token"
        url = self.api.set_url(path)
        data = {
            "grant_type": "user_token",
            "client_id": self.conf.get_params("fmp_client_id"),
            "user_token": self.conf.get_header("x-user-token"),
        }
        print(self.conf.get_header("x-user-token"))
        code = self.api.https_post(url=url, header=self.header, data=data, value_name="status_code")
        response = self.api.https_post(url=url, header=self.header, data=data, value_name="json")
        print(response)
        token_type = response["token_type"]
        access_token = response["access_token"]
        self.assertEqual(code, 200)
        self.assertIsNotNone(response)
        self.assertIn("expires_in", response)
        self.conf.set_header(name="fmp_authorization", value=token_type + ' ' + access_token)


if __name__ == '__main__':
    unittest.main()
