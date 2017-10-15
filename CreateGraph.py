# Input: N, which means tha quantity of nodes in the graph
# Output: A list with the nodes used to

from random import *
inf = 99999999

def creategraph(n):
    if n <= 0:
        return "Ingrese un valor psitivo"
    nodes = [x for x in range(n)]
    distances = {}
    temp = {}
    for node in nodes:
        for i in range(len(nodes)):
            if nodes[i] != node:
                num = randint(1, 101)
                num //= 2
                if num >= 46:
                    print(num)
                    num = inf
                temp[nodes[i]] = num
        distances[node] = temp
        temp = {}
    return nodes, distances


# Input: A graph (done with dictionaries)
# Output: A matrix based on the dictionary

def graphtomatrix(graph):
    matrix = [[graph[x] for x in range(len(graph))] for x in range(len(graph))]
    for x in graph:
        matrix[x][x] = 0
        for y in graph[x]:
            matrix[x][y] = graph[x][y]
    print(matrix)
    return matrix

print(creategraph(3))
