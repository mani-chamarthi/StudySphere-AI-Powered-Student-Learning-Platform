from utils import menu
from task_manager import TaskManager

manager = TaskManager()

while True:
    try:
        menu()

        choice = input("\nEnter your choice(1-5): ").strip()

        if choice == "1":
            title = input("\nEnter title for task: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.complete_task()

        elif choice == "4":
            manager.delete_task()

        elif choice == "5":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid choice")

    except KeyboardInterrupt:
        print("\n\nERROR: Program interrupted.\n")
        break

    except EOFError:
        print("\n\nERROR: Input ended.\n")
        break