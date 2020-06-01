# description: test_lambda
# date: 2020/6/1 5:06 下午
# author: objcat
# version: 1.0

import time


# lambda其实是一种函数的缩写

# 1，lambda 函数不能包含命令，
# 2，包含的表达式不能超过一个。

# 1.基本使用

# 加法
p = lambda x, y: x + y
print(p(1, 2))

# 乘法
p = lambda x: x * x
print(p(3))

# 2.替换某些函数
time.sleep = lambda x: None
time.sleep(3)
print("sleep over")

# 3.结合map使用

"""
map就是把数组中的每个值都传入函数, 然后批量进行处理
"""

m = map(lambda x: x ** x, [1, 2, 3, 4, 5])
print(list(m))  # [1, 4, 27, 256, 3125]

# 4.结合reduce使用 (首先取出1, 2个元素进行函数 然后用结果与第3个元素再次进行函数 以此类推)
from functools import reduce, cmp_to_key
m = reduce(lambda x, y: x + y, [1, 2, 3, 4])
# m2 = sum([1, 2, 3, 4]) # 求和
print(m)

# 5.结合sorted使用
m = sorted([1, 5, 12, 6, 7, 9, 7])
print(m)

# 排序元组 如果只是淡村的排序 sorted回取第一个元素
m = sorted([('a', '1'), ('f', '2'), ('b', '3')])
print(m)

# 排序元组使用第二个参数进行排序
m = sorted([('a', '1'), ('f', '2'), ('b', '3')])

cmp = lambda x, y:(x > y) - (x < y)
# 通过lamda表达式让sorted根据每个元组中第二个元素进行排序
m = sorted([('a', '1'), ('f', '2'), ('b', '3')], key=cmp_to_key(lambda x, y: cmp(x[1], y[1])))
print(m)
