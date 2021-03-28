# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logcat.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Logcat(object):
    def setupUi(self, Logcat):
        Logcat.setObjectName("Logcat")
        Logcat.resize(311, 240)
        Logcat.setMaximumSize(QtCore.QSize(320, 240))
        self.centralwidget = QtWidgets.QWidget(Logcat)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 251, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        #Logcat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Logcat)
        self.pushButton_2.clicked.connect(Logcat.get_csh)
        self.pushButton.clicked.connect(Logcat.killLogcat)
        QtCore.QMetaObject.connectSlotsByName(Logcat)

    def retranslateUi(self, Logcat):
        _translate = QtCore.QCoreApplication.translate
        Logcat.setWindowTitle(_translate("Logcat", "崩溃日志窗口"))
        self.pushButton.setText(_translate("Logcat", "停止logcat"))
        self.pushButton_2.setText(_translate("Logcat", "获取.csh"))
        self.textEdit.setHtml(_translate("Logcat", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1b1f5d;\">我是输出框～～～</span></p></body></html>"))

