# description: da.py
# date: 2021/2/5 21:58
# author: objcat
# version: 1.0

from tools.adb import Adb


class Da:
    adb = Adb("5e49ca6b")
    adb.connect(adb.device)

    for i in range(100):
        adb.click(349, 890)



    pass


