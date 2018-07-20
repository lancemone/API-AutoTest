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

path = "oauth/v1/sign_in"

req = http_config.post(path=path, header=headers, data=data)
user_token = req.get('req_headers').get('X-User-Token')
codes = req.get('req_status_code')

print(req)
print(user_token)
print(codes)
print(req.get('Set-Cookie'))
