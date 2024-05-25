import os
from typing import List, Dict

from utils.tools import set_info_page
from utils.worker import Worker


class DeleteFiles:
    def __init__(self, ui, config: Dict, dir_selector):
        self.ui = ui
        self.__config = config
        self.dir_selector = dir_selector
        self.len_to_del = 0
        self.scanned = 0
        self.worker = None

    @classmethod
    def delete_files(cls, file_list: List[str]):
        for file in file_list:
            try:
                os.remove(file)
                yield file
            except:
                yield False

    def delete_all(self):
        to_remove = [self.ui.res_table.item(row, 3).text() for row in range(self.ui.res_table.rowCount())]
        self.start_delete(to_remove)

    def delete_selected(self):
        to_remove = []
        for row in range(self.ui.res_table.rowCount()):
            if self.ui.res_table.cellWidget(row, 0).isChecked():
                to_remove.append(self.ui.res_table.item(row, 3).text())
        self.start_delete(to_remove)

    def start_delete(self, file_list: List[str]):
        self.len_to_del = len(file_list)
        self.scanned = 0
        self.ui.progressBar.setValue(self.scanned)
        self.ui.stackedWidget.setCurrentIndex(0)
        set_info_page(
            self.ui,
            self.__config["deleting"]["text"],
            self.__config["deleting"]["icon"]
        )
        self.worker = Worker(self.delete_files, file_list)
        self.worker.data_ready.connect(self.on_file_delete)
        self.worker.finished.connect(self.on_files_deleted)
        self.worker.start()

    def on_file_delete(self, item):
        item = item.replace("/", "\\")
        self.dir_selector.files.remove(item)
        self.scanned += 1
        self.ui.progressBar.setValue(int(self.scanned / self.len_to_del * 100))

    def on_files_deleted(self):
        self.ui.progressBar.setValue(100)
        set_info_page(
            self.ui,
            self.__config["complete"]["text"],
            self.__config["complete"]["icon"]
        )
