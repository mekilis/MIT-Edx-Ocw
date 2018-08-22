# MIT6_0001 PS1a - House Hunting

# Ask for the annual salary, portion of salary to be saved and cost of home
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


months = 0
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12

while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12)
    current_savings += portion_saved * monthly_salary
    months += 1

print("Number of months:", months)
