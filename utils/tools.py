from typing import Dict
from json import load

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


def get_config(filename: str) -> Dict:
    with open(filename, "r", encoding="utf-8") as file:
        data: Dict = load(file)
    return data


def set_info_page(ui, text: str, icon_path: str):
    icon = QIcon()
    icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)
    ui.info_icon.setIcon(icon)
    ui.info_icon.setIconSize(QSize(100, 100))
    ui.info_text.setText(text)
