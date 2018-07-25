# -*- coding: utf-8 -*-

import json
from cgitb import html

import requests

# 登录 url
loginUrl = 'https://accounts.douban.com/login'


# 通过用户名／密码获取cookies
def login(userName, password):
    """
    登录信息  json.dumps	将 Python 对象编码成 JSON 字符串
                json.loads	将已编码的 JSON 字符串解码为 Python 对象
    :param userName:
    :param password:
    :return:
    """
    jsonData = json.dumps(
        {
            'user': {
                'userName': userName,
                'password': password
            },
            'loginURL': html + '/login.html'
        }
    )

    headers = {"Cookie": 'viewed="4123377"; bid=dEiv72_xR-Q; gr_user_id=7a6e2bcc-480e-4e57-9d8e-70ce7c48ff0f; '
                         '_vwo_uuid_v2=D70CA279D4A09E3C2C9776974C30690FD|55daf29647f1d71a00a3438cdb8c63ca; '
                         '__utma=30149280.868029105.1532082385.1532082385.1532082385.1; __utmc=30149280; '
                         '__utmz=30149280.1532082385.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / '
                             '537.36(KHTML, like Gecko) Chrome/66.0.3359.181Safari / 537.36 '
               }
    response = requests.Session().post(loginUrl, data=jsonData, headers=headers)
    return response
