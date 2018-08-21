# MIT6_0001 PS1b - Saving, with a raise

# Ask for the annual salary, portion of salary to be saved and cost of home
# In addition, ask for the semiannual salary raise
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))


months = 0
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12

while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12)
    current_savings += portion_saved * monthly_salary
    months += 1
    if months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)
        monthly_salary = annual_salary / 12

print("Number of months:", months)
