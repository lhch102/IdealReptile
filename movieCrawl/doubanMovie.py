# -*- coding: utf-8 -*-
import json

import pymysql
import requests


def getMovie():
    sort = 'T'
    range = '0,10'
    tags = '电影'
    start = 0

    header = {
        "Cookie": 'bid=JghEKk7X-2A; __utma=30149280.1700385934.1523158608.1525661550.1525672953.7; __utmz=30149280.1525661550.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1525673000%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=496aa0a622b0b435.1524808171.4.1525673197.1525664260.; __yadk_uid=RJWNziih4EsWTPIfQxTLE5jR9WPjyjJ5; __utma=223695111.2042794536.1524808175.1525661550.1525673000.4; __utmz=223695111.1525673000.4.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=DCB4CE8DE695EAB7D6510CFFE3DA94FAE|bb40a1425a73b626fdd1dd295f0f6e45; __utmc=30149280; __utmc=223695111; __utmb=30149280.5.10.1525672953; __utmt=1; ps=y; push_noty_num=0; push_doumail_num=0; _pk_ses.100001.4cf6=*; __utmb=223695111.0.10.1525673000; ap=1; dbcl2="103623208:nBAzO0a38XQ"; ck=H49T; __utmv=30149280.10362'}

    while True:
        doubanUrl = 'https://movie.douban.com/j/new_search_subjects?sort=%s&range=%s&tags=%s&start=%d' \
                    % (sort, range, tags, start)
        if start == 0:
            print("请求地址：", doubanUrl)
        start = start + 20
        session = requests.Session()
        result = session.get(doubanUrl, headers=header)
        movieJson = json.loads(result.text)
        listData = movieJson['data']
        conDataBase(listData)
        if len(listData) == 0:
            break


def main():
    print(getMovie())


def conDataBase(listData):
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='ideal',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()

    for dict in listData:
        sql = "INSERT INTO movie(title,rate,url) " \
              "VALUES ('%s','%s')" % ((dict['title']), dict['title'], dict['url'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            connect.commit()
        except:
            # Rollback in case there is any error
            print("wrong")
            connect.rollback()


if __name__ == '__main__':
    main()
