from utils import menu
from tasks import add_task, view_tasks, complete_task, delete_task

while True:
    
    menu()
    choice = input("\tChoose your choice(1-5):")
    
    if choice == "1":
        add_task()
    
    elif choice == "2":
        view_tasks()
    
    elif choice == "3":
        complete_task()
    
    elif choice == "4":
        delete_task()
    
    elif choice == "5":
        print("\n\tExiting........\n")
        break
    
    else:
        print("\n\t\tInvalid Input")
        
    