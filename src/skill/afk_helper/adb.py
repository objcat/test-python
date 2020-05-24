import datetime
import os
import re

import PIL
import numpy as np

from skill.afk_helper.config import *


class Adb:

    def get_screen_size(self):
        """
        获取屏幕高度getter方法
        有时候真机和模拟器的高度和宽度是相互颠倒的 所以这里取大值做高度 小值做高度
        :return: (w, h)
        """
        if self.__screen_size == (0, 0):
            size_str = os.popen(f"adb -s {self.__device} shell wm size").read()
            m = re.search(r'(\d+)x(\d+)', size_str)

            a = int(m.group(1))
            b = int(m.group(2))

            width, height = 0, 0

            # 取大值作为高度
            if a > b:
                width = b
                height = a
            else:
                width = a
                height = b

            print("成功获取屏幕高度 ", "屏幕宽度", width, "屏幕高度", height)

            if m:
                return width, height
        else:
            return self.__screen_size

    def __init__(self, device):
        self.__device = device
        self.__screen_size = (0, 0)
        self.connect(device)

    def np_screencap(self):
        """
        返回图片的 np.array
        :return: array
        """
        print(f"adb -s {self.__device} exec-out screencap -p > sc.png")
        os.system(f"adb -s {self.__device} exec-out screencap -p > sc.png")
        return np.array(PIL.Image.open('sc.png'), dtype="uint8")

    def save_screencap(self):
        """
        保存截图到本地
        :return:
        """
        os.system(f"adb -s {self.__device} exec-out screencap -p > sc.png")

    def click(self, key):
        """
        点击按键
        :param key: 按键指令 在key.py中进行设置
        :return:
        """
        name = key["name"]
        x, y = key["point"]

        print(f"[{datetime.datetime.now()}] 点击{name} x={x} y={y}")
        os.system(f"adb -s {self.__device} shell input tap {x} {y}")

    def connect(self, device):
        os.system(f"adb connect {device}")

    def disconnect(self):
        os.system("adb disconnect")


adb = Adb(device)
