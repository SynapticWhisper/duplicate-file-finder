from PySide6 import QtCore
from PySide6.QtCore import Signal


class Worker(QtCore.QThread):
    finished = Signal()
    data_ready = Signal(object)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        for item in self.func(*self.args, **self.kwargs):
            self.data_ready.emit(item)
        self.finished.emit()
