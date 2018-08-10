#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 上午10:44
# @Author  : motao
# @Site    : 
# @File    : tests.py
# @Software: PyCharm
import json

dic = {"device_id": "bcabdd8bde2d95e80fa083cc91e2c68e",
       "secret_key": "cbf0d5a3f030617e4d454dbcd5b891093fc830b89b005ee392e39daa446b7653"}
json_v = {'device_id': '2055a1659953ab0de48dc9bddbb55385',
          'secret_key': '4af60606b34885b0aea89d9506de9d85affceff195fce407c130c424920a58f4'}
json_dic = json.loads(json_v)
print(json_dic)
print(dic["device_id"])
print(type(json_dic))
# print(json_dic["device_id"])
