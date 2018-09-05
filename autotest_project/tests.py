res = {"jsonrpc": "2.0",
       "id": 1,
       "result": [{"tenantId": "772cbb220daaa39a148db3cdcfbdadac",
                   "shortName": "鑫泰产业"},
                  {"tenantId": "dc0158b7be85b9e64a76fbd98eb439b7",
                   "shortName": "motest"},
                  {"tenantId": "f40ccb4caad440170ea378adc184d775",
                   "shortName": "jingj"}]}
result = res["result"]
print(result)
inter = int(result.index("鑫泰产业"))
print(inter)
tenant_id = result[inter]["tenantId"]
print(tenant_id)
