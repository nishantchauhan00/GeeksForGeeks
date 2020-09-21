#code
def solver1(arr, n, k):
    return 1 if k in arr else -1 


def solver(arr, n, k):
    if k < arr[0] or k > arr[n - 1]:
        return -1

    l, r = 0, n - 1
    while l <= r:
        mid = (l + r)//2
        if arr[mid] > k:
            r = mid - 1
        elif arr[mid] < k:
            l = mid + 1
        else:
            return 1

    return -1


T = int(input())
for _ in range(T):
    n, k = input().split()
    arr = list(map(int, input().split()))
    print(solver(arr, int(n), int(k)))





