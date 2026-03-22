tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(i + 1, "-", task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task removed")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")