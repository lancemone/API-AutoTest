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


class AssertRefact(unittest.TestCase):
    def assert_equal(self, value_return, value_true, msg):
        try:
            self.assertEqual(value_return, value_true, msg)
        except AssertionError as reason:
            raise msg

    def assert_not_equal(self, value_return, value_true, msg):
        try:
            assert value_return != value_true
        except TypeError:
            return msg
        else:
            return True

    def assert_in(self, value_return, value_true, msg):
        try:
            assert value_true in value_return
        except TypeError:
            return msg
        else:
            return True

    def assert_not_in(self, value_return, value_true, msg):
        try:
            assert value_true not in value_return
            return True
        except TypeError:
            return msg
