# description: qt平台封装
# date: 2020/6/9 1:18
# author: objcat
# version: 1.0
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

def show_dialog():

    pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle('123')
    win.resize(300, 200)
    win.show()
    sys.exit(app.exec_())

