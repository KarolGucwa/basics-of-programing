car_number = input('Enter car registration number: ')
is_krakow = car_number[0:2] in ("KR", "KK")
print(f'Car is from Krakow: {is_krakow}')