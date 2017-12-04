import datetime


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


if __name__ == '__main__':
    print(getFirstDay())
