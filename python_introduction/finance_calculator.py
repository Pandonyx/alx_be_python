income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")

income = int(income)
expenses = int(expenses)

monthly_savings = income - expenses

print("Your monthly savings are", monthly_savings)

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Projected savings after one year, with interest, is:", projected_savings)
