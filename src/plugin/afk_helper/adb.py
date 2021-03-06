# description: adb工具类
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

import datetime
import os
import re
import PIL
import numpy as np
import matplotlib.pyplot as plt
import cv2
from plugin.afk_helper import config
from tools import zstr
from plugin.afk_helper import gl


class Adb:

    def __init__(self, device):
        self.adb = config.adb_path
        self.device = device
        self.rp = ""
        self.__screen_size = (0, 0)
        self.connect(device)
        self.get_screen_size()

    def get_screen_size(self):
        """
        获取屏幕高度getter方法
        有时候真机和模拟器的高度和宽度是相互颠倒的 所以这里取大值做高度 小值做高度
        :return: (w, h)
        """
        if self.__screen_size == (0, 0):
            shell = f"{self.adb} -s {self.device} shell wm size"
            size_str = None
            try:
                size_str = os.popen(shell).read()
                print(size_str)
            except Exception:
                print(Exception)

            if zstr.isEmpty(size_str) is True:
                gl.isConnected = False
                gl.zstr.log("设备连接失败, 请重新连接")
                return
            else:
                gl.zstr.log(f"成功连接到 {gl.current_device.display_name}")
                gl.isConnected = True

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

            self.rp = ratio_key = str(width) + "x" + str(height)

            log = "屏幕宽度 " + str(width) + " 屏幕高度 " + str(height)
            gl.zstr.log(log)

            if m:
                self.__screen_size = (width, height)
                return self.__screen_size
            else:
                return 0, 0

        else:
            return self.__screen_size

    def np_screencap(self):
        """
        返回图片的 np.array
        :return: array
        """
        shell = f"{self.adb} -s {self.device} exec-out screencap -p > ./img/sc.png"
        print(shell)
        os.system(shell)
        return np.array(PIL.Image.open('img/sc.png'), dtype="uint8")

    def cv_rgb_screencap(self):
        shell = f"{self.adb} -s {self.device} exec-out screencap -p > ./img/sc.png"
        os.system(shell)
        image = cv2.imread("img/sc.png")
        b, g, r = cv2.split(image)
        img_rgb = cv2.merge([r, g, b])
        return img_rgb

    def cv_rgb_screencap_cut_x1_y1_x2_y2(self, cut_point):
        img_rgb = self.cv_rgb_screencap()
        x1, y1, x2, y2 = cut_point
        img_cut = img_rgb[y1:y2, x1:x2]
        return img_cut

    def cv_rgb_screencap_cut_ratio_num(self, ratio_num: str = 0):
        """
        根据比例截取 0 ~ 1
        :param ratio_num: 截取高度开始比例 比例 * 高度 起始
        :return:
        """
        if ratio_num == 0:
            return self.cv_rgb_screencap()

        screen_width = self.__screen_size[0]
        screen_height = self.__screen_size[1]
        cut_point = 0, int(float(ratio_num) * int(screen_height)), screen_width, screen_height
        cut_img = self.cv_rgb_screencap_cut_x1_y1_x2_y2(cut_point)
        return cut_img

    def pl_screencap(self):
        os.system(f"{self.adb} -s {self.device} exec-out screencap -p > ./img/sc.png")
        return plt.imread("./img/sc.png")

    def save_screencap(self):
        """
        保存截图到本地
        :return:
        """
        os.system(f"{self.adb} -s {self.device} exec-out screencap -p > ./img/sc.png")

    def click(self, key):
        """点击按键
        :param key: 按键指令 在key.py中进行设置
        :return:
        """

        from plugin.afk_helper.model.key import Key
        key: Key

        name = key.name
        x, y = key.point
        gl.zstr.log(f"点击{name} x={x} y={y}")
        os.system(f"{self.adb} -s {self.device} shell input tap {x} {y}")

    def swipe(self, key):
        x1, y1, x2, y2 = key
        gl.zstr.log(f"滑动屏幕 从 {x1, y1} 到 {x2, y2}")
        os.system(f"{self.adb} -s {self.device} shell input swipe {x1} {y1} {x2} {y2}")

    def connect(self, device):
        os.system(f"{self.adb} connect {self.device}")

    def disconnect(self):
        os.system(f"{self.adb} disconnect")
