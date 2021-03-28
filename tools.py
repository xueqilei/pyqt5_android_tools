# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setMaximumSize(QtCore.QSize(480, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 421, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_install = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_install.setObjectName("pushButton_install")
        self.gridLayout.addWidget(self.pushButton_install, 0, 0, 1, 1)
        self.pushButton_logcat = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_logcat.setObjectName("pushButton_logcat")
        self.gridLayout.addWidget(self.pushButton_logcat, 0, 1, 1, 1)
        self.pushButton_anr = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_anr.setObjectName("pushButton_anr")
        self.gridLayout.addWidget(self.pushButton_anr, 0, 2, 1, 1)
        self.pushButton_deviceinfo = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_deviceinfo.setObjectName("pushButton_deviceinfo")
        self.gridLayout.addWidget(self.pushButton_deviceinfo, 1, 0, 1, 1)
        self.pushButton_screenshot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_screenshot.setObjectName("pushButton_screenshot")
        self.gridLayout.addWidget(self.pushButton_screenshot, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line_1 = QtWidgets.QFrame(self.layoutWidget)
        self.line_1.setLineWidth(1)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout_4.addWidget(self.line_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(38, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_get_package_name = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_get_package_name.setObjectName("pushButton_get_package_name")
        self.verticalLayout.addWidget(self.pushButton_get_package_name)
        self.pushButton_uninstall = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_uninstall.setObjectName("pushButton_uninstall")
        self.verticalLayout.addWidget(self.pushButton_uninstall)
        self.pushButton_clear_data = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear_data.setObjectName("pushButton_clear_data")
        self.verticalLayout.addWidget(self.pushButton_clear_data)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textEdit_output_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_output_2.setObjectName("textEdit_output_2")
        self.horizontalLayout.addWidget(self.textEdit_output_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(38, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_output = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_output.setObjectName("textEdit_output")
        self.verticalLayout_3.addWidget(self.textEdit_output)
        spacerItem2 = QtWidgets.QSpacerItem(38, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_2.addWidget(self.pushButton_exit)
        spacerItem3 = QtWidgets.QSpacerItem(108, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_version = QtWidgets.QLabel(self.layoutWidget)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_2.addWidget(self.label_version)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_clear_data.clicked.connect(MainWindow.clear_data)
        self.pushButton_screenshot.clicked.connect(MainWindow.screen_shot)
        self.pushButton_anr.clicked.connect(MainWindow.get_anr)
        self.pushButton_deviceinfo.clicked.connect(MainWindow.get_deviceinfo)
        self.pushButton_get_package_name.clicked.connect(MainWindow.getPackageName)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "安卓小工具"))
        self.pushButton_install.setText(_translate("MainWindow", "全新安装"))
        self.pushButton_logcat.setText(_translate("MainWindow", "截取logcat"))
        self.pushButton_anr.setText(_translate("MainWindow", "截取ANR"))
        self.pushButton_deviceinfo.setText(_translate("MainWindow", "获取设备信息"))
        self.pushButton_screenshot.setText(_translate("MainWindow", "截屏"))
        self.pushButton_get_package_name.setText(_translate("MainWindow", "获取包名"))
        self.pushButton_uninstall.setText(_translate("MainWindow", "卸载"))
        self.pushButton_clear_data.setText(_translate("MainWindow", "清除程序数据"))
        self.textEdit_output_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#999999;\">获取手机当前页面包名</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#999999;\">卸载&amp;清除数据，依赖与该提示框里显示的包名</span></p></body></html>"))
        self.textEdit_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; color:#808080;\">提示信息输出框～～～</span></p></body></html>"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))
        self.label_version.setText(_translate("MainWindow", "version1.0"))