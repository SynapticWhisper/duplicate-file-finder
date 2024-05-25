# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from style import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 679)
        MainWindow.setStyleSheet(u"background-color: #444;\n"
"font-size: 12pt;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"background-color: #333;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.left_header = QFrame(self.header)
        self.left_header.setObjectName(u"left_header")
        self.left_header.setLayoutDirection(Qt.RightToLeft)
        self.left_header.setFrameShape(QFrame.StyledPanel)
        self.left_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.left_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.program_name = QLabel(self.left_header)
        self.program_name.setObjectName(u"program_name")
        font = QFont()
        font.setPointSize(18)
        self.program_name.setFont(font)
        self.program_name.setStyleSheet(u"color: #fff;\n"
"font-size:18pt;\n"
"")

        self.horizontalLayout_3.addWidget(self.program_name, 0, Qt.AlignLeft)

        self.logo = QLabel(self.left_header)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(60, 60))
        self.logo.setPixmap(QPixmap(u":/icons/icons/format_paint_white_24dp.svg"))
        self.logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.logo)


        self.horizontalLayout.addWidget(self.left_header, 0, Qt.AlignRight)

        self.central_header = QFrame(self.header)
        self.central_header.setObjectName(u"central_header")
        self.central_header.setFrameShape(QFrame.StyledPanel)
        self.central_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.central_header)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.header_spacer = QSpacerItem(603, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.header_spacer)


        self.horizontalLayout.addWidget(self.central_header)

        self.right_header = QFrame(self.header)
        self.right_header.setObjectName(u"right_header")
        self.right_header.setMaximumSize(QSize(150, 16777215))
        self.right_header.setLayoutDirection(Qt.LeftToRight)
        self.right_header.setFrameShape(QFrame.StyledPanel)
        self.right_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.right_header)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.minimize_btn = QPushButton(self.right_header)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(25, 25))
        self.minimize_btn.setMaximumSize(QSize(25, 25))
        self.minimize_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #666;\n"
"	border: 0;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #555;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minimize_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.resize_btn = QPushButton(self.right_header)
        self.resize_btn.setObjectName(u"resize_btn")
        self.resize_btn.setMinimumSize(QSize(25, 25))
        self.resize_btn.setMaximumSize(QSize(25, 25))
        self.resize_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #666;\n"
