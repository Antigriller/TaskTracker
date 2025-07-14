# main.py

from model import Task, TaskManager
from datetime import date

def main():
    manager = TaskManager()

    # Добавим пару задач
    manager.add_task(Task("Купить молоко", "Магазин возле дома", date(2025, 7, 6)))
    manager.add_task(Task("Сделать проект", "GUI через PySide6", date(2025, 7, 10)))

    # Сохраним
    manager.save_to_file("tasks.json")
    print("Список сохранён.")

    # Очистим, затем загрузим снова
    manager.tasks.clear()
    manager.load_from_file("tasks.json")

    # Выведем
    for i, task in enumerate(manager.get_all(), 1):
        print(f"{i}. {task.title} — До: {task.deadline}, Выполнено: {task.done}")

if __name__ == "__main__":
    main()
