annual_salary = float(input("Enter your salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise, as a decimal: "))
number_of_months = 0
r = 0.04
current_savings = 0
portion_down_payment = total_cost * 0.25

while current_savings <= portion_down_payment:
    current_savings += current_savings * r / 12 + portion_saved * (annual_salary/12)
    number_of_months += 1

    if number_of_months % 6 == 0:
        annual_salary = annual_salary + (semi_annual_raise * annual_salary)

print("Number of Months: ", number_of_months)
