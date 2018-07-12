import requests

url_c = "https://www.baidu.com/"
r_c = requests.get(url_c)
# 将RequestsCookiesJar转换成字典
ck = requests.utils.dict_from_cookiejar(r_c.cookies)
s = requests.session()
ck.set('ck-name', 'ck-value', path='/path/cookies', domain='.test.com')
s.cookies.update(ck)
