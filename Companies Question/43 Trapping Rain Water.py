def solver1(arr, n):
    water = 0
    maxleft = [0 for _ in range(n)]
    maxright = [0 for _ in range(n)]

    temp = arr[0]
    for i in range(1, n-1):
        maxleft[i] = temp
        temp = max(temp, arr[i])

    temp = arr[-1]
    for i in range(n-2, 0, -1):
        maxright[i] = temp
        temp = max(temp, arr[i])

    for i in range(1, n-1):
        water += max(0, min(maxleft[i], maxright[i]) - arr[i])

    return water


def solver(arr, n):
    # instead of looping for maxleft different just find maxleft while 
    # calculating water
    water = 0
    maxright = [0 for _ in range(n)]

    temp = arr[-1]
    for i in range(n-2, 0, -1):
        maxright[i] = temp
        temp = max(temp, arr[i])

    temp = arr[0]
    for i in range(1, n-1):
        water += max(0, min(temp, maxright[i]) - arr[i])
        temp = max(temp, arr[i])

    return water


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))


'''
4
6
3 0 0 2 0 4
4
7 4 0 9
3
6 9 9
7
8 8 2 4 5 5 1


10
10
0
4
'''