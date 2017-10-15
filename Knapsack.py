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
        print(matrix)
        i = len(matrix) - 1
        j = len(matrix[0]) - 1
        selection = []
        while matrix[i][j] != 0:
            if matrix[i][j] == matrix[i - 1][j]:
                if (products[i] + sum(selection)) <= weight:
                    selection += [products[i]]
                i -= 1
            j -= 1
        return selection

    products = arrayProducts(cantProducts)
    values = setValues(products)
    matrix = [[0]*(weight+1)]*(len(products))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j >= products[i]:
                matrix[i][j] = max(matrix[i-1][j], values[i] + matrix[i-1][j-products[i]])
                print("the fuck is this\t",matrix[i-1][j], "--\t",matrix[i-1][j-products[i]])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(matrix)-1][len(matrix[0])-1], values, selectProducts(products,matrix)



print(knapsack(5,7))