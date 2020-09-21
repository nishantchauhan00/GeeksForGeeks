def solver(arr, n):
    left_greatest = [-1 for _ in range(n)]
    left_greatest[0] = arr[0]
    right_smallest = [-1 for _ in range(n)]
    right_smallest[-1] = arr[-1]

    temp = arr[0]
    for i in range(1, n):
        temp = max(temp, arr[i])
        left_greatest[i] = temp
    
    temp = arr[-1]
    for i in range(n-1, -1, -1):
        temp = min(temp, arr[i])
        right_smallest[i] = temp
    
    for i in range(1, n-1):
        if left_greatest[i] == right_smallest[i]:
            return left_greatest[i]
    

    return -1



for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))
