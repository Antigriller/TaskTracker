import json
from datetime import date, datetime
from typing import List


class Task:
    def __init__(self, title: str, description: str, deadline: date, done: bool = False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = done

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.isoformat(),
            "done": self.done
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            title=data["title"],
            description=data["description"],
            deadline=datetime.fromisoformat(data["deadline"]).date(),
            done=data["done"],
        )


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_all(self) -> List[Task]:
        return self.tasks

    def save_to_file(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_from_file(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(entry) for entry in data]