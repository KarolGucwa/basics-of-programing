def is_subset(array1, array2):
    return all(elem in array2 for elem in array1)

array1 = [1, 2, 3]
array2 = [3, 2, 1, 4, 5]

if is_subset(array1, array2):
    print("Pierwsza tablica jest podzbiorem drugiej.")
else:
    print("Pierwsza tablica nie jest podzbiorem drugiej.")
