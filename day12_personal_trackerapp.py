import os
import csv
from datetime import datetime

def add_expense(description, amount):
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def view_expenses():
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print("Expenses:")
            for row in reader:
                print(f"Description: {row[0]}, Amount: {row[1]}, Date: {row[2]}")
    else:
        print("No expenses recorded.")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            add_expense(description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
