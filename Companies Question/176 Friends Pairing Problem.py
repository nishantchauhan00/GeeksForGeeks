"""
Suppose you have n-1 people and nth person comes then that nth person have 
follwing choice:
1. To be single
2. To get paired with of ( n - 1 ) people.

When the nth person is single then the no of ways to do so is simply 
dp [ n - 1 ] .
but if the nth person pairs then he have to choose from n -1 friends and hence 
with have to see combination of ( n - 2 ) people now
hence Dp [ n ] = Dp [ n - 1 ] + ( n - 1 ) * Dp [ n - 2 ] 
"""

mod = 1000000007
def solver(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % mod

    return dp[n]



if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(solver(n))
