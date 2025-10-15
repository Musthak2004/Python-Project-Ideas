import json
from datetime import datetime
import os

expenses = []

class Expense:
    def __init__(self):
        pass

    def add_expense(self):
        global expenses

        print('\n--- Welcome to "Add Expense" section ---')
        name = input('Enter your expense name (food, travel or something etc...): ')
        
        try:
            amount = float(input('Enter your budget amount: $'))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        category = input('Enter your category: ')

        # Load existing data safely
        if os.path.exists("expenses.json"):
            try:
                with open("expenses.json", "r", encoding="utf-8") as f:
                    expenses = json.load(f)
            except json.JSONDecodeError:
                print("JSON file is empty or corrupted. Starting fresh.")
                expenses = []
        else:
            expenses = []

        # Create new entry
        entry = {
            'Expense Name': name,
            'Expense amount': amount,
            'Expense category': category,
            'Date_time': datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }

        # Add and save
        expenses.append(entry)

        with open("expenses.json", "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=2)

        print("Expense added successfully!")

    def view_all_expenses(self):
        print('\n--- Welcome to "View All Expenses" section ---')

        if not os.path.exists("expenses.json"):
            print("No expenses file found.")
            return

        try:
            with open("expenses.json", "r", encoding="utf-8") as f:
                expenses_data = json.load(f)
        except json.JSONDecodeError:
            print("Unable to read expenses. File may be corrupted.")
            return

        if not expenses_data:
            print('No expenses!')
            return

        for i, x in enumerate(expenses_data, start=1):
            print(f"\n{i}. Expense Name: {x['Expense Name']}\n   Expense amount: ${x['Expense amount']:.2f}\n   Expense category: {x['Expense category']}\n   Date: {x['Date_time']}")

    def total_spent(self):
        print('\n--- Welcome to "Money" section ---')

        if not os.path.exists("expenses.json"):
            print("No expenses file found.")
            return

        try:
            with open("expenses.json", "r", encoding="utf-8") as f:
                expenses_data = json.load(f)
        except json.JSONDecodeError:
            print("Unable to read expenses. File may be corrupted.")
            return

        if not expenses_data:
            print("Please try to add some expenses!")
            return

        try:
            your_money = float(input("Enter your budget money for all expenses: $"))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        total_spent = sum(x["Expense amount"] for x in expenses_data)
        remaining = your_money - total_spent

        print(f"\nTotal spent: ${total_spent:.2f}")
        print(f"Remaining: ${remaining:.2f}")

# Main loop
e1 = Expense()

while True:
    print("\n--- Welcome to 'Expense Tracker' ---")
    print("1. Add Expense.")
    print("2. View All Expense.")
    print("3. Total Spent.")
    print("4. Exit.")

    choice = input("Enter your choices (1-4): ")

    if choice == '1':
        e1.add_expense()
    elif choice == '2':
        e1.view_all_expenses()
    elif choice == '3':
        e1.total_spent()
    elif choice == '4':
        print("Thank you for using me... Goodbye!")
        break
    else:
        print("Invalid choice Type (1-4)!!!")