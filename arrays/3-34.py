def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrices_sizes = [3, 5, 8]

for size in matrices_sizes:
    matrix = identity_matrix(size)
    print_matrix(matrix)
    print()