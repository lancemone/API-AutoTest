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

# 关闭证书验证警告
# urllib3.disable_warnings()
logging.captureWarnings(True)

header_get = config.header_get
header_post = config.header_post
tenant_id = config.tenant_id
username = config.username
passeord = config.password


class TestGetToken(unittest.TestCase):
    def setUp(self):
        self.header_get = config.header_get
        self.header_post = config.header_post
        self.tenant_id = config.tenant_id
        self.username = config.username
        self.password = config.password
        logging.captureWarnings(True)

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
        req_json = json.load(req.json())
        items = req_json.get('items')
        self.assertEqual(int(req.status_code), 200)
        self.assertEqual(items[0].get('unique_id'), self.tenant_id)

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()
