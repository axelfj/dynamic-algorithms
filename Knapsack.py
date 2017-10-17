from random import *
x = int(randrange(0,99999))

# This algorithm search the best value for the backpack #
# Input: cantProducts & Weight.
#   Basically the products are the quantity and the weight is how much the backpack support. #
# Output: Best Value, Selection of products.
#   The backpack algorithm returns the best value found and the selection of products who are the most valuable.
# Every value we set here is randomly picked.

def knapsack(cantProducts, weight):

    # CreateArrayProducts #
    def arrayProducts(cantProducts):
        products = [x for x in range(1,cantProducts+1,1)]
        return products

    # SetValues Algorithm #
    def setValues(products):
        values = []
        for i in range(len(products)):
            x = randint(i, products[len(products)-1]*2)
            while x in values:
                x*=2
            values.append(x)
        return values

    # Select Products #
    def selectProducts(products, matrix):
        i = len(matrix)-1
        j = len(matrix[0])-1
        selection = []
        while i >= 0 and j >= 0:
            if matrix[i][j] == matrix[i - 1][j]:
                i-=1
            else:
                selection += [products[i-1]]
                j -= products[i-1]
        return selection

    products = arrayProducts(cantProducts)
    values = setValues(products)
    matrix = [[0 for _ in range(weight+1)] for _ in range(len(values)+1)]

    for i in range(len(values) + 1):
        for j in range(weight + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif products[i-1] <= j:
                matrix[i][j] = max(values[i-1] + matrix[i-1][j - products[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]

    return matrix[len(values)][weight], values, selectProducts(products,matrix)