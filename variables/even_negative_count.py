def f(x, y):
    return sum(1 for i in range(x, y+1) if i < 0 and i % 2 == 0)
