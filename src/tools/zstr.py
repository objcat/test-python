# description: 封装字符串工具类
# date: 2020/6/5 20:38
# author: objcat
# version: 1.0

import datetime


def isEmpty(string):
    if string is None or string == '':
        return True
    else:
        return False


def log(text):
    print(f"[{datetime.datetime.now()}] {text}")
