from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class PageFavorites(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Vos favoris")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
