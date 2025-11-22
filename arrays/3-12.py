def unique_elements(arr):
    unique = [item for item in set(arr) if arr.count(item) == 1]
    return unique

arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique = unique_elements(arr)
print(f"Array: {' '.join(map(str, arr))}")
print(f"Unique elements: {' '.join(map(str, unique))}")
