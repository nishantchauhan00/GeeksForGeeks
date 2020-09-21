def solver(arr, n):
    if n < 3:
        return max(arr)

    # we can do it by dp, but we need only two previous values
    # so to save space we use just two integer variables
    prev_before = arr[0]
    prev = max(arr[0], arr[1]) # previous value can be first value if its greater
    for i in range(2, n):
        curr = max(prev_before + arr[i], prev)
        prev_before = prev
        prev = curr

    # the last value stores the max value 
    return prev



T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))
