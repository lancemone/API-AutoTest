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
from smart_app_interfacetest.lib import log_conf

logger = log_conf.logger


class Test_DeviceList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # logger.info("Test_App_Login start")
        log_conf.case_start("Test_App_Login")

    @classmethod
    def tearDownClass(cls):
        # logger.info("Test_App_Login end")
        log_conf.case_end("Test_App_Login")

    def setUp(self):
        self.api = api_module.Api_module()
        self.conf = read_conf.Read_conf()
        self.tenantid = self.conf.get_params(name="tenant_id")
        self.header = self.api.set_header(name="authorization", value=self.conf.get_header("fmp_authorization"))


    def tearDown(self):
        # time.sleep(1)
        # logger.info("case end")
        log_conf.case_end(case_name="%s" % sys._getframe().f_code.co_name)

    # 测试根据角色获取小区
    def test_get_areaid(self):
        log_conf.case_start(case_name="%s" % sys._getframe().f_code.co_name)
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
        # self.log.case_line(case_name="%s" % sys._getframe().f_code.co_name, code=str(code), msg=str(re))
        area_detail = re["result"]["manageAreaDetails"]
        area_id = area_detail[0]["id"]
        self.assertEqual(code, 200)
        self.conf.set_value(v_type="PARAMS", name="area_id", value=str(area_id))
        self.assertIn("fullName", area_detail[0])

    # 获取小区下设备数量和健康度
    def test_get_devicenum(self):
        log_conf.case_start(case_name="%s" % sys._getframe().f_code.co_name)
        path = "/api/apps/fmp/devices/summary/health?communityIds=%s" % self.conf.get_params("area_id")
        url = self.api.set_url(path)
        code = self.api.https_get(url=url, headers=self.header, value_name="code")
        re = self.api.https_get(url=url, headers=self.header, value_name="json")
        data = re["data"]
        self.assertEqual(code, 200)
        self.assertIn('health_score', data)
        self.assertIn('device_count', data)
