

import requests
import json


# HTTP协议是一个基于请求/响应模式的、无状态的，应用层协议
'''
# request中的常用响应信息
requests.Response.text                      # 返回响应对象，Unicode型数据，主要取文本
requests.Response.content                   # 返回响应对象，bytes型，二进制的数据，取图片和文件等，中文能显示为字符
requests.Response.json()                    # requests中内置的json解码器
requests.Response.status_code               # 响应状态码
requests.Response.reason                    # 状态原因
requests.Response.cookies                   # 返回cookies
requests.Response.encoding                  # 返回编码方式
requests.Response.request.headers           # 返回请求消息报头
requests.Response.url                       # 最终的url
requests.Response.headers                   # 以字典对象存储服务器的响应头，若键不存在则返回None
requests.Response.raw                       # 返回原始响应体，也就是urllib的response对象，使用.raw.read()读取
requests.Response.raise_for_status()        # 失败请求（非200响应）抛出异常  '''


# get方法简单使用
'''
环境搭建：
http://httpbin.org/
一个使用 Python + Flask 编写的 HTTP 请求和响应服务，该服务主要用于测试 HTTP 库。后续测试我们都基于这个网站
考虑到测试时要不断访问 httpbin 网站，请求过多担心被拉到黑名单，我们自己在本地搭建一套httpbin服务。

1、安装：pip install gunicorn

2、安装：pip install httpbin

3、启动：gunicorn httpbin:app

”'''


# 不带参数的get
# 此处暂时先讨论http请求，https请求需要证书，后面介绍
my_url = "http://127.0.0.1:8000"
r = requests.get(my_url)
#response = r.json()
print(type(r.text))
print(r.text)





