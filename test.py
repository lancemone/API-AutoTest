import requests
import json

host = 'http://httpbin.org/'
endpoint2 = "post"
header = {"User-Agent": "test request headers"}
url_11 = ''.join([host, endpoint2])
datas = {'key1': 'value1', 'key2': 'value2'}

data_json = {
    "sites": [
        {"name": "test", "url": "www.test.com"},
        {"name": "google", "url": "www.google.com"},
        {"name": "weibo", "url": "www.weibo.com"}
    ]
}

print(requests.post(url_11, json=data_json).json())
print(requests.post(url_11, data=json.dumps(data_json)))
