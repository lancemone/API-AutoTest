#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 下午6:09
# @Author  : motao
# @Site    : 
# @File    : test_get_token.py
# @Software: PyCharm

import re
import requests
import logging
import unittest
import json
from smart_app_interfacetest.lib import HTMLTestRunner
from smart_app_interfacetest import config
from smart_app_interfacetest import https_config


class TestGetToken(unittest.TestCase):
    def setUp(self):
        self.header_get = config.header_get
        self.header_post = config.header_post
        self.tenant_id = str(config.tenant_id)
        self.username = config.username
        self.password = config.password

    @classmethod
    def setUpClass(cls):
        logging.captureWarnings(True)  # 关闭证书验证警告

    def test_get_tennant_id(self):
        path = "/pro_app_api/tenant/loginName"
        params = {
            "page": "0",
            "page_size": "999",
            "filter_name": "login_name",
            "filter_params": self.username
        }
        url = https_config.set_url(path=path)
        req = requests.get(url=url, headers=self.header_get, params=params, verify=False)
        req_json = json.loads(req.text)
        items = req_json['items']
        self.assertEqual(int(req.status_code), 200, msg="状态码为%s" % req.status_code)
        self.assertEqual(items[1]['unique_code'], self.tenant_id, msg="错误")
        print('test_get_tennant_id pass')

    def test_get_user_token(self):
        path = '/oauth/v1/devices'
        url = https_config.set_url(path=path)
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "okhttp/3.8.0"
        }
        data = {
            "device_id": None,
            "tenant_id": self.tenant_id,
            "username": self.username,
            "password": self.password,
            "trusted": "true",
            "setting": "%7B%22jpush%22%3A%7B%22registration_id%22%3A%22160a3797c80f5e50e6c%22%7D%7D"
        }
        req = requests.patch(url=url, headers=headers, data=data, verify=False)
        req_json = req.json()
        user_token = req.headers['x-user-token']
        self.assertEqual(req.status_code, 200)
        self.assertIn("device_id", req_json)
        self.assertIn('secret_key', req_json)
        self.assertIsNotNone(user_token)
        print('test_get_user_token pass')
        return req_json

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()
