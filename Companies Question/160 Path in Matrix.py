'''
first i did by brutefore, then i applied dp, as if we have already reached
greater then the result from that will greater then current, if its equal
then it is making same computations again  
'''
def solver(arr, n):
    out = 0
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    def helper(i, j, curr):
        nonlocal out
        if j < 0 or j >= n or dp[i][j] >= curr:
            return

        dp[i][j] = curr
        if i == n - 1:
            # instead of updating out, we can just output max of last row of dp 
            out = max(out, curr + arr[i][j])
            return

        helper(i + 1, j - 1, curr + arr[i][j])
        helper(i + 1, j, curr + arr[i][j])
        helper(i + 1, j + 1, curr + arr[i][j])

    for j in range(n):
        helper(0, j, 0)
    return out


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

    print(solver(arr, n))
