from json import JSONDecodeError

import requests
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import config
from sqbj_uat_web_interfacetest.smart_uat_fmp_testcases import http_config

host = config.host_url
headers = config.header_post
data = {
    'tenant_id': config.tenant_id,
    'username': config.username,
    'password': config.password
}


def get_user_token(return_lst):
    path = "oauth/v1/sign_in"

    req = http_config.post(path=path, header=headers, data=data)
    user_token = req.get('req_headers').get('X-User-Token')
    codes = req.get('req_status_code')
    print(codes)
    return user_token

path_get = "/oauth/v1/authorize"
url = ''.join([config.host_url, path_get])
params = {
    "response_type": "token",
    "redirect_uri": "http://smart.uat.sqbj.com/fmp/#!/facility-ledger/list",
    "state": "123",
    "client_id": config.fmp_client_id
}
header_get = config.header_get
header_get['Cookie'] = 'user_token=' + get_user_token()
print(header_get)
req_get = requests.get(url=url, headers=header_get, params=params)
try:
    req_get.json()
except JSONDecodeError:
    req_get.json = {}
print(req_get.headers)
print(req_get)
