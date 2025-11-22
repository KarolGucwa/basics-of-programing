arr = [15, 8, 31, 47, 2, 19]

sum_arr = 0
count = len(arr)

for num in arr:
    sum_arr += num

average = sum_arr / count

print("Array:", *arr)
print("Average:", average)
