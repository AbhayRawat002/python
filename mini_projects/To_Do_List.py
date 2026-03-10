tasks=[]

def view_task():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print(f"Your to-do list: {tasks}")

def add_tasks(tasks):
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"Your to-do list: {tasks}")

def remove_task(tasks):
    task_to_remove = input("Enter task to remove: ")
    try:
        tasks.remove(task_to_remove)
        print(f"Your to-do list: {tasks}")
    except ValueError:
        print("Task not found!")


while True:

    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    user_choice=int(input("Enter your choice: "))

    if user_choice == 1:
        view_task()
    elif user_choice== 2:
        add_tasks(tasks)
    elif user_choice== 3:
        remove_task(tasks)
    elif user_choice== 4:
        break


