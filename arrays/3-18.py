import MyArrays

numbers = [7, 3, 8, 5, 2]

print(f"Numbers: {MyArrays.to_string(numbers)}")
print(f"Second largest number: {MyArrays.second_largest(numbers)}")
print(f"Median: {MyArrays.median(numbers)}")
print(f"Smallest and largest number: {', '.join(map(str, MyArrays.min_max(numbers)))}")
print(f"Numbers as a string: {MyArrays.to_string(numbers)}")
