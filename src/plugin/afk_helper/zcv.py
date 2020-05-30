# description: 封装opencv
# date: 2020/5/24 21:34 
# author: objcat 
# version: 1.0

import cv2
import matplotlib.pyplot as plt


class Zcv:

    def imread(self, path):
        """
        读取图片
        由于cv2读取的图片默认通道是 b g r 的这里把它封装成 r g b
        :param path: 图片路径
        :return: RGB图片
        """
        img = cv2.imread(path)
        b, g, r = cv2.split(img)
        rgb_img = cv2.merge([r, g, b])
        return rgb_img

    def imshow(self, image):
        """
        展示图片
        :param image: 图片
        :return:
        """
        plt.figure()
        plt.imshow(image, animated=True)
        plt.show()

    def get_point_center(self, img, template, debug):
        """
        模板匹配法 计算匹图片中心点
        :param template: 模板图片
        :param debug: 是否为调试模式 调试模式会画出识别的区域
        :return: 中心点坐标 x, y
        """
        h, w = template.shape[:2]

        if debug:
            self.imshow(img)
            self.imshow(template)

        # 模板匹配
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        print(min_val, max_val, min_loc, max_loc)

        if max_val < 0.45:
            return

        img2 = img.copy()

        x, y = max_loc

        # 计算中心点
        center_x = x + w / 2
        center_y = y + h / 2

        if debug:
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255.0, 255.0, 255.0), 2)
            self.imshow(img2)

        return center_x, center_y

    def bf(self, img1, img2, debug):
        """
        蛮力匹配
        :param img1: 图片1
        :param img2: 图片2
        :param debug: 是否调试模式
        :return:
        """

        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

        if debug:
            self.imshow(img3)

        return matches, kp1

    def bf_distance(self, img1, img2):
        matches, kp1 = self.bf(img1, img2, False)
        queryIdx = matches[0].queryIdx
        kp = kp1[queryIdx]
        return matches[0].distance, kp.pt


zcv = Zcv()
