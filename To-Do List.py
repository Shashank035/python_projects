import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from a file if it exists."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.read().splitlines()
        return tasks
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display the to-do list."""
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}\n")

def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task removed: {removed}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

if __name__ == "__main__":
    tasks = load_tasks()
    
    while True:
        print("To-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice! Please enter 1-4.\n")
