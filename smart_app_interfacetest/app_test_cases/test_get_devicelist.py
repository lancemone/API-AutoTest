#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 下午6:34
# @Author  : motao
# @Site    : 
# @File    : test_get_devicelist.py
# @Software: PyCharm

import unittest
import sys
from smart_app_interfacetest.config import read_conf
from smart_app_interfacetest.lib import api_module
from smart_app_interfacetest.lib.LogOut import MyLog


class Test_DeviceList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        MyLog.get_log().get_logger().info(">>>>>>>>>>Test_App_Login Start<<<<<<<<<<")

    @classmethod
    def tearDownClass(cls):
        MyLog.get_log().get_logger().info(">>>>>>>>>>Test_App_Login End<<<<<<<<<<")

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.api = api_module.Api_module()
        self.conf = read_conf.Read_conf()
        self.logger.info("%s start run" % sys._getframe().f_code.co_name)
        self.tenantid = self.conf.get_params(name="tenant_id")
        self.header = self.api.set_header(name="authorization", value=self.conf.get_header("fmp_authorization"))

    def tearDown(self):
        # time.sleep(1)
        self.logger.info("%s test end" % sys._getframe().f_code.co_name)

    # 测试根据角色获取小区
    def test_get_areaid(self):
        path = "/api/basic/json-rpc/views"
        url = self.api.set_url(path)
        self.header["x-user-token"] = self.conf.get_header("x-user-token")
        data = {
            "jsonrpc": 2.0,
            "method": "common_getManangeAreaBasicsByAppKey_RoleKey",
            "params": ["FMP", "OPERATOR_MANAGER"],
            "id": 1
        }
        code = self.api.https_json_post(url=url, header=self.header, data=data, value_name="code")
        re = self.api.https_json_post(url=url, header=self.header, data=data, value_name="json")
        area_detail = re["result"]["manageAreaDetails"]
        area_id = area_detail[0]["id"]
        self.conf.set_value(v_type="PARAMS", name="area_id", value=area_id)
        self.assertIn("fullName", area_detail)
