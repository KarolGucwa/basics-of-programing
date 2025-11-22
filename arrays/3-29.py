def create_2d_arr(x, y):
    return [[0] * y for _ in range(x)]

matrix = create_2d_arr(3, 5)

for row in matrix:
    print(' '.join(map(str, row)))