# 智社区web基础配置

# HTTP
protocol = "http"
port = 8888
oauth_host = "smart.uat.sqbj.com"
host_url = "http://smart.uat.sqbj.com/"
oauth_baseURL = "/oauth/v1"
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
unique_id = "501f380a64c925e2c8a6ab0db1cb0413"
username = "16811011103"
password = "111111"
serial_number = "1613100053"

# HEADER
header_get = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
header_post = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "79",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

# EMAIL
mail_host = "mail.sqbj.com"
mail_user = "motao@sqbj.com"
mail_pass = "mo95tao95"
mail_port = ""
sender = "motao@sqbj.com"
receiver = "lancemone@gmail.com/chendn@sqbj.com"
subject = "Interface Test Report"
content = "All interface test has been complited\nplease read the report file about the detile of result in the attachment"
testuser = "MOTAO"
on_off = "off"
