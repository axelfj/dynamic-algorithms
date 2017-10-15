import CreateGraph as CG


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
    return visited


node, distance = CG.creategraph(3)

print(dijkstra(node, 1, distance))
