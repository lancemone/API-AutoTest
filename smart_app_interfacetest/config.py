#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 下午6:44
# @Author  : motao
# @Site    : 
# @File    : config.py
# @Software: PyCharm


# 参数配置

# HTTP
host = "https://smart.uat.sqbj.com"
timeout = 10

# PARAMS
pms_client_id = "51e929909c3511e7a795b264e03878af"  # 物管基础
tsp_client_id = "51e929909c3511e7a795b264e03878af"  # 客服工单
egs_client_id = "d0584301baa26e84251ee737314f02fa"  # 门禁管理
bpp_client_id = "da3e88f7c2a9bcb505adab121de8f51e"  # 物业收费
fmp_client_id = "aa0b01ce58a0420c8801f84c89f1c68d"  # 设备设施
pbp_client_id = "566ff8db02e08b29cf491efb4914ea37"  # 社区党建
gsp_client_id = "447785b30ab6d22284881ba318627685"  # 社区政务
tenant_id = "7e04d72e14f827e77fe7dac3e70b5183"
username = "16811011102"
password = "111111"
serial_number = "1613100053"

# HEADER
header_get = {
    "method": "GET",
    "authority": "smart.uat.sqbj.com",
    "scheme": "https",
    "app_id": "prop-pro-android",
    "client_id": "7567436B853D65E7385A98066CCE5504",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9500 Build/R16NW)",
    "accept-encoding": "gzip"
}
header_post = {
    "method": "POST",
    "authority": "smart.uat.sqbj.com",
    "scheme": "https",
    "app_id": "prop-pro-android",
    "client_id": "7567436B853D65E7385A98066CCE5504",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9500 Build/R16NW)",
    "connect-type": "application/x-www-form-urlencoded",
    "content-length": "275",
    "accept-encoding": "gzip"

}

# EMAIL
smtp_server = "smtp.mxhichina.com"
mail_host = "mail.sqbj.com"
mail_user = "motao@sqbj.com"
mail_pass = "mo95tao95"
mail_port = "465"
sender = "motao@sqbj.com"
receiver = "lancemone@gmail.com/chendn@sqbj.com"
subject = "Interface Test Report"
content = "All interface test has been complited\nplease read the report file about the detile of result in the attachment"
testuser = "MOTAO"
on_off = "off"
