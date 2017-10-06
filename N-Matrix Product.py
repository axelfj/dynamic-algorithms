# This will be the programmed part of the matrix problem
# Algorithm to calculate in which order you should multiply matrices
# Input: Vector with 2 dimensions of the matrices to multiply
# Output: Quantity of multiplications you have to

from copy import deepcopy

Values = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]


def matrixproduct(values):
    def matrixproductaux(array, i, j):
        if i == j:
            return 0
        min = 100000
        if i > j:
            return "x"
        for k in range(i, j):
            temp = matrixproductaux(array, i, k) + matrixproductaux(array, k+1, j)+ array[i-1] * array[k] * array[j]

            if temp < min:
                min = temp
        return min


    cantmatrix = len(values)
    matrix = [[0 for j in range(cantmatrix)] for i in range(cantmatrix)]
    routes = deepcopy(matrix)
    p = [values[0][0]]
    for i in range(cantmatrix):
        p.append(values[i][1])
    for i in range(cantmatrix):
        for j in range(cantmatrix):
            matrix[i][j] = matrixproductaux(p, i, j)

    return matrix[0][cantmatrix-1]


print(matrixproduct(Values))
