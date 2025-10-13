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

        print("Expense added successfully!")

    def view_all_expenses(self):
        print('\n--- Welcome to "View All Expenses" section ---')
        if not expenses:
            print('No expenses!')
            return
        
        else:
            for i, x in enumerate(expenses, start=1):
                print(f"\n{i}. Expense Name: {x['Expense Name']}\n Expense amount: {x['Expense amount']}\n Expense category: {x['Expense category']}\n Date: {x['Date_time']}")

    def money(self):
        print('\n--- Welcome to "Money" section ---')
        if not expenses:
            print("Please try to add some expenses!")
            return
        
        else:
            your_money = ("Enter your budget money for all expenses: ")
            total_spent = 
            remaining = your_money - total_spent

            print("Total spent: ", total_spent)
            print("Remaining: ", remaining)

e1 = Expense()
e1.add_expense()
e1.view_all_expenses()
e1.money()