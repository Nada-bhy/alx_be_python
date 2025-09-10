monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are : {monthly_savings}$")


annual_interest = 0.05

projected_year_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

print(f"Projected savings after one year, with interest, is : {projected_year_savings}")