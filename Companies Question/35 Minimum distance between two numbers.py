import math

"""
i/p:
2
4
1 2 3 2
1 2
7
86 39 90 67 84 66 62
42 12

o/p:
1
-1
"""


def minDist1(arr, n, x, y):
    if x == y:
        return 0 if x in arr else -1
        
    x_i = []
    y_i = []
    for i in range(n):
        if arr[i] == x:
            x_i.append(i)
        elif arr[i] == y:
            y_i.append(i)

    out = n + 1
    for i in x_i:
        for j in y_i:
            out = min(out, abs(i - j))

    return -1 if out == n + 1 else out


def minDist(arr, n, x, y):
    if x == y:
        return 0 if x in arr else -1
        
    x_i = -1
    y_i = -1
    out = n + 1
    for i in range(n):
        if arr[i] == x:
            x_i = i
            if not(y_i == -1):
                out = min(out, abs(x_i - y_i))
        elif arr[i] == y:
            y_i = i
            if not(x_i == -1):
                out = min(out, abs(x_i - y_i))

    return -1 if out == n + 1 else out



T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    x, y = list(map(int, input().split()))
    print(minDist(arr, n, x, y))
