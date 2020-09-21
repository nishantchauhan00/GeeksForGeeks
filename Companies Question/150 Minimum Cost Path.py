"""
This problem is also similar to rat in maze


Given a square grid of size N, each cell of which contains integer cost which
represents a cost to traverse through that cell, we need to find a path from 
top left cell to bottom right cell by which total cost incurred is minimum. 
You can move in 4 directions : up, down, left an right.

Note : It is assumed that negative cost cycles do not exist in input matrix.
"""
import sys


def findPath(arr, n):
    min_distance = sys.maxsize
    paths = []

    # U-UP   D-Down   L-Left   R-Right
    def helper(i, j, curr_cost, curr_path):
        nonlocal min_distance
        if (
            i < 0
            or j < 0
            or i >= n
            or j >= n
            or arr[i][j] == -1
            or curr_cost > min_distance
        ):
            return

        if i == n - 1 and j == n - 1:
            curr_cost += arr[i][j]
            paths.append([curr_path, curr_cost])
            if min_distance >= curr_cost:
                min_distance = curr_cost
            return

        temp = arr[i][j]
        arr[i][j] = -1
        helper(i, j - 1, curr_cost + temp, curr_path + "L")  # left
        helper(i - 1, j, curr_cost + temp, curr_path + "U")  # up
        helper(i + 1, j, curr_cost + temp, curr_path + "D")  # down
        helper(i, j + 1, curr_cost + temp, curr_path + "R")  # right
        arr[i][j] = temp

    helper(0, 0, 0, "")
    print(paths)
    return min_distance




for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    arr = []
    for i in range(0, n * n, n):
        arr.append(lis[i : i + n])

    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end="  ")
    #     print()

    print(findPath(arr, n))
