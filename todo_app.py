"""
To-Do List Application
----------------------
A simple command-line To-Do List app built with Python.

Features:
✅ Add tasks
✅ View tasks
✅ Delete tasks
✅ Quit the program

This project demonstrates:
- Lists for storage
- Functions for organization
- Input validation
- Error handling with try/except/finally
"""

# -----------------------------
# Global list to store tasks
# -----------------------------
tasks = []


# -----------------------------
# Function Definitions
# -----------------------------
def display_menu():
    """Displays the main menu options."""
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    print("================================")


def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task added: '{task}'")
    else:
        print("⚠️ Task cannot be empty!")


def view_tasks():
    """Display all tasks in the to-do list."""
    if not tasks:
        print("\n📭 No tasks found. Your to-do list is empty!")
    else:
        print("\n📝 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def delete_task():
    """Delete a task by its number."""
    if not tasks:
        print("\n⚠️ Cannot delete. Your to-do list is empty!")
        return

    view_tasks()  # Show tasks before deletion

    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"🗑 Task deleted: '{removed_task}'")
        else:
            print("❌ Invalid task number. Please choose a valid one.")
    except ValueError:
        print("⚠️ Please enter a valid number!")


def quit_app():
    """Exit the application gracefully."""
    print("\n👋 Goodbye! Thanks for using the To-Do List App.")
    exit()


def main():
    """Main loop that runs the app."""
    print("🎯 Welcome to Your To-Do List App!")

    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        try:
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                delete_task()
            elif choice == '4':
                quit_app()
            else:
                print("🚫 Invalid choice. Please select 1, 2, 3, or 4.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")
        finally:
            print("\n------------------------------------")


# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    main()
