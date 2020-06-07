# description: 开发第一个基于PyQt5的桌面应用
# date: 2020/6/7 12:42
# author: objcat
# version: 1.0

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(300, 150)
    # 移动窗口(设置窗口x,y)
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    # 显示窗口
    w.show()
    # 进入程序主循环, 并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

    pass


if __name__ == '__main__':
    main()
