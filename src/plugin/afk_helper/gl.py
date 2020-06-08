# description: 全局变量管理类
# date: 2020/6/7 19:19
# author: objcat
# version: 1.0


from plugin.afk_helper.afk import AFK
from plugin.afk_helper.adb import Adb
from plugin.afk_helper.model.key import KeyList
from plugin.afk_helper import config
from tools.zsq3 import Zsq3
from plugin.afk_helper.model.device import Device
from tools import zstr

"""
此处保存全局变量, 可以灵活的在程序中进行控制
"""

# db
db = None
# adb
adb = None
# key_list
key_list = None
# afk
afk = None
# 设备列表
device_list = None
# 当前设备
current_device = None
# 设备是否连接成功
isConnected = False


def init():
    global device_list
    global current_device
    global db
    global afk
    # 初始化数据库
    db = Zsq3(config.db)
    # 初始化设备列表
    device_list = Device.device_list(db)
    # 设置默认设备
    try:
        current_device = device_list[0]
    except:
        print("设备列表为空, 请在数据库中添加")
        pass
    # 初始化afk
    afk = AFK()


def init_device_info():
    # 导入全局变量 否则不能进行改变
    global adb
    global key_list

    # 初始化adb
    adb = Adb(current_device.device)

    if isConnected == False:
        return

    # 通过数据库初始化key_list
    key_list = KeyList.init_with_db(db)

