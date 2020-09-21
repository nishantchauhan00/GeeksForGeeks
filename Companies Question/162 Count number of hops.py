# bruteforce
# recursion
def solver1(n):
    ways = 0
    def helper(i):
        nonlocal ways
        if i == n:
            ways += 1
            return
        if i > n:
            return

        helper(i + 1)
        helper(i + 2)
        helper(i + 3)

    helper(0)
    return ways


'''
number - steps
0 - 0
1 - 1
2 - 2
3 - 4
4 - 7
5 - 13
6 - 24
7 - 44
8 - 81
9 - 149
10 - 274

we saw a pattern that arr[i] = arr[i-1] + arr[i-2] + arr[i-3] 

its similar to fibonacci, but instead of 2 values like in fibonacci, we take 
sum of last 3 values
'''
def solver(n):
    if n <=2:
        return n
    dp = [None for _ in range(n)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n-1]





for _ in range(int(input())):
    n = int(input())
    print(solver(n))
