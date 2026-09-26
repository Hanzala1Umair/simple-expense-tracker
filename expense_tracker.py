# expense tracker

expenses = []

print("---- Simple expense tracker ----")
print("Welcome to the Expense Tracker!")

while True:
    item = input("what did you spend on ?")
    if item.lower() == "done":
        break
    amount = float(input("how much ? Rs."))
    expenses.append({"item": item, "amount": amount})
    
print("\n---- Expenses Summary ----")
total_expense = 0
for expense in expenses:
    print(f"{expense['item']}: Rs.{expense['amount']}")
    total_expense += expense['amount']
    
    
print(f"\nTotal Expenses: Rs.{total_expense}")
