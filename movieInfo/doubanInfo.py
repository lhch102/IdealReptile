# -*- coding: utf-8 -*-
import requests, json,pymysql


def getMovie():
    sort = 'T'
    range = '0,10'
    tags = '电影'
    start = 0
    movieList = []
    while True:
        print('正在获取第%d页...' % start)
        doubanUrl = 'https://movie.douban.com/j/new_search_subjects?sort=%s&range=%s&tags=%s&start=%d' \
                    % (sort, range, tags, start)
        start = start + 20
        session = requests.Session()
        result = session.get(doubanUrl)
        movieJson = json.loads(result.text)
        listData = movieJson['data']
        movieList.extend(listData)
        print(len(movieList))
        if len(movieList) == 200:
            # TODO 将前200条数据插入数据库
            movieList.clear()
        # for dict in movieList:
        #     print(dict)
        if len(listData) == 0:
            break
    movieList.append(listData)
    return movieList


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
