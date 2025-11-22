# MyArrays.py

def second_largest(arr):
    largest = None
    second = None
    for num in arr:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or num > second:
            second = num
    return second

def range_of_values(arr):
    return max(arr) - min(arr)

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2

def min_max(arr):
    return [min(arr), max(arr)]

def to_string(arr):
    return "-".join(map(str, arr))
