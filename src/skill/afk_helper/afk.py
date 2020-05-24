# description: 剑与远征自动推图
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

import time

import cv2
import matplotlib.pyplot as plt

from skill.afk_helper import key
from skill.afk_helper.adb import adb
from skill.afk_helper.zcv import zcv


class AFK:

    # 开始
    def start(self):
        # img1 = adb.cv_rgb_screencap()
        # img2 = zcv.imread("./img/1.png")

        self.auto_challenge2()


        # for i in range(100):
        #     zcv.bf(img1, img2, True)
        #     time.sleep(3)



        # zcv.get_point_center(img1, img2, True)

        # print(cv2.__version__)

        # 屏幕截图
        # self.show_screen()
        # 自动推关
        # self.auto_challenge()

        # 图像识别
        # image = self.cv_read("./img/3.png")
        # self.get_button_center(image, True)

    def show_screen(self):
        zcv.imshow(adb.cv_rgb_screencap())

    def auto_challenge(self):
        """
        自动推图 1.0
        :return:
        """
        for i in range(100):
            # 点击挑战首领
            adb.click(key.challenge_boss)
            time.sleep(1)
            # 点击弹窗中的挑战首领(有时会出现)
            adb.click(key.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            adb.click(key.battle)
            time.sleep(25)
            # 点击空白
            adb.click(key.white_place)
            time.sleep(1)

    def auto_challenge2(self):
        """
        自动推图 2.0 加入图像识别
        :return:
        """

        # 点击挑战首领
        adb.click(key.challenge_boss)
        time.sleep(1)

        for i in range(100):
            # 点击弹窗中的挑战首领(有时会出现)
            adb.click(key.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            adb.click(key.battle)
            time.sleep(10)
            # 15截图等待结束
            while 1:
                img1 = adb.cv_rgb_screencap()
                img2 = zcv.imread("./img/1.png")
                d = zcv.bf_distance(img1, img2)
                print(d)
                if d == 31.575305938720703:
                    print("战斗失败, 即将重新挑战!")
                    break
                time.sleep(1)
            # 点击再次挑战
            adb.click(key.retry)
            time.sleep(1)


if __name__ == '__main__':
    afk = AFK()
    afk.start()
