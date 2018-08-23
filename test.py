from smart_app_interfacetest.lib import api_module
from smart_app_interfacetest.config import read_conf
import requests
import logging


logging.captureWarnings(True)
conf = read_conf.Read_conf()
api = api_module.Api_module()
tenantid = "f40ccb4caad440170ea378adc184d775"
path = "/api/basic/json-rpc/views"
url = api.set_url(path)
header = api.set_header()
# header["content-type"] = "application/x-www-form-urlencoded"
print(header)
params = {
    "provider": "password",
    "tenant_id": tenantid,
    "username": conf.get_params("username"),
    "password": conf.get_params("password")
}
data = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "common_getTenantByUsername",
    "params": ["16811011109"]
}
r = requests.post(url=url, headers=header, json=data, verify=False)
print(r.json())
