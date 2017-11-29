# -*- coding:utf-8 -*-
from urllib import request, parse

# 网址
url = "http://210.51.169.193:8080/login.html"

headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  r'Chrome/43.0.2357.81 Safari/537.36',
    'Referer': r'http://210.51.169.193:8080/login.html',
    'Content-Type': r'application/json; charset=UTF-8'
}
data = {'user': {'userName': '60000852', 'password': '60000852'}, 'loginURL': 'http://210.51.169.193:8080/login.html'}
parmas = request.urlencode(data)
req = request.urlopen(url, parmas)

print(req)
