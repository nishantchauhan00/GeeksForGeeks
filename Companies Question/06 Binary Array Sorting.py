def sortbarr(arr):
    l = 0 
    r = len(arr) - 1

    while arr[r] == 1 and r > 0:
        r -= 1

    while l < r:
        if arr[l] is 1:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
        l += 1
        while arr[r] == 1:
            r -= 1

    return " ".join(list(map(str, arr)))


N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sortbarr(arr))


'''
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0

0 0 1 1 1
0 0 0 0 1 1 1 1 1 1
'''


