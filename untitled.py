# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

import xmindparser
import os
import re




class Ui_MainWindow(QMainWindow):
    def jiagongchang(self):
        self.textEdit.setText("")
        wenjianzonghe = []
        xmind_files = []
        result=[]
        dizhi=self.lineEdit.text()
        leirong=self.lineEdit_2.text()
        for dirpath, dirname, filename in os.walk(dizhi):
            for filenamex in filename:
                wenjianzonghe.append(dirpath + '\\' + filenamex)

        for wenjainzonghex in wenjianzonghe:
            bianshi = os.path.splitext(wenjainzonghex)[-1]
            if bianshi == ".xmind":
                xmind_files.append(wenjainzonghex)

        for XFX in xmind_files:
            neirong = xmindparser.xmind_to_dict(XFX)
            panduan = re.search(leirong, str(neirong))
            if panduan != None:
                result.append(XFX)

        if len(result)==0:
            self.textEdit.append("没有找到任何匹配文件")
        else:
            for resultx in result:
                self.textEdit.append(resultx)


    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setWindowTitle("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 661, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("这里输入地址")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 661, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("这里输入文本")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 10, 101, 101))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 781, 431))
        self.textEdit.setObjectName("textEdit")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(lambda:self.jiagongchang())


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("XMIND文件解析")
        self.pushButton.setText("开始")




if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Ui_MainWindow()
    w.show()
    sys.exit(app.exec_())







