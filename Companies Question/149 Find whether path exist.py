"""
A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.

we can go through blank cell, blank wall stops
# its similar to rat in maze problem

i think it would be more faster if implemented using queue, but space complexity
is definitely gonna increase
"""


def findPath(arr, n):
    # U-UP   D-Down   L-Left   R-Right
    def helper(i, j,  search_for):
        if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == 0:
            return False

        if arr[i][j] == search_for:
            return True

        # next previous position is current direction according to next position,
        # which is opposite direction of next position
        found = False
        arr[i][j] = 0
        if not found:  # up
            found = helper(i - 1, j, search_for)
        if not found:  # down
            found = helper(i + 1, j, search_for)
        if not found:  # right
            found = helper(i, j + 1, search_for)
        if not found:  # left
            found = helper(i, j - 1, search_for)
        arr[i][j] = 3

        return found

    search_for = -1
    res = False
    # find either source or destination
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2 or arr[i][j] == 1:
                search_for = 1 if (arr[i][j] == 2) else 2
                arr[i][j] = 3
                res = helper(i, j, search_for)
                return 1 if res else 0
                
    return 0


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
