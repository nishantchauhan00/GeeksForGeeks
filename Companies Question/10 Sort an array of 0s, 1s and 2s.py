def sort012(arr,n): # O(n)
    low = 0
    mid = 0
    high = n-1
    # we wont swap on 1, just swap 0 in start and 2 at last
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # high at last can be 2 so even after swap, check mid again in next loop
        else:
            mid += 1
    return arr


def sort012_brute(arr,n): # O(2n)
    numsOccurences = [0]*3
    for el in arr:
        numsOccurences[el] += 1
    
    j = 0
    for i in range(3):
        for _ in range(numsOccurences[i]):
            arr[j] = i
            j += 1

    return arr
 

t = int(input())

for _ in range(t):
    n = int(input()) 
    arr = list(map(int, input().split()))
    print(sort012(arr, n))


