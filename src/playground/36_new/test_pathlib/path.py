# description: path
# date: 2020/8/4 9:44 上午
# author: objcat
# version: 1.0

import pathlib
import os


"""
3.6新增路径构造工具
是否能兼容windows有待验证
"""

# 读取文件
with open(pathlib.Path("1.txt")) as f:
    s = f.read()
    print(s)

"""
获取文件夹路径
"""

# os获取当前文件路径
print("os获取当前文件路径")
print(os.getcwd())

# pathlib获取当前文件路径
# 注:这里发现一个问题, 当外层路径为pathlib时则无法打印正确路径
# 显示为 /Users/macmini/project/python/test-python/src/playground/36_new
print("pathlib获取当前文件路径")
print(pathlib.Path.cwd())

# os获取上层路径
print("os获取上层路径")
print(os.path.dirname(os.getcwd()))

# pathlib获取上层路径
print("pathlib获取上层路径")
print(pathlib.Path.cwd().parent)

# os获取上上层路径
print("os获取上上层路径")
print(os.path.dirname(os.path.dirname(os.getcwd())))

# pathlib获取上上层路径
print("pathlib获取上上层路径")
print(pathlib.Path.cwd().parent.parent)

"""
拼接路径
"""

# os拼接路径
print("os拼接路径")
print(os.path.join(os.getcwd(), "test", "1.txt"))

# pathlib拼接路径
print("pathlib拼接路径")
print(pathlib.Path.cwd().joinpath("test", "1.txt"))

# pathlib拼接路径数组
print("pathlib拼接路径数组")
path = ["test", "2.txt"]
print(pathlib.Path.cwd().joinpath(*path))

# os创建文件夹 exist_ok: 默认为False如果文件夹存在提示错误信息, 为True后不提示错误信息文件夹不会覆盖
# print("os创建文件夹")
# os.makedirs(os.path.join('project', 'test'), exist_ok=True)

# pathlib创建文件夹
# print("pathlib创建文件夹")
# pathlib.Path("project", "test").mkdir(parents=True, exist_ok=True)

# os文件剪切
# os.rename(os.path.join("1.txt"), os.path.join("project", "test", "1.txt"))

# pathlib文件剪切
pathlib.Path("1.txt").rename(pathlib.Path("project", "test", "2.txt"))









