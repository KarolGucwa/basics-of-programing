arr = [15, 8, 31, 47, 2, 19]

sum_arr = 0
count = len(arr)
i = 0

while i < count:
    sum_arr += arr[i]
    i += 1

average = sum_arr / count

print("Array:", *arr)
print("Average:", average)
