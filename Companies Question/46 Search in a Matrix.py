'''
# direct search
def search(arr, n, m, val):
    for row in arr:
        if val in row:
            return 1
    return 0
    

T = int(input())
for i in range (T):
    n, m = map(int, input().split())
    arr = [[None for _ in range(m)] for _ in range(n)]
    temparr = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            arr[i][j] = temparr[i * m + j]
    val = int(input())
        
    print(search(arr, n, m, val))
'''


def search(arr, n, m, val):
    for i in range(n):
        if val>= arr[i][0] and val <= arr[i][m-1]:
            l, r = 0, m
            while l <= r:
                mid = (l+r)//2
                if arr[i][mid] == val:
                    return 1
                elif arr[i][mid] > val:
                    r = mid - 1
                else: # arr[i][mid] < val
                    l = mid + 1
    return 0
    

T = int(input())
for i in range (T):
    n, m = map(int, input().split())
    arr = [[None for _ in range(m)] for _ in range(n)]
    temparr = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            arr[i][j] = temparr[i * m + j]
    val = int(input())
        
    print(search(arr, n, m, val))

    
    