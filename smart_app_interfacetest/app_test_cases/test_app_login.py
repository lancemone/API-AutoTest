#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 下午8:31
# @Author  : motao
# @Site    : 
# @File    : test_app_login.py
# @Software: PyCharm

import unittest
import sys
from smart_app_interfacetest.config.read_conf import Read_conf as conf
from smart_app_interfacetest.lib import api_module
from smart_app_interfacetest.lib.LogOut import MyLog


class Test_App_Login(unittest.TestCase):
    def setUp(self):
        '''

        :return:
        '''
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.api = api_module.Api_module()
        self.header = self.api.set_header()
        self.username = conf.get_params("username")
        self.password = conf.get_params("password")
        self.tenantid = conf.get_params("tenant_id")

    def test_01_tenantid(self):
        '''

        :return:
        '''
        self.logger.info("%s start run" % sys._getframe().f_code.co_name)
        path = "/api/basic/json-rpc/views"
        url = self.api.set_url(path)
        data = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "common_getTenantByUsername",
            "params": [self.username]
        }
        code = self.api.https_post(url=url, header=self.header, json=data, value_name="status_code")
        response = self.api.https_post(url=url, header=self.header, data=data, value_name="json")
        result = response.get("result")
        self.tenantid = result[0].get("tenantId")
