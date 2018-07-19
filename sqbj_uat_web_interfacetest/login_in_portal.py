#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 下午5:30
# @Author  : motao
# @Site    : 
# @File    : login_in_portal.py
# @Software: PyCharm

import requests
import json
import urllib.request


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
        req = requests.get(url=url, params=params, headers=LoginIn.header_request)
        response = req.json()
        self.area_number = response.get('items')[0].get('area_number')  # 获取第一个租户id
        self.unique_code = response.get('items')[0].get('unique_code')  # 获取租户id
        return {'area_number': self.area_number, 'unique_code': self.unique_code}

    # 获取登录token
    def get_login_token(self):
        self.get_area_number()
        path = "oauth/v1/sign_in"
        data = {
            'tenant_id': self.get_area_number().get('unique_code'),
            'username': self.name,
            'password': self.passwd
        }
        url = ''.join([LoginIn.host, path])
        req = requests.post(url=url, headers=LoginIn.header_request, data=data)
        login_token = req.headers['X-User-Token']


mommmm = LoginIn(16811011103, 111111)
print(mommmm.get_login_token())
