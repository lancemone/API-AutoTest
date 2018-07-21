#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 下午3:42
# @Author  : motao
# @Site    : 
# @File    : test_add_device.py
# @Software: PyCharm


import re
import requests
import unittest
import json
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import config
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import http_config


class Test_Add_Devices(unittest.TestCase):
    '添加设备台账测试用例'

    def setUp(self):
        self.host = config.host_url
        self.headers_post = config.header_post
        self.headers_get = config.header_get
        self.fmp_client_id = config.fmp_client_id
        self.username = config.username
        self.password = config.password
        self.tenant_id = config.tenant_id

    def test_login_portal(self):
        path = "oauth/v1/sign_in"
        data = {
            'tenant_id': self.tenant_id,
            'username': self.username,
            'password': self.password
        }
        req = http_config.post(path=path, header=self.headers_post, data=data)
        user_token = req.get('req_headers').get('X-User-Token')
        status_code = int(req.get('req_status_code'))
        self.assertEqual(status_code, 200)
        self.assertIn("Set-Cookie", str(req))
        self.assertIn("user_token=", req.get('req_headers').get('Set-Cookie'))
        return user_token

    def test_get_authorize(self):
        path = "/oauth/v1/authorize"
        params = {
            "response_type": "token",
            "redirect_uri": "http://smart.uat.sqbj.com/fmp/#!/facility-ledger/list",
            "state": "123",
            "client_id": self.fmp_client_id
        }
        self.headers_get['Cookie'] = 'user_token=' + self.test_login_portal()
        print(self.headers_get)
        req = http_config.get(path=path, header=self.headers_get, params=params)
        print(req)
        # cookie = str(req.get('req_header').get('Cookie'))
        # print(cookie)
        # status_code = int(req.get('req_status_code'))
        # self.assertEqual(status_code, 302)










    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
