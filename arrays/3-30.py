matrix = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        matrix[i][j] = (i+1) * (j+1)

for row in matrix:
    print(' '.join(map(str, row)))
