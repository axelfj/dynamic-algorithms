# This will be the programmed part of the matrix problem
# Algorithm to calculate in which order you should multiply matrices
# Input: Vector with 2 dimensions of the matrices to multiply
# Output: Quantity of multiplications you have to

from copy import deepcopy

Values = [[5, 4], [4, 6], [6, 3], [3, 2]]


def matrixproduct(values):
    def matrixproductaux(array, i, j, route):
        if i == j:
            return 0
        last = 100000
        tempo = 0
        if i > j:
            return "x"
        for k in range(j-1, i-1, -1):
            temp = matrixproductaux(array, i, k, route) + matrixproductaux(array, k+1, j, route) + array[i-1] * array[k] * array[j]

            if temp < last:
                last = temp
                print(k)
                route[i][j] = k
        return last

    cantmatrix = len(values)
    matrix = [[0 for j in range(cantmatrix)] for i in range(cantmatrix)]
    routes = deepcopy(matrix)

    print(matrix, routes)
    p = [values[0][0]]
    for i in range(cantmatrix):
        p.append(values[i][1])
    for i in range(cantmatrix):
        for j in range(cantmatrix):
            a= matrixproductaux(p, i, j, routes)
            matrix[i][j] = a
    return matrix, routes


print(matrixproduct(Values))
