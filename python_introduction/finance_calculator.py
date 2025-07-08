income = input("Enter your monthly income:")
expenses = input("Enter your monthly expenses:")

income = int(income)
expenses = int(expenses)

savings = income - expenses

print("Your monthly savings are:", savings)

projected_savings = (savings * 12) + (savings * 12 * 0.05)

print("Projected savings after one year:", projected_savings)
