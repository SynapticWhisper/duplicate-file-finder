from PySide6 import QtWidgets, QtCore

from utils.mode import Mode
from utils.tools import set_info_page
from utils.worker import Worker
from hashlib import md5, sha256
from service.HashService import generate_table_data as hash_service
from service.NameService import generate_table_data as name_service


class Scaner:
    def __init__(self, ui, selector, config):
        self.__config = config
        self.ui = ui
        self.select_row = selector
        self.scanned = 0
        self.duplicates_count = 0
        self.size = 0
        self.files_count = 0
        self.worker = None

    def find_duplicates(self, mode, files):
        self.files_count = len(files)
        self.clear_table()
        if mode == Mode.MEDIUM:
            self.worker = Worker(hash_service, files, md5)
        elif mode == Mode.HARD:
            self.worker = Worker(hash_service, files, sha256)
        else:
            self.worker = Worker(name_service, files)

        # Show table widget and reset progress bar
        self.ui.stackedWidget.setCurrentIndex(1)
        self.worker.data_ready.connect(self.on_data_ready)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.start()

    # After the scan is complete
    def on_worker_finished(self):
        self.ui.progressBar.setValue(100)
        if self.ui.res_table.rowCount() > 0:
            self.ui.delete_all_btn.setEnabled(True)
            self.ui.select_all.setEnabled(True)
        else:
            set_info_page(self.ui, "DUPLICATES NOT FOUND!", self.__config["icon"])
            self.ui.stackedWidget.setCurrentIndex(0)

    # Add item to the table
    def on_data_ready(self, item):
        self.scanned += 1
        self.ui.files_count.setText(str(self.scanned))
        if item:
            self.duplicates_count += 1
            self.ui.duplicates_count.setText(str(self.duplicates_count))
            self.size += (item["file_size"] / 1024)
            self.ui.size_count.setText("%.2f KB" % self.size)
            row_position = self.ui.res_table.rowCount()
            self.ui.res_table.insertRow(row_position)

            check_box = QtWidgets.QCheckBox()
            check_box.setStyleSheet(
                "background-color: #333;\n"
                "padding-left: 15px;"
            )
            check_box.toggled.connect(self.select_row)
            self.ui.res_table.setCellWidget(row_position, 0, check_box)

            file_name = QtWidgets.QTableWidgetItem()
            file_name.setText(str(item["file_name"]))
            file_name.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable)
            self.ui.res_table.setItem(row_position, 1, file_name)

            file_size = QtWidgets.QTableWidgetItem()
            file_size.setText("%.2f KB" % (item["file_size"] / 1024))
            file_size.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable)
            self.ui.res_table.setItem(row_position, 2, file_size)

            file_path = QtWidgets.QTableWidgetItem()
            file_path.setText(str(item["file_path"].replace("\\", "/")))
            file_path.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable)
            self.ui.res_table.setItem(row_position, 3, file_path)
        self.ui.progressBar.setValue(int(self.scanned / self.files_count * 100))

    def clear_table(self):
        self.size = 0
        self.scanned = 0
        self.duplicates_count = 0
        self.ui.size_count.setText("N/A")
        self.ui.files_count.setText("N/A")
        self.ui.duplicates_count.setText("N/A")
        self.ui.delete_selected_btn.setEnabled(False)
        self.ui.delete_all_btn.setEnabled(False)
        self.ui.res_table.setRowCount(0)
