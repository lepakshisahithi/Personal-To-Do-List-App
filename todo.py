import json

# Task Class
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

# Save tasks to JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Load tasks from JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Add Task
def add_task(tasks):
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    category = input("Enter Category (Work/Personal/Urgent): ")

    task = {
        "title": title,
        "description": description,
        "category": category,
        "completed": False
    }

    tasks.append(task)
    print("Task Added Successfully!")

# View Tasks
def view_tasks(tasks):
    if not tasks:
        print("No Tasks Available")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print("\nTask", i)
        print("Title:", task["title"])
        print("Description:", task["description"])
        print("Category:", task["category"])
        print("Status:", status)

# Mark Task as Completed
def complete_task(tasks):
    view_tasks(tasks)

    if tasks:
        num = int(input("\nEnter Task Number to Complete: ")) - 1

        if 0 <= num < len(tasks):
            tasks[num]["completed"] = True
            print("Task Marked as Completed")
        else:
            print("Invalid Task Number")

# Delete Task
def delete_task(tasks):
    view_tasks(tasks)

    if tasks:
        num = int(input("\nEnter Task Number to Delete: ")) - 1

        if 0 <= num < len(tasks):
            tasks.pop(num)
            print("Task Deleted Successfully")
        else:
            print("Invalid Task Number")

# Main Function
def main():
    tasks = load_tasks()

    while True:
        print("\n===== PERSONAL TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks Saved Successfully")
            print("Exiting Application...")
            break

        else:
            print("Invalid Choice! Please Try Again.")

if __name__ == "__main__":
    main()