tasks = [
    
]

def add_task():
    task = {}
    title = input("\n\tEnter Task Title: ")
    task["title"] = title
    task["status"] = False
    tasks.append(task)
    print("\n\tTask added successfully\n")

def view_tasks():
    if not tasks:
        print("\n\tNo tasks available")
        return
    
    for i, task in enumerate(tasks, start=1):
        status_check = "Yes" if task["status"] else "No"
        print(f"\n\tTask {i}\n\tTitle: {task['title']}\n\tCompleted: {status_check}")
    print()

def complete_task():
    if not tasks:
        print("\n\tNo tasks available")
        return
    
    index = int(input("\n\tEnter task number: "))-1
    tasks[index]["status"] = True
    print(f"\n\tTask '{tasks[index]['title']}' is marked as completed")

def delete_task():
    if not tasks:
        print("\n\tNo tasks available")
        return
    
    index = int(input("\n\tEnter task number: "))-1
    tasks.pop(index)