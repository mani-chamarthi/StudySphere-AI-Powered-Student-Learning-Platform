from utils import menu
from tasks import add_task, view_tasks

while True:
    
    menu()
    choice = input("\tChoose your choice(1-5):")
    
    if choice == "1":
        add_task()
    
    elif choice == "2":
        view_tasks()
    
    elif choice == "3":
        pass
    
    elif choice == "4":
        pass
    
    elif choice == "5":
        break
    
    else:
        print("\n\t\tInvalid Input")
        
    