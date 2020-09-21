def solver(V, E, m, edges):
    colors = [None for _ in range(V)]

    # checking if connected edges doesn't contain same color 
    def isSafe(ver, color):
        for edge in edges[ver]:
            if colors[edge] == color:
                return False
        return True

    # you might be thinking, why I'm taking (ver+1) instead of taking adjacent
    # nodes and doing dfs, but it is more efficient and helps in traversing all 
    # nodes even if it is disconnected, otherwise we would have to run dfs from
    # all nodes     
    def helper(ver):
        if ver == V:
            return True
        for i in range(m):
            if isSafe(ver, i):
                colors[ver] = i
                works = helper(ver + 1)
                if works:
                    return True
                colors[ver] = None
        return False

    return 1 if helper(0) else 0


for _ in range(int(input())):
    V = int(input())
    m = int(input())
    E = int(input())
    lis = list(map(int, input().split()))
    edges = [[] for _ in range(V)] # adjacency matrix
    for i in range(E):
        # vertex are given 1-based index, I made them 0-based
        v1 = lis[2*i]
        v2 = lis[2*i + 1]
        edges[v1-1].append(v2-1)
        edges[v2-1].append(v1-1)
    # Print 1 if it is possible to colour vertices and 0 otherwise.
    print(solver(V, E, m, edges))

