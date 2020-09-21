def dfs(at, i, vis, graph, topoOrdering):
    vis[at] = True
    for edge in graph[at]:
        if not vis[edge]:
            i = dfs(edge, i, vis, graph, topoOrdering)

    topoOrdering[i] = at
    return i - 1


# (no. of vertices, adjacency matrix)
def topoSort(V, graph):
    vis = [False for _ in range(V)]
    topoOrdering = [0 for _ in range(V)]
    i = V - 1

    for at in range(V):
        if not vis[at]:
            i = dfs(at, i, vis, graph, topoOrdering)

    # print(topoOrdering)
    return topoOrdering





# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
#        Copied prewritten runner code(reads input and do output)
# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
import sys

sys.setrecursionlimit(10 ** 6)


def creategraph(e, n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


def check(graph, N, res):
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


from collections import defaultdict

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)

        if check(graph, N, res):
            print(1)
        else:
            print(0)
