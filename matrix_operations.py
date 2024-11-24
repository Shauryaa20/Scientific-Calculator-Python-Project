def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    size = len(matrix1)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(size))
    return result
