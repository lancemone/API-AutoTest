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
        req_json = req.json()
        unique_code = req_json.get('items')[0].get('unique_code')
        # print(unique_code)
        tenant_id = config.tenant_id
        self.assertEqual(int(req.status_code), 200, msg="状态码为%s" % req.status_code)
        self.assertEqual(tenant_id, unique_code, msg="错误")
        # self.assertEqual("7e04d72e14f827e77fe7dac3e70b5183", unique_code, msg="错误")



    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()
