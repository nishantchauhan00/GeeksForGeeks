# recursion - brute force kind of technique
# VERY BAD APPROACH
def solver1(arr, n):
    def helper(i, curr1, curr2):
        if i == n:
            if curr1 == curr2:
                return True
            return False

        possible = False
        possible = helper(i + 1, curr1 + arr[i], curr2)
        if not possible:
            possible = helper(i + 1, curr1, curr2 + arr[i])

        return possible

    res = helper(0, 0, 0)
    return "YES" if res else "NO"


# as we know the sum of both subsets are equal, so sum of 1 subset is half
# of total sum of array.
# If total sum is odd, then it is not possible to divide array.
#
# A LITTLE MORE EFFICIENT THEN PREVIOUS ONE, BUT NOT GOOD
def solver2(arr, n):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return "NO"

    def helper(i, total):
        if i >= n:
            return False
        if total == arr[i]:
            return True
        if arr[i] > total:
            return False
        return helper(i + 1, total - arr[i]) or helper(i + 1, total)

    res = helper(0, total_sum / 2)
    return "YES" if res else "NO"


# more space complexity, but faster
# same solution as previous one, but uses dp
def solver(arr, n):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return "NO"

    dp = [[None for _ in range(total_sum // 2 + 1)] for _ in range(n + 1)]

    def helper(i, total):
        if dp[i][total] != None:
            return dp[i][total]
        if i >= n:
            dp[i][total] = False
            return False
        if total == arr[i]:
            dp[i][total] = True
            return True
        if arr[i] > total:
            dp[i][total] = False
            return False

        dp[i][total] = helper(i + 1, total - arr[i]) or helper(i + 1, total)
        return dp[i][total]

    res = helper(0, total_sum // 2)
    return "YES" if res else "NO"


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solver(arr, n))
