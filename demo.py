import requests,json,datetime,calendar

# 登录 url
loginUrl = 'http://210.51.169.193:8080/login.whtml'
# 登录信息  dumps:将 Python 对象编码成 JSON 字符串
jsonData = json.dumps(
    {
        'user': {
            'userName': '60000852',
            'password': '60000852'
        },
        'loginURL': 'http://210.51.169.193:8080/login.html'
    })

userAgent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'
headers = {
    'User-Agent': userAgent,
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json'
}
s = requests.Session()
responseIndex = s.post(loginUrl, data=jsonData, headers=headers)
# 提取cookies
cookies = {c.name: c.value for c in responseIndex.cookies}

queryUrl = 'http://210.51.169.193:8080/system/queryCurrentUserInfo.whtml'
responseUserInfo = requests.get(queryUrl, cookies=cookies)

datetimeDate = datetime.date
firstMonthDay = datetimeDate(datetimeDate.today().year,datetimeDate.today().month,1)
print("月初：%s "%firstMonthDay)
# 今天的日期
currentDate = datetime.datetime.today().date()
print("今天：%s"%currentDate)
jsonData = {
    'cardQueryParameter.begin': firstMonthDay,
    'cardQueryParameter.end': currentDate,
    'start': 0,
    'count': 31
}
userCardInfoUrl = 'http://210.51.169.193:8080/selfProcess/queryCurrentUserCardInfo.whtml'
s1 = requests.Session()
responseIserCardInfoUrl = s1.post(userCardInfoUrl, data=jsonData,  cookies=cookies)


print(responseIserCardInfoUrl.text)
