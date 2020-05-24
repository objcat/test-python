from skill.afk_helper.adb import adb

class Size:
    """
    屏幕尺寸转换类, 基于 720 1280 进行屏幕坐标等比例缩放
    理论上可以支持所有分辨率但对于一些特殊机型 还是不能完全实现适配
    """
    width_fix = 0
    height_fix = 0
    screen_width = 0
    screen_height = 0

    def __init__(self, size):
        self.screen_width, self.screen_height = size
        if self.screen_height == 2340:
            self.height_fix = 0.03

    def width(self, width):
        width = (width / 720.0 + self.width_fix) * float(self.screen_width)
        return int(width)

    def height(self, height):
        height = (height / 1280.0 + self.height_fix) * float(self.screen_height)
        return int(height)


size = Size(adb.get_screen_size())
