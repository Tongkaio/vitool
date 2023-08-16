# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vitool.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(372, 266)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_video = QToolButton(Form)
        self.button_video.setObjectName(u"button_video")

        self.horizontalLayout_3.addWidget(self.button_video)

        self.lineEdit_videopath = QLineEdit(Form)
        self.lineEdit_videopath.setObjectName(u"lineEdit_videopath")

        self.horizontalLayout_3.addWidget(self.lineEdit_videopath)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_output = QToolButton(Form)
        self.button_output.setObjectName(u"button_output")

        self.horizontalLayout_4.addWidget(self.button_output)

        self.lineEdit_outputpath = QLineEdit(Form)
        self.lineEdit_outputpath.setObjectName(u"lineEdit_outputpath")

        self.horizontalLayout_4.addWidget(self.lineEdit_outputpath)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.lineEdit_suffix = QLineEdit(Form)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.horizontalLayout_7.addWidget(self.lineEdit_suffix)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_7.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.button_2img = QPushButton(Form)
        self.button_2img.setObjectName(u"button_2img")

        self.horizontalLayout_5.addWidget(self.button_2img)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_img = QToolButton(Form)
        self.button_img.setObjectName(u"button_img")

        self.horizontalLayout.addWidget(self.button_img)

        self.lineEdit_imgpath = QLineEdit(Form)
        self.lineEdit_imgpath.setObjectName(u"lineEdit_imgpath")

        self.horizontalLayout.addWidget(self.lineEdit_imgpath)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_output_2 = QToolButton(Form)
        self.button_output_2.setObjectName(u"button_output_2")

        self.horizontalLayout_2.addWidget(self.button_output_2)

        self.lineEdit_outputpath_2 = QLineEdit(Form)
        self.lineEdit_outputpath_2.setObjectName(u"lineEdit_outputpath_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_outputpath_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_framefate = QLineEdit(Form)
        self.lineEdit_framefate.setObjectName(u"lineEdit_framefate")

        self.horizontalLayout_8.addWidget(self.lineEdit_framefate)

        self.horizontalSpacer_6 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.checkBox_deleteimg = QCheckBox(Form)
        self.checkBox_deleteimg.setObjectName(u"checkBox_deleteimg")

        self.horizontalLayout_8.addWidget(self.checkBox_deleteimg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.button_2video = QPushButton(Form)
        self.button_2video.setObjectName(u"button_2video")

        self.horizontalLayout_6.addWidget(self.button_2video)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"vitool", None))
        self.button_video.setText(QCoreApplication.translate("Form", u"\u89c6\u9891", None))
        self.button_output.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u540e\u7f00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u95f4\u9694", None))
        self.button_2img.setText(QCoreApplication.translate("Form", u"\u62bd\u5e27", None))
        self.button_img.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.button_output_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5e27\u7387", None))
        self.checkBox_deleteimg.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u540e\u5220\u9664\u56fe\u7247", None))
        self.button_2video.setText(QCoreApplication.translate("Form", u"\u5408\u5e76", None))
    # retranslateUi

