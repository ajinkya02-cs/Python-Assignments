tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def view_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['task']}")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Done\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_task(input("Enter task: "))
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done(int(input("Enter task number: ")) - 1)
    elif choice == '4':
        break
