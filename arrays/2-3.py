# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

total_food = 0
total_transport = 0
total_utilities = 0
total_weekly_expenses = [0, 0, 0, 0]  

for week in range(4):
    total_food += monthly_expenses[week][0]
    total_transport += monthly_expenses[week][1]
    total_utilities += monthly_expenses[week][2]
    total_weekly_expenses[week] = sum(monthly_expenses[week]) 

total_expenses = total_food + total_transport + total_utilities

# Drukowanie wyników
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', total_weekly_expenses[0])
print('Week 2:', total_weekly_expenses[1])
print('Week 3:', total_weekly_expenses[2])
print('Week 4:', total_weekly_expenses[3])
print('---------------')
print('TOTAL:', total_expenses)
