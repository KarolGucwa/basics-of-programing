def f(number, even):
    digits = [int(digit) for digit in str(number)]
    if even:
        return sum(digit for digit in digits if digit % 2 == 0)
    else:
        return sum(digit for digit in digits if digit % 2 != 0)
