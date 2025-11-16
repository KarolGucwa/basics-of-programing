def f(number):
    digits = str(number)
    return sum(int(digit) for digit in set(digits) if digits.count(digit) > 1)
