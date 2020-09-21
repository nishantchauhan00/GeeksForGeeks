def solver(cents, M, N):
    arr = [0] * (N + 1)
    arr[0] = 1
    for i in range(M):
        num = cents[i]
        for j in range(num, N + 1):
            arr[j] += arr[j - num]
    return arr[N]


T = int(input())

for _ in range(T):
    arrsize = int(input())
    cents = list(map(int, input().split()))
    N = int(input())
    print(solver(cents, arrsize, N))


