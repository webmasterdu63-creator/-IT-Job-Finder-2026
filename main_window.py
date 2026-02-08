from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QStackedWidget
)
from PySide6.QtCore import Qt

from .sidebar import SideBar
from .pages.page_home import PageHome
from .pages.page_search import PageSearch
from .pages.page_favorites import PageFavorites
from .pages.page_settings import PageSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IT Job Finder 2026")
        self.setMinimumSize(1100, 700)

        # Layout principal
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # Sidebar
        self.sidebar = SideBar()
        main_layout.addWidget(self.sidebar)

        # Zone centrale = QStackedWidget
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack, stretch=1)

        # Ajout des pages
        self.page_home = PageHome()
        self.page_search = PageSearch()
        self.page_favorites = PageFavorites()
        self.page_settings = PageSettings()

        self.stack.addWidget(self.page_home)      # index 0
        self.stack.addWidget(self.page_search)    # index 1
        self.stack.addWidget(self.page_favorites) # index 2
        self.stack.addWidget(self.page_settings)  # index 3

        self.setCentralWidget(main_widget)

        # Connexion des boutons
        self.sidebar.buttons[0].clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.sidebar.buttons[1].clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.sidebar.buttons[2].clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.sidebar.buttons[3].clicked.connect(lambda: self.stack.setCurrentIndex(3))
