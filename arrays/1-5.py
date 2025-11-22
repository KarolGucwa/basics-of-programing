arr = [2, 3, 7, 5, 4]
print(f'Arr przed zmianą: {arr}')

print('Odejmowanie od pierwsego elemntu :', arr[0] - 1)
print('zwiększ ostatni element tablicy o 4 :', arr[len(arr)-1] + 4)
print('pomnóż środkowy element tablicy przez 2:', arr[2] * 2)
new_arr = [arr[0] - 1, 3, arr[len(arr)-1] + 4, 5, arr[2] * 2]

print(f'Arr po zmianie: {new_arr}')
