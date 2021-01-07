# description: 1
# date: 2021/1/7 12:57 下午
# author: objcat
# version: 1.0

"""
练习1：华氏温度转换为摄氏温度。

提示：华氏温度到摄氏温度的转换公式为：C = (F - 32) / 1.8。
"""

def Celsius(f):
    # 输出小数点后一位
    return "%.1f" % ((f - 32) / 1.8)

print(Celsius(100))
