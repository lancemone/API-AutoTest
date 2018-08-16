import requests

url = 'https://smart.uat2.sqbj.com/api/basic/json-rpc/views'
data_json = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "common_getTenantByUsername",
    "params": ["16811011109"]
}

r = requests.request(url=url, method='post', data=data_json)
