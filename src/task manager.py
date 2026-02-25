import json
import os

TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title):
    tasks = load_tasks()
    tasks.append({
        "title": title,
        "completed": False
    })
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    return tasks


def delete_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task number")

    removed = tasks.pop(index)
    save_tasks(tasks)
    return removed


def complete_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task number")

    tasks[index]["completed"] = True
    save_tasks(tasks)
