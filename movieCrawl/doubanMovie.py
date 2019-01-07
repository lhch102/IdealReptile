# -*- coding: utf-8 -*-
import codecs
import datetime
import gzip
import json
import random
import string
import sys
import time
from http import cookiejar
from json import JSONDecodeError
from urllib import request
from urllib.parse import quote

import pymysql

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# 获取cookie对象
cookie = cookiejar.CookieJar()
# 返回一个cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 获取一个带有cookie请求管理器
opener = request.build_opener(cookie_handler)

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-CA;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Host": "movie.douban.com",
    "Upgrade - Insecure - Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36 "
}


def getRequest(url):
    """请求url函数"""
    url = quote(url, safe=string.printable)
    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    try:
        html = gzip.decompress(res.read()).decode('utf-8')
    except OSError:
        html = res.read().decode('utf-8')
    if html is None or html == '':
        return html
    try:
        json_html = json.loads(html)
    except JSONDecodeError as err:
        print("Json解析错误！原因：", err)
    except Exception as e:
        print("错误！原因：", e)
    return json_html


def getTags():
    """获取tags列表"""
    tags_url = 'https://movie.douban.com/j/search_tags'
    tags = getRequest(tags_url)
    return tags['tags']


def getMovie(start, tags):
    """获取影片列表"""
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%s&page_limit=20&page_start=%d' % (tags, start)
    print("爬取%s中的第%d" % (tags, start/20))
    return getRequest(url)
    # try:
    #     result = session.get(doubanUrl, headers=header)
    #     code = result.status_code
    #     if code == 403:
    #         userName = input("请输入用户名：")
    #         password = input("请输入密码：")
    #         response = login(userName, password)
    #     movieJson = json.loads(result.text)
    #     listData = movieJson['data']
    #     conDataBase(listData)
    #     i = 5 + float(random.randint(1, 100)) / 20
    #     print("停留%s秒" % i)
    #     # time.sleep(i)
    #     if len(listData) == 0:
    #         break
    #     start += 20
    # except Exception as e:
    #     traceback.print_exc()
    #     print("错误！原因：", e)


def queryInfo(cursor, title, grade, tags):
    sql = "select count(1) from movie_info where title='%s' and grade = '%s' and type = '%s'" % (title, grade, tags)
    try:
        # 使用execute()方法执行SQL查询
        cursor.execute(sql)
        # print("查询SQL：%s" % sql)
        # 使用fetchall()获取所有结果
        count = cursor.fetchone()[0]
        print("本次查询条数：%d" % count)
        return count
    except Exception as err:
        print("SQL执行错误，原因：", err)


def conDataBase(movieList, tags):
    # 连接数据库
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='movie',
        charset='utf8'
    )
    # 获取游标
    cursor = db.cursor()
    subjects = movieList['subjects']
    for movie in subjects:
        title = movie['title']
        grade = movie['rate']
        images = movie['cover']
        url = movie['url']
        count = queryInfo(cursor, title, grade, tags)
        if count > 0:
            break
        insert_sql = "insert into movie_info(title,grade,images,url,type,create_by,create_time) values (%s,%s,%s,%s,%s,%s,%s)"
        val = [(title, grade, images, url, tags, 'admin', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))]
        try:
            # 批量插入sql语句
            cursor.executemany(insert_sql, val)
            # 提交到数据库执行
            db.commit()
            # print("插入SQL：%s" % title)
        except Exception as err:
            db.rollback()
            print("插入SQL执行错误，原因：", err)
    db.close()
    cursor.close()


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
            # 'loginURL': html + '/login.html'
        }
    )

    headers = {"Cookie": 'viewed="4123377"; bid=dEiv72_xR-Q; gr_user_id=7a6e2bcc-480e-4e57-9d8e-70ce7c48ff0f; '
                         '_vwo_uuid_v2=D70CA279D4A09E3C2C9776974C30690FD|55daf29647f1d71a00a3438cdb8c63ca; '
                         '__utma=30149280.868029105.1532082385.1532082385.1532082385.1; __utmc=30149280; '
                         '__utmz=30149280.1532082385.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / '
                             '537.36(KHTML, like Gecko) Chrome/66.0.3359.181Safari / 537.36 '
               }
    # 登录 url
    loginUrl = 'https://accounts.douban.com/login'
    # response = requests.Session().post(loginUrl, data=jsonData, headers=headers)


def main():
    tagsList = getTags()
    for tags in tagsList:
        start = 0
        while True:
            moviedata = getMovie(start, tags)
            if moviedata is None or moviedata == '':
                break
            conDataBase(moviedata, tags)
            start += 20
            interval = 5 + float(random.randint(1, 100)) / 20
            time.sleep(interval)
            print("休眠：%s秒" % interval)


if __name__ == '__main__':
    main()
