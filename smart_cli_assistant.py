#!/usr/bin/env python3
# Mudita's To-Do Manager + Logging (Smart CLI Assistant)

import os
import datetime

TODO_FILE = "todo.txt"
LOG_FILE = "activity.log"

def log_action(action):
    """Append an action with timestamp to the log file."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {action}\n")

def todo_manager():
    """Command-line To-Do manager with persistent storage and logging."""
    while True:
        print("\n==========================")
        print("      TO-DO MANAGER")
        print("==========================")
        print("1) Add Task")
        print("2) View Tasks")
        print("3) Delete Task")
        print("4) Clear All Tasks")
        print("5) Exit")
        choice = input("Choose [1-5]: ").strip()

        if choice == "1":
            task = input("Enter new task: ").strip()
            if task:
                with open(TODO_FILE, "a") as f:
                    f.write(task + "\n")
                print("✅ Task added.")
                log_action(f"Added task: {task}")
            else:
                print("⚠️ No text entered. Task not added.")

        elif choice == "2":
            if not os.path.exists(TODO_FILE):
                print("No tasks yet.")
            else:
                with open(TODO_FILE, "r") as f:
                    tasks = [t.strip() for t in f if t.strip()]
                if not tasks:
                    print("No tasks yet.")
                else:
                    print("\nYour tasks:")
                    for i, t in enumerate(tasks, 1):
                        print(f"{i}. {t}")
                log_action("Viewed tasks")

        elif choice == "3":
            if not os.path.exists(TODO_FILE):
                print("No tasks to delete.")
            else:
                with open(TODO_FILE, "r") as f:
                    tasks = [t for t in f if t.strip()]
                if not tasks:
                    print("No tasks to delete.")
                else:
                    print("\nSelect a task to delete:")
                    for i, t in enumerate(tasks, 1):
                        print(f"{i}. {t.strip()}")
                    num = input("Enter number (or Enter to cancel): ").strip()
                    if not num:
                        print("Cancelled.")
                    else:
                        try:
                            idx = int(num) - 1
                            removed = tasks.pop(idx).strip()
                            with open(TODO_FILE, "w") as f:
                                f.writelines(tasks)
                            print(f"❌ Deleted: {removed}")
                            log_action(f"Deleted task: {removed}")
                        except (ValueError, IndexError):
                            print("Invalid number. No task deleted.")

        elif choice == "4":
            confirm = input("Are you sure you want to clear all tasks? (y/N): ").strip().lower()
            if confirm == "y":
                open(TODO_FILE, "w").close()
                print("🗑️ All tasks cleared.")
                log_action("Cleared all tasks")
            else:
                print("Cancelled. No changes made.")

        elif choice == "5":
            print("Exiting To-Do Manager. Bye!")
            log_action("Exited To-Do Manager")
            break

        else:
            print("Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_manager()



       
           
           
