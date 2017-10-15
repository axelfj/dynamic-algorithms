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


print(creategraph(3))
