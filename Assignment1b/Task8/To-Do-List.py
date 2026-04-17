# TO-DO LIST

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"'{task}' has been added to your list.")

    elif choice == "3":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                removed_task = todo_list.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from your list.")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting the to-do list. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-4.")
