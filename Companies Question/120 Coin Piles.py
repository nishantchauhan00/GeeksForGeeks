def solver(arr, n, k):
    out = 999999 # INT_MAX
    arr.sort()
    # prev_sum maintains sum of all values before the current index, also
    # exluding the current value
    prev_sum = 0
    for i in range(n):
        sum_before = prev_sum
        for j in range(n - 1, i, -1):
            if arr[j] - arr[i] > k:
                excess_val = arr[j] - arr[i] - k
                sum_before += excess_val
            else:
                # as array is sorted so if above condition is satisfied then
                # we don't need to go back more, as the value of arr[j] will
                # be less
                break
        out = min(out, sum_before)
        prev_sum += arr[i]

    return out


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solver(arr, n, k))
