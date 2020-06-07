# description: run_test_main.py
# date: 2020/6/7 14:22
# author: objcat
# version: 1.0

import sys
from playground.test_qt.QT2_useQTDesigner import test_main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


def start():
    print("start")
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    win = QMainWindow()
    # 引用自动生成的UI
    ui = test_main.Ui_MainWindow()
    # 将UI设置到主窗口上
    ui.setupUi(win)
    # 绑定事件
    bind_solt(ui)
    # 设置窗口居中
    center(win)
    # 初始化状态栏
    win.status = win.statusBar()
    # 状态栏进行显示信息
    win.status.showMessage('我是一个只显示五秒的消息', 5000)
    # 显示窗口
    win.show()
    # 设置runloop
    sys.exit(app.exec_())


def bind_solt(ui):
    ui.comboBox_2.currentIndexChanged.connect(lambda: currentIndexChanged(ui.comboBox_2))


def currentIndexChanged(box):
    print(box.currentText())


def center(win: QMainWindow):
    # 获取屏幕坐标系
    screen = QDesktopWidget().screenGeometry()
    size = win.geometry()
    new_left = (screen.width() - size.width()) / 2
    new_top = (screen.height() - size.height()) / 2
    win.move(new_left, new_top)


if __name__ == '__main__':
    start()
