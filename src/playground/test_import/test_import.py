# description: test
# date: 2020/6/7 19:07
# author: objcat
# version: 1.0


# from playground.test_import.a import A
from playground.test_import import a
from playground.test_import import b
from playground.test_import.tool import Tool
from playground.test_import import gl


def start():

    gl.tool = Tool()

    aa = a.A()
    aa.use()

    bb = b.B()
    bb.use()


    pass



if __name__ == '__main__':
    start()