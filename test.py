import requests

# 员工姓名和密码
username = 16811011102
passwd = 111111
# 鑫泰租户ID
tenant_id = "772cbb220daaa39a148db3cdcfbdadac"


def get_token():
    url = "http://smart.uat2.sqbj.com/oauth/v1/sign_in"
    data = {
        "tenant_id": tenant_id,
        "username": username,
        "password": passwd
    }
    r = requests.post(url=url, data=data)
    userToken = r.headers["X-User-Token"]
    url_token = "http://smart.uat2.sqbj.com/oauth/v1/token"
    data_token = {
        "grant_type": "user_token",
        "user_token": userToken,
        "client_id": "94509b599031542be74bc83ac835a361"
    }
    r_token = requests.post(url=url_token, data=data_token)
    access_token = r_token.json()["token_type"] + ' ' + r_token.json()["access_token"]
    return access_token


token = get_token()
print(token)
