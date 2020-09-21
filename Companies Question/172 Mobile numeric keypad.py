"""
1  2  3
4  5  6
7  8  9
*  0  #

Given the mobile numeric keypad. You can only press buttons that are up, 
left, right or down to the current button and also the current button. You 
are not allowed to press bottom row corner buttons (i.e. * and # ). 
"""

# brute force - recursion
# check every possible way
def solver(n):
    dp = [[[-1 for _ in range(3)] for _ in range(4)] for _ in range(n)]

    def helper(i, j, pressed=1):
        #  ( if (i, j) goes out of bound    ) or (for * and # key)
        if i < 0 or j < 0 or i >= 4 or j >= 3 or (i == 3 and j != 1):
            return 0

        if pressed == n:
            return 1

        if dp[pressed][i][j] != -1:
            return dp[pressed][i][j]

        # current, top, right, bottom, left
        res = 0
        res += helper(i, j, pressed + 1)
        res += helper(i - 1, j, pressed + 1)
        res += helper(i, j + 1, pressed + 1)
        res += helper(i + 1, j, pressed + 1)
        res += helper(i, j - 1, pressed + 1)

        dp[pressed][i][j] = res
        return res

    ways = 0
    for i in range(4):
        for j in range(3):
            ways += helper(i, j)

    return ways





for _ in range(int(input())):
    n = int(input())
    print(solver(n))
