"""
NOt WORkInG

I tried it this way:
Let string k be lcs of string a and b
Then the answer would be lcs of k and c.
But this approach is not passing all test cases. 
Can someone tell why is this wrong?

Basically we can have more than one lcs for two string (let say a and b) so 
it may or may not give correct o/p when taking lcs with string c.


def solver(X, Y, Z, n, m, k):

    def lcs(str1, str2, m , n):
        print(str1, str2, m , n)
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j] )

        common_substr = ""
        # to get common subsequence string
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                common_substr += str1[i-1]
                i -= 1
                j -= 1
            else:
                # if value are same, go in left direction
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1

        return [dp[m][n], common_substr[::-1]]
    
    lcs1, common_substr1 = lcs(X, Z, n, k)
    lcs2, common_substr2 = lcs(common_substr1, Y, len(common_substr1), m)
    
    print(common_substr1, lcs1)
    print(common_substr2, lcs2)

    return lcs2
"""


# O(n^3) solution
def solver(X, Y, Z, n, m, k):
    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, k+1):
                if X[i-1] == Y[j-1] == Z[k-1]:
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]    
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],    
                        dp[i][j-1][k],    
                        dp[i][j][k-1]    
                    )

    return dp[n][m][k]




if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, k = map(int, input().strip().split())
        X, Y, Z = input().strip().split()
        print(solver(X, Y, Z, n, m, k))
