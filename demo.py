# -*- coding:utf-8 -*-
from urllib import request

url = "https://www.baidu.com/"
# 直接请求

req = request.Request(url)
req.add_header("User-Agent",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/62.0.3202.94 Safari/537.36")
response = request.urlopen(req)

print(response.read().decode('utf-8'))
