import os

from typing import Dict

from PySide6.QtWidgets import QFileDialog

from utils.tools import set_info_page
from utils.worker import Worker


class DirectorySelector:
    def __init__(self, ui, config: Dict):
        self.ui = ui
        self.__config = config
        self.files = list()
        self.path = None
        self.worker = None

    @classmethod
    def get_files(cls, directory: str):
        """
        Returns a generator that yields all files within a given directory and its subdirectories.

        args:
        - directory: A string representing the directory path.

        yields:
        - A string representing the path of a file in the directory and its subdirectories.

        """
        for root, dirs, files in os.walk(directory):
            for file in files:
                yield os.path.normpath(os.path.join(root, file))

    def select_directory(self, cls):
        """
        Opens a file dialog to allow the user to select a directory and starts a worker thread
        to find all files in the selected directory and its subdirectories.

        args:
        - cls: The parent widget of the file dialog.

        """
        self.files = []

        path = QFileDialog.getExistingDirectory(cls)
        if path:
            self.path = path
            self.ui.select_input.setText(path)

            self.worker = Worker(self.get_files, path)
            self.worker.data_ready.connect(self.add_file)
            self.worker.finished.connect(self.on_ready)
            self.worker.start()

    def add_file(self, item):
        """
        Adds a file path to the list of files found in the selected directory and its subdirectories.

        args:
        - item: A string representing the path of a file.

        """
        self.files.append(item)

    def on_ready(self):
        """
        Updates the application UI with the results of the directory search.

        """
        set_info_page(self.ui, self.__config["text"], self.__config["icon"])
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.start_btn.setEnabled(True)

