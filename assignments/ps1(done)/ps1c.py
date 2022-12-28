# remember this is a search problem, and we can use finite search
annual_salary = float(input("please input your annual salary "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_saving = 0
monthly_salary = annual_salary / 12
month_to_buy = 36

# portion saved is unknown

low = 0
high = 10000
portion_saved = (low + high) // 2

num_guesses = 0

#print(portion_down_payment, 'portion')
for i in range(1, month_to_buy + 1):
    current_saving = current_saving + current_saving * (0.04 / 12) + monthly_salary * 1
    if i % 6 == 0:
       monthly_salary += monthly_salary * semi_annual_raise

if current_saving < portion_down_payment:
    print('It is not possible to pay the down payment in three years')
    exit()

while abs(current_saving - portion_down_payment) > 100:
  current_saving = 0
  monthly_salary = annual_salary / 12
  for i in range(1, month_to_buy + 1):
    current_saving = current_saving + current_saving * (0.04 / 12) + monthly_salary * (portion_saved / 10000)
    if i % 6 == 0:
       monthly_salary += monthly_salary * semi_annual_raise
  if current_saving - portion_down_payment > 100:
    high = portion_saved
  else:
    low = portion_saved
    #print(low, 'low')
  portion_saved = (low + high) // 2
  print(portion_saved, 'portion')
  
  num_guesses += 1
print(current_saving, 'current saving')
print(portion_saved / 10000)
print(num_guesses)
  
    
  
  


