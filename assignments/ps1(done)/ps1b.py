annual_salary = float(input("please input your annual salary "))
portion_saved = float(input("please enter the portion of salary to be saved "))
total_cost = float(input("please input the cost of your dream house "))
semi_annual_raise = float(input("please enter your semi annual salary raise percent(decimal) "))
portion_down_payment = 0.25 * total_cost
current_saving = 0

monthly_salary = annual_salary / 12

# this is for each month
month_to_buy = 0

while current_saving < portion_down_payment:
  # current saving += raise due to investment + raise due to save from monthly salary
   current_saving = current_saving + current_saving * (0.04 / 12) + monthly_salary * portion_saved
   month_to_buy += 1
   if month_to_buy % 6 == 0:
     monthly_salary += monthly_salary * semi_annual_raise

print(month_to_buy)
