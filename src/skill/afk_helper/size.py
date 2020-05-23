class Size:
    width_ratio = 0.4944
    height_ratio = 0.85
    width_fix = 0
    height_fix = 0
    screen_width = 0
    screen_height = 0


    def __init__(self, size):
        self.screen_width, self.screen_height = size

        print("初始化 ", "宽度", self.screen_width, "高度", self.screen_height)

        if self.screen_height == 2340:
            self.height_fix = 0.03
            pass

    def width(self, width):
        width = (width / 720.0 + self.width_fix) * float(self.screen_width)
        return int(width)

    def height(self, height):
        height = (height / 1280.0 + self.height_fix) * float(self.screen_height)
        return int(height)

    pass
