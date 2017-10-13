# This will be the programmed part of the matrix problem
# Algorithm to calculate in which order you should multiply matrices
# Input: Vector with 2 dimensions of the matrices to multiply
# Output: Quantity of multiplications you have to

from copy import deepcopy

# Values = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
Values = [[2, 3], [3, 6], [6, 4], [4, 5]]

def matrixproduct(values):
    def matrixproductaux(array, i, j, route):
        if i == j:
            return 0
        last = 100000
        tempo = 0
        if i > j:
            return "x"
        for k in range(j - 1, i - 1, -1):
            temp = matrixproductaux(array, i, k, route) + matrixproductaux(array, k + 1, j, route) + \
                   array[i] * array[k + 1] * array[j + 1]

            if temp < last:
                last = temp
                route[i][j] = k+1
        return last

    cantmatrix = len(values)
    matrix = [[0 for j in range(cantmatrix)] for i in range(cantmatrix)]
    routes = deepcopy(matrix)
    p = [values[0][0]]

    for i in range(cantmatrix):
        p.append(values[i][1])
    for i in range(cantmatrix):
        for j in range(cantmatrix):
            a = matrixproductaux(p, i, j, routes)
            matrix[i][j] = a
    return routes


def rutas(routes):

    def rutasaux(i, j):
        if routes[i][j] == 0 or (routes[i][j] == j and j - i == 1):
            if i == j:
                print(i)

            else:

                print(str(i) + "*" + str(j))

        else:
            #print(str(i) + '*' + str(j))
            value = routes[i][j]
            rutasaux(i, value - 1)
            rutasaux(value, j)

    cant = len(routes)
    rutasaux(0, cant - 1)


rutas(matrixproduct(Values))
