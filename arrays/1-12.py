categories = ["Food", "Transport", "Rent", "Entertainment"]

expenses = [500, 150, 1000, 200]

max_expense = max(expenses) 
max_expense_index = expenses.index(max_expense) 

print(f"The most expensive category is {categories[max_expense_index]} with an expense of {max_expense}.")
