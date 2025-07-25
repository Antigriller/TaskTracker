from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QDateEdit, QTextEdit, QLineEdit, QCheckBox

from model import Task


class EditTaskDialog(QDialog):
    def __init__(self, task: Task, parent=None):
        super().__init__(parent)

        self.title_input = QLineEdit()
        self.description_input = QTextEdit()
        self.date_input = QDateEdit()
        self.done_checkbox = QCheckBox()

        self.title_input.setText(task.title)
        self.description_input.setText(task.description)
        self.date_input.setDate(QDate(task.deadline.year, task.deadline.month, task.deadline.day))
        self.done_checkbox.setChecked(task.done)