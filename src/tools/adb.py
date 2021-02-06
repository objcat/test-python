# description: Adb
# date: 2021/2/5 22:17
# author: objcat
# version: 1.0

import PIL
import os
from tools import zstr


class Adb:

    def __init__(self, device):
        self.device = device
        self.adb = "G:\\PycharmProjects\\test-python\\src\\plugin\\afk_helper\\adbs\\adb\\adb"

    def connect(self, device):
        os.system(f"{self.adb} connect {self.device}")

    def click(self, x, y):
        zstr.log(f"点击屏幕 x={x} y={y}")
        os.system(f"{self.adb} -s {self.device} shell input tap {x} {y}")
