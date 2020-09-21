#code
def solver1(arr, n):
    ordered = False
    end = n
    while not ordered:
        ordered = True
        while end > 0 and arr[end - 1] == 0:
            end -= 1
        for i in range(end, 0, -1):
            if arr[i - 1] is 0 and arr[i] is not 0:
                ordered = False
                arr[i - 1] = arr[i]
                arr[i] = 0
    
    return arr


def solver(arr, n): 
    # python make it easy but c++ code will require some changes
    # like making last count_zero numbers equal to 0
    count_zero = 0
    j = 0
    for i in range(n):
        if arr[i] is 0:
            count_zero += 1
        else: 
            arr[j] = arr[i]
            j += 1
    
    return arr[:j] + [0]*count_zero


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ".join(map(str, solver(arr, n))))


