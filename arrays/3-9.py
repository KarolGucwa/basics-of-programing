def compare(array1, array2):
    return array1 == array2

def print_comparison(array1, array2):
    result = compare(array1, array2)
    print(f"Array1: {' '.join(map(str, array1))}")
    print(f"Array2: {' '.join(map(str, array2))}")
    print(f"Comparison: {'arrays are the same' if result else 'arrays are different'}")

array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]

array1_2 = [True, False]
array2_2 = [True, False, True]

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]

array1_4 = [3, 2, 1]
array2_4 = [3, 2]

print_comparison(array1_1, array2_1)
print_comparison(array1_2, array2_2)
print_comparison(array1_3, array2_3)
print_comparison(array1_4, array2_4)
