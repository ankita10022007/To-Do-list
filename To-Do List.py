# To-Do List CLI App

tasks = []


def add_task():
    """Add a new task to the list."""
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- To-Do List -----")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("----------------------")


def remove_task():
    """Remove a task from the list."""
    if not tasks:
        print("\nNo tasks to remove.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def save_tasks():
    """Save tasks to a text file."""
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("Tasks saved to tasks.txt")

    except Exception as e:
        print("Error saving tasks:", e)


def load_tasks():
    """Load tasks from a text file if it exists."""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()

                if task:
                    tasks.append(task)

        print("Tasks loaded from tasks.txt")

    except FileNotFoundError:
        # File doesn't exist yet, which is okay.
        pass


def main():
    """Main program."""
    load_tasks()

    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            save_tasks()

        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()