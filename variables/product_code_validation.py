def f(product_code):
    digits = [int(digit) for digit in product_code]
    return sum(digits[:3]) % 7 == digits[3]