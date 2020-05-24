import time

import cv2
import matplotlib.pyplot as plt

from skill.afk_helper import key
from skill.afk_helper.adb import adb


class AFK:

    # 开始
    def start(self):
        # 屏幕截图
        self.show_screen()
        # 自动推关
        self.auto_challenge()

        # 图像识别
        # image = self.cv_read("./img/3.png")
        # self.get_button_center(image, True)

    def cv_read(self, path):
        img = cv2.imread(path)
        b, g, r = cv2.split(img)
        rgb_img = cv2.merge([r, g, b])
        return rgb_img

    def show_screen(self):
        # self.make_figure(adb.np_screencap())
        self.plt_show(adb.cv_rgb_screencap())

    def plt_show(self, image):
        plt.figure()
        plt.imshow(image, animated=True)
        plt.show()

    def get_button_center(self, template, debug):
        """
        返回匹配按钮中心点
        :param template: 模板
        :param debug: 是否为调试模式 调试模式会画出识别的区域
        :return: 中心点坐标 x, y
        """
        h, w = template.shape[:2]

        adb.save_screencap()

        screencast = self.cv_read("./img/sc.png")

        # 模板匹配
        result = cv2.matchTemplate(screencast, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(min_val, max_val, min_loc, max_loc)

        if max_val < 0.45:
            return

        img2 = screencast.copy()

        x, y = max_loc

        # 计算中心点
        center_x = x + w / 2
        center_y = y + h / 2

        if debug:
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255.0, 255.0, 255.0), 2)
            self.plt_show(img2)

        return center_x, center_y

    def auto_challenge(self):

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


if __name__ == '__main__':
    afk = AFK()
    afk.start()
