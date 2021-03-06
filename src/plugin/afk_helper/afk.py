# description: 剑与远征自动推图
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

import time

from plugin.afk_helper import gl
from tools.zcv import zcv
from tools import zstr
from plugin.afk_helper.model.key import Key


def func(event):
    print('you pressed', event.button, event.xdata, event.ydata)


class AFK:

    # 开始
    def start(self):
        pass

    def show_screen(self):
        zcv.imshow(gl.adb.cv_rgb_screencap())

    def make_sift_line(self):
        img1 = gl.adb.cv_rgb_screencap()
        img2 = zcv.imread("./img/next.png")
        zcv.bf(img1, img2, True)

    def log_sift_distance(self):
        img1 = gl.adb.cv_rgb_screencap()
        img2 = zcv.imread("./img/next.png")
        d, pt = zcv.bf_distance(img1, img2)
        print(d)
        print(pt)

    def auto_challenge(self):
        """自动推图1.0
        使用了固定坐标作为按钮定位点
        :return:
        """
        for i in range(100):
            # 点击挑战首领
            gl.adb.click(gl.key_list.challenge_boss)
            time.sleep(1)
            # 点击弹窗中的挑战首领(有时会出现)
            gl.adb.click(gl.key_list.second_challenge_boss)
            time.sleep(1)
            # 点击战斗
            gl.adb.click(gl.key_list.battle)
            time.sleep(25)
            # 点击空白
            gl.adb.click(gl.key_list.white_place)
            time.sleep(1)

    def auto_challenge2(self):
        """自动推图2.0
        加入了图像识别技术
        :return:
        """

        retry_flag = 0
        breakthrough_num = gl.breakthrough_num

        # 点击挑战首领
        gl.adb.click(gl.key_list.challenge_boss)
        time.sleep(1)

        for i in range(100):
            if retry_flag == 0 and breakthrough_num == 0:
                # 点击弹窗中的挑战首领(有时会出现)
                gl.adb.click(gl.key_list.second_challenge_boss)
                time.sleep(2)
            # 点击战斗
            gl.adb.click(gl.key_list.battle)
            time.sleep(10)
            # 10秒后开始截图监听结束状态
            waiting_key = self.waiting_keys([gl.key_list.retry, gl.key_list.next])
            # waiting_key = self.waiting_keys_2([gl.key_list.retry, gl.key_list.next])

            if waiting_key == gl.key_list.retry:
                gl.zstr.log("战斗失败, 即将重新挑战!")
                gl.adb.click(waiting_key)
                retry_flag = 1
                time.sleep(2)
                continue

            if waiting_key == gl.key_list.next:
                gl.zstr.log("挑战成功, 即将进入下一关!")
                gl.adb.click(waiting_key)
                retry_flag = 0
                breakthrough_num = self.setting_window_num(breakthrough_num)
                time.sleep(2)
                continue

    def setting_window_num(self, breakthrough_num):
        breakthrough_num += 1
        if breakthrough_num == 4:
            breakthrough_num = 0
        print(breakthrough_num)
        return breakthrough_num

    def auto_challenge_king_tower(self):
        """自动挑战王座之塔
        :return:
        """

        king_tower_flag = 0

        for i in range(100):

            if king_tower_flag == 0:
                # 滑动到最下方
                # swipe_key = (100, 500, 100, 1000)
                # adb.swipe(swipe_key)
                # time.sleep(1)

                # 点击挑战王座之塔
                gl.adb.click(gl.key_list.king_challenge)
                time.sleep(1)

            # 点击挑战
            gl.adb.click(gl.key_list.battle)
            time.sleep(10)

            # 10秒后开始截图监听结束状态
            # waiting_key = self.waiting_keys([gl.key_list.retry, gl.key_list.king_tower_continue])
            waiting_key = self.waiting_keys_2([gl.key_list.retry, gl.key_list.king_tower_continue])

            if waiting_key is gl.key_list.retry:
                gl.zstr.log("战斗失败, 即将重新挑战!")
                gl.adb.click(waiting_key)
                time.sleep(2)
                king_tower_flag = 1
                continue

            if waiting_key is gl.key_list.king_tower_continue:
                gl.zstr.log("挑战王座之塔成功, 即将点击屏幕")
                gl.adb.click(waiting_key)
                time.sleep(2)
                king_tower_flag = 0
                continue

    def auto_da_pai(self):

        while True:
            gl.adb.click(gl.key_list.xuan_pai)
            gl.adb.click(gl.key_list.zhua_pai)
            time.sleep(1)

        pass

    def waiting_keys(self, keys):
        """流程识别1.0
        匹配distance, 如果与key_model中的distance相等, 就说明是一个key
        :param keys:
        :return:
        """
        # 建立计数索引
        i = {}
        for key in keys:
            i[key.en_name] = 0
        while 1:
            flag = 0
            for key in keys:
                cut_ratio = 0
                if zstr.isEmpty(key.cut_ratio) is False:
                    cut_ratio = key.cut_ratio
                img1 = gl.adb.cv_rgb_screencap_cut_ratio_num(cut_ratio)
                img2 = zcv.imread(key.img)
                d, pt = zcv.bf_distance(img1, img2)

                i[key.en_name] += 1

                if i[key.en_name] >= 35:
                    gl.zstr.log(f'特征匹配失败, 请在{key.en_name}的distance字段中加入或替换, "{gl.adb.rp}": "{d}"')

                gl.zstr.log(f"识别到特征 {d} {key.en_name}: {key.distance}")

                if float(gl.key_list.retry.distance) + 1 >= d >= float(gl.key_list.retry.distance) - 1:
                    return gl.key_list.retry

                if float(gl.key_list.next.distance) + 1 >= d >= float(gl.key_list.next.distance) - 1:
                    return gl.key_list.next

                if float(gl.key_list.king_tower_continue.distance) + 1 >= d >= float(
                        gl.key_list.king_tower_continue.distance) - 1:
                    return gl.key_list.king_tower_continue

    def waiting_keys_2(self, keys):
        """流程识别2.0 (1.0进化方法)
        开启一个for循环匹配keys中img的特征, 如果特征相似度比较高, 就返回那个key, 并且把该特征对象的坐标(一般是按钮的坐标)赋值给key
        从而key可以进行点击操作
        :param keys: key的数组, 可以同时监控多个key
        :return: KeyModel
        """
        # 建立计数索引
        for key in keys:
            while 1:
                flag = 0
                for key in keys:
                    cut_ratio = 0
                    if zstr.isEmpty(key.cut_ratio) is False:
                        cut_ratio = key.cut_ratio

                    img1 = gl.adb.cv_rgb_screencap_cut_ratio_num(cut_ratio)
                    img2 = zcv.imread(key.img)
                    d, pt = zcv.bf_distance(img1, img2)

                    gl.zstr.log(f"开始匹配{key.en_name} 特征点{d}")
                    if d <= 40:
                        gl.zstr.log(f"匹配到坐标点为 {pt}")
                        key.point = pt
                        return key
                        pass
                    time.sleep(1)


if __name__ == '__main__':
    afk = AFK()
    afk.start()

# afk = AFK()
