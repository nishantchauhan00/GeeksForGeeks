def solver1(arr, n):
    # its expensive, beacause inserting in between of array/list is expensive 
    # operation 
    evenarr = []
    oddarr = []

    for i in range(n):
        if arr[i] % 2 is 0:  # Even
            e = len(evenarr) - 1
            while e >= 0 and evenarr[e] > arr[i]:
                e -= 1
            evenarr.insert(e+1, arr[i])
        else:  # odd
            o = len(oddarr) - 1
            while o >= 0 and oddarr[o] > arr[i]:
                o -= 1
            oddarr.insert(o+1, arr[i])

    evenarr.extend(oddarr)
    return evenarr 


def solver2(arr, n):
    evenarr = []
    oddarr = []

    for i in range(n):
        if arr[i] % 2 is 0:  # Even
            evenarr.append(arr[i])  
        else:  # odd
            oddarr.append(arr[i])
    
    evenarr = sorted(evenarr)
    oddarr = sorted(oddarr)

    evenarr.extend(oddarr)
    return evenarr


# even better, just sort before
def solver(arr, n):
    evenarr = []
    oddarr = []
    arr = sorted(arr)

    for i in range(n):
        if arr[i] % 2 is 0:  # Even
            evenarr.append(arr[i])  
        else:  # odd
            oddarr.append(arr[i])

    evenarr.extend(oddarr)
    return evenarr 




T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ".join(list(map(str, solver(arr, n)))))


'''
# O(1) time complexity 
def solver(arr, n):
    j = -1

    for i in range(n):
        if arr[i] % 2 is 0:  # Even
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    for el in sorted(evenarr[:j]):
        print(el, end=" ")
    for el in sorted(oddarr[j:]):
        print(el, end=" ")
    print()


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    solver(arr, n)
'''



# even better, insted of merging two array, print them inside function
'''
def solver(arr, n):
    evenarr = []
    oddarr = []
    arr = sorted(arr)

    for i in range(n):
        if arr[i] % 2 is 0:  # Even
            evenarr.append(arr[i])  
        else:  # odd
            oddarr.append(arr[i])

    for el in evenarr:
        print(el, end=" ")
    for el in oddarr:
        print(el, end=" ")
    print()


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    solver(arr, n)
'''


