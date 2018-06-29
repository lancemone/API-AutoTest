import requests

# https协议的SSL证书验证处理

# requests支持的证书验证方式：SSL证书验证、客户端证书验证、CA证书验证


'''
SSL:Secure Sockets Layer,安全套接层。是为了解决HTTP协议是明文，避免传输的数据被窃取、篡改、劫持等。
TSL：Transport Layer Security，传输层安全协议。TSL其实是SSL标准化后的产物，即SSL/TSL实际上是表示同一个东西。
HTTPS：HTTPS是兼容HTTP的，可以把HTTPS理解为‘HTTP over TSL’，即HTTPS是HTTP协议和TSL协议的组合。
HTTPS在传输数据时，同样会先建立TCP连接，建立起TCP连接之后，会建立TSL连接
'''

# Requests 可以为 HTTPS 请求验证 SSL 证书，就像 web 浏览器一样。SSL 验证默认是开启的，如果证书验证失败，Requests 会抛出 SSLError
requests.get('https://github.com')


# 设置SSL证书
# 可以为 verify参数传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径（如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理）
# openssl是一个强大的安全套接字密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及SSL协议，并提供丰富的应用程序供测试或其他目的使用
'''
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have this software first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include'''

# 通过c_rehash处理CA证书文件夹:　　c_rehash - 为文件创建一个符号连接，并将此符号连接的名称设为文件的hash值。
# c_rehash扫描指定目录列表中的.pem，.crt，.cer及.crl文件并为这些文件计算hash值，并以计算出的hash值为名字为这些文件创建符号连接。（如果你的操作平台不支持符号连接，则执行的是一个拷贝。）这个功能像很多程序一样有用，对于使用OpenSSL要求建立的目录，其目的是找到证书
# verify参数仅用于主机证书，对于私有证书，可以传递一个 CA_BUNDLE 文件的路径给verify，也可以设置REQUEST_CA_BUNDLE环境变量
# CA bundle file 是一个文件，包含 PEM(base64)编码的、被信任的所有根证书(CA Root)。
# ssl client cert file 是用于 SSL 双向认证的客户端证书，通常还有一个对应的私钥。一般的网站不使用双向认证，故在大多数情况下无需配置
# 设置REQUEST_CA_BUNDLE环境变量（以下代码仅为参考）
import os
os.environ['REQUEST_CA_BUNDLE'] = os.path.join('/etc/ssl/certs', 'ca-certificates.crt')

# 指定一个本地证书作为客户端证书
requests.get(url='https://smart.sqbj.com', cert=('/usr/bin/client.cert', '/usr/bin/client.key'))
# 将客户端证书保持在会话中
s = requests.session()
s.cert = '/usr/bin/client.cert'

# 一般情况下访问经过认证的https网站，由于verify默认为True，会从certifi库里面获取证书验证安全性。如果网站是有效证书，那么 verify=False 或者 True 都可以访问。
# 如果将verify置为False，则不会验证https网站证书的安全性（无论是否在第三方机构认证都可以正常访问），并使用从源网站接收的公钥进行加密通信。
# 如果目标https站确认安全，但是证书不在certifi库里面，可以将其根证书base64编码信息添加到cacert.pem 文件末尾。也可以使用verify=/file/to/cacert.pem指定新的证书系统文件目录。
# 如果不需要进行SSL双向认证，也就不需要使用参数cert来自定双向验证的证书和key。

# Certifi 是一个精心准备的根证书集合，用来验证 SSL 证书的可信任度，同时还会验证 TLS 主机的身份
# 通过certifi包使用Mozilla证书
import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

# 使用其他定制证书
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs='/path/to/your/certificate_bundle')

# 同时携带客户端证书供服务器验证
http = urllib3.PoolManager(cert_file='/path/to/your/client_cert.pem', cert_reqs='CERT_REQUIRED', ca_certs='/path/to/your/certificate_bundle')



# 关闭证书验证并关闭SSL警告
import logging
# 关闭SSL警告
urllib3.disable_warnings()      # 方法1
logging.captureWarnings(True)   # 方法2
host = "https://smart.sqbj.com/pro_app_api/tenant/loginName?filter_name=login_name&filter_params=13273522511"
my_header = {
    'method': 'GET',
    'authority': 'smart.sqbj.com',
    'scheme': 'https',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.9.0'
}
endpoint = "get"
url = ''.join([host, endpoint])
r = requests.get(url, headers=my_header, verify=False)      # 关闭证书验证
response = r.json()
print(type(r.text))
print(r.json())

