# recursive approach, takes time
def solver1(row, col):
    def helper(i=0, j=0):
        if i == row or j == col:
            return 0
        elif i == row - 1 and j == col - 1:
            return 1
        else:
            return helper(i + 1, j) + helper(i, j + 1)

    return helper()


# dp approach
"""
As only right and down movement allowed, so for every element for first row only
way possible to reach any of its element is one, which is by moving only left
Similarly for first element of each row is only way possible to reach any of its
element is one, which is by moving only left
"""
def solver(row, col):
    # generate dp array first, containing ways to reach at every position in it
    dp = [[None for _ in range(col)] for _ in range(row)]

    # make each element of first row except first element = 1
    for i in range(1, col):
        dp[0][i] = 1

    # make each element of every row except first row = 1
    for i in range(1, row):
        dp[i][0] = 1

    """
    *   x
    y   z=x+y
    """
    for i in range(1, row):
        for j in range(1, col):
            # current = ways to reach top position + ways to reach left position
            # Since output can be very large number use %10^9+7
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10 ** 9 + 7)

    return dp[row - 1][col - 1]


T = int(input())
for _ in range(T):
    row, col = map(int, input().split())
    print(solver(row, col))
