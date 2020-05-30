# description: 剑与远征自动推图
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

import time

from plugin.afk_helper.adb import adb
from plugin.afk_helper.zcv import zcv
from plugin.afk_helper.key_model import key_list, KeyModel, KeyList


class AFK:

    # 开始
    def start(self):

        # img1 = adb.cv_rgb_screencap_cut_ratio_num(0)
        # zcv.imshow(img1)

        # 自动推图2.0
        # self.auto_challenge2()

        self.auto_challenge_king_tower()

        # self.waiting_keys([key_list.retry, key_list.king_tower_continue])

        # 测试使用

        # 屏幕截图
        # self.show_screen()

        # img1 = adb.cv_rgb_screencap()
        # img1 = adb.cv_rgb_screencap_cut((352, 1885, 731, 2017))
        # img2 = zcv.imread("./img/touch_screen_continue.png")

        # 识别画线
        # zcv.bf(img1, img2, True)
        # 获取特征点
        # distance = zcv.bf_distance(img1, img2)
        # print(distance)

        pass

    def show_screen(self):
        zcv.imshow(adb.cv_rgb_screencap())

    def auto_challenge(self):
        """
        自动推图 1.0
        """
        for i in range(100):
            # 点击挑战首领
            adb.click(key_list.challenge_boss)
            time.sleep(1)
            # 点击弹窗中的挑战首领(有时会出现)
            adb.click(key_list.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            adb.click(key_list.battle)
            time.sleep(25)
            # 点击空白
            adb.click(key_list.white_place)
            time.sleep(1)

    def auto_challenge2(self):
        """
        自动推图 2.0 加入图像识别
        """

        # 点击挑战首领
        adb.click(key_list.challenge_boss)
        time.sleep(1)

        for i in range(100):
            # 点击弹窗中的挑战首领(有时会出现)
            adb.click(key_list.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            adb.click(key_list.battle)
            time.sleep(10)
            # 10秒后开始截图监听结束状态
            waiting_key = self.waiting_keys([key_list.retry, key_list.next])

            if waiting_key == key_list.retry:
                adb.log("战斗失败, 即将重新挑战!")
                adb.click(waiting_key)
                time.sleep(1)
                continue

            if waiting_key == key_list.next:
                adb.log("挑战成功, 即将进入下一关!")
                adb.click(waiting_key)
                time.sleep(1)
                continue

    king_tower_flag = 0

    def auto_challenge_king_tower(self):

        for i in range(100):

            if self.king_tower_flag == 0:
                # 滑动到最下方
                swipe_key = (100, 500, 100, 1000)
                adb.swipe(swipe_key)
                time.sleep(1)

                # 点击挑战王座之塔
                adb.click(key_list.king_challenge)
                time.sleep(1)

            # 点击挑战
            adb.click(key_list.battle)
            time.sleep(10)

            # 10秒后开始截图监听结束状态
            # waiting_key = self.waiting_keys([key_list.retry, key_list.king_tower_continue])
            waiting_key = self.waiting_keys_2([key_list.retry, key_list.king_tower_continue])

            if waiting_key is key_list.retry:
                adb.log("战斗失败, 即将重新挑战!")
                adb.click(waiting_key)
                time.sleep(1)
                self.king_tower_flag = 1
                continue

            if waiting_key is key_list.king_tower_continue:
                adb.log("挑战王座之塔成功, 即将点击屏幕")
                adb.click(waiting_key)
                time.sleep(1)
                self.king_tower_flag = 0
                continue

    def waiting_keys(self, keys):
        # 建立计数索引
        i = {}
        for key in keys:
            key: KeyModel
            i[key.en_name] = 0
        while 1:
            flag = 0
            for key in keys:
                cut_ratio = 0
                if key.cut_ratio is not None:
                    cut_ratio = key.cut_ratio

                img1 = adb.cv_rgb_screencap_cut_ratio_num(cut_ratio)
                img2 = zcv.imread(key.img)
                d, pt = zcv.bf_distance(img1, img2)

                i[key.en_name] += 1

                if i[key.en_name] >= 35:
                    adb.log(f'特征匹配失败, 请在{key.en_name}的distance字段中加入或替换, "{adb.ratio_key}": "{d}"')

                adb.log(f"识别到特征 {d} 目标特征 {key.distance}")

                if str(d) is key_list.retry.distance:
                    return key_list.retry

                if str(d) is key_list.next.distance:
                    return key_list.next

                if str(d) is key_list.king_tower_continue.distance:
                    return key_list.king_tower_continue

    def waiting_keys_2(self, keys):
        # 建立计数索引
        for key in keys:
            key: KeyModel
        while 1:
            flag = 0
            for key in keys:
                cut_ratio = 0
                if key.cut_ratio is not None:
                    cut_ratio = key.cut_ratio

                img1 = adb.cv_rgb_screencap_cut_ratio_num(cut_ratio)
                img2 = zcv.imread(key.img)
                d, pt = zcv.bf_distance(img1, img2)

                adb.log(f"特征点{d}")
                if d <= 40:
                    adb.log(f"匹配到坐标点为 {pt}")
                    key.point = pt
                    return key
                    pass


if __name__ == '__main__':
    afk = AFK()
    afk.start()
