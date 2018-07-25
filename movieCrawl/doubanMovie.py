# -*- coding: utf-8 -*-
import json
import pymysql
import requests
import traceback
import random
import login

def getMovie():
    sort = 'T'
    range = '0,10'
    tags = '电影'
    start = 0

    header = {
        "Cookie": 'bid=JghEKk7X-2A; __utma=30149280.1700385934.1523158608.1525661550.1525672953.7; __'
                  'utmz=30149280.1525661550.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; _'
                  'pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1525673000%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _'
                  'pk_id.100001.4cf6=496aa0a622b0b435.1524808171.4.1525673197.1525664260.; __yadk_'
                  'uid=RJWNziih4EsWTPIfQxTLE5jR9WPjyjJ5; _'
                  '_utma=223695111.2042794536.1524808175.1525661550.1525673000.4;'
                  'utmz=223695111.1525673000.4.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _'
                  'vwo_uuid_v2=DCB4CE8DE695EAB7D6510CFFE3DA94FAE|bb40a1425a73b626fdd1dd295f0f6e45; __'
                  'utmc=30149280; __utmc=223695111; __utmb=30149280.5.10.1525672953; __'
                  'utmt=1; ps=y; push_noty_num=0; push_doumail_num=0; _pk_ses.100001.4cf6=*; __'
                  'utmb=223695111.0.10.1525673000; ap=1; dbcl2="103623208:nBAzO0a38XQ"; ck=H49T; __'
                  'utmv=30149280.10362'
    }

    while True:
        doubanUrl = 'https://movie.douban.com/j/new_search_subjects?sort=%s&range=%s&tags=%s&start=%d' \
                    % (sort, range, tags, start)

        session = requests.Session()
        try:
            result = session.get(doubanUrl, headers=header)
            code = result.status_code
            if code == 403:
                userName = input("请输入用户名：")
                password = input("请输入密码：")
                response = login(userName, password)
            movieJson = json.loads(result.text)
            listData = movieJson['data']
            conDataBase(listData)
            i = 5 + float(random.randint(1, 100)) / 20
            print("停留%s秒" % i)
            # time.sleep(i)
            if len(listData) == 0:
                break
            start += 20
        except Exception as e:
            traceback.print_exc()
            print("错误！原因：", e)

def main():
    print(getMovie())



def conDataBase(listData):
    # 连接数据库
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='ideal',
        charset='utf8'
    )
    # 获取游标
    cursor = db.cursor()

    for dict in listData:
        sql = "INSERT INTO movie(title,rate,url) VALUES ('%s','%s','%s')" % ((dict['title']), dict['rate'], dict['url'])
        print("SQL：",sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as info:
            db.rollback()
            print("错误！原因：", info)


if __name__ == '__main__':
    main()
