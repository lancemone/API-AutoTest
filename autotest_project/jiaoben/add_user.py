#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 下午1:34
# @Author  : motao
# @Site    : 
# @File    : add_user.py
# @Software: PyCharm

import requests
import time

'''
小区id:
香溢园 98   留春庭 99    测试小区 147

测试小区：
A区  845    B区   846   C区   847   D区   848
A区： 
1号楼   2654    2号楼   2655        3号楼    2659
1号楼：
1单元     6661        2单元     6662
2号楼:
1单元     6663        2单元     6664
3号楼：
1单元     6665        2单元     6666      
'''
# 员工姓名和密码
username = 16811011101
passwd = 111111
# 鑫泰租户ID
tenant_id = "772cbb220daaa39a148db3cdcfbdadac"
# 小区id
area_id = 147
# 项目id
pro_id = 845
# 目前没写循环
# 楼宇id
build_id = 2654
# build_id2 = 2644
# 单元id
unit_id = 6662
# unit_id1_2 = 6643
# unit_id2_1 = 6644
# unit_id2_2 = 6645
# 每个单元添加房间的数量
house_num = 50
# 每个房间下添加的住户数量
household_num = 4
# 应用token
access_token = None
# userToken
user_token = None
# 第一个住户的手机号，之后每次加1
phone = 12011104200
# 选择添加房间还是住户
statu = int(input("输入运行方式编号：1 仅添加房间   2 添加住户  3 添加房间和住户: \n"))


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
    headers_token = {
        "Authorization": access_token,
        "x-user-token": userToken,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    return headers_token


def get_headers():
    header = get_token()
    return header


def add_house():
    url = "http://smart.uat2.sqbj.com/api/basic/json-rpc/views"
    houseId = []
    headers = get_headers()
    buildId = build_id
    unitId = unit_id
    for i in range(house_num):
        # 生成房间编号
        id = "%03d" % (i + 1)
        data_add_house = {
            "jsonrpc": "2.0",
            "id": "123",
            "method": "GP:MAINWEBB:HouseCreate:CreateHouse",
            "params": [{
                "parentId": None,
                "parentNumber": "",
                "parentName": "",
                "projectId": pro_id,
                "buildingId": buildId,
                "unitId": unitId,
                "id": None,
                "number": id,
                "name": "室",
                "grossArea": "120",
                "netArea": "120",
                "handoverDate": "2018-09-19",
                "moveinState": "EMPTY",
                "decorateState": None,
                "houseTypeId": None,
                "floorId": 142,
                "builtupArea": 120,
                "dwellingareaArea": 120
            }]
        }
        data_get_house = {
            "jsonrpc": "2.0",
            "id": "123",
            "method": "GP:MAINWEBB:HouseList:GetPage",
            "params": [area_id, pro_id, buildId, unitId, id, None, None, None, 0, 10, ""]
        }
        try:
            # 创建房间
            r_create_house = requests.post(url=url, headers=headers, json=data_add_house)
            time.sleep(1)
            # 获取新建房间的id
            r_get_house = requests.post(url=url, headers=headers, json=data_get_house)
            time.sleep(2)
            house = r_get_house.json()["result"]["houses"]
            houseId.append(house["items"][0]["id"])
            print("添加房间%s完成" % id)
        except:
            print("添加房屋失败")
    print("添加全部房间完成")
    return houseId


def add_household(houseid):
    url = "http://smart.uat2.sqbj.com/api/basic/json-rpc/views"
    i = 200
    phone1 = phone
    headers = get_headers()
    for house_id in houseid:
        for n in range(household_num):
            i += 1
            phone1 += 1
            data = {
                "jsonrpc": "2.0",
                "method": "GP:MAINWEBB:ResidentCreate:CreateResident",
                "params": [{
                    "sex": "Female",
                    "identity": "resident_owner",
                    "islivein": "true",
                    "labels": [],
                    "areaId": area_id,
                    "buildingId": build_id,
                    "unitId": unit_id,
                    "houseId": house_id,
                    "name": "莫的住户%d" % i,
                    "phone": "%d" % phone1
                }],
                "id": "0.30630253884076186"
            }
            try:
                r_add_hold = requests.post(url=url, json=data, headers=headers)
                time.sleep(1)
                print("添加住户%s %d完成" % (i, phone1))
            except:
                print("添加住户失败")
    print("添加全部住户完成！")


if statu == 1:
    houseadd = add_house()
elif statu == 2:
    houses_id = list(int(input("输入房间编号")))
    household = add_household(houseid=houses_id)
elif statu == 3:
    houseadd = add_house()
    print("house_id = ")
    print(houseadd)
    household = add_household(houseid=houseadd)
