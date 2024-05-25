import sys

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPoint, Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QSizeGrip

from style.main_window import Ui_MainWindow
from utils.delete_worker import DeleteFiles
from utils.dialog_widget import DialogWidget
from utils.directory_selector import DirectorySelector
from utils.mode import Mode
from utils.scaner import Scaner
from utils.tools import get_config, set_info_page


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.config = get_config("config.json")
        self.offset = None
        self.max_deep = True
        self.mode = Mode.MEDIUM
        self.ui = Ui_MainWindow()

        self.dir_selector = DirectorySelector(
            self.ui,
            self.config["text"]["info_page"]["ready_to_scan"]
        )
        self.scaner = Scaner(
            self.ui,
            self.select_row,
            self.config["text"]["info_page"]["ready_to_scan"]
        )

        self.deleter = DeleteFiles(
            self.ui,
            self.config["text"]["info_page"],
            self.dir_selector
        )

        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.resize_btn.clicked.connect(self.maximize)
        self.ui.close_btn.clicked.connect(self.close)

        # Set info page
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.progressBar.setValue(100)
        self.ui.scan_subfolders.setChecked(True)

        # Set table ui
        self.ui.res_table.setAutoFillBackground(False)
        self.ui.res_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.ui.res_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.ui.res_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.ui.res_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.ui.res_table.setHorizontalHeaderItem(3, item)
        self.ui.res_table.horizontalHeader().setVisible(False)
        self.ui.res_table.horizontalHeader().setCascadingSectionResizes(True)
        self.ui.res_table.horizontalHeader().setSortIndicatorShown(False)
        self.ui.res_table.horizontalHeader().setStretchLastSection(True)
        self.ui.res_table.verticalHeader().setVisible(False)
        self.ui.res_table.verticalHeader().setDefaultSectionSize(40)
        self.ui.res_table.verticalHeader().setHighlightSections(False)
        self.ui.res_table.verticalHeader().setSortIndicatorShown(False)
        self.ui.res_table.verticalHeader().setStretchLastSection(False)
        self.ui.res_table.setColumnWidth(0, 30)
        self.ui.res_table.setColumnWidth(1, 100)
        self.ui.res_table.setColumnWidth(2, 80)
        self.ui.res_table.setColumnWidth(3, 110)

        # Set tooltips stylesheet
        self.ui.help_easy.setStyleSheet(self.config["style"]["tool_tip"])
        self.ui.help_medium.setStyleSheet(self.config["style"]["tool_tip"])
        self.ui.help_hard.setStyleSheet(self.config["style"]["tool_tip"])

        # Set tooltips text
        self.ui.help_easy.setToolTip(self.config["text"]["help_messages"]["name_service"])
        self.ui.help_medium.setToolTip(self.config["text"]["help_messages"]["md5_service"])
        self.ui.help_hard.setToolTip(self.config["text"]["help_messages"]["sha_service"])

        # Disable buttons
        self.ui.delete_all_btn.setEnabled(False)
        self.ui.delete_selected_btn.setEnabled(False)
        self.ui.start_btn.setEnabled(False)

        self.ui.medium_btn.setChecked(True)

        self.ui.easy_btn.toggled.connect(self.set_easy_mode)
        self.ui.medium_btn.toggled.connect(self.set_medium_mode)
        self.ui.hard_btn.toggled.connect(self.set_hard_mode)
        self.ui.select_all.toggled.connect(self.select_all)
        self.ui.scan_subfolders.toggled.connect(self.set_max_deep)

        self.ui.select_btn.clicked.connect(self.select_folder)
        self.ui.start_btn.clicked.connect(self.start_scan)
        self.ui.delete_all_btn.clicked.connect(self.delete_all)
        self.ui.delete_selected_btn.clicked.connect(self.delete_selected)
        QSizeGrip(self.ui.resize_grid)

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
            icon = QIcon()
            icon.addFile("style/icons/web_asset_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.resize_btn.setIcon(icon)

        else:
            self.showMaximized()
            icon = QIcon()
            icon.addFile("style/icons/cil-window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.resize_btn.setIcon(icon)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.position().y() <= 60:
            self.offset = QPoint(event.position().x(), event.position().y())

        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.isMaximized():
            icon = QIcon()
            icon.addFile("style/icons/web_asset_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.resize_btn.setIcon(icon)
            self.showNormal()
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def mode_reset(self):
        if self.dir_selector.files:
            self.ui.stackedWidget.setCurrentIndex(0)
            set_info_page(
                self.ui,
                self.config["text"]["info_page"]["ready_to_scan"]["text"],
                self.config["text"]["info_page"]["ready_to_scan"]["icon"]
            )

    def set_easy_mode(self):
        self.mode_reset()
        self.ui.scan_subfolders.setChecked(True)
        self.ui.scan_subfolders.setEnabled(False)
        self.max_deep = True
        self.mode = Mode.EASY

    def set_medium_mode(self):
        self.mode_reset()
        self.ui.scan_subfolders.setChecked(True)
        self.ui.scan_subfolders.setEnabled(True)
        self.max_deep = True
        self.mode = Mode.MEDIUM

    def set_hard_mode(self):
        self.mode_reset()
        self.mode = Mode.HARD

    def select_folder(self):
        self.dir_selector.select_directory(self)

    def start_scan(self):
        self.scaner.find_duplicates(self.mode, self.dir_selector.files)

    def select_row(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.delete_selected_btn.setEnabled(True)
        else:
            for row in range(self.ui.res_table.rowCount()):
                if self.ui.res_table.cellWidget(row, 0).isChecked():
                    break
            else:
                self.ui.delete_selected_btn.setEnabled(False)

    def select_all(self):
        for i in range(self.ui.res_table.rowCount()):
            check_box = self.ui.res_table.cellWidget(i, 0)
            if self.ui.select_all.isChecked():
                check_box.setChecked(True)
                self.ui.delete_selected_btn.setEnabled(True)
            else:
                check_box.setChecked(False)
                self.ui.delete_selected_btn.setEnabled(False)

    @classmethod
    def show_dialog(cls):
        window = DialogWidget()
        result = window.exec()
        if result == QDialog.Accepted:
            return True
        else:
            return False

    def delete_all(self):
        dialog = self.show_dialog()
        if dialog:
            self.deleter.delete_all()
        else:
            set_info_page(self.ui, "CANCELED", ":/icons/icons/warning_white_24dp.svg")
            self.ui.stackedWidget.setCurrentIndex(0)

    def delete_selected(self):
        dialog = self.show_dialog()
        if dialog:
            self.deleter.delete_selected()
        else:
            set_info_page(self.ui, "CANCELED", ":/icons/icons/warning_white_24dp.svg")
            self.ui.stackedWidget.setCurrentIndex(0)

    def set_max_deep(self):
        if self.ui.scan_subfolders.isChecked():
            self.max_deep = True
        else:
            self.max_deep = False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.show()

    sys.exit(app.exec())
