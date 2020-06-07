# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'afk_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_screen_cut_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_screen_cut_btn.setGeometry(QtCore.QRect(330, 100, 75, 23))
        self.show_screen_cut_btn.setObjectName("show_screen_cut_btn")
        self.draw_sift_line_btn = QtWidgets.QPushButton(self.centralwidget)
        self.draw_sift_line_btn.setGeometry(QtCore.QRect(330, 140, 75, 23))
        self.draw_sift_line_btn.setObjectName("draw_sift_line_btn")
        self.print_distance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_distance_btn.setGeometry(QtCore.QRect(330, 180, 75, 23))
        self.print_distance_btn.setObjectName("print_distance_btn")
        self.auto_challenge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.auto_challenge_btn.setGeometry(QtCore.QRect(330, 220, 75, 23))
        self.auto_challenge_btn.setObjectName("auto_challenge_btn")
        self.auto_tower_btn = QtWidgets.QPushButton(self.centralwidget)
        self.auto_tower_btn.setGeometry(QtCore.QRect(330, 260, 75, 23))
        self.auto_tower_btn.setObjectName("auto_tower_btn")
        self.stop_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_all_btn.setGeometry(QtCore.QRect(330, 300, 80, 23))
        self.stop_all_btn.setObjectName("stop_all_btn")
        self.device_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.device_combo_box.setGeometry(QtCore.QRect(20, 120, 121, 22))
        self.device_combo_box.setObjectName("device_combo_box")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.connect_btn.setObjectName("connect_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_screen_cut_btn.setText(_translate("MainWindow", "显示屏幕"))
        self.draw_sift_line_btn.setText(_translate("MainWindow", "绘制特征线"))
        self.print_distance_btn.setText(_translate("MainWindow", "打印特征"))
        self.auto_challenge_btn.setText(_translate("MainWindow", "自动挑战"))
        self.auto_tower_btn.setText(_translate("MainWindow", "自动爬塔"))
        self.stop_all_btn.setText(_translate("MainWindow", "终止所有操作"))
        self.connect_btn.setText(_translate("MainWindow", "连接"))
