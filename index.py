

tasks = {}

def get_id(tasks):
    return max(tasks.keys(), default=0) + 1

def tasks_to_string(tasks):
    result = ""
    for task_id, task_values in tasks.items():
        result += f"{task_id}:{task_values['title']}|{task_values['desk']}|{task_values['priority']}|{task_values['status']}\n"
    return result

def priority_tasks():
    while True:
        try:
            priority = int(input("Choose priority (1-low, 2-middle, 3-high): "))
            if priority == 1:
                return "low"
            elif priority == 2:
                return "middle"
            elif priority == 3:
                return "high"
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def status_tasks():
    while True:
        try:
            status = int(input("Enter status (1-not started, 2-in progress, 3-completed): "))
            if status == 1:
                return "not started"
            elif status == 2:
                return "in progress"
            elif status == 3:
                return "completed"
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_task(tasks):
    task_id = get_id(tasks)
    title = input("Enter task title: ")
    desk = input("Enter task description: ")
    priority = priority_tasks()
    status = status_tasks()
    tasks[task_id] = {
        "title": title,
        "desk": desk,
        "priority": priority,
        "status": status
    }
    save_tasks(tasks)
    print(f"Task {task_id} created.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.write(tasks_to_string(tasks))

def read_tasks(filename):
    tasks = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    task_id, title = parts[0].split(":")
                    tasks[int(task_id)] = {
                        "title": title,
                        "desk": parts[1],
                        "priority": parts[2],
                        "status": parts[3]
                    }
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
    return tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id}: {task['title']} | {task['desk']} | Priority: {task['priority']} | Status: {task['status']}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        delete_choice = int(input("Enter the ID of the task to delete: "))
        if delete_choice in tasks:
            del tasks[delete_choice]
            save_tasks(tasks)
            print(f"Task {delete_choice} deleted.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def ask(tasks):
    while True:
        print("\nMenu:")
        print("1. Create a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        try:
            choice = int(input("Choose an action: "))
            if choice == 1:
                create_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tasks = read_tasks("tasks.txt")
    ask(tasks)
