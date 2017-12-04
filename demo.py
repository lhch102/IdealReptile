import datetime
import json
import requests

html = 'http://210.51.169.193:8080'
# 登录 url
loginUrl = html + '/login.whtml'
userCardInfoUrl = html + '/selfProcess/queryCurrentUserCardInfo.whtml'


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
    headers = {
        'User-Agent': userAgent,
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    s = requests.Session()
    responseIndex = s.post(loginUrl, data=jsonData, headers=headers)
    return responseIndex


# queryUrl = 'http://210.51.169.193:8080/system/queryCurrentUserInfo.whtml'
# responseUserInfo = requests.get(queryUrl, cookies=cookies)
def resultData(userName, password):
    s1 = requests.Session()
    jsonData = {
        'cardQueryParameter.begin': getFirstDay(),
        'cardQueryParameter.end': currentDate(),
        'start': 0,
        'count': 31
    }

    responseIndex = login(userName, password)
    data = json.loads(responseIndex.text)
    if data['success']:
        # 提取cookies
        cookies = {c.name: c.value for c in responseIndex.cookies}
        responseIserCardInfoUrl = s1.post(userCardInfoUrl, data=jsonData, cookies=cookies)
        return data['message']+"\n"+responseIserCardInfoUrl.text
    else:
        return data['message']


# 获取月初第一天的日期
def getFirstDay():
    datetimeDate = datetime.date
    getfirstDay = datetimeDate(datetimeDate.today().year, datetimeDate.today().month, 1)
    return getfirstDay


# 获取当前日期
def currentDate():
    # 今天的日期
    currentDate = datetime.datetime.today().date()
    return currentDate


def main():
    userName = input("请输入用户名：")
    password = input("请输入密码：")
    print(resultData(userName, password))


if __name__ == '__main__':
    main()
