import os
from datetime import datetime

tasks = []

while True:
    print("\n--- To-Do List (Offline Console App) ---")
    print("1. Add new task")
    print("2. Mark task as completed!")
    print("3. Delete task")
    print("4. Exit")

    action = input("Enter your option (1-4): ")

    if action == '1':
        print("\n--- Welcome to Add new task section ---")
        try:
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            print("New task added successfully!")
        except ValueError:
            print("Invalid input!")

        # Optional: check if file exists
        if os.path.exists("tasks.txt"):
            print("tasks.txt file exists.")
        else:
            print("tasks.txt file not found.")

    elif action == '2':
        print("\n--- Welcome to Mark task as completed! section ---")
        if not tasks:
            print("No tasks to complete!")
            continue

        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

        try:
            complete = int(input("Enter task number to mark as completed: "))
            if 1 <= complete <= len(tasks):
                completed = tasks.pop(complete - 1)
                print(f"Task '{completed}' marked as completed and removed!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    elif action == "3":
        print("\n--- Welcome to Delete task section ---")
        if not tasks:
            print("No tasks to delete!")
            continue

        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

        delete_task = input("Do you want to delete all tasks or a single task (one/all): ").lower()

        if delete_task == "all":
            tasks.clear()
            print("All tasks deleted successfully!")
        elif delete_task == "one":
            try:
                delete = int(input("Enter the task number to delete: "))
                if 1 <= delete <= len(tasks):
                    deleted = tasks.pop(delete - 1)
                    print(f"Task '{deleted}' deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("Invalid input... Try again later")

    elif action == "4":
        print("Thank you for using me!!! Goodbye!")
        break

    else:
        print("Invalid action! Please try again later!")