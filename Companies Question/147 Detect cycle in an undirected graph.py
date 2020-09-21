# https://www.youtube.com/watch?v=tJkpxwg90KY&ab_channel=CodingBlocks
def isCyclic(graph, V):
    vis = [False for _ in range(V)]
    def dfs(at, parent):
        vis[at] = True
        for to in graph[at]:
            if not vis[to]:
                cyclePresent = dfs(to, at)
                if cyclePresent:
                    return True
            elif to != parent: 
                # if the already visited node is not parent then its a loop
                return True

        return False

    for at in range(V):
        if not vis[at]:
            cyclePresent = dfs(at, -1)
            if cyclePresent:
                return 1
    
    return 0










# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
#        prewritten geeks code
# //////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
import atexit
import io
import sys
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))

        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i + 1]
            g.addEdge(u, v)  # add an undirected edge from u to v
            g.addEdge(v, u)
        print(isCyclic(g.graph, N))
