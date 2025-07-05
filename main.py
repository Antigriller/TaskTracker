# main.py

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Task Tracker")
window.resize(800, 600)
window.show()

app.exec()