# main.py

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
