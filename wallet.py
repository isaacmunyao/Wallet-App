#Import json module to help with reading json file
import json

#Variables
income = 0.0
expenses = []
savings = 0.0

#loading the data
def load_data():
    global income, expenses, savings
    try:
        #reading the json file
        with open("transaction.json", "r") as file:
            data = json.load(file)
            income = data.get("income", 0.0)
            expenses = data.get("expenses", [])
            savings = data.get("savings", 0.0)
    except FileNotFoundError:
        pass

 #save data
def save_data():
    data ={
        "income":income,
        "expenses":expenses,
        "savings":savings
     }
    with open("transaction.json", "w") as file:
        json.dump(data, file)

#Add Income
def add_income():
    global income
    amount = float(input("Enter amount: "))
    income = income + amount
    print(f"{amount} has been added to your wallet. Total income is now {income}")

#Add Expense
def add_expense():
    global expenses
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expense ={
        "description": description,
        "amount":amount,
        "category": category
    }
    expenses.append(expense)
    print(f"New expense {category} of amount {amount} added successfully")

#Calculate savings
def calculate_savings():
    global savings
    savings = income - sum(expense["amount"] for expense in expenses)
    print(f"Total savings is {savings}")

#Expense per category
def expense_category():
    category = input("Enter category: ")
    expense_amount = sum(expense["amount"] for expense in expenses if expense["category"]==category)
    print(f"Total expense for {category} is {expense_amount}")


#main program
def main():
    load_data()
      
    while True:
        print("===== Personal Wallet Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Savings")
        print("4. Generate Expense Report by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_savings()
        elif choice == "4":
            expense_category()
        elif choice == "5":
            save_data()
            print("Thank you for using the Personal Wallet Tracker!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()


    
 

        