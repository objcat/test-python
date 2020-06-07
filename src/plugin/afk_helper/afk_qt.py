# description: afk_qt
# date: 2020/6/7 16:24
# author: objcat
# version: 1.0

import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from plugin.afk_helper.pages.main import afk_main
from tools import ztr
from plugin.afk_helper import gl


class AFKMainWindow(QMainWindow):

    def __init__(self):
        super(AFKMainWindow, self).__init__()
        # 初始化ui
        self.ui = afk_main.Ui_MainWindow()
        # 设置ui
        self.ui.setupUi(self)
        # 绑定点击事件
        self.bind_slot()
        # 设置标题
        self.setWindowTitle('afk assistant')

    def bind_slot(self):
        # 显示屏幕
        self.ui.show_screen_cut_btn.clicked.connect(lambda: self.btn_action(self.ui.show_screen_cut_btn))
        # 绘制特征线
        self.ui.draw_sift_line_btn.clicked.connect(lambda: self.btn_action(self.ui.draw_sift_line_btn))
        # 打印特征
        self.ui.print_distance_btn.clicked.connect(lambda: self.btn_action(self.ui.print_distance_btn))
        # 自动挑战
        self.ui.auto_challenge_btn.clicked.connect(lambda: self.btn_action(self.ui.auto_challenge_btn))
        # 自动爬塔
        self.ui.auto_tower_btn.clicked.connect(lambda: self.btn_action(self.ui.auto_tower_btn))
        # 终止所有操作
        self.ui.stop_all_btn.clicked.connect(lambda: self.btn_action(self.ui.stop_all_btn))

    def btn_action(self, btn):

        if btn == self.ui.show_screen_cut_btn:
            # 由于plt只能在主线程中调用
            gl.afk.show_screen()
            return

        if btn == self.ui.draw_sift_line_btn:
            gl.afk.make_sift_line()
            return

        if btn == self.ui.print_distance_btn:
            ztr.add('打印特征', lambda: gl.afk.log_sift_distance())
            return

        if btn == self.ui.auto_challenge_btn:
            ztr.add('自动挑战2.0', lambda: gl.afk.auto_challenge2())
            return

        if btn == self.ui.auto_tower_btn:
            ztr.add('自动爬塔', lambda: gl.afk.auto_challenge_king_tower())
            return

        if btn == self.ui.stop_all_btn:
            gl.adb.log("终止所有操作")
            ztr.stop_all()
            return


def start():
    # 创建app
    app = QApplication(sys.argv)
    # 创建加载图 - 这里要先创建启动图, 先初始化资源会造成软件界面卡顿
    splash = show_launch_screen()
    # 初始化全局变量
    gl.init()
    # 关掉启动图
    splash.close()
    # 创建主窗口
    win = AFKMainWindow()
    # 显示窗口
    win.show()
    # 设置runloop
    sys.exit(app.exec_())


def show_launch_screen():
    # 创建启动图
    splash = QSplashScreen(QtGui.QPixmap('./img/launch.png'))
    # 展示启动图
    splash.show()
    # 附加信息
    # splash.showMessage('正在加载....')
    return splash


if __name__ == '__main__':
    start()
