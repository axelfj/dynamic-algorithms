# Input: N, which means tha quantity of nodes in the graph
# Output: A list with the nodes used to

from random import *


def creategraph(n):
    if n <= 0:
        return "Ingrese un valor psitivo"
    nodes = [x for x in range(n)]
    distances = {}
    temp = {}
    for node in nodes:
        for i in range(len(nodes)):
            if nodes[i] != node:
                temp[nodes[i]] = randint(0, 50)
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


node, distance = creategraph(3)
print(distance)
graphtomatrix(distance)

