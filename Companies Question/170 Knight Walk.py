INT_MAX = 99999999

# tracing every path
# prune/return from the path if steps gets more than or equal to current 
# minimum steps, as we are interseted in not finding the path but the min steps
# gives tle
def solver1(s1, s2, d1, d2, n, m):
    min_steps = INT_MAX
    vis = [[False for _ in range(m)] for _ in range(n)]

    def helper(i=s1, j=s2, steps=0):
        nonlocal min_steps
        if i < 0 or j < 0 or i >= n or j >= m or vis[i][j] or steps >= min_steps:
            return
        if i == d1 and j == d2:
            min_steps = min(min_steps, steps)
            return

        vis[i][j] = True
        # it can go in any of eight positions
        helper(i - 2, j - 1, steps + 1)  # top left
        helper(i - 2, j + 1, steps + 1)  # top right
        helper(i - 1, j - 2, steps + 1)  # left up
        helper(i + 1, j - 2, steps + 1)  # left down
        helper(i + 2, j - 1, steps + 1)  # bottom left
        helper(i + 2, j + 1, steps + 1)  # bottom right
        helper(i - 1, j + 2, steps + 1)  # right up
        helper(i + 1, j + 2, steps + 1)  # right down
        vis[i][j] = False

    helper()
    return -1 if min_steps == INT_MAX else min_steps


# lets try dp
# passed
def solver(s1, s2, d1, d2, n, m):
    dp = [[INT_MAX for _ in range(m)] for _ in range(n)]

    def helper(i=s1, j=s2, steps=0):
        if i < 0 or j < 0 or i >= n or j >= m or steps >= dp[i][j] or steps >= dp[d1][d2]:
            return
        if i == d1 and j == d2:
            dp[d1][d2] = min(dp[d1][d2], steps)
            return
        
        dp[i][j] = steps

        # it can go in any of eight positions
        helper(i - 2, j - 1, steps + 1)  # top left
        helper(i - 2, j + 1, steps + 1)  # top right
        helper(i - 1, j - 2, steps + 1)  # left up
        helper(i + 1, j - 2, steps + 1)  # left down
        helper(i + 2, j - 1, steps + 1)  # bottom left
        helper(i + 2, j + 1, steps + 1)  # bottom right
        helper(i - 1, j + 2, steps + 1)  # right up
        helper(i + 1, j + 2, steps + 1)  # right down

    helper()
    return -1 if dp[d1][d2]== INT_MAX else dp[d1][d2]





if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        s1, s2, d1, d2 = map(int, input().split())
        # these values are 1 indexed
        print(solver(s1-1, s2-1, d1-1, d2-1, n, m))
