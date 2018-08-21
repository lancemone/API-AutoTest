from smart_app_interfacetest.lib.api_module import Api_module as api
import json
import requests
import logging

logging.captureWarnings(True)

url = "https://smart.uat2.sqbj.com/api/basic/json-rpc/views"
header = api().set_header()
json_data = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "common_getTenantByUsername",
    "params": ["16811011109"]
}
data = json.dumps(json_data)
code = api().https_post(url=url, header=header, json=json_data, value_name="json")
r = api().https_post(url=url, header=header, json=data, value_name="json")
re = r.get("result")
# te = re[0].get("tenantId")
print(type(json_data))
print(type(data))
print(code)
# print(r)
rr = requests.post(url=url, json=data, headers=header, verify=False)
print(rr.json())
