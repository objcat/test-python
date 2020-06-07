# description: test
# date: 2020/6/7 17:59
# author: objcat
# version: 1.0

from tools import ztr


def haha(name, *args, **kwargs):
    print(args)
    print(kwargs)
    print("233333")
    print(name)


def start():
    # ztr非常方便可以直接传参
    ztr.run("123", haha(123, 456, foot="123"))


if __name__ == '__main__':
    start()
