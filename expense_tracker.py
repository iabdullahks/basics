# expense_tracker.py

import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category):
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def show_summary():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expenses: ${total}")
    print("All Expenses:")
    for exp in expenses:
        print(exp)

if __name__ == "__main__":
    print("1. Add Expense")
    print("2. Show Summary")
    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)
    elif choice == "2":
        show_summary()
    else:
        print("Invalid option")
