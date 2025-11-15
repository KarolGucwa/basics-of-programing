total_sum = 0
count = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
    count += 1
mean = total_sum / count if count > 0 else 0
print(f"Total sum: {total_sum}, Arithmetic mean: {mean}")
