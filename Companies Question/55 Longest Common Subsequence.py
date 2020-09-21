def solver1(str1, str2, m, n):  # recursion
    def lcs(i, j):
        if i == -1 or j == -1:
            return 0
        elif str1[i] == str2[j]:
            return 1 + lcs(i - 1, j - 1)
        else:
            return max(lcs(i, j - 1), lcs(i - 1, j))

    return lcs(m - 1, n - 1)


# as there are cases of same recursion step multiple times we use dp
def solver(str1, str2, m, n):  # dp
    # first string on left side and second on top side
    dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):  # rows
        for j in range(n + 1):  # element in rows
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    str1 = list(input())
    str2 = list(input())
    print(solver(str1, str2, m, n))
