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
        self.fmp_client = config.fmp_client_id
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
        self.req = http_config.post(path=path, header=self.headers_post, params=None, data=data)
        self.user_token = self.req.get('req_header').get('X-User-Token')
        self.assertEqual(self.req.get('req_status_code'), 200)
        self.assertIn("Set-Cookie", self.req)
        self.assertIn("user_token=", self.req.get('Set-Cookie'))


if __name__ == '__main__':
    unittest.main()
