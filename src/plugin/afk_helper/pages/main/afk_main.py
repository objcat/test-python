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
        MainWindow.resize(733, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 150, 311, 231))
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_screen_cut_btn = QtWidgets.QPushButton(self.frame)
        self.show_screen_cut_btn.setObjectName("show_screen_cut_btn")
        self.verticalLayout.addWidget(self.show_screen_cut_btn)
        self.draw_sift_line_btn = QtWidgets.QPushButton(self.frame)
        self.draw_sift_line_btn.setObjectName("draw_sift_line_btn")
        self.verticalLayout.addWidget(self.draw_sift_line_btn)
        self.print_distance_btn = QtWidgets.QPushButton(self.frame)
        self.print_distance_btn.setObjectName("print_distance_btn")
        self.verticalLayout.addWidget(self.print_distance_btn)
        self.auto_challenge_btn = QtWidgets.QPushButton(self.frame)
        self.auto_challenge_btn.setObjectName("auto_challenge_btn")
        self.verticalLayout.addWidget(self.auto_challenge_btn)
        self.auto_tower_btn = QtWidgets.QPushButton(self.frame)
        self.auto_tower_btn.setObjectName("auto_tower_btn")
        self.verticalLayout.addWidget(self.auto_tower_btn)
        self.stop_all_btn = QtWidgets.QPushButton(self.frame)
        self.stop_all_btn.setObjectName("stop_all_btn")
        self.verticalLayout.addWidget(self.stop_all_btn)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(222, 120, 311, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame1.setObjectName("frame1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.device_combo_box = QtWidgets.QComboBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_combo_box.sizePolicy().hasHeightForWidth())
        self.device_combo_box.setSizePolicy(sizePolicy)
        self.device_combo_box.setMinimumSize(QtCore.QSize(0, 26))
        self.device_combo_box.setObjectName("device_combo_box")
        self.horizontalLayout.addWidget(self.device_combo_box)
        self.connect_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy)
        self.connect_btn.setMinimumSize(QtCore.QSize(0, 27))
        self.connect_btn.setObjectName("connect_btn")
        self.horizontalLayout.addWidget(self.connect_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

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
