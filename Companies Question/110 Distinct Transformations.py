"""
find the number of subsequence of str2 in str1..this is the question

https://practice.geeksforgeeks.org/problems/distinct-transformations/0/
"""
# recursion
def solver1(A, B, n1, n2):
    def helper(i, j):
        if j == n2:  # if we reach end of B, then we found B in A
            return 1
        elif i == n1:  # if we reach end of A, but not of B
            return 0

        # return helper(i+1, j) + (helper(i+1, j+1) if A[i] == B[j] else 0)
        # or
        if A[i] == B[j]:
            return helper(i + 1, j + 1) + helper(i + 1, j)
        else:
            return helper(i + 1, j)

    return helper(0, 0)

'''
case 1: if B[i] != A[j], then the solution would be to ignore the character 
A[j] and align substring B[0..i] with A[0..(j-1)]. Therefore, 
DP[i][j] = DP[i][j-1].

case 2: if B[i] == A[j], then first we could have the solution in case 1, 
but also we could match the characters B[i] and A[j] and place the rest of 
them (i.e. B[0..(i-1)] and A[0..(j-1)]. As a result, 
DP[i][j] = DP[i][j-1] + matrixDP[i-1][j-1]
'''
# dp
def solver(A, B, n1, n2):
    # (n1+1)*(n2+1)
    dp = [[None for i in range(n2 + 1)] for j in range(n1 + 1)]

    # if length of string 1 is zero
    for i in range(n2 + 1):
        dp[0][i] = 0

    # if length of string 2 is zero
    for i in range(n1 + 1):
        dp[i][0] = 1

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if A[i - 1] == B[j - 1]: # 
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else: # if not same ignore the current character of 'A'
                dp[i][j] = dp[i - 1][j]

    return dp[n1][n2]


# it do not check for no solution in which we have to print "EMPTY"
T = int(input())
for _ in range(T):
    A = input()
    B = input()
    n1, n2 = len(A), len(B)
    if n1 <= n2:
        print(1 if A == B else 0)
    else:
        print(solver(A, B, n1, n2))
