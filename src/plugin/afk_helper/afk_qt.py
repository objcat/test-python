# description: afk_qt
# date: 2020/6/7 16:24
# author: objcat
# version: 1.0

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *

from plugin.afk_helper import gl
from plugin.afk_helper.pages.main import afk_main
from tools import ztr


class AFKMainWindow(QMainWindow):

    def __init__(self):
        super(AFKMainWindow, self).__init__()
        # 初始化ui
        self.ui = afk_main.Ui_MainWindow()
        # 设置ui
        self.ui.setupUi(self)
        # 绑定数据
        self.bind_data()
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
        # 自动抓牌
        self.ui.auto_pai.clicked.connect(lambda: self.btn_action(self.ui.auto_pai))
        # 终止所有操作
        self.ui.stop_all_btn.clicked.connect(lambda: self.btn_action(self.ui.stop_all_btn))
        # device下拉框
        self.ui.device_combo_box.currentIndexChanged.connect(
            lambda: self.device_combo_box_change(self.ui.device_combo_box))
        # 连接
        self.ui.connect_btn.clicked.connect(lambda: self.connect_device())
        # 单选框
        self.ui.radio0.clicked.connect(lambda: self.choose_radio(self.ui.radio0))
        self.ui.radio1.clicked.connect(lambda: self.choose_radio(self.ui.radio1))
        self.ui.radio2.clicked.connect(lambda: self.choose_radio(self.ui.radio2))
        self.ui.radio3.clicked.connect(lambda: self.choose_radio(self.ui.radio3))

    def choose_radio(self, radio):
        if radio == self.ui.radio0:
            gl.breakthrough_num = 0
        elif radio == self.ui.radio1:
            gl.breakthrough_num = 1
        elif radio == self.ui.radio2:
            gl.breakthrough_num = 2
        elif radio == self.ui.radio3:
            gl.breakthrough_num = 3

    def connect_device(self):
        gl.zstr.log("尝试重新连接")
        gl.init_device_info()

    def btn_action(self, btn):

        if gl.isConnected is False:
            gl.zstr.log("设备未连接, 请点击连接")
            return

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

        if btn == self.ui.auto_pai:
            ztr.add('自动打牌', lambda: gl.afk.auto_da_pai())

        if btn == self.ui.stop_all_btn:
            gl.zstr.log("终止所有操作")
            ztr.stop_all()
            return

    def bind_data(self):
        for device in gl.device_list:  # type: gl.Device
            self.ui.device_combo_box.addItem(device.display_name)

    def device_combo_box_change(self, box):
        # 获取设备索引
        i = box.currentIndex()
        # 更改当前设备
        gl.current_device = gl.device_list[i]


def start():
    # 创建app
    app = QApplication(sys.argv)
    # 创建加载图 - 这里要先创建启动图, 先初始化资源会造成软件界面卡顿
    splash = show_launch_screen()
    # 初始化设备
    gl.init()
    # 初始设备相关
    gl.init_device_info()
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
