arr = [2, 3, 7, 5, 4]

print(arr)

print('Number of elements:', len(arr))
print('First value:', arr[0])
print('Second value:', arr[1])
print('Last value:', arr[len(arr)-1])
print('Second to last value:', arr[len(arr)-2])
print('Sum of first and last values:', arr[0] + arr[len(arr)-1])

average = sum(arr) / len(arr)
print('Average value:', average)

print('All values:', end=' ')
for value in arr:
    print(value, end=' ')
print()  
