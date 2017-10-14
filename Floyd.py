def floyd(matrix):
    for m in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] >= 0 and matrix[i][m] >= 0 and matrix[m][j] >= 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i][m]+matrix[m][j])
                elif matrix[i][j] == -1:
                    if matrix[i][m] >= 0 and matrix[m][j] >= 0:
                        matrix[i][j] = matrix[i][m] + matrix[m][j]
    return matrix

inf = 9999
elements = [[0, 6, inf, 4, 7],
            [9, 0, 7, inf, inf],
            [inf, 5, 0, inf, 14],
            [8, 1, inf, 0, 15],
            [2, inf, 2, 19, 0]]

#print(floyd(elements))