graph = [ # adjacency list
    [1, 2],
    [0],
    [0, 3],
    [2,4,8],
    [3,5],
    [4,8],
    [5,7],
    [6,8],
    [3,7],
]

n = len(graph)
visited = [False]*n

def dfs(at):
    print(at, end="  ")
    visited[at] = True
    neighbours = graph[at]

    for neighbour in neighbours:
        if not visited[neighbour]:
            dfs(neighbour)


src = 0
dfs(src)

