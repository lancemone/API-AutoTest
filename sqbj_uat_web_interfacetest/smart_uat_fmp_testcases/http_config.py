#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 下午4:05
# @Author  : motao
# @Site    : 
# @File    : http_config.py
# @Software: PyCharm
from json import JSONDecodeError

import requests
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import config
import logging
import json

# 测试用例的http配置


host = config.host_url
timeout = config.timeout
header_get = config.header_get


def get(path, header, params):
    url = ''.join([host, path])
    try:
        r = requests.get(url=url, headers=header, timeout=float(timeout))
        req_header = r.headers
        try:
            r.json()
        except JSONDecodeError:
            r.json = {}
        req_json = r.json
        req_text = r.text
        req_status_code = int(r.status_code)
        req_cookie = r.cookies
        req_raise_for_status = r.raise_for_status()
        req_ok = r.ok
        return {"req_header": req_header, "req_json": req_json, "req_cookie": req_cookie, "req_ok": req_ok, \
                "req_raise_for_status": req_raise_for_status, "req_status_code": req_status_code, "req_text": req_text}
    except TimeoutError:
        logging.info("Time out!")
        return None


def post(path, header, data):
    url = ''.join([host, path])
    try:
        r = requests.post(url=url, headers=header, data=data, timeout=float(timeout))
        req_text = r.text
        req_header = r.headers
        req_status_code = r.status_code
        return {"req_text": req_text, "req_headers": req_header, "req_status_code": req_status_code}
    except TimeoutError:
        logging.info("Time out!")
        return None
