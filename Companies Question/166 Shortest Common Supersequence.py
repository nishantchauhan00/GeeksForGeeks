def solver(str1, str2, m, n):
    def lcs(str1, str2):
        # first string on left side and second on top side
        # so that 'i' is for str1 and 'j' for str2
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

    return len(a) + len(b) - lcs(str1, str2)



for _ in range(int(input())):
    a, b = input().split()
    print(solver(a, b, len(a), len(b)))
