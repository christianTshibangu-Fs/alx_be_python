monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")

monthly_savings = int(monthly_income) - int(monthly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected savings after one year, with interest, is: {projected_savings}")