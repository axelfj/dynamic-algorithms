nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16},
    'G': {'B': 2, 'D': 1, 'C': 2}}

def dijkstra(nodes, init):
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

print(dijkstra(nodes,'A'))