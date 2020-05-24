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
        # 自动推图2.0
        self.auto_challenge2()

        # 识别特征
        # img1 = adb.cv_rgb_screencap()
        # img2 = zcv.imread("./img/next.png")
        # zcv.bf(img1, img2, True)

        # 屏幕截图
        # self.show_screen()
        # 自动推关
        # self.auto_challenge()

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
            # 10秒后开始截图监听成功或失败
            self.waiting_keys([key.retry, key.next], 1)

    def waiting_keys(self, keys, second):

        i = {}

        # 建立计数索引
        for keyy in keys:
            i[keyy['en_name']] = 0

        while 1:
            flag = 0
            for keyy in keys:
                img1 = adb.cv_rgb_screencap()
                img2 = zcv.imread(keyy["img"])
                d = zcv.bf_distance(img1, img2)

                i[keyy['en_name']] += 1

                if i[keyy['en_name']] >= 35:
                    adb.log(f'特征匹配失败, 请在{keyy["en_name"]}的distance字段中加入或替换, "{adb.ratio_key}": "{d}"')

                # adb.log(f"目标特征 {d}")
                # adb.log(f"按钮特征 {keyy['distance'][adb.ratio_key]}")

                if str(d) == key.retry['distance'][adb.ratio_key]:
                    adb.log("战斗失败, 即将重新挑战!")
                    flag = 1
                    adb.click(keyy)
                    time.sleep(1)

                if str(d) == key.next['distance'][adb.ratio_key]:
                    adb.log("挑战成功, 即将进入下一关!")
                    flag = 1
                    adb.click(keyy)
                    time.sleep(1)

            if flag == 1:
                break


if __name__ == '__main__':
    afk = AFK()
    afk.start()
