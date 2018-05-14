# -*- coding: utf-8 -*-

import datetime
import json

import pymysql
import requests

# 登录 url
loginUrl = 'https://accounts.douban.com/login'


# 通过用户名／密码获取cookies
def login(userName, password):
    '''
        登录信息  json.dumps	将 Python 对象编码成 JSON 字符串
                json.loads	将已编码的 JSON 字符串解码为 Python 对象
    '''
    jsonData = json.dumps(
        {
            'user': {
                'userName': userName,
                'password': password
            },
            'loginURL': html + '/login.html'
        }
    )

    userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'
    headers = {"Cookie": 'bid=JghEKk7X-2A; __utma=30149280.1700385934.1523158608.1525661550.1525672953.7; '
                         '__utmz=30149280.1525661550.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; '
                         '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1525673000%2C%22https%3A%2F%2Fwww.douban.com%2F%22'
                         '%5D; _pk_id.100001.4cf6=496aa0a622b0b435.1524808171.4.1525673197.1525664260.; '
                         '__yadk_uid=RJWNziih4EsWTPIfQxTLE5jR9WPjyjJ5; '
                         '__utma=223695111.2042794536.1524808175.1525661550.1525673000.4; '
                         '__utmz=223695111.1525673000.4.3.utmcsr=douban.com|utmccn=('
                         'referral)|utmcmd=referral|utmcct=/; '
                         '_vwo_uuid_v2=DCB4CE8DE695EAB7D6510CFFE3DA94FAE|bb40a1425a73b626fdd1dd295f0f6e45; '
                         '__utmc=30149280; __utmc=223695111; __utmb=30149280.5.10.1525672953; __utmt=1; ps=y; '
                         'push_noty_num=0; push_doumail_num=0; _pk_ses.100001.4cf6=*; '
                         '__utmb=223695111.0.10.1525673000; ap=1; dbcl2="103623208:nBAzO0a38XQ"; ck=H49T; '
                         '__utmv=30149280.10362'}
    responseIndex = requests.Session().post(loginUrl, data=jsonData, headers=headers)
    return responseIndex

def main():
    userName = '60000901'
    password = '60000901'
    # userName = '60000852'
    # password = '60000852'
    print(login(userName, password))

if __name__ == '__main__':
    main()
