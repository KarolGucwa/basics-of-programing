def swap_rows(matrix):
    matrix[0], matrix[-1] = matrix[-1], matrix[0]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Przed zamianą:")
print_matrix(matrix)

swap_rows(matrix)

print("\nPo zamianie:")
print_matrix(matrix)