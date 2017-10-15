# This algorithm search the minimum path between every node in a graph #
# Input: graph.
#   graph contains every value between nodes
# Output: graph
#   The same graph, but with the best routes. #

def floyd(graph):
    for m in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] >= 0 and graph[i][m] >= 0 and graph[m][j] >= 0:
                    graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
                elif graph[i][j] == -1:
                    if graph[i][m] >= 0 and graph[m][j] >= 0:
                        graph[i][j] = graph[i][m] + graph[m][j]
    return graph

inf = 9999
elements = [[0, 6, inf, 4, 7],
            [9, 0, 7, inf, inf],
            [inf, 5, 0, inf, 14],
            [8, 1, inf, 0, 15],
            [2, inf, 2, 19, 0]]

#print(floyd(elements))