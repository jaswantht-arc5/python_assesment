annual_salary = float(input("Enter your starting annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04

down_payment = 0.25 * total_cost
months = 36

low = 0
high = 10000
steps = 0
best_rate = None

while low <= high:
    steps += 1
    rate = (low + high) // 2
    portion_saved = rate / 10000

    current_savings = 0
    monthly_salary = annual_salary / 12

    for m in range(1, months + 1):
        current_savings += current_savings * (r / 12)
        current_savings += monthly_salary * portion_saved
        if m % 6 == 0:
            monthly_salary *= (1 + semi_annual_raise)

    if abs(current_savings - down_payment) <= 100:
        best_rate = portion_saved
        break
    elif current_savings < down_payment:
        low = rate + 1
    else:
        high = rate - 1

if best_rate is None:
    print("Not possible to save enough in 36 months")
else:
    print("Best savings rate:", best_rate)
    print("Steps in bisection search:", steps)