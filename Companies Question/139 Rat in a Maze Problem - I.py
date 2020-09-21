def findPath(arr, n):
    out = []
    def helper(curr, i, j):
        if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == 0:
            return
        if i == n - 1 and j == n - 1:
            out.append(curr)
            return

        # mark it visited, so that you can't come back here
        arr[i][j] = 0

        helper(curr + "D", i + 1, j)
        helper(curr + "L", i, j - 1)
        helper(curr + "R", i, j + 1)
        helper(curr + "U", i - 1, j)

        # mark it unvisited, backtrack
        arr[i][j] = 1

    helper("", 0, 0)
    return "-1" if len(out) == 0 else " ".join(out)



for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    arr = []
    for i in range(0, n * n, n):
        arr.append(lis[i : i + n])

    print(findPath(arr, n))


"""
1
4
1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1
"""

