# Part A: House Hunting
# program that calculate how many months it will take to save up enough money for a '''downpayment''' -> floats

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

# savings
total_savings = 0
r = 0.04
total_savings = 0

portion_down_payment = 0.25
downpayment = total_cost * portion_down_payment

num_of_months = 0
while total_savings < downpayment:
    interest = total_savings*r/12
    total_savings += interest + portion_saved*(annual_salary/12)
    num_of_months += 1

print("Number of months: " + str(num_of_months))
