distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))


total_fuel_consumption = (distance / 100) * fuel_consumption
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption: {total_fuel_consumption}')
print(f'Total cost: {total_cost}')