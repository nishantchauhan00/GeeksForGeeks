"""
its like spreading a disease, you have to spread it in all direction, if its 
start, i.e., a[i][j] is 1, then disease in that region is new and have to spread
it from there.
0 are immune to disease, 1 is transmitter.

"""

import sys

sys.setrecursionlimit(100000)


def findIslands(arr, n, m):
    out = 0

    def spreadCoronavirus(n, m, i, j):
        if i < 0 or i > n - 1 or j < 0 or j > m - 1 or arr[i][j] == 0:
            return
        arr[i][j] = 0
        # now we will spread it in all 8 directions
        # clockwise start from northwest
        spreadCoronavirus(n, m, i - 1, j - 1)
        spreadCoronavirus(n, m, i - 1, j)
        spreadCoronavirus(n, m, i - 1, j + 1)
        spreadCoronavirus(n, m, i, j + 1)
        spreadCoronavirus(n, m, i + 1, j + 1)
        spreadCoronavirus(n, m, i + 1, j)
        spreadCoronavirus(n, m, i + 1, j - 1)
        spreadCoronavirus(n, m, i, j - 1)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                out += 1
                spreadCoronavirus(n, m, i, j)
    return out


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = [[None for _ in range(m)] for _ in range(n)]
    temparr = input().split()
    for i in range(n):
        for j in range(m):
            arr[i][j] = int(temparr[i * m + j])
    print(findIslands(arr, n, m))
