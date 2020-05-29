# description: 尺寸变化工具类
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

from plugin.afk_helper.adb import adb


class Size:
    """
    屏幕尺寸转换类, 基于 720 1280 进行屏幕坐标等比例缩放
    """
    screen_width = 0
    screen_height = 0

    def __init__(self, size):
        self.screen_width, self.screen_height = size

    def width(self, width):
        width = (width / 720.0) * float(self.screen_width)
        return int(width)

    def height(self, height):
        height = (height / 1280.0) * float(self.screen_height)
        return int(height)


size = Size(adb.get_screen_size())
