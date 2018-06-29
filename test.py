import urllib
from urllib import parse
from urllib import request
import requests
import ssl


context = ssl._create_unverified_context()      # 忽略未经核实的SSL证书认证
https_url = 'https://smart.sqbj.com'            # url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request(https_url)     # Request对象作为urlopen()方法的参数，发送给服务器并接收响应


