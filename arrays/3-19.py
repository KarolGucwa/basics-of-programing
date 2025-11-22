arr = [1.5, 3.2, 7.8, 2.1, 5.5, 0.9, 8.0]

value = float(input("Podaj wartość, do której chcesz porównać elementy tablicy: "))

count = sum(1 for x in arr if x > value)

print(f"Liczba elementów większych od {value}: {count}")
