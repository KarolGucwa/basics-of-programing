def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

result = power(5, 3)
print(result)
