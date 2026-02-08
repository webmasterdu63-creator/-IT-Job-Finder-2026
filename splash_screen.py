from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer

class SplashScreen(QSplashScreen):
    def __init__(self):
        # Image de fond (tu mettras ton splash.png dans /assets)
        pixmap = QPixmap("assets/splash.png")

        super().__init__(pixmap)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFont(QFont("Segoe UI", 12))

        self.message = "Chargement..."
        self.showMessage(
            self.message,
            Qt.AlignBottom | Qt.AlignHCenter,
            Qt.white
        )

        # Animation du texte "Chargement..."
        self.dot_count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_text)
        self.timer.start(400)

    def animate_text(self):
        self.dot_count = (self.dot_count + 1) % 4
        dots = "." * self.dot_count
        self.showMessage(
            f"Chargement{dots}",
            Qt.AlignBottom | Qt.AlignHCenter,
            Qt.white
        )