"	border: 0;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #555;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/web_asset_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.resize_btn)

        self.close_btn = QPushButton(self.right_header)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(25, 25))
        self.close_btn.setMaximumSize(QSize(25, 25))
        self.close_btn.setFocusPolicy(Qt.NoFocus)
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #666;\n"
"	border: 0;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #555;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.right_header)


        self.verticalLayout.addWidget(self.header)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setLayoutDirection(Qt.LeftToRight)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.select_folder_frame = QFrame(self.main_container)
        self.select_folder_frame.setObjectName(u"select_folder_frame")
        self.select_folder_frame.setMaximumSize(QSize(16777215, 70))
        self.select_folder_frame.setStyleSheet(u"background-color: #333;\n"
"border: 0;\n"
"border-radius: 15px;")
        self.select_folder_frame.setFrameShape(QFrame.StyledPanel)
        self.select_folder_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.select_folder_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.select_text = QLabel(self.select_folder_frame)
        self.select_text.setObjectName(u"select_text")
        font1 = QFont()
        font1.setPointSize(16)
        self.select_text.setFont(font1)
        self.select_text.setStyleSheet(u"color: #fff;\n"
"font-size: 16pt;\n"
"")

        self.horizontalLayout_4.addWidget(self.select_text)

        self.select_input = QLineEdit(self.select_folder_frame)
        self.select_input.setObjectName(u"select_input")
        self.select_input.setMinimumSize(QSize(20, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.select_input.setFont(font2)
        self.select_input.setStyleSheet(u"background-color: #444;\n"
"border: 0;\n"
"border-radius: 15px;\n"
"padding-left: 15px;\n"
"color: #fff;\n"
"font-size: 12pt;")
        self.select_input.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.select_input)

        self.select_btn = QPushButton(self.select_folder_frame)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setMinimumSize(QSize(60, 40))
        self.select_btn.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/create_new_folder_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_btn.setIcon(icon3)
        self.select_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.select_btn)


        self.verticalLayout_2.addWidget(self.select_folder_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: #333;\n"
"border: 0;\n"
"border-radius: 15px;")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.options_frame = QFrame(self.main_frame)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setMinimumSize(QSize(280, 0))
        self.options_frame.setMaximumSize(QSize(280, 16777215))
        self.options_frame.setStyleSheet(u"background-color: #333;\n"
"border: 0;\n"
"")
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.options_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 20)
        self.start_btn = QPushButton(self.options_frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setEnabled(True)
        font3 = QFont()
        self.start_btn.setFont(font3)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #25c23f;\n"
"    border: 0;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"	font-size: 18px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1a8a2d;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #5ca167;\n"
"}")

        self.gridLayout_3.addWidget(self.start_btn, 3, 0, 1, 2)

        self.scan_subfolders = QCheckBox(self.options_frame)
        self.scan_subfolders.setObjectName(u"scan_subfolders")
        self.scan_subfolders.setStyleSheet(u"color: #fff;\n"
"padding-left: 11px;\n"
"margin-bottom: 25px;")
        self.scan_subfolders.setChecked(False)

        self.gridLayout_3.addWidget(self.scan_subfolders, 1, 0, 1, 1)

        self.radio_frame = QFrame(self.options_frame)
        self.radio_frame.setObjectName(u"radio_frame")
        self.radio_frame.setStyleSheet(u"background-color: #444;\n"
"border: 0;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.radio_frame.setFrameShape(QFrame.StyledPanel)
        self.radio_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.radio_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.easy_btn = QRadioButton(self.radio_frame)
        self.easy_btn.setObjectName(u"easy_btn")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.easy_btn.setFont(font4)
        self.easy_btn.setStyleSheet(u"color: #fff;")

        self.gridLayout_2.addWidget(self.easy_btn, 0, 0, 1, 1)

        self.help_easy = QLabel(self.radio_frame)
        self.help_easy.setObjectName(u"help_easy")
        self.help_easy.setPixmap(QPixmap(u":/icons/icons/help_outline_white_24dp.svg"))
        self.help_easy.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.help_easy, 0, 1, 1, 1, Qt.AlignRight)

        self.medium_btn = QRadioButton(self.radio_frame)
        self.medium_btn.setObjectName(u"medium_btn")
        self.medium_btn.setFont(font4)
        self.medium_btn.setStyleSheet(u"color: #fff;")

        self.gridLayout_2.addWidget(self.medium_btn, 2, 0, 1, 1)

        self.sep = QFrame(self.radio_frame)
        self.sep.setObjectName(u"sep")
        self.sep.setStyleSheet(u"background-color: #333")
        self.sep.setFrameShape(QFrame.HLine)
        self.sep.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.sep, 1, 0, 1, 2)

        self.help_medium = QLabel(self.radio_frame)
        self.help_medium.setObjectName(u"help_medium")
        self.help_medium.setPixmap(QPixmap(u":/icons/icons/help_outline_white_24dp.svg"))
        self.help_medium.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.help_medium, 2, 1, 1, 1, Qt.AlignRight)

        self.hard_btn = QRadioButton(self.radio_frame)
        self.hard_btn.setObjectName(u"hard_btn")
        self.hard_btn.setFont(font4)
        self.hard_btn.setStyleSheet(u"color: #fff;")

        self.gridLayout_2.addWidget(self.hard_btn, 4, 0, 1, 1)

        self.help_hard = QLabel(self.radio_frame)
        self.help_hard.setObjectName(u"help_hard")
        self.help_hard.setPixmap(QPixmap(u":/icons/icons/help_outline_white_24dp.svg"))
        self.help_hard.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.help_hard, 4, 1, 1, 1, Qt.AlignRight)

        self.sep1 = QFrame(self.radio_frame)
        self.sep1.setObjectName(u"sep1")
        self.sep1.setStyleSheet(u"background-color: #333")
        self.sep1.setFrameShape(QFrame.HLine)
        self.sep1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.sep1, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.radio_frame, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.options_frame, 2, 1, 1, 1)

        self.progressBar = QProgressBar(self.main_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 15px;\n"
"	padding: 2px;\n"
"	border: 0;\n"
"	background-color: #444;\n"
"	color: #fff;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	border: 0;\n"
"	color: green;\n"
"	background-color: #25c23f;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 2)

        self.text_frame = QFrame(self.main_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setMaximumSize(QSize(16777215, 120))
        self.text_frame.setStyleSheet(u"background-color: #444;\n"
"border: 0;\n"
"border-radius: 15px;")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.text_frame)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.options = QLabel(self.text_frame)
        self.options.setObjectName(u"options")
        self.options.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.options.setFont(font5)
        self.options.setStyleSheet(u"font-size: 16pt;\n"
"color: #fff;\n"
"")

        self.verticalLayout_8.addWidget(self.options)

        self.info = QLabel(self.text_frame)
        self.info.setObjectName(u"info")
        self.info.setMaximumSize(QSize(16777215, 20))
        self.info.setStyleSheet(u"color: #fff;\n"
"font-size: 12pt;\n"
"")

        self.verticalLayout_8.addWidget(self.info)


        self.gridLayout.addWidget(self.text_frame, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(550, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: #444;\n"
"border-radius: 15px;\n"
"border: 0;\n"
"padding: 10px;")
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_3 = QVBoxLayout(self.info_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_icon = QPushButton(self.info_page)
        self.info_icon.setObjectName(u"info_icon")
        self.info_icon.setMinimumSize(QSize(140, 140))
        self.info_icon.setMaximumSize(QSize(140, 140))
        self.info_icon.setIcon(icon3)
        self.info_icon.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.info_icon, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.info_text = QLabel(self.info_page)
        self.info_text.setObjectName(u"info_text")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.info_text.setFont(font6)
        self.info_text.setStyleSheet(u"color: #fff;\n"
"font-size: 14pt;")
        self.info_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.info_text, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.info_page)
        self.results_page = QWidget()
        self.results_page.setObjectName(u"results_page")
        self.verticalLayout_5 = QVBoxLayout(self.results_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stats_frame = QFrame(self.results_page)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setMinimumSize(QSize(0, 120))
        self.stats_frame.setMaximumSize(QSize(16777215, 125))
        self.stats_frame.setFrameShape(QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.stats_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.size_count = QLabel(self.stats_frame)
        self.size_count.setObjectName(u"size_count")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.size_count.setFont(font7)
        self.size_count.setStyleSheet(u"color: #fff;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.size_count, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.size = QLabel(self.stats_frame)
        self.size.setObjectName(u"size")
        self.size.setMinimumSize(QSize(160, 0))
        self.size.setMaximumSize(QSize(160, 16777215))
        self.size.setFont(font7)
        self.size.setStyleSheet(u"color: #fff;\n"
"padding-left: 10px;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.size, 2, 0, 1, 1)

        self.files_count = QLabel(self.stats_frame)
        self.files_count.setObjectName(u"files_count")
        self.files_count.setFont(font7)
        self.files_count.setStyleSheet(u"color: #fff;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.files_count, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(287, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)

        self.files = QLabel(self.stats_frame)
        self.files.setObjectName(u"files")
        self.files.setMinimumSize(QSize(160, 0))
        self.files.setMaximumSize(QSize(160, 16777215))
        self.files.setFont(font7)
        self.files.setStyleSheet(u"color: #fff;\n"
"padding-left: 10px;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.files, 0, 0, 1, 1)

        self.duplicates = QLabel(self.stats_frame)
        self.duplicates.setObjectName(u"duplicates")
        self.duplicates.setMinimumSize(QSize(175, 0))
        self.duplicates.setMaximumSize(QSize(175, 16777215))
        self.duplicates.setFont(font7)
        self.duplicates.setStyleSheet(u"color: #fff;\n"
"padding-left: 10px;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.duplicates, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.duplicates_count = QLabel(self.stats_frame)
        self.duplicates_count.setObjectName(u"duplicates_count")
        self.duplicates_count.setFont(font7)
        self.duplicates_count.setStyleSheet(u"color: #fff;\n"
"font-size: 10pt;")

        self.gridLayout_5.addWidget(self.duplicates_count, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.stats_frame)

        self.res_table = QTableWidget(self.results_page)
        self.res_table.setObjectName(u"res_table")
        self.res_table.setMinimumSize(QSize(510, 180))
        self.res_table.setStyleSheet(u"QScrollBar:vertical {\n"
"     background-color: #333;\n"
"     width: 10px;\n"
"     padding-top: 3px;\n"
"     padding-button: 3px;\n"
"     padding-left: 2px;\n"
"     border-radius: 50%;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"     background-color: #777;         \n"
"     min-height: 10px;\n"
"     border-radius: 4px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"     background-color: #333;\n"
"     height: 0px;\n"
"     border-radius: 4px;\n"
"     width: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"     height: 0px;\n"
"     width: 0px;\n"
"     background-color: #333;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on {\n"
"     height: 10px;\n"
"     background-color: #333;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar:"
                        ":down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}\n"
"QTableWidget {\n"
"     color: #FFF;\n"
"     padding: 5px;\n"
"     background-color: #333;\n"
"     border: 0;\n"
"     border-radius: 15px;\n"
"     selection-background-color: #333;\n"
"}")

        self.verticalLayout_5.addWidget(self.res_table)

        self.actions_frame = QFrame(self.results_page)
        self.actions_frame.setObjectName(u"actions_frame")
        self.actions_frame.setMinimumSize(QSize(0, 62))
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.select_all = QCheckBox(self.actions_frame)
        self.select_all.setObjectName(u"select_all")
        self.select_all.setMinimumSize(QSize(0, 40))
        self.select_all.setMaximumSize(QSize(16777215, 40))
        self.select_all.setStyleSheet(u"font-size: 11pt;\n"
"color: #FFF;")

        self.horizontalLayout_5.addWidget(self.select_all)

        self.delete_all_btn = QPushButton(self.actions_frame)
        self.delete_all_btn.setObjectName(u"delete_all_btn")
        self.delete_all_btn.setEnabled(True)
        self.delete_all_btn.setMinimumSize(QSize(160, 42))
        self.delete_all_btn.setMaximumSize(QSize(160, 42))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        self.delete_all_btn.setFont(font8)
        self.delete_all_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2655cf;\n"
"	font-size: 8pt;\n"
"    border: 0;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2048ac;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: #5f7dc7;\n"
"}")

        self.horizontalLayout_5.addWidget(self.delete_all_btn)

        self.delete_selected_btn = QPushButton(self.actions_frame)
        self.delete_selected_btn.setObjectName(u"delete_selected_btn")
        self.delete_selected_btn.setEnabled(True)
        self.delete_selected_btn.setMinimumSize(QSize(160, 42))
        self.delete_selected_btn.setMaximumSize(QSize(160, 42))
        self.delete_selected_btn.setFont(font8)
        self.delete_selected_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2655cf;\n"
"	font-size: 8pt;\n"
"    border: 0;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2048ac;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #5f7dc7;\n"
"}")

        self.horizontalLayout_5.addWidget(self.delete_selected_btn)


        self.verticalLayout_5.addWidget(self.actions_frame, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.results_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.main_container)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 40))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setStyleSheet(u"background-color: #333;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.created_by = QLabel(self.footer)
        self.created_by.setObjectName(u"created_by")
        font9 = QFont()
        font9.setPointSize(10)
        self.created_by.setFont(font9)
        self.created_by.setStyleSheet(u"color: #fff;\n"
"font-size: 10pt;")

        self.horizontalLayout_6.addWidget(self.created_by)

        self.resize_grid = QFrame(self.footer)
        self.resize_grid.setObjectName(u"resize_grid")
        self.resize_grid.setMinimumSize(QSize(10, 10))
        self.resize_grid.setMaximumSize(QSize(10, 10))
        self.resize_grid.setFrameShape(QFrame.StyledPanel)
        self.resize_grid.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.resize_grid, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.program_name.setText(QCoreApplication.translate("MainWindow", u"DuplicatesCleaner", None))
        self.logo.setText("")
        self.minimize_btn.setText("")
        self.resize_btn.setText("")
        self.close_btn.setText("")
        self.select_text.setText(QCoreApplication.translate("MainWindow", u"Selected folder:", None))
        self.select_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose directory to check ...", None))
        self.select_btn.setText("")
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.scan_subfolders.setText(QCoreApplication.translate("MainWindow", u"Scan sub-folders", None))
        self.easy_btn.setText(QCoreApplication.translate("MainWindow", u"by filename", None))
        self.help_easy.setText("")
        self.medium_btn.setText(QCoreApplication.translate("MainWindow", u"by md5 hash", None))
        self.help_medium.setText("")
        self.hard_btn.setText(QCoreApplication.translate("MainWindow", u"by sha256 hash", None))
        self.help_hard.setText("")
        self.options.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"Select the scanning method:", None))
        self.info_icon.setText("")
        self.info_text.setText(QCoreApplication.translate("MainWindow", u"SELECT A FOLDER TO SCAN", None))
        self.size_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.size.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.files_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.files.setText(QCoreApplication.translate("MainWindow", u"Files scanned:", None))
        self.duplicates.setText(QCoreApplication.translate("MainWindow", u"Duplicates found:", None))
        self.duplicates_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.select_all.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
        self.delete_all_btn.setText(QCoreApplication.translate("MainWindow", u"DELETE ALL", None))
        self.delete_selected_btn.setText(QCoreApplication.translate("MainWindow", u"DELETE SELECTED", None))
        self.created_by.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Designed & Created by BlackRazor", None))
    # retranslateUi

