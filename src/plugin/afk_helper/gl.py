# description: 全局变量管理类
# date: 2020/6/7 19:19
# author: objcat
# version: 1.0


from plugin.afk_helper.afk import AFK
from plugin.afk_helper.adb import Adb
from plugin.afk_helper.key import KeyList
from plugin.afk_helper import config

"""
此处保存全局变量, 可以灵活的在程序中进行控制
"""


# adb
adb = None
# key_list
key_list = None
# afk
afk = None


def init():
    # 初始化adb
    global adb
    adb = Adb(config.device)
    # 初始化key_list
    global key_list
    key_list = KeyList.init_with_db()
    # 初始化afk
    global afk
    afk = AFK()
