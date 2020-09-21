def isCyclic(V, graph):
    vis = [False for _ in range(V)]
    curr_traverse = [False for _ in range(V)]

    def dfs(at):
        if curr_traverse[at] == True:
            return True

        vis[at] = True
        curr_traverse[at] = True
        for edge in graph[at]:
            if vis[edge]:
                cyclePresent = dfs(edge)
                if cyclePresent:
                    return True
        
        curr_traverse[at] = False
        
        return False

    for at in range(V):
        if not vis[at]:
            cyclePresent = dfs(at)
            if cyclePresent:
                return 1
    
    return 0





# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////
from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)