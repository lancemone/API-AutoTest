

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
print(type(r.text))
print(r.text)

host = "http://httpbin.org/"
endpoint_g = "get"
url_01 = ''.join([host, endpoint_g])
r_01 = requests.get(url_01)
response = r_01.json()
print(response)
print(r_01.text)

# 带参数的get
params = {"show_env": "1"}
r_02 = requests.get(url=url_01, params=params)
print(r_02.url)
print(r_02.text)

# 带header的get请求
header = {"User-Agent": "test request headers"}
r_03 = requests.get(url=url_01, headers=header)
print(r_03.headers)
print(r_03.status_code)

# 同时带有参数和header
r_04 = requests.get(url=url_01, headers=header, params=params)

# post方法

# 带数据的post
endpoint_p = "post"
url_11 = ''.join([host, endpoint_p])
datas = {'key1': 'value1', 'key2': 'value2'}
print(requests.post(url_11, data=datas).text)

# 带header的post
print(requests.post(url_11, headers=header))
# print(requests.post(url_11, headers=header).status_code)

# 带json的post
data_json = {
    "sites": [
        {"name": "test", "url": "www.test.com"},
        {"name": "google", "url": "www.google.com"},
        {"name": "weibo", "url": "www.weibo.com"}
    ]
}

print(requests.post(url_11, json=data_json).json())
print(requests.post(url_11, data=json.dumps(data_json)))

# 带参数的post
params = {"key1": "params1", "key2": "params2"}
print(requests.post(url_11, params=params).text)

# 普通文件上传
files = {
    'file': open('test.txt', 'rb')
}
print(requests.post(url_11, files=files))

# 定制化文件上传
files_rename = {
    'file': ('my_test.png', open('test.png', 'rb'), 'image/png')
}
print(requests.post(url_11, files=files_rename).text)

# 多文件上传
files_onemore = {
    ('file1', ('test1.txt', open('test1.txt', 'rb')))
    ('file2', ('test2.txt', open('test2.txt', 'rb')))
}
print(requests.post(url_11, files=files_onemore).text)

# 流式上传
with open('test.txt') as f:
    print(requests.post(url_11, data=f).text)

# 获取cookie
url_c = "https://www.baidu.com/"
r_c = requests.get(url_c)
# 将RequestsCookiesJar转换成字典
ck = requests.utils.dict_from_cookiejar(r_c.cookies)
print(r_c.cookies)
print(ck)
for a in r_c.cookies:
    print(a.name, a.value)

# 发送cookie到服务器
# cookies = {"aaa":"bbb"}        # 简单的定义cookies并发送
# 复杂方式发送
s = requests.session()  # s = requests.session()
ck.set('ck-name', 'ck-value', path='/path/cookies', domain='.test.com')
s.cookies.update(ck)

# Session
# 保持会话同步
endpoint_ck = "cookies"
url_s = ''.join([host, endpoint_ck])
url_s01 = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
print(requests.get(url_s).text)
s.get(url_s01)  # cookies信息存在session中
print(s.get(url_s).text)

# 保存会话信息
endpoint_h = "headers"
url_h = ''.join([host, endpoint_h])
header1 = {"test1": "AAA"}
header2 = {"test2": "BBB"}
s.headers.update(header1)  # 已经存在于服务器中的信息
print(s.get(url_h, headers=header2).text)  # 发送新的信息

# 删除已存在的会话信息保存为None
s.headers['test1'] = None
print(s.get(url_h, headers=header2).text)

# 提供默认数据
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
print(s.get('http://httpbin.org/headers', headers={'x-test2': 'true'}).text)  # both 'x-test' and 'x-test2' are sent

# 认证
# 基本认证
url_au = "http://httpbin.org/basic-auth/user/passwd"
print("未提供用户名和密码：" + str(requests.get(url_au).status_code))
print("提供用户名和密码：" + str(requests.get(url_au, auth=('user', 'passwd')).status_code))
# 数字认证
from requests.auth import HTTPDigestAuth

url_au1 = "http://httpbin.org/digest-auth/auth/user/pass"
print(requests.get(url_au1, auth=HTTPDigestAuth('user', 'pass')).status_code)
# OAuth认证   http://docs.python-requests.org/en/master/user/authentication/

# 超时配置
r = requests.get(my_url, timeout=5)  # 利用timeout参数来配置最大请求时间
r = requests.get(my_url, timeout=None)  # 设置timeout=None，告诉请求永远等待响应，而不将请求作为超时值传递
