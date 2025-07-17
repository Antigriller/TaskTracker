from datetime import date

from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QDialog, QLineEdit, QFormLayout, QDateEdit, QCheckBox, QDialogButtonBox, QTextEdit

from model import Task


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Новая задача")

        self.title_input = QLineEdit()
        self.description_input = QTextEdit()
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        self.done_checkbox = QCheckBox("Выполнено")

        layout = QFormLayout()
        layout.addRow("Название", self.title_input)
        layout.addRow("Описание", self.description_input)
        layout.addRow("Дата", self.date_input)
        layout.addRow("Статус", self.done_checkbox)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_task(self) -> Task:
        q_date = self.date_input.date()
        deadline = date(q_date.year(), q_date.month(), q_date.day())
        return Task(
            title=self.title_input.text(),
            description=self.description_input.text(),
            deadline=deadline,
            done=self.done_checkbox.checkState() == Qt.CheckState.Checked
        )