# This will be the programmed part of the matrix problem
# Algorithm to calculate in which order you should multiply matrices
# Input: Vector with 2 dimensions of the matrices to multiply
# Output: Quantity of multiplications you have to

from copy import deepcopy

Values = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]


def matrixproduct(values):

    def multiplicands(matrices):
        for i in range(len(matrices)-1):
            if matrices[i][1] != matrices[i+1][0]:
                return False
        return True

    def rutas(route):

        def rutas_aux(i, j):
            if route[i][j] == 0 or (route[i][j] == j and j - i == 1):
                if i == j:
                    lista.append(str(i))
                else:
                    lista.append(str(i) + "*" + str(j))
            else:
                value = route[i][j]
                rutas_aux(i, value - 1)
                rutas_aux(value, j)

        lista = []
        cant = len(route)
        rutas_aux(0, cant - 1)
        return lista

    def matrixproductaux(array, i, j, route):
        if i == j:
            return 0
        last = 100000
        if i > j:
            return "x"
        for k in range(j - 1, i - 1, -1):
            temp = matrixproductaux(array, i, k, route) + matrixproductaux(array, k + 1, j, route) + \
                   array[i] * array[k + 1] * array[j + 1]
            if temp < last:
                last = temp
                route[i][j] = k+1
        return last

    if not multiplicands(values):
        return "Not multiplicands"

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

    associativity = rutas(routes)

    return matrix[0][cantmatrix-1], associativity