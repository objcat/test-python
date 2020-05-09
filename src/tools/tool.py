"""
 description: tool.py
 time: 2019/9/1 10:57
 author: objcat
 version: 1.0
"""
import time
import os
from configs.config import *
# import pymongo

# client = pymongo.MongoClient(MONGO_URL)


def write_to_file(path, content):
    """写入字符串到文件
    :param content: 字符串
    :return: None
    """
    with open(path, 'a', encoding='utf-8') as txt:
        txt.write(content)


def sleep_5_do(function):
    """间隔五秒执行方法
    :param f:
    :return: None
    """
    time.sleep(5)
    function()


def sleep_1_print(content):
    """间隔一秒打印
    :param str: 需要打印的字符串或数字
    :return: None
    """
    time.sleep(1)
    print(content)

def mkdir(path):
    """
    创建文件夹
    :param path:
    :return:
    """
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    return path


# def save_to_mongo(tableName, dic):
#     table = client[MONGO_DB_NAME][tableName]
#     table.insert(dic)
