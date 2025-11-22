arr = [15, 8, 31, 47, 2, 19]

print("Existed array:", *arr)

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
