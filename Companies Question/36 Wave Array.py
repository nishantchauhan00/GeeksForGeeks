'''
Given a sorted array arr[] of non-repeating integers without duplicates. Sort 
the array into a wave-like array and return it. In other words, arrange the 
elements into a sequence such that 
a1 >= a2 <= a3 >= a4 <= a5..... 
(considering the increasing lexicographical order).

Input:
1
5
1 2 3 4 5
Output:
2 1 4 3 5
'''


# this solution works for unsorted array too 
def solver1(arr, n):
    for i in range(n - 1):
        if i%2 == 0:
            if not(arr[i] >= arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if not(arr[i] <= arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
    return arr


# faster, but only for sorted array 
def solver(arr, n):
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



T = int(input())

for _ in range(T):
    n = int(input())
    # arr = list(map(int, input().split()))
    # print(" ".join(str(el) for el in solver(arr, n)))
    # # OR, 
    # # we are using this beacuse of some memory error in online ide
    arr=input().split()
    for i in range(n):
        arr[i]=int(arr[i])
    arr = solver1(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
    print()


