array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

unique_elements = [item for item in array1 if item not in array2]

print(f"Numbers from the first array that do not appear in the second array: {unique_elements}")
