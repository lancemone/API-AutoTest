#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 下午5:54
# @Author  : motao
# @Site    : 
# @File    : GenerateToken.py
# @Software: PyCharm


# 生成JWT
# 根据接口返回数据生成uesr_token和access_token

import os
import jwt
import time
import logging
from smart_app_interfacetest import config
from smart_app_interfacetest.app_test_cases.test_get_token import TestGetToken

return_value = TestGetToken()
device_id = return_value.test_get_user_token()
print(device_id)
secret_key = "298268b9d8572a02ca0478a604386832cdab06219d53616cdb1ff68f04814c64"
iat = int(time.time())
exp = int(iat + 30)
header = {
    # "kid": device_id,
    "typ": "JWT",
    "alg": "HS256"
}


class generate_token():

    def set_payload(self, client_id):
        if client_id is None:
            payload = {
                "exp": exp,
                "iat": iat
            }
        else:
            payload = {
                "aud": client_id,
                "exp": exp,
                "iat": iat
            }
        return payload

    def get_token(self):
        token = str(jwt.encode({"aud": "979a9078490c8b15dd59dc17719c6225",
                                "exp": 1533202520,
                                "iat": 1533202490}, secret_key, algorithms=['HS256'],
                               headers={"kid": device_id}))
        return token

    print(get_token)


token = jwt.encode({"exp": 1533202519,
                    "iat": 1533202489}, secret_key, algorithm='HS256', headers=header)
print(token)
logging.info(token)
