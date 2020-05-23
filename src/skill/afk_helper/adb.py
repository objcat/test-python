import os
import PIL
import numpy as np
import re


class Adb:
    device = ""

    def np_screencap(self):
        print(f"adb -s {self.device} exec-out screencap -p > sc.png")
        os.system(f"adb -s {self.device} exec-out screencap -p > sc.png")
        return np.array(PIL.Image.open('sc.png'), dtype="uint8")

    def screencap(self):
        os.system(f"adb -s {self.device} exec-out screencap -p > sc.png")

    def click(self, x, y):
        print("开始点击屏幕", "x=", x, "y=", y)
        os.system(f"adb -s {self.device} shell input tap {x} {y}")

    def connect(self, ip):
        self.device = ip
        os.system(f"adb connect {ip}")

    def disconnect(self):
        os.system("adb disconnect")

    def screen_size(self):
        # return os.system(f"adb -s {self.device} shell wm size")
        size_str = os.popen(f"adb -s {self.device} shell wm size").read()
        m = re.search(r'(\d+)x(\d+)', size_str)
        # print(m.group(2), m.group(1))
        if m:
            return m.group(2), m.group(1)
