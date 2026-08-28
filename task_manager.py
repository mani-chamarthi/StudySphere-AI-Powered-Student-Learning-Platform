from  task import Task
from utils import load_tasks, save_tasks
import json

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):

        title = title.strip()

        if not title:
            print("Task title cannot be empty")
            return

        task = Task(title)
        
        self.tasks.append(task.to_dict())
        
        if save_tasks(self.tasks):
            print("\nTask added successfully")
    
    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available")
            return
        
        print("\n==========YOUR TASKS==========")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['title']} --> {task['status']}")
        print("==============================")
    
    def complete_task(self):
        if not self.tasks:
            print("\nNo tasks available")
            return
        try:
            task_number = int(input("\nEnter task number to mark as complete: "))
        
            if task_number <= 0 or task_number > len(self.tasks):
                print(f"\nEnter task number in range of 1 - {len(self.tasks)}")
                return
        
            index = task_number - 1
        
            if self.tasks[index]["status"] == "Complete":
                print("\nTask is already marked")
                return
        
            self.tasks[index]["status"] = "Complete"
            
            if save_tasks(self.tasks):
                print("\nTask marked as complete")
        
        except ValueError:
            print("Enter a valid task number")
    
    def delete_task(self):
        if not self.tasks:
            print("\nNo tasks available")
            return
        
        try:
            
            task_number = int(input("\nEnter task number to delete: "))

            if task_number <= 0 or task_number > len(self.tasks):
                print(f"\nEnter task number in range of 1 - {len(self.tasks)}")
                return

            index = task_number - 1

            if self.tasks[index]["status"] == "Pending":
                print("\nTask is not completed")
                print("\nContinue delete")
                print("\nEnter 1 to continue")
                print("\nEnter 0 to stop")

                choice = input("\nDelete the task or not: ")

                if choice == "1":
                    pass
                
                elif choice == "0":
                    print("\nTask deletion discarded")
                    return

                else:
                    print("\nEnter 1 or 0")
                    return

            del self.tasks[index]
            
            if save_tasks(self.tasks):
                print("\nTask is deleted successfully")
        
        except ValueError:
            print("Enter a valid task number")
