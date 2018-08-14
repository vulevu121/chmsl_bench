# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chmslGui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(59, 56, 56, 80);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    height: 40px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px 0px 10px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(59, 56, 56);\n"
"    border: 1px solid gray;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    padding: 10px;\n"
"    min-width: 150px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 rgb(59, 56, 56), stop: 0.4 rgb(100, 95, 95),\n"
"                                stop: 0.5 rgb(80, 75, 75), stop: 1.0 rgb(59, 56, 56));\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.background.setObjectName("background")
        self.titleText = QtWidgets.QLabel(self.centralwidget)
        self.titleText.setGeometry(QtCore.QRect(320, 20, 167, 24))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.titleText.setFont(font)
        self.titleText.setObjectName("titleText")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 741, 341))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 30, 681, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        self.activePage = QtWidgets.QWidget()
        self.activePage.setObjectName("activePage")
        self.layoutWidget = QtWidgets.QWidget(self.activePage)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 4, 2, 1, 1)
        self.stackedWidget.addWidget(self.activePage)
        self.schedulePage = QtWidgets.QWidget()
        self.schedulePage.setObjectName("schedulePage")
        self.layoutWidget1 = QtWidgets.QWidget(self.schedulePage)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 681, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_46 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_2.addWidget(self.pushButton_46, 0, 0, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_2.addWidget(self.pushButton_47, 0, 1, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_2.addWidget(self.pushButton_48, 0, 2, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_2.addWidget(self.pushButton_49, 1, 0, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_2.addWidget(self.pushButton_50, 1, 1, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_2.addWidget(self.pushButton_51, 1, 2, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_2.addWidget(self.pushButton_52, 2, 0, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_2.addWidget(self.pushButton_53, 2, 1, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_2.addWidget(self.pushButton_54, 2, 2, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_2.addWidget(self.pushButton_55, 3, 0, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_2.addWidget(self.pushButton_56, 3, 1, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout_2.addWidget(self.pushButton_57, 3, 2, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_2.addWidget(self.pushButton_58, 4, 0, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout_2.addWidget(self.pushButton_59, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.schedulePage)
        self.layoutWidget.raise_()
        self.stackedWidget.raise_()
        self.titleBar = QtWidgets.QLabel(self.centralwidget)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 819, 82))
        self.titleBar.setObjectName("titleBar")
        self.activeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.activeBtn.setGeometry(QtCore.QRect(30, 50, 125, 30))
        self.activeBtn.setObjectName("activeBtn")
        self.scheduleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scheduleBtn.setGeometry(QtCore.QRect(630, 50, 145, 30))
        self.scheduleBtn.setObjectName("scheduleBtn")
        self.startAutoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startAutoBtn.setGeometry(QtCore.QRect(30, 430, 121, 28))
        self.startAutoBtn.setObjectName("startAutoBtn")
        self.stopAutoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopAutoBtn.setGeometry(QtCore.QRect(650, 430, 121, 28))
        self.stopAutoBtn.setObjectName("stopAutoBtn")
        self.background.raise_()
        self.titleBar.raise_()
        self.groupBox.raise_()
        self.titleText.raise_()
        self.activeBtn.raise_()
        self.scheduleBtn.raise_()
        self.startAutoBtn.raise_()
        self.stopAutoBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.background.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.jpg\"/></p></body></html>"))
        self.titleText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CHMSL Test Bench</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Active Charging"))
        self.pushButton_1.setText(_translate("MainWindow", "No Display && Asleep"))
        self.pushButton_2.setText(_translate("MainWindow", "No Display && Awake"))
        self.pushButton_3.setText(_translate("MainWindow", "Plug Recognition"))
        self.pushButton_4.setText(_translate("MainWindow", "0% - 9%"))
        self.pushButton_5.setText(_translate("MainWindow", "10% - 19%"))
        self.pushButton_6.setText(_translate("MainWindow", "20% - 29%"))
        self.pushButton_7.setText(_translate("MainWindow", "30% - 39%"))
        self.pushButton_8.setText(_translate("MainWindow", "40% - 49%"))
        self.pushButton_9.setText(_translate("MainWindow", "50% - 59%"))
        self.pushButton_10.setText(_translate("MainWindow", "60% - 69%"))
        self.pushButton_11.setText(_translate("MainWindow", "70% - 79%"))
        self.pushButton_12.setText(_translate("MainWindow", "80% - 89%"))
        self.pushButton_13.setText(_translate("MainWindow", "90% - 99%"))
        self.pushButton_14.setText(_translate("MainWindow", "100%"))
        self.pushButton_15.setText(_translate("MainWindow", "Fault"))
        self.pushButton_46.setText(_translate("MainWindow", "No Display && Asleep"))
        self.pushButton_47.setText(_translate("MainWindow", "No Display && Awake"))
        self.pushButton_48.setText(_translate("MainWindow", "Plug Recognition"))
        self.pushButton_49.setText(_translate("MainWindow", "0% - 9%"))
        self.pushButton_50.setText(_translate("MainWindow", "10% - 19%"))
        self.pushButton_51.setText(_translate("MainWindow", "20% - 29%"))
        self.pushButton_52.setText(_translate("MainWindow", "30% - 39%"))
        self.pushButton_53.setText(_translate("MainWindow", "40% - 49%"))
        self.pushButton_54.setText(_translate("MainWindow", "50% - 59%"))
        self.pushButton_55.setText(_translate("MainWindow", "60% - 69%"))
        self.pushButton_56.setText(_translate("MainWindow", "70% - 79%"))
        self.pushButton_57.setText(_translate("MainWindow", "80% - 89%"))
        self.pushButton_58.setText(_translate("MainWindow", "90% - 99%"))
        self.pushButton_59.setText(_translate("MainWindow", "100%"))
        self.titleBar.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.activeBtn.setText(_translate("MainWindow", "Active Charging"))
        self.scheduleBtn.setText(_translate("MainWindow", "Schedule Charging"))
        self.startAutoBtn.setText(_translate("MainWindow", "Start Auto Test"))
        self.stopAutoBtn.setText(_translate("MainWindow", "Stop Auto Test"))

import graphics_rc
