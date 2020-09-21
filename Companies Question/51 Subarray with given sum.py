#code
def solver1(arr, N, K): # brute force
    for i in range(N):
        sum_val = arr[i]
        for j in range(i + 1, N):
            sum_val += arr[j]
            if sum_val == K:
                return [i + 1, j + 1]
    return [-1]


def solver(arr, N, K):
    curr_sum = 0
    l = 0 # left index from where curr_sum start
    for i in range(N):
        curr_sum += arr[i]

        while curr_sum > K and l <= i:
            curr_sum -= arr[l]
            l += 1

        if curr_sum == K:
            return [l + 1, i + 1]

    return [-1]
  


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(" ".join(str(el) for el in solver(arr, n, k)))



