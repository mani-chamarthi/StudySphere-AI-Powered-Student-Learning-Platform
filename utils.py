import json

def menu():
    display = """
    =========== StudySphere ===========
    
    1. Add Task
    2. View Tasks
    3. Mark Task as Complete
    4. Delete Task
    5. Exit
    
    ===================================
    """
    
    print(display)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        tasks = []

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return tasks

    except json.JSONDecodeError:
        tasks = []

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return tasks

def save_tasks(tasks):
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        return True

    except PermissionError:
        print("Error: Permission denied. Cannot save tasks.")
        return False

    except TypeError:
        print("Error: Tasks contain data that cannot be saved as JSON.")
        return False

    except OSError:
        print("Error: Could not save tasks.")
        return False