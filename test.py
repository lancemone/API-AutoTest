import requests

host = "http://httpbin.org/"
url_c = "https://www.baidu.com/"
r_c = requests.get(url_c)
# 将RequestsCookiesJar转换成字典
ck = requests.utils.dict_from_cookiejar(r_c.cookies)
s = requests.session()
# ck.set('ck-name', 'ck-value', path='/path/cookies', domain='.test.com')
s.cookies.update(ck)
endpoint3 = "cookies"
url_s = ''.join([host, endpoint3])
url_s01 = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
# print(requests.get(url_s).text)
s.get(url_s01)  # cookies信息存在session中
endpoint_h = "headers"
url_h = ''.join([host, endpoint_h])
header1 = {"test1": "AAA"}
header2 = {"test2": "BBB"}
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
# print(s.get('http://httpbin.org/headers', headers={'x-test2': 'true'}).text)  # both 'x-test' and 'x-test2' are sent
url_au = "http://httpbin.org/basic-auth/user/passwd"
print("未提供用户名和密码：" + str(requests.get(url_au).status_code))
print("提供用户名和密码：" + str(requests.get(url_au, auth=('user', 'passwd')).status_code))
from requests.auth import HTTPDigestAuth

url_au1 = "http://httpbin.org/digest-auth/auth/user/pass"
print(requests.get(url_au1, auth=HTTPDigestAuth('user', 'pass')).status_code)
