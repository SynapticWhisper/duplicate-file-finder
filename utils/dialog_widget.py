from PySide6 import QtWidgets

from style.dialog_window import Ui_Dialog


class DialogWidget(QtWidgets.QDialog):
    def __init__(self):
        super(DialogWidget, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.yes_btn.clicked.connect(self.accept)
        self.ui.no_btn.clicked.connect(self.reject)
