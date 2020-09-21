def solver(arr, n):
    if n <= 1:
        return n

    # stores sum upto i'th index
    dp = arr.copy()
    for i in range(1, n):
        dp[i] += dp[i-1]
    
    total = dp[n-1]
    for i in range(n-1, -1, -1):
        if total == dp[i]:
            return i+1
        total -= arr[i]

    return -1




if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solver(arr, n))
