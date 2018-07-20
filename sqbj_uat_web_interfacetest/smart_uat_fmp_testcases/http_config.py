#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 下午4:05
# @Author  : motao
# @Site    : 
# @File    : http_config.py
# @Software: PyCharm


import requests
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import config
import logging

# 测试用例的http配置


host = config.host_url
timeout = config.timeout
header_get = config.header_get


def get(path, header, params):
    url = ''.join([host, path])
    try:
        r = requests.get(url=url, headers=header, params=params, timeout=float(timeout))
        req_header = r.headers
        req_json = r.json()
        req_text = r.text
        req_status_code = int(r.status_code)
        req_cookie = r.cookies
        req_raise_for_status = r.raise_for_status()
        req_ok = r.ok
        return [req_header, req_json, req_cookie, req_ok, req_raise_for_status, req_status_code, req_text]
    except TimeoutError:
        logging.info("Time out!")
        return None


def post(path, header, params, data):
    url = ''.join([host, path])
    try:
        r = requests.post(url=url, headers=header, params=params, data=data, timeout=float(timeout))
        req_text = r.text
        req_header = r.headers
        return [req_text, req_header]
    except TimeoutError:
        logging.info("Time out!")
        return None
