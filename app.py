import os
TASKS_FILE="ex.txt"

#loading task
def load_tasks():
    if not os.path.exists(TASKS_FILE):  #  Only return [] if file does NOT exist
        return []
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]


#saving task
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

#adding task
def add_task():
    task = input("Enter a task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")
    
#viewing task
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-do list:")
        for i, task in enumerate(tasks, 1):
            print(i,task)

#updating task
def update_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return
    
    view_tasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):  # ✅ correct range check
            new_task = input("Enter the new task: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

        
#deleting task
def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
        else:
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully!")
    except ValueError:
        print("Please enter a valid number.")
        
#main function
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the program.... Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()