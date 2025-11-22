def convert_to_1d(arr_2d):
    return [element for row in arr_2d for element in row]

arrays_2d = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5]],
    [[7, 4], [2, 6]]
]

for arr in arrays_2d:
    print(convert_to_1d(arr))