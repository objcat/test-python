# description: zdate
# date: 2021/1/8 1:22 下午
# author: objcat
# version: 1.0


from datetime import datetime, timedelta


def date_to_str_ymd(date):
    """
    日期转字符串
    :param date: 日期
    :return: 字符串日期 例 2021-01-18
    """
    return datetime.strftime(date, "%Y-%m-%d")


def str_to_date(str):
    """
    字符串转日期
    :param str: 日期字符串
    :return: datetime
    """
    return datetime.strptime(str, "%Y-%m-%d")


def nextday(date):
    """
    明天
    :param date: 日期对象
    :return: 明天的日期对象
    """
    return date + timedelta(days=1)


def lastday(date):
    """
    昨天
    :param date: 日期对象
    :return: 昨天的日期对象
    """
    return date - timedelta(days=1)
