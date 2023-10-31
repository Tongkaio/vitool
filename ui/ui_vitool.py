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
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 246)
        Form.setMinimumSize(QSize(474, 246))
        Form.setMaximumSize(QSize(474, 246))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_video = QToolButton(Form)
        self.button_video.setObjectName(u"button_video")

        self.horizontalLayout_3.addWidget(self.button_video)

        self.lineEdit_videopath = QLineEdit(Form)
        self.lineEdit_videopath.setObjectName(u"lineEdit_videopath")
        self.lineEdit_videopath.setEnabled(True)
        self.lineEdit_videopath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_videopath)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_output = QToolButton(Form)
        self.button_output.setObjectName(u"button_output")

        self.horizontalLayout_4.addWidget(self.button_output)

        self.lineEdit_outputpath = QLineEdit(Form)
        self.lineEdit_outputpath.setObjectName(u"lineEdit_outputpath")
        self.lineEdit_outputpath.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_outputpath)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_ImgPrefix = QLineEdit(Form)
        self.lineEdit_ImgPrefix.setObjectName(u"lineEdit_ImgPrefix")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ImgPrefix.sizePolicy().hasHeightForWidth())
        self.lineEdit_ImgPrefix.setSizePolicy(sizePolicy)
        self.lineEdit_ImgPrefix.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_ImgPrefix)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBox_SuffixLength = QSpinBox(Form)
        self.spinBox_SuffixLength.setObjectName(u"spinBox_SuffixLength")
        self.spinBox_SuffixLength.setValue(6)

        self.horizontalLayout_5.addWidget(self.spinBox_SuffixLength)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.spinBox_frame = QSpinBox(Form)
        self.spinBox_frame.setObjectName(u"spinBox_frame")
        self.spinBox_frame.setMinimum(1)

        self.horizontalLayout_5.addWidget(self.spinBox_frame)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.button_2img = QPushButton(Form)
        self.button_2img.setObjectName(u"button_2img")

        self.horizontalLayout_7.addWidget(self.button_2img)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

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

        self.spinBox_fps = QSpinBox(Form)
        self.spinBox_fps.setObjectName(u"spinBox_fps")
        self.spinBox_fps.setMinimum(1)
        self.spinBox_fps.setMaximum(60)
        self.spinBox_fps.setValue(25)

        self.horizontalLayout_8.addWidget(self.spinBox_fps)

        self.checkBox_deleteimg = QCheckBox(Form)
        self.checkBox_deleteimg.setObjectName(u"checkBox_deleteimg")
        self.checkBox_deleteimg.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.checkBox_deleteimg)

        self.checkBox_deletedir = QCheckBox(Form)
        self.checkBox_deletedir.setObjectName(u"checkBox_deletedir")
        self.checkBox_deletedir.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.checkBox_deletedir)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.button_2video = QPushButton(Form)
        self.button_2video.setObjectName(u"button_2video")

        self.horizontalLayout_6.addWidget(self.button_2video)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.progresstext = QLabel(Form)
        self.progresstext.setObjectName(u"progresstext")
        self.progresstext.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.progresstext)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"vitool", None))
        self.button_video.setText(QCoreApplication.translate("Form", u"\u89c6\u9891", None))
        self.button_output.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u524d\u7f00:", None))
        self.lineEdit_ImgPrefix.setText(QCoreApplication.translate("Form", u"frame", None))
        self.label_5.setText(QCoreApplication.translate("Form", u", \u540e\u7f00\u957f\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u", \u6bcf", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5e27\u62bd\u53d61\u5e27", None))
        self.button_2img.setText(QCoreApplication.translate("Form", u"\u62bd\u5e27", None))
        self.button_img.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.button_output_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5e27\u7387", None))
        self.checkBox_deleteimg.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u540e\u5220\u9664\u6587\u4ef6", None))
        self.checkBox_deletedir.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u540e\u5220\u9664\u76ee\u5f55", None))
        self.button_2video.setText(QCoreApplication.translate("Form", u"\u5408\u5e76", None))
        self.progresstext.setText("")
    # retranslateUi

