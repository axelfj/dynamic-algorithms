# This algorithm search the minimum path from one node to another #
# Input: nodes & init & distances.
#   Nodes is basically the graph, init is the node you are using as the initial point and the distances are all the
#   values between nodes. #
# Output: visited, distances
#   visited is the nodes you visited with the value, and the distance is to see every route between nodes. #

def dijkstra(nodes, init, distances):
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = init
    currentDistance = 0
    unvisited[current] = currentDistance
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return "The nodes you visited are:\t", visited,\
           "\nThe distance between the nodes are:", distances