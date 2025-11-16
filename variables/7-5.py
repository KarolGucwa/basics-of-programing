from range_checker import is_in_range

num = 7
x, y = 2, 15
result = is_in_range(num, x, y)
print(f"Number {num} in the range <{x},{y}>: {'yes' if result else 'no'}")
