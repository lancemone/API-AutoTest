#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 下午7:39
# @Author  : motao
# @Site    : 
# @File    : api_module.py
# @Software: PyCharm


import requests
import urllib3
from smart_app_interfacetest.config import read_conf
from smart_app_interfacetest.lib.LogOut import MyLog as Log

conf = read_conf()


class Api_module:
    def __init__(self):
        urllib3.disable_warnings()

    def get_header(self):
        r = requests.request()
