from task import Task

from database import (
    create_database,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)

class TaskManager:
    def __init__(self):
        create_database()
        
        rows = get_tasks()

        self.tasks = []

        for row in rows:
            task = Task(
                title=row[1],
                status=row[2],
                task_id=row[0]
            )

            self.tasks.append(task)

    def get_task_by_display_number(self, display_number):

        if display_number < 1 or display_number > len(self.tasks):
            return None

        return self.tasks[display_number - 1]

    def add_task(self, title):

        title = title.strip()

        if not title:
            print("Task title cannot be empty")
            return

        for task in self.tasks:
            if task.title.lower() == title.lower():
                print("\nTask already exists")
                return
        
        task = Task(title)
        
        task_id = add_task(task.title, task.status)

        if task_id is None:
            return

        task.id = task_id

        self.tasks.append(task)

        print("\nTask added successfully")
    
    def view_tasks(self):

        if not self.tasks:
            print("\nNo tasks available")
            return

        print("\n========== YOUR TASKS ==========")

        for display_number, task in enumerate(self.tasks, start=1):
            print(f"{display_number}. {task.title} --> {task.status}")

        print("===============================")
    
    def complete_task(self):
    
        if not self.tasks:
            print("\nNo tasks available")
            return

        try:
            display_number = int(
                input("\nEnter task number to mark as complete: ")
            )

            task = self.get_task_by_display_number(display_number)

            if task is None:
                print("\nTask number does not exist")
                return

            if task.status == "Complete":
                print("\nTask is already marked as complete")
                return

            rows_affected = complete_task(task.id)

            if rows_affected == 0:
                print("\nTask could not be marked as complete")
                return

            task.status = "Complete"

            print("\nTask marked as complete")

        except ValueError:
            print("\nEnter a valid task number")

    def delete_task(self):

        if not self.tasks:
            print("\nNo tasks available")
            return

        try:
            display_number = int(
                input("\nEnter task number to delete: ")
            )

            task = self.get_task_by_display_number(display_number)

            if task is None:
                print("\nTask number does not exist")
                return

            if task.status == "Pending":
                print("\nTask is not completed")
                print("\nContinue delete")
                print("\nEnter 1 to continue")
                print("\nEnter 0 to stop")

                choice = input("\nDelete the task or not: ").strip()

                if choice == "0":
                    print("\nTask deletion discarded")
                    return

                elif choice != "1":
                    print("\nEnter 1 or 0")
                    return

            rows_affected = delete_task(task.id)

            if rows_affected == 0:
                print("\nTask could not be deleted")
                return

            self.tasks.remove(task)

            print("\nTask deleted successfully")

        except ValueError:
            print("\nEnter a valid task number")

