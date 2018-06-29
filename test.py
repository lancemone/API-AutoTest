import requests

r = requests.get(
    url='https://smart.sqbj.com/pro_app_api/tenant/loginName?filter_name=login_name&filter_params=13273522511')
print(r.json())
