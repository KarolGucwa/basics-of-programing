def transpose_matrix(m):
    return [list(row) for row in zip(*m)]

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [5, 6, 7, 8]]
]

for matrix in matrices:
    transposed = transpose_matrix(matrix)
    for row in transposed:
        print(row)
    print()