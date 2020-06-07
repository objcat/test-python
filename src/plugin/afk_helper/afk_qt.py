# description: afk_qt
# date: 2020/6/7 16:24
# author: objcat
# version: 1.0


from PyQt5.QtWidgets import *
from plugin.afk_helper.pages.main import afk_main
import sys


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
        self.ui.show_screen_cut_btn.clicked.connect(lambda: self.haha('123'))
        # 绘制特征线
        self.ui.draw_sift_line_btn.clicked.connect(lambda: xixi())
        pass

    def haha(self, name):
        print(name)


def xixi():
    print(xixi)


def start():
    # 创建app
    app = QApplication(sys.argv)
    # 创建主窗口
    win = AFKMainWindow()
    # 显示窗口
    win.show()
    # 设置runloop
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
