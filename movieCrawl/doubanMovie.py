# -*- coding: utf-8 -*-
import requests, json,pymysql


def getMovie():
    sort = 'T'
    range = '0,10'
    tags = '电影'
    start = 0
    while True:
        print('正在获取第%d页...' % start)
        doubanUrl = 'https://movie.douban.com/j/new_search_subjects?sort=%s&range=%s&tags=%s&start=%d' \
                    % (sort, range, tags, start)
        start = start + 20
        session = requests.Session()
        result = session.get(doubanUrl)
        movieJson = json.loads(result.text)
        listData = movieJson['data']
        print(len(listData))
        # TODO 将前200条数据插入数据库
        for dict in listData:
            print(dict)
        if len(listData) == 0:
            break


def main():
    print(getMovie())

def conDataBase():
    # 连接数据库
    connect = pymysql.Connect(
        host='47.93.235.231',
        port=3306,
        user='lhch',
        passwd='123456',
        db='test',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()



if __name__ == '__main__':
    main()
