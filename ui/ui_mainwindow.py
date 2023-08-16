# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 192)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dirList = QComboBox(self.centralwidget)
        self.dirList.setObjectName(u"dirList")
        self.dirList.setGeometry(QRect(120, 70, 68, 22))
        self.selectVideo = QToolButton(self.centralwidget)
        self.selectVideo.setObjectName(u"selectVideo")
        self.selectVideo.setGeometry(QRect(230, 70, 61, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"vitool", None))
        self.selectVideo.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
    # retranslateUi

