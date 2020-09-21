def solver(arr):
    newstr = arr[0]
    for i in range(1, len(arr)):
        if not(arr[i-1] == arr[i]):
            newstr += arr[i]
    return newstr


T = int(input())

for _ in range(T):
    arr = list(input())
    print(solver(arr))


