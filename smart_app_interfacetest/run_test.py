import requests
import logging
import paramunittest

# 员工姓名和密码
username = 16811011101
passwd = 111111
# 鑫泰租户ID
tenant_id_1 = "772cbb220daaa39a148db3cdcfbdadac"
# 小区ID
area_id = 98
# 需要创建的项目名称
project_name = ["南园E区"]
# 需要创建的楼宇数量
building_num = 3
# 每个楼宇下需要创建的单元数量
unit_num = 2
# 每个单元下需要创建的房屋数量
house_num = 10


class Add_House:

    def __init__(self):
        logging.captureWarnings(True)
        self.username = username
        self.passwd = passwd
        self.tenantId = tenant_id_1
        self.areaId = area_id
        self.projictName = project_name

    def get_accessToken(self):
        url = "http://smart.uat2.sqbj.com/oauth/v1/sign_in"
        data = {
            "tenant_id": self.tenantId,
            "username": self.username,
            "password": self.passwd
        }
        r = requests.post(url=url, data=data)
        self.userToken = r.headers["X-User-Token"]
        url_token = "http://smart.uat2.sqbj.com/oauth/v1/token"
        data_token = {
            "grant_type": "user_token",
            "user_token": self.userToken,
            "client_id": "94509b599031542be74bc83ac835a361"
        }
        r_token = requests.post(url=url_token, data=data_token)
        self.access_token = r_token.json()["token_type"] + ' ' + r_token.json()["access_token"]
        self.headers = {
            "Authorization": self.access_token,
            "x-user-token": self.userToken,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        return self.headers

    def create_project(self):
        # Add Project
        url_project = "http://smart.uat2.sqbj.com/api/basic/json-rpc/views"
        for i in self.projictName:
            data_project = {
                "id": "0.3091097128374325",
                "jsonrpc": "2.0",
                "method": "GP:MAINWEBB:BuildingSetting:CreateProject",
                "params": [
                    {
                        "manageAreaId": self.areaId,
                        "name": i,
                        "type": "area"
                    }
                ]
            }
            re = requests.post(url=url_project, headers=self.headers, )


hh = Add_House()
he = hh.get_accessToken()
print(he)
