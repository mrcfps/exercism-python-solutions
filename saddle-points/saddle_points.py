def check_matrix_validity(matrix):
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("invalid matrix")


def saddle_points(matrix):
    check_matrix_validity(matrix)
    matrix_T = list(zip(*matrix))
    saddles = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            elem = matrix[row][col]
            if max(matrix[row]) == elem and min(matrix_T[col]) == elem:
                saddles.add((row, col))
    return saddles
