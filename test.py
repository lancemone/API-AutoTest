from smart_app_interfacetest import https_config
from smart_app_interfacetest import config
import logging
import requests

path = '/oauth/v1/devices'
url = https_config.set_url(path=path)
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "okhttp/3.8.0"
}
data = {
    "device_id": None,
    "tenant_id": config.tenant_id,
    "username": config.username,
    "password": config.password,
    "trusted": "true",
    "setting": "%7B%22jpush%22%3A%7B%22registration_id%22%3A%22160a3797c80f5e50e6c%22%7D%7D"
}
logging.captureWarnings(True)
req = requests.patch(url=url, headers=headers, data=data, verify=False)
print(req.status_code)
req_json = req.json()
print(req_json)
user_token = req.headers['x-user-token']
print(user_token)
