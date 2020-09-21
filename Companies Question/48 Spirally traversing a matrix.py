# code
import math


class Solution:
    def spiralMatrix(self, arr, row, col):
        out = []

        def printloop():
            left, right = 0, col - 1
            up, down = 0, row - 1

            while left <= right and up <= down:
                # left to right
                for i in range(left, right + 1):
                    # print(arr[up][i], up, i, end="  h1\n")
                    out.append(arr[up][i])
                up += 1

                # up to down
                for i in range(up, down + 1):
                    # print(arr[i][right], i, right, end="  h2\n")
                    out.append(arr[i][right])
                right -= 1

                if up <= down:  # as above we increased up
                    # right to left
                    for i in range(right, left - 1, -1):
                        # print(arr[down][i], down, i, end="  h3\n")
                        out.append(arr[down][i])
                    down -= 1

                if left <= right:  # as above we decreased right
                    # down to up
                    for i in range(down, up - 1, -1):
                        # print(arr[i][left], i, left, end="  h4\n")
                        out.append(arr[i][left])
                    left += 1

        printloop()

        return out


# the form of array it expects
# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

s = Solution()

T = int(input())

for _ in range(T):
    row, col = map(int, input().split())
    arr = [[None for _ in range(col)] for _ in range(row)]
    temparr = list(map(int, input().split()))
    for i in range(row):
        for j in range(col):
            arr[i][j] = temparr[i * col + j]

    print(" ".join(str(el) for el in s.spiralMatrix(arr, row, col)))
