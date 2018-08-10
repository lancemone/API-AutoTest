#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:29
# @Author  : motao
# @Site    : 
# @File    : https_config.py
# @Software: PyCharm

import unittest
from smart_app_interfacetest import config

host = config.host


def set_url(path):
    url = ''.join([host, path])
    return url


