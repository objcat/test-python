import os
import subprocess
import cv2
import numpy as np
import PIL
import matplotlib.pyplot as plt
import time

from skill.afk_helper.adb import Adb
from skill.afk_helper.size import Size


class AFK:
    adb = Adb()
    conver = {}

    # conver = SizeConver();

    def start(self):
        # 获取屏幕截图 - 调试使用
        # self.show_screencap()

        # 连接设备
        self.adb.connect("127.0.0.1:7555")
        # self.adb.connect("5e49ca6b")
        # 初始化转换工具
        self.conver = Size(self.adb.screen_size())

        self.auto_challenge()

    def show_screencap(self):
        self.make_figure(self.adb.np_screencap())

    def make_figure(self, image):
        figure = plt.figure()
        # 将图片画到坐标轴上面
        plt.imshow(image, animated=True)
        # 显示图片出来
        plt.show()

    def imshow(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_button_center(self, template, debug):
        """
        返回匹配按钮中心点
        :param template: 模板
        :param debug: 是否为调试模式 调试模式会画出识别的区域
        :return: 中心点坐标 x, y
        """
        h, w = template.shape[:2]

        self.adb.screencap()

        screencap = cv2.imread("sc.png", 0)

        # 模板匹配
        result = cv2.matchTemplate(screencap, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(min_val, max_val, min_loc, max_loc)

        if (max_val < 0.5):
            return

        img2 = screencap.copy()

        x, y = max_loc

        # 计算中心点
        centerX = x + w / 2
        centerY = y + h / 2

        if debug:
            bottom_right = (x + w, y + h)
            cv2.rectangle(img2, (x, y), bottom_right, 255, 2)
            plt.imshow(img2)
            plt.show()

        return centerX, centerY

    def auto_challenge(self):

        print("开始")
        print(self.conver.width(356))
        print(self.conver.height(1088))
        print("结束")

        # 点击挑战首领
        self.adb.click(self.conver.width(356), self.conver.height(1088))
        time.sleep(1)
        for i in range(100):
            # 点击挑战首领(优势互会出现)
            self.adb.click(self.conver.width(356), self.conver.height(980))
            time.sleep(1)
            # 点击战斗
            self.adb.click(self.conver.width(356), self.conver.height(1223))
            time.sleep(15)
            # 点击重试
            self.adb.click(self.conver.width(356), self.conver.height(1140))
            time.sleep(1)


if __name__ == '__main__':
    afk = AFK()
    afk.start()
