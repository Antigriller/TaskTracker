from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QMessageBox, QDialog)

from add_task_dialog import AddTaskDialog
from model import TaskManager, Task
from datetime import date


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Tracker")

        self.manager = TaskManager()
        try:
            self.manager.load_from_file("tasks.json")
        except:
            pass

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Название", "Дедлайн", "Выполнено"])

        self.add_button = QPushButton("Добавить задачу")
        self.remove_button = QPushButton("Удалить")
        self.save_button = QPushButton("Сохранить")

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)
        self.save_button.clicked.connect(self.save_tasks)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_button)
        btn_layout.addWidget(self.remove_button)
        btn_layout.addWidget(self.save_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.refresh_table()

    def refresh_table(self):
        self.table.setRowCount(0)
        for task in self.manager.get_all():
            row = self.table.rowCount()
            self.table.insertRow(row)

            self.table.setItem(row, 0, QTableWidgetItem(task.title))
            self.table.setItem(row, 1, QTableWidgetItem(str(task.deadline)))
            self.table.setItem(row, 2, QTableWidgetItem("✔" if task.done else "✗"))

    def add_task(self):
        dialog = AddTaskDialog(self)
        if dialog.exec() == QDialog.Accepted:
            task = dialog.get_task()
            self.manager.add_task(task)
            self.refresh_table()

    def remove_task(self):
        row = self.table.currentRow()
        if row >= 0:
            self.manager.remove_task(row)
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")

    def save_tasks(self):
        self.manager.save_to_file("tasks.json")
        QMessageBox.information(self, "Сохранено", "Список задач сохранён")