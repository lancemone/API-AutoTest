#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 下午5:30
# @Author  : motao
# @Site    : 
# @File    : login_in_portal.py
# @Software: PyCharm

import requests
import json
import urllib3


# 进入portal页并获取用户的user_token

class LoginIn(object):
    host = "http://smart.uat.sqbj.com/"
    header_request = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "smart.uat.sqbj.com",
        "Referer": "http://smart.uat.sqbj.com/login",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    }

    # 设置用户登录名和密码
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    # 获取用户账号下的所有租户信息
    def get_area_number(self):
        path = "pro_app_api/tenant/loginName"
        params = {
            "filter_name": "login_name",
            "filter_params": self.name,
            "$page": 0,
            "$page_size": 50
        }
        url = ''.join([LoginIn.host, path])
        r = requests.get(url=url, params=params)
        response = requests.
        data = json.load(response.read())
        print(data['area_number'])
        # return data['area_number']


mommmm = LoginIn(16811011103, 111111)
mommmm.get_area_number()
