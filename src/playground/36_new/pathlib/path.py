# description: path
# date: 2020/8/4 9:44 上午
# author: objcat
# version: 1.0

import pathlib


"""
3.6新增路径构造工具
是否能兼容windows有待验证
"""


with open(pathlib.Path("1.txt")) as f:
    s = f.read()
    print(s)