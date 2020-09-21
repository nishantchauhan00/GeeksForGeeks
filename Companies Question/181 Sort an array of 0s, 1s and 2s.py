def solver(arr, n):
    l, r = 0, n-1
    i = 0
    while i <= r:
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
            i += 1
        elif arr[i] == 2: 
            arr[r], arr[i] = arr[i], arr[r]
            r -= 1
        else:
            i += 1
    
    return arr




if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(" ".join(str(el) for el in solver(arr, n)))

