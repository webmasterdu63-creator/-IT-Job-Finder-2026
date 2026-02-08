from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class PageHome(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Bienvenue dans IT Job Finder 2026")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout.addWidget(label)
