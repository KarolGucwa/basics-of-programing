from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

# filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# reduce to calculate the sum
sum_even = reduce(lambda x, y: x + y, even_numbers)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", sum_even)
