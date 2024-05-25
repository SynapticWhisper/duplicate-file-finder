# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
from style import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(349, 203)
        Dialog.setStyleSheet(u"background-color: #444;\n"
"color: #fff;\n"
"font-size: 12pt;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon = QPushButton(Dialog)
        self.icon.setObjectName(u"icon")
        self.icon.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/warning_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.text = QTextBrowser(Dialog)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.text, 1, 0, 1, 3)

        self.yes_btn = QPushButton(Dialog)
        self.yes_btn.setObjectName(u"yes_btn")
        self.yes_btn.setMinimumSize(QSize(160, 42))
        self.yes_btn.setMaximumSize(QSize(160, 42))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.yes_btn.setFont(font1)
        self.yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2655cf;\n"
"    border: 0;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2048ac;\n"
"}")

        self.gridLayout.addWidget(self.yes_btn, 2, 0, 1, 2)

        self.no_btn = QPushButton(Dialog)
        self.no_btn.setObjectName(u"no_btn")
        self.no_btn.setMinimumSize(QSize(160, 42))
        self.no_btn.setMaximumSize(QSize(160, 42))
        self.no_btn.setFont(font1)
        self.no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #ba3329;\n"
"    border: 0;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7a1f18;\n"
"}")

        self.gridLayout.addWidget(self.no_btn, 2, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"WARNING", None))
        self.text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Do you really want to irretrievably delete files?</p></body></html>", None))
        self.yes_btn.setText(QCoreApplication.translate("Dialog", u"YES", None))
        self.no_btn.setText(QCoreApplication.translate("Dialog", u"NO", None))
    # retranslateUi

