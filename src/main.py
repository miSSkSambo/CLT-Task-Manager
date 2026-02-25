import json
import os
import sys

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📋 Task List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def delete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("❌ Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"🗑 Removed: {removed}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py add 'Task name'")
        print("  python main.py list")
        print("  python main.py delete <task_number>")
        return

    command = sys.argv[1]

    if command == "add":
        task = sys.argv[2]
        add_task(task)

    elif command == "list":
        list_tasks()

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    else:
        print("❌ Unknown command.")


if __name__ == "__main__":
    main()
