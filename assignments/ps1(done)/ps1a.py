total_cost = float(input("please input the cost of your dream house "))
portion_down_payment = 0.25 * total_cost
current_saving = 0
annual_salary = float(input("please input your annual salary "))
monthly_salary = annual_salary / 12

# this is for each month
portion_saved = float(input("please enter the portion of salary to be saved "))
month_to_buy = 0
monthly_saved = monthly_salary * portion_saved

while current_saving < portion_down_payment:
   current_saving = current_saving + current_saving * (0.04 / 12) + monthly_saved
   month_to_buy += 1

print(month_to_buy)
