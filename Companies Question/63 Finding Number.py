'''
An array is called Bitonic if it is comprises of an increasing sequence of 
integers followed immediately by a decreasing sequence of integers.
Given a bitonic array A of N distinct integers. Find a element X in it.
'''
def solver1(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

# as subarray is bitonic, so it will be increasing at start abd decrease at last
# so we start from begining, if element becomes less than elements in array, then
# we start search from last, if element gets lower than elements in array, then
# return -1
def solver(arr, n, k):
    # check from starting
    for i in range(n):
        if arr[i] == k:
            return i
        elif arr[i] > k:
            break

    # check from last
    for i in range(n-1, -1, -1):
        if arr[i] == k:
            return i
        elif arr[i] > k:
            break
        
    return -1



T = int(input())
for _ in range(T):
    n = int(input())
    arr = input().split()
    for i in range(n):
        arr[i] = int(arr[i])
    k = int(input())
    print(solver(arr, n, k))


