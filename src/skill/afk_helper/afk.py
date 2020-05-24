import time

import cv2
import matplotlib.pyplot as plt

from skill.afk_helper import key
from skill.afk_helper.adb import adb


class AFK:
    # 初始化屏幕尺寸转换类

    # 开始
    def start(self):
        # 屏幕截图
        self.show_screen()
        # 自动推关
        self.auto_challenge()

    def show_screen(self):
        self.make_figure(adb.np_screencap())

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

        adb.save_screencap()

        screencast = cv2.imread("/img/sc.png", 0)

        # 模板匹配
        result = cv2.matchTemplate(screencast, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(min_val, max_val, min_loc, max_loc)

        if max_val < 0.5:
            return

        img2 = screencast.copy()

        x, y = max_loc

        # 计算中心点
        center_x = x + w / 2
        center_y = y + h / 2

        if debug:
            bottom_right = (x + w, y + h)
            cv2.rectangle(img2, (x, y), bottom_right, 255, 2)
            plt.imshow(img2)
            plt.show()

        return center_x, center_y

    def auto_challenge(self):

        # 点击挑战首领
        adb.click(key.challenge_boss)
        time.sleep(1)
        for i in range(100):
            # 点击弹窗中的挑战首领(有时会出现)
            adb.click(key.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            adb.click(key.battle)
            time.sleep(30)
            # 点击重试
            adb.click(key.retry)
            time.sleep(1)


if __name__ == '__main__':
    afk = AFK()
    afk.start()
