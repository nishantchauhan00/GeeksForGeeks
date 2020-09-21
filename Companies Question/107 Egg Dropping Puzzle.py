'''
**F(n, k) -> 1 + min(max(F(n - 1, x - 1), F(n , k - x)))for all 0 < x <= k
**i will try to explain it in simple way ,just try to read this explaination 
loudly so that you can imagine and understand.

Now we have n eggs and k floors to try.

**first condition:- if egg break in xth floor.
if we break nth egg then we will have n - 1 eggs and all floors above it, will 
be responsible for breaking eggs , so there is no sense to visit all those 
above floors.Now, we need to look into all below floors, so we have x - 1 
floors to visit with n - 1 eggs. if f(n, k) gives minimum trials in worst 
case, so f(n - 1, x - 1) where 0 < x <= k, give minimum trial for n - 1 eggs 
by visiting x - 1 floors. """""F(n - 1, x - 1)"""""

**second condition:- if egg doesnt break in xth floor, then all below floors 
should not be visited, so we have only k - x floors to visit. """""F(n , k - x)"""""".

We need to consider the worse case, therefore we need to take max of both the 
calls and after the we can find the answer by taking min.

Don't look directly on bottom up approach ,first write recurrence then try to 
convert in it to bottom up.

https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
'''

INT_MAX = 99999999


def solver1(n, k):
    # If there are no floors, then no trials needed.
    # OR if there is one floor, one trial needed.
    if k == 0 or k == 1:
        return k

    # We need k trials for one egg and k floors
    if n == 1:
        return k

    minworst = INT_MAX
    # range is (1, K+1) becuase we cant consider 0, and we need to take into
    # account k'th floor
    for x in range(1, k + 1):
        minworst = min(minworst, 1 +  max(solver1(n - 1, x - 1), solver1(n, k - x)))
    return minworst


# using dp with recursion
def solver(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, n + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        dp[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = INT_MAX
            for x in range(1, j + 1):
                dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][x - 1], dp[i][j - x]))

    return dp[n][k]


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(solver(n, k))

