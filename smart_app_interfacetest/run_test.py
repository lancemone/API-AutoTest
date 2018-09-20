import requests
import logging
from asn1crypto._ffi import null

# 员工姓名和密码
username = 16811011101
passwd = 111111
# 鑫泰租户ID
tenant_id_1 = "772cbb220daaa39a148db3cdcfbdadac"
# 小区ID
area_id = 98
# 需要创建的项目名称
project_name = ["南园E区"]
# 项目 project_id
project_id = []
# 需要创建的楼宇数量
building_num = 3
# 楼宇 building_id
building_id = []
# 每个楼宇下需要创建的单元数量
unit_num = 2
# 单元 unit_id
unit_id = []
# 每个单元下需要创建的房屋数量
house_num = 10
# 房间ID
house_id = []


class Add_House:

    def __init__(self):
        logging.captureWarnings(True)
        self.username = username
        self.passwd = passwd
        self.tenantId = tenant_id_1
        self.areaId = area_id
        self.projectName = project_name
        self.projectId = project_id
        self.buildingId = building_id
        self.unitId = unit_id
        self.unit_num = unit_num
        self.house_num = house_num
        self.houseId = house_id
        self.bbp_url = "http://smart.uat2.sqbj.com/api/basic/json-rpc/views"

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
        for i in self.projectName:
            data_add_project = {
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
            data_get_project = {
                "jsonrpc": "2.0",
                "id": "123",
                "method": "GP:MAINWEBB:BuildingSetting:GetPage",
                "params": [self.areaId]

            }
            r_add_project = requests.post(url=self.bbp_url, headers=self.headers, data=data_add_project)
            assert "error" in r_add_project.json(), "%s" % r_get_project.json()['error']
            r_get_project = requests.post(url=self.bbp_url, headers=self.headers, data=data_get_project)
            assert "error" in r_get_project.json(), "%s" % r_get_project.json()['error']
            project = r_get_project.json()["result"]["projects"]
            self.projectId.append(project[-1]["id"])
        return self.projectId

    def create_building(self, pro_id=None):
        if pro_id is None:
            pro_id = self.projectId
        for i in range(building_num):
            for id in pro_id:
                data_add_building = {
                    "jsonrpc": "2.0",
                    "method": "GP:MAINWEBB:BuildingSetting:CreateBuilding",
                    "params": [{
                        "projectId": id,
                        "type": "building",
                        "children": [],
                        "number": i + 1,
                        "name": "号楼"}],
                    "id": "0.7327886772009835"
                }
                data_get_building = {
                    "jsonrpc": "2.0",
                    "id": "123",
                    "method": "GP:MAINWEBB:BuildingSetting:GetPage",
                    "params": [self.areaId, id]
                }
            try:
                r_create_building = requests.post(url=self.bbp_url, headers=self.headers, data=data_add_building)
                assert "error" in r_create_building.json(), "%s" % r_create_building.json()['error']
                r_get_building = requests.post(url=self.bbp_url, headers=self.headers, data=data_get_building)
                assert "error" in r_get_building.json(), "%s" % r_get_building.json()['error']
                building = r_get_building.json()["result"]["buildings"]
                self.buildingId.append(building[-1]["id"])
                return self.buildingId
            except:
                print("create building error")

    def create_unit(self, bu_id=None):
        if bu_id is None:
            bu_id = self.buildingId
        for i in range(self.unit_num):
            for id in bu_id:
                data_add_unit = {
                    "jsonrpc": "2.0",
                    "method": "GP:MAINWEBB:BuildingSetting:CreateUnit",
                    "params": [{
                        "buildingId": id,
                        "type": "unit",
                        "number": i + 1,
                        "name": "单元",
                        "floors": [{
                            "type": "aboveground",
                            "number": 1,
                            "name": "1"
                        }]
                    }],
                    "id": "0.8230573498944478"
                }
                data_get_unit = {
                    "jsonrpc": "2.0",
                    "id": "123",
                    "method": "GP:MAINWEBB:BuildingSetting:GetUnits",
                    "params": [id]
                }
            try:
                r_create_unit = requests.post(url=self.bbp_url, headers=self.headers, data=data_add_unit)
                assert "error" in r_create_unit.json(), "%s" % r_create_unit.json()['error']
                r_get_unit = requests.post(url=self.bbp_url, headers=self.headers, data=data_get_unit)
                assert "error" in r_get_unit.json(), "%s" % r_get_unit.json()['error']
                unit = r_get_unit.json()["result"]["units"]
                self.unitId.append(unit[-1]["id"])
                return self.unitId
            except:
                print("create building error")

    def create_house(self, un_id=None):
        if un_id is None:
            un_id = self.unitId
        for i in range(self.unit_num):
            for id in un_id:
                data_add_house = {
                    "jsonrpc": "2.0",
                    "id": "123",
                    "method": "GP:MAINWEBB:HouseCreate:CreateHouse",
                    "params": [{
                        "parentId": null,
                        "parentNumber": "",
                        "parentName": "",
                        "projectId": 816,
                        "buildingId": 2601,
                        "unitId": 6589,
                        "id": null,
                        "number": "001",
                        "name": "室",
                        "grossArea": "120",
                        "netArea": "120",
                        "handoverDate": "2018-09-19",
                        "moveinState": "EMPTY",
                        "decorateState": null,
                        "houseTypeId": null,
                        "floorId": 142,
                        "builtupArea": 120,
                        "dwellingareaArea": 120
                    }]
                }

                data_get_house = {
                    "jsonrpc": "2.0",
                    "id": "123",
                    "method": "GP:MAINWEBB:HouseList:GetPage",
                    "params": [98, 816, 2601, 6589, "001", null, null, null, 0, 10, ""]}

            try:
                r_create_house = requests.post(url=self.bbp_url, headers=self.headers, data=data_add_house)
                assert "error" in r_create_house.json(), "%s" % r_create_house.json()['error']
                r_get_house = requests.post(url=self.bbp_url, headers=self.headers, data=data_get_house)
                house = r_get_house.json()["result"]["houses"]
                self.houseId.append(house["items"][0]["id"])
                return self.houseId
            except:
                print("create building error")
