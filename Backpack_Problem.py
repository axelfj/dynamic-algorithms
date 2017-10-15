from random import *
x = int(randrange(0,99999))

# This algorithm search the best value for the backpack #
# Input: Products & Weight.
#   Basically the products are the quantity and the weight is how much the backpack support. #
# Output: Best Value, Selection of products.
#   The backpack algorithm returns the best value found and the selection of products who are the most valuable.

products = [1,2,3,4,5]
values = [1,6,18,22,28]
weight = 11
matrix = []

def backpack(products, values, weight):
    if not len(values) == len(products):
        return False
    for i in range(len(products)):
        row = [x * 0 for x in range(weight + 1)]
        matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j >= products[i]:
                matrix[i][j] = max(matrix[i-1][j], values[i] + matrix[i-1][j-products[i]])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(matrix)-1][len(matrix[0])-1]

def selectProducts(products, weight):
    if backpack(products,weight) == False:
        return 'Cant choose the products'
    else:
        i = len(matrix)-1
        j = len(matrix[0])-1
        selection = []
        while matrix[i][j] != 0:
            if matrix[i][j] == matrix[i-1][j]:
                if (products[i]+sum(selection)) <= weight:
                    selection += [products[i]]
                i-=1
            j-=1
        return selection

#print(backpack(products,weight))
#print(selectProducts(products,weight))