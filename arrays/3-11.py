def bubblesort(array):
    n = len(array)
    for i in range(n):
        swapped = False  
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

array1 = [64, 25, 12, 22, 11]
array2 = [5, 1, 9, 2, 8, 6]
array3 = [10, 20, 5, 12, 8, 3, 1]

sorted_array1 = bubblesort(array1)
sorted_array2 = bubblesort(array2)
sorted_array3 = bubblesort(array3)

print(f"Original array 1: [64, 25, 12, 22, 11] -> Sorted array 1: {sorted_array1}")
print(f"Original array 2: [5, 1, 9, 2, 8, 6] -> Sorted array 2: {sorted_array2}")
print(f"Original array 3: [10, 20, 5, 12, 8, 3, 1] -> Sorted array 3: {sorted_array3}")
