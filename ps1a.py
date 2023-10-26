annual_salary = float(input("Enter your salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

number_of_months = 0
r = 0.04
current_savings = 0
portion_down_payment = total_cost * 0.25

while current_savings <= portion_down_payment:

    current_savings += current_savings * r / 12 + portion_saved * (annual_salary/12)
    number_of_months += 1

print("Number of Months: ", number_of_months)
