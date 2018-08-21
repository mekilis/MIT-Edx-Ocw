# MIT6_0001 PS1c - Finding the right amount to save away

# globals
total_cost = 1000000.0
portion_down_payment = 0.25 * total_cost

def compute_savings_36months(annual_salary, portion_saved):
    portion_saved = portion_saved / float(10000)
    semi_annual_raise = 0.07
    months = 0
    current_savings = 0.0
    r = 0.04
    monthly_salary = annual_salary / 12
    
    for _ in range(36):
        current_savings += (current_savings*r/12)
        current_savings += portion_saved * monthly_salary
        months += 1
        if months % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            
    return current_savings

# Ask only for the annual salary
annual_salary = float(input("Enter the starting salary: "))

# bisection search
steps = 0
epilson = 29.0 # within $100
low, high = 0, 10000
guess = (low + high) / 2.0 # portion_saved

no_changes = 0 # needed to catch recurring non possible scenarios
prev_savings = 0
possible = True

savings = compute_savings_36months(annual_salary, guess)
while abs(savings - portion_down_payment) > epilson:
    if savings <= portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    steps += 1

    if prev_savings == savings:
        no_changes += 1
    else:
        no_changes = 0

    if no_changes >= 10:
        possible = False
        break

    prev_savings = savings
    savings = compute_savings_36months(annual_salary, guess)
    
if possible:
    print("Best savings rate: {0:.4f}".format(guess / 10000))
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
