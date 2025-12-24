tasks = []

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Goodbye 👋")
        break
