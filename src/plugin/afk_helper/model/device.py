# description: device
# date: 2020/6/7 23:00
# author: objcat
# version: 1.0

from tools.zsq3 import Zsq3


class Device:
    def __init__(self):
        self.id = None
        self.display_name = None
        self.device = None

    @classmethod
    def device_list(cls, db: Zsq3):
        """获取设备列表
        :param db:
        :return:
        """
        l = db.select_dic_list(Device)
        r = []
        for dic in l:
            device = cls()
            device.__dict__ = dic
            r.append(device)
        return r
