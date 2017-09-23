from random import *

x = int(randrange(0,99999))

products = [1,2,3,4,5]
values = [1,6,18,22,28]
weight = 11
matrix = []

def backpack(products, weight):
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
    backpack(products,weight)
    i = len(matrix)-1
    j = len(matrix[0])-1
    selection = []
    while matrix[i][j] != 0:
        if (products[i]+sum(selection)) <= weight:
            selection += [products[i]]
        
            i-=1
        j-=1
    return selection

print(backpack(products,weight))
#print(selectProducts(products,weight))