from smart_app_interfacetest import https_config
from smart_app_interfacetest import config
import logging
import requests
import jwt
import hmac
import hashlib
import base64
import time

secret_key = '298268b9d8572a02ca0478a604386832cdab06219d53616cdb1ff68f04814c64'
device_id = "03f9603789c42920beb67d6c4b573323"

iat = int(time.time())
exp = int(iat + 30)

ste = b'{"alg": "HS256","typ": "JWT"}'
stw = b'{"sub": "1234567890","name": "John Doe","iat": 1516239022}'
header = {
    # "kid": device_id,
    "typ": "JWT",
    "alg": "HS256"
}
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
}
ba_header = base64.b64encode(ste)
print(ba_header)
ba_payload = base64.b64encode(stw)
print(ba_payload)
msg = ba_header + b'.' + ba_payload
print(msg)
key = b'secret'
h = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
print(h.digest())
d = base64.b64encode(h.digest())
print(d)
