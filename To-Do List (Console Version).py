import os
from datetime import datetime

to_do = []

class Project:
    def __init__(self):
        pass  # No setup needed for now

    def add_task(self):
        try:
            task = input('Your task: ')
        except ValueError:
            print('Value error')
            return
        
        entry = {
            'Task': task,
            'Date_Time': datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }

        to_do.append(entry)
        print("Task added successfully!")

    def complete_task(self):
        print('\n--- Welcome to "complete task" section ---')

        if not to_do:
            print("No tasks to complete.")
            return
        
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['Task']} (Added on {task['Date_Time']})")

        try:
            choice = int(input("Enter the task number to mark as complete: "))
            if 1 <= choice <= len(to_do):
                removed = to_do.pop(choice - 1)
                print(f"Task '{removed['Task']}' marked as complete and removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        print('\n--- Welcome to "delete task" section ---')

        if not to_do:
            print("No tasks to delete.")
            return
            
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['Task']} (Added on {task['Date_Time']})")

        tasks = input("Do you want to delete ('one task') or ('all tasks')? ").lower()

        if tasks == 'one task':
            try:
                choice = int(input("Enter the task number to delete: "))
                if 1 <= choice <= len(to_do):
                    removed = to_do.pop(choice - 1)
                    print(f"Task '{removed['Task']}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif tasks == 'all tasks':
            to_do.clear()
            print("All tasks removed successfully!")

        else:
            print("Invalid option. Please type 'one task' or 'all tasks'.")

    def show_all(self):
        print('\n--- Welcome to "show all" section ---')

        if not to_do:
            print('No tasks to show.')
            return
        
        print("\n--- Your tasks ---")
        for i, task in enumerate(to_do, start=1):
            print(f"{i}. {task['Task']} (Added on {task['Date_Time']})")

    def save_to_file(self):
        if not to_do:
            print("No tasks to save.")
            return

        with open("tasks.txt", "w") as file:
            for i, task in enumerate(to_do, start=1):
                line = f"{i}. {task['Task']} (Added on {task['Date_Time']})\n"
                file.write(line)
                
        print("All tasks saved to 'tasks.txt' successfully!")

project = Project()

while True:
    print('\n--- Welcome to To-Do List (Console Version) ---')
    print('1. Add Task.')
    print('2. Complete task.')
    print('3. Delete Task/ Tasks.')
    print('4. Show All Tasks.')
    print('5. Save to File.')
    print('6. Exit.')

    try:
        choice = int(input('Enter your choice (1-6): '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        project.add_task()
    elif choice == 2:
        project.complete_task()
    elif choice == 3:
        project.delete_task()
    elif choice == 4:
        project.show_all()
    elif choice == 5:
        project.save_to_file()
    elif choice == 6:
        print('\nThank You for using me! Goodbye!')
        break

    else:
        print('Invalid choices')