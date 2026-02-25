import sys
from task_manager import add_task, list_tasks, delete_task, complete_task


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py add 'Task name'")
        print("  python main.py list")
        print("  python main.py delete <task_number>")
        print("  python main.py complete <task_number>")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(sys.argv[2])
            print("✅ Task added.")

        elif command == "list":
            tasks = list_tasks()
            if not tasks:
                print("📭 No tasks.")
            else:
                for i, task in enumerate(tasks):
                    status = "✔" if task["completed"] else "✘"
                    print(f"{i}. [{status}] {task['title']}")

        elif command == "delete":
            removed = delete_task(int(sys.argv[2]))
            print(f"🗑 Removed: {removed['title']}")

        elif command == "complete":
            complete_task(int(sys.argv[2]))
            print("🎉 Task completed.")

        else:
            print("❌ Unknown command.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
