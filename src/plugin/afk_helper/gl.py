# description: 全局变量管理类
# date: 2020/6/7 19:19
# author: objcat
# version: 1.0


from plugin.afk_helper.afk import AFK
from plugin.afk_helper.adb import Adb
from plugin.afk_helper.model.key import KeyList
from plugin.afk_helper import config
from tools.zsq3 import Zsq3

"""
此处保存全局变量, 可以灵活的在程序中进行控制
"""

# adb
adb = None
# key_list
key_list = None
# afk
afk = None
# 初始化device
device = None


def init():
    # 导入全局变量 否则不能进行改变
    global adb
    global key_list
    global afk
    global device

    # 初始化adb
    adb = Adb(config.device)
    # 初始化数据库
    db = Zsq3(config.db)
    # 通过数据库初始化key_list
    key_list = KeyList.init_with_db(db)
    # 初始化afk
    afk = AFK()
    # 初始化device
    # device = db.select()