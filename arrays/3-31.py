def find_min_max(matrix):
    min_value = float('inf')
    max_value = float('-inf')
    min_pos = None
    max_pos = None

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_pos = (i, j)
            if value > max_value:
                max_value = value
                max_pos = (i, j)

    return min_value, min_pos, max_value, max_pos

def print_result(min_value, min_pos, max_value, max_pos):
    print(f"Najmniejsza wartość: {min_value} na pozycji (wiersz: {min_pos[0]}, kolumna: {min_pos[1]})")
    print(f"Największa wartość: {max_value} na pozycji (wiersz: {max_pos[0]}, kolumna: {max_pos[1]})")

matrix = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value, min_pos, max_value, max_pos = find_min_max(matrix)
print_result(min_value, min_pos, max_value, max_pos)